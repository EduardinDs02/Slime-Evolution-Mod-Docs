#!/usr/bin/env python3
"""Build a portable, searchable player guide from the repository's canonical Markdown."""
import argparse,hashlib,html,json,re,shutil,unicodedata,zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote,unquote,urlsplit,urlunsplit
import markdown

ROOT=Path(__file__).resolve().parents[2];TOOLS=ROOT/'tools/docs'
config=json.loads((TOOLS/'site.json').read_text());DOCS=ROOT/config.get('content_root','docs')
version=config.get('mod_version') or re.search(r'^mod_version=(.+)$',(ROOT/'gradle.properties').read_text(),re.M)[1]
screen=ROOT/'src/main/java/com/slimeevolution/client/screen/SlimepediaScreen.java'
if screen.exists():
    assert config['url']==re.search(r'GUIDE_URL="([^"]+)"',screen.read_text())[1],'Website and Slimepedia addresses differ'
source_repository=config.get('source_repository',config['repository'])
ARROW='<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6 18 18 6M6 6h12v12"/></svg>'
def slug(text,separator):return ''.join(c for c in html.unescape(text).lower() if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ',separator)
def output_path(source):return (source.parent/('index.html' if source.name=='README.md' else source.stem+'.html')).relative_to(DOCS).as_posix()
sources=[DOCS/name for name in ['README.md','INSTALLATION.md','CONFIGURATION.md','BALANCE.md','RELEASE_NOTES.md','PRESENTATION.md']]
for directory in ['guides','reference','updates']:sources+=sorted((DOCS/directory).glob('*.md'))
sources=sorted(set(sources));mapping={p.resolve():output_path(p) for p in sources}

class Rewrite(HTMLParser):
    def __init__(self,source):super().__init__(convert_charrefs=False);self.source=source;self.chunks=[]
    def link(self,value):
        url=urlsplit(value)
        if url.scheme or url.netloc or value.startswith(('#','/')):return value
        target=(self.source.parent/unquote(url.path)).resolve() if url.path else self.source.resolve()
        assert target.exists(),f'Broken Markdown destination: {self.source}: {value}'
        if target in mapping:
            import posixpath
            path=posixpath.relpath(mapping[target],str(Path(mapping[self.source.resolve()]).parent))
        elif target.is_relative_to(DOCS/'assets'):
            import posixpath
            path=posixpath.relpath(target.relative_to(DOCS).as_posix(),str(Path(mapping[self.source.resolve()]).parent))
        else:
            path=source_repository+('/tree/main/' if target.is_dir() else '/blob/main/')+target.relative_to(ROOT).as_posix()
        return urlunsplit(('', '', path, url.query,url.fragment))
    def handle_starttag(self,tag,attrs):
        if tag=='img':attrs=[*attrs,('loading','lazy'),('decoding','async')]
        values=[]
        for key,value in attrs:
            if key in {'href','src'} and value:value=self.link(value)
            values.append(key if value is None else key+'="'+html.escape(value,quote=True)+'"')
        self.chunks.append('<'+tag+(' '+' '.join(values) if values else '')+'>')
    def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs)
    def handle_endtag(self,tag):self.chunks.append('</'+tag+'>')
    def handle_data(self,data):self.chunks.append(data)
    def handle_entityref(self,name):self.chunks.append('&'+name+';')
    def handle_charref(self,name):self.chunks.append('&#'+name+';')
    def handle_comment(self,data):self.chunks.append('<!--'+data+'-->')

def build(destination):
    destination.mkdir(parents=True,exist_ok=True)
    if (DOCS/'assets').resolve()!=(destination/'assets').resolve():
        shutil.copytree(DOCS/'assets',destination/'assets',dirs_exist_ok=True)
    for name in ['site.css','site.js']:shutil.copyfile(TOOLS/name,destination/name)
    index=[];manifest={}
    for source in sources:
        text=source.read_text();title=re.search(r'^#\s+(.+)',text,re.M)[1];path=mapping[source.resolve()];prefix='../'*len(Path(path).parent.parts)
        converter=markdown.Markdown(extensions=['tables','fenced_code','toc','sane_lists'],extension_configs={'toc':{'slugify':slug,'toc_depth':'2-3'}})
        body=converter.convert(text);rewriter=Rewrite(source);rewriter.feed(body);body=''.join(rewriter.chunks)
        nav=[]
        for group,pages in config['navigation'].items():
            entries=[]
            for label,name in pages.items():
                target=DOCS/name;active=' aria-current="page"' if target==source else ''
                entries.append(f'<a href="{prefix}{mapping[target.resolve()]}"{active}>{html.escape(label)}</a>')
            nav.append('<section><h2>'+html.escape(group)+'</h2>'+''.join(entries)+'</section>')
        hero=''
        if source==DOCS/'README.md':
            banner='slime-evolution-banner-web.png' if (DOCS/'assets/cover/slime-evolution-banner-web.png').exists() else 'slime-evolution-cover-landscape.png'
            hero=f'<section class="hero"><img src="assets/cover/{banner}" alt="Criaturas e descobertas do Slime Evolution ao pôr do sol"><div><span class="eyebrow">GUIA DO MOD · {version}</span><h1>Um mundo de slimes<br>para descobrir.</h1><p>Crie vínculos, combine a genética e encontre sua próxima evolução.</p><a class="primary" href="guides/GETTING_STARTED.html">Começar a jogar {ARROW}</a></div></section>'
            body=re.sub(r'^<h1.*?</h1>','',body,count=1,flags=re.S)
        canonical=config['url']+quote(path,safe='/')
        source_url=source_repository+'/blob/main/'+source.relative_to(ROOT).as_posix()
        page=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{html.escape(title)} · Slime Evolution</title><meta name="description" content="Guia do Slime Evolution: espécies, genética, criação, metamorfoses, trabalho e aventura."><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="{prefix}site.css"></head>
<body data-root="{prefix}"><a class="skip" href="#conteudo">Ir para o conteúdo</a><header class="topbar"><button id="menu-toggle" aria-controls="navigation" aria-expanded="false" aria-label="Abrir navegação">☰</button><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">✦</span><span>Slime Evolution<small>GUIA DE CAMPO</small></span></a><div class="search"><label class="sr-only" for="search">Buscar na documentação</label><input id="search" type="search" placeholder="Buscar espécies, receitas, funções…" autocomplete="off" aria-controls="search-results" aria-expanded="false"><div id="search-results" role="region" aria-label="Resultados da busca" hidden></div></div><a class="repository" href="{config['repository']}">GitHub ↗</a></header>
<div class="layout"><aside id="navigation" class="navigation"><span class="version">VERSÃO {version}</span>{''.join(nav)}</aside><main id="conteudo" tabindex="-1">{hero}<div class="reading"><article class="article-body">{body}</article><aside class="outline" aria-label="Nesta página"><span>NESTA PÁGINA</span>{converter.toc}</aside></div><footer>Slime Evolution · Minecraft 1.21.1 / NeoForge / GeckoLib<a href="{source_url}">Ver esta página no GitHub ↗</a></footer></main></div><script src="{prefix}search-index.js" defer></script><script src="{prefix}site.js" defer></script></body></html>'''
        page=page.replace('GitHub ↗','GitHub '+ARROW)
        target=destination/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(page)
        plain=html.unescape(re.sub('<[^>]+>',' ',body));plain=re.sub(r'\s+',' ',plain).strip()
        index.append({'title':title,'url':path,'text':plain})
        manifest[source.relative_to(ROOT).as_posix()]=hashlib.sha256(source.read_bytes()).hexdigest()
    (destination/'search-index.js').write_text('window.SLIME_DOC_INDEX='+json.dumps(index,ensure_ascii=False).replace('</','<\\/')+';\n')
    (destination/'.nojekyll').touch();(destination/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+config['url']+'sitemap.xml\n')
    (destination/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(config['url']+quote(row['url'],safe='/'))+'</loc></url>' for row in index)+'</urlset>')
    (destination/'build-info.json').write_text(json.dumps({'version':version,'url':config['url'],'pages':len(index),'sources':manifest},indent=2)+'\n')
    return check(destination)

class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for k in ['id','name']:
            if k in a:self.ids.add(a[k])
        for k in ['href','src']:
            if a.get(k):self.refs.append(a[k])

def check(destination):
    pages={};links=0
    for name in mapping.values():
        p=destination/name
        parser=Links();parser.feed(p.read_text());pages[p.resolve()]=parser
    for p,parser in pages.items():
        for value in parser.refs:
            u=urlsplit(value)
            if u.scheme or u.netloc:continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p
            assert target.exists(),f'Broken site link: {p}: {value}'
            if u.fragment and target in pages:assert unquote(u.fragment) in pages[target].ids,f'Missing site anchor: {p}: {value}'
            links+=1
    return {'pages':len(pages),'local_links_and_assets_checked':links,'errors':0,'version':version,'url':config['url']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'build/site');p.add_argument('--zip',type=Path);a=p.parse_args()
    report=build(a.output)
    if a.zip:
        a.zip.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(a.zip,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
            for source in sorted(a.output.rglob('*')):
                if source.is_file():
                    entry=zipfile.ZipInfo(source.relative_to(a.output).as_posix(),(1980,1,1,0,0,0));entry.compress_type=zipfile.ZIP_DEFLATED;archive.writestr(entry,source.read_bytes())
        with zipfile.ZipFile(a.zip) as archive:assert archive.testzip() is None
        report.update(zip=str(a.zip),sha256=hashlib.sha256(a.zip.read_bytes()).hexdigest())
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
