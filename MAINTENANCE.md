# Atualizar o guia

Os arquivos Markdown, as imagens em `assets/` e o gerador do site estão neste
repositório. As páginas HTML são publicadas pelo GitHub Pages a partir da raiz
do branch `main`, usando o arquivo `.nojekyll`.

Depois de editar os guias, regenere as páginas na raiz antes de enviar o commit:

```bash
python -m pip install -r tools/docs/requirements.txt
python tools/docs/build-site.py --output .
```

O gerador confere os links, as imagens e as âncoras. A versão e o endereço do site
ficam em `tools/docs/site.json`. As atualizações por versão ficam em `updates/`;
os guias de uso ficam em `guides/` e `reference/`.
