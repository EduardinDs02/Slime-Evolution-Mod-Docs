# Reprodução, crescimento e inspeção

Combine adultos compatíveis para obter filhotes com herança genética própria.
As 47 espécies usam 61 pares de reprodução, incluindo 14 cruzamentos entre espécies.

## Preparar os pais

1. Alimente manualmente dois adultos compatíveis, vinculando ambos ao
   mesmo cuidador. A confiança mínima é 20 em dóceis, 40 em neutros e 70 em
   hostis. Alimentadores ajudam com a fome, mas não aumentam confiança.
2. Cada adulto precisa de fome até 40, conforto de pelo menos 60, energia de
   pelo menos 60 e metade da vida ou mais. Não pode estar em combate,
   recuperação reprodutiva, sob efeito da recarga de dano recente, preso por
   laço, montado ou transportando passageiros.
3. O cuidador usa uma `slimeevolution:breeding_gel` em cada pai. Uma preparação
   válida consome uma geleia em sobrevivência e dura 1.200 ticks, normalmente
   60 segundos. Cliques repetidos enquanto pronto não consomem outra geleia
   nem renovam a duração. Uma tentativa inválida não consome o item.
4. Mantenha os dois a até quatro blocos, com visão livre. O servidor procura
   piso sólido, seco e desocupado perto do centro do casal. Não há deslocamento
   automático dos pais para procurar parceiros nesta versão.

Há 47 receitas de mesma espécie e 14 pares entre espécies. As combinações completas estão no
[guia de evolução](EVOLUTION.md). A ordem dos pais não altera o resultado.
Pais e filhos, irmãos e meios-irmãos não podem cruzar. O registro guarda UUIDs
dos dois pais e geração; ele não detecta parentesco ancestral mais distante.
As receitas JSON e suas validações estão em [referência de datapacks](../reference/SPECIES_DATA.md).

O limite padrão é 12 slimes vivos carregados na região de 32 blocos ao redor
do nascimento, contando os pais e outras espécies. A consulta usa uma caixa
espacial. Se o limite foi atingido, não nasce outro slime.

## Nascimento e recuperação

Cada nascimento bem-sucedido produz um único indivíduo com UUID novo, genoma
herdado, identificação dos pais e geração seguinte à maior geração parental.
O filhote herda o cuidador e começa com tamanho 1, fome 60, conforto 60,
confiança 20 e energia 70. Ele não causa dano de contato enquanto jovem.
Sua espécie de nascimento é o resultado da receita. Histórico e exposição
de metamorfose dos pais não são herdados; os alelos continuam herdados normalmente.

Somente após o servidor aceitar o filhote no mundo, cada pai gasta 30 de
energia, recebe 30 de fome e entra em recuperação. A recuperação-base é
6.000 ticks, cinco minutos a 20 ticks por segundo, multiplicada por
`1.25 - 0.5 × fertilidade`: entre 3min45s e 6min15s.

Falta de espaço, incompatibilidade, limite populacional ou cancelamento da
inserção por outro mod não aplicam esses custos nem a recuperação. Os pais
continuam prontos até o prazo expirar; a geleia usada na preparação não é
devolvida. Expirar a prontidão não produz um filhote.

## Crescimento e persistência

O crescimento-base leva 12.000 ticks, dez minutos com o indivíduo carregado e
em boas condições. Avança a cada segundo enquanto fome for menor que 80,
conforto pelo menos 40 e energia pelo menos 20. Aumentos de tamanho exigem
espaço livre; paredes ou teto podem pausar o crescimento. Idade cronológica
e progresso de crescimento são contadores distintos.

O gene de tamanho determina o tamanho adulto dentro dos limites da espécie.
Um adulto de tamanho 1 continua sendo adulto: o estágio não depende apenas
do tamanho. Mudanças de tamanho preservam a proporção de vida.

Genoma, pais, geração, estágio, progresso e recuperação são salvos no NBT e
preservados pela cápsula. Crescimento e contadores ficam pausados enquanto
o indivíduo estiver na cápsula ou sem receber ticks no mundo. O token de
captura mantém as mesmas proteções descritas em [CARE.md](CARE.md).
Indivíduos antigos sem campos de crescimento são carregados como adultos de
geração zero, preservando seu genoma, UUID, cuidador e necessidades.

## Analisador genético

Use `slimeevolution:genetic_analyzer` em um slime para abrir a inspeção.
Qualquer jogador que alcance e veja o indivíduo pode consultá-lo. A tela
apresenta espécie, geração, UUID, pais, habilidade, vida, tamanho, estágio,
idade, necessidades, crescimento restante, recuperação e prontidão.

Os 15 genes mostram os dois alelos e sua expressão. A roda do mouse ou as
setas percorrem a lista; tooltips explicam o tipo de expressão e quais genes
ainda não têm efeito no jogo. A inspeção não edita o indivíduo, não consome
o analisador e não possui espaços para itens. O servidor invalida o menu
quando o slime desaparece, fica fora de visão ou se afasta mais de oito blocos.
A aba Evolução mostra origem, quantidade de metamorfoses e exigências da
receita ambiental. Trocar espécie, genoma ou receita também invalida a tela.

## Receitas

Ambos os itens ficam na aba de ferramentas/utilidades. Obter uma bola de
slime desbloqueia suas receitas no livro; cada receita produz um item.

Geleia reprodutiva: dois trigos (`T`), duas bagas brilhantes (`B`) e uma bola
de slime (`S`). Espaços vazios estão representados por pontos.

```text
.T.
BSB
.T.
```

Analisador: quatro barras de ferro (`F`), um bloco de vidro (`V`) e uma bola
de slime (`S`).

```text
.FV
FSF
.F.
```

## Configuração do servidor

Seção `[breeding]` da configuração do mod:

| Opção | Padrão | Intervalo / efeito |
| --- | --- | --- |
| `enabled` | `true` | Habilita reprodução iniciada pelo jogador |
| `localPopulationLimit` | `12` | 2–64 slimes carregados na região |
| `recoveryTicks` | `6000` | 200–240000; fertilidade ajusta a duração aplicada |
| `growthTicks` | `12000` | 200–240000; afeta novos filhotes |
| `mutationChance` | `0.02` | 0–0.25 por alelo; estabilidade e pais instáveis ajustam a chance |
| `mutationStep` | `0.1` | 0–0.25 de mudança máxima em um alelo |

Filhotes existentes conservam sua duração de crescimento. Recuperações já
iniciadas conservam seus contadores. Os tempos em segundos pressupõem
20 ticks por segundo; não são relógios que avançam com o mundo parado.

Herança, expressão e limites estão em [GENETICS.md](../reference/GENETICS.md). Cruzamentos
e metamorfoses estão no [guia de evolução](EVOLUTION.md).

## Preparação com estabilizador

Aplique antes da geleia em um pai apto e de seu cuidado. Uma unidade protege
o próximo nascimento do par contra novas mutações, sem alterar os alelos
herdados. Não prepara o pai para reproduzir nem dispensa os requisitos normais.
A proteção aparece no analisador e persiste em saves/cápsulas. Falhas, nascimento
cancelado e prontidão expirada a mantêm; nascimento aceito a consome nos pais
tratados. O filhote não a herda. Receitas e custos: [MATERIALS.md](MATERIALS.md).

Consulte também [linhagens avançadas](ADVANCED_LINEAGES.md):
quatro híbridos novos, rota Musgo + Água e reprodução das duas formas raras.

O nascimento de Eclipse exige o [ritual solar e lunar](ASCENSION.md):
carga solar, Lunar de Lua Nova, entardecer e catalisador com o cuidador.
