# Genética e herança

O genoma imutável contém os 15 genes da especificação, cada um com dois alelos
finitos no intervalo `[0, 1]`. `GenePair` calcula a expressão por média nos
genes aditivos, máximo nos dominantes e mínimo nos recessivos. Essa é uma
regra fictícia de gameplay; a expressão não substitui os alelos armazenados.

## Fundadores e descendentes

Slimes que passam pela finalização de spawn natural ou de ovos recebem
30 alelos aleatórios em `[0.25, 0.75)`, usando o RNG do servidor. Instâncias
criadas diretamente, sem finalizar o spawn, mantêm o genoma basal de
`0.5/0.5` até receber outro genoma. Carregar um save ou liberar uma cápsula
preserva o genoma existente, sem sortear novamente.

Na reprodução, `GeneticsService.inherit` seleciona com igual probabilidade
um dos dois alelos de cada progenitor para cada gene. Cada alelo herdado
pode sofrer uma mutação independente. A probabilidade efetiva é
`min(0.25, mutationChance × (1.5 - estabilidade média dos pais) × (1 + 0.5 × pais instáveis))`.
O valor padrão de `mutationChance` é 0.02; portanto, a estabilidade ajusta
a chance por alelo entre 1% e 3% sem pais instáveis. Um pai com habilidade
`unstable_touch` multiplica por 1,5; dois multiplicam por 2 (2%–6% no padrão).
Isso altera somente a probabilidade no nascimento: a amplitude continua
limitada por `mutationStep`, os alelos ficam em 0–1, e os pais não mudam.
`mutationChance=0` desativa mutações também para Corrompidos. Não há
mutação espontânea durante a vida nem contágio genético por ataques.

Uma mutação soma uma mudança aleatória entre `-mutationStep` e
`+mutationStep`, com resultado limitado a `[0, 1]`. A amplitude padrão é 0.1;
chance e amplitude configuráveis aceitam no máximo 0.25. Não há categorias
de mutações raras ou eventos narrativos nesta versão. O serviço recebe uma
fonte aleatória: sementes fixas nos testes e RNG do servidor nos nascimentos.

## Genes com efeito nesta versão

`e` representa a expressão do gene, sempre entre 0 e 1. Valores-base vêm da
espécie. O fator de tamanho usado em vida e dano é `tamanho atual / 2`.

| Gene | Expressão | Efeito |
| --- | --- | --- |
| Tamanho | Aditiva | Tamanho adulto: `min(máximo, mínimo + floor(e × (máximo - mínimo + 1)))` |
| Elasticidade | Aditiva | Multiplica o salto pela elasticidade da espécie e por `0.75 + 0.5e`; empurrão ofensivo do comum usa `0.35 × (0.5 + e)` |
| Vitalidade | Aditiva | Multiplica a vida-base por tamanho e por `0.75 + 0.5e` |
| Velocidade | Aditiva | Multiplica a velocidade-base por `0.8 + 0.4e` |
| Metabolismo | Aditiva | Aumenta fome em `0.1 × (0.5 + e)` por segundo carregado |
| Resistência | Dominante | Armadura: `base + (e - 0.5) × 4`, limitada a 0–20; proteção mineral contra impactos: `min(0.75, configuração × (0.5 + e))` |
| Fertilidade | Aditiva | Multiplica a recuperação reprodutiva por `1.25 - 0.5e` |
| Estabilidade | Aditiva | Ajusta a chance de mutação conforme a média parental |
| Regeneração | Recessiva | Cura do musgo: `(0.5 + e) × configuração`, de 0 a 6 pontos por ativação |
| Potência elemental | Aditiva | Duração de fogo/lama/frio multiplicada por `0.5 + e` e pela configuração, limitada a 200 ticks |
| Agressividade | Dominante | Retaliação `100 + 200e` ticks (100–300); dóceis fogem abaixo de `0.4 - 0.2e` da vida (40–20%) |
| Sociabilidade | Aditiva | Nas espécies sociais: raio de busca `4 + 8e` (4–12 blocos), distância de parada `4 - 2e` (4–2 blocos) |
| Transparência | Aditiva | Alfa-base do gel `round(255 - 102e)` (255–153), combinado com o material visual da espécie |
| Luminosidade | Recessiva | No Luminoso, luz visual do corpo `round(8 + 7e)` (8–15); demais espécies ficam sem emissão própria |
| Pigmentação | Dominante | Multiplica canais RGB da espécie por `0.85 + 0.3e`, limitando cada canal a 255 |

Todos os 15 genes têm expressão implementada. Transparência, luminosidade e
pigmentação têm efeitos de apresentação; a aparência é sincronizada com os clientes
sob Xvfb/Mesa; shaders e outros equipamentos ainda exigem validação. Transparência não concede invisibilidade e luminosidade
não ilumina blocos nem muda spawn. O basal dá ao gel alfa-base 204, antes do
material da espécie. No Luminoso, a emissão basal é 12, com máximo 15.
Potência elemental continua ajustando a duração da Visão Noturna; luminosidade
altera somente o brilho do corpo. Detalhes em [ECOSYSTEM.md](../guides/ECOSYSTEM.md).
O temperamento e a escolha da habilidade continuam definidos pela espécie;
o genoma ajusta os efeitos descritos. Regras detalhadas: [COMBAT.md](../guides/COMBAT.md).

## Linhagem, crescimento e consulta

`Lineage` guarda geração e UUIDs dos dois pais. Fundadores são geração zero;
filhotes recebem a maior geração parental mais um, limitada a um milhão.
O sistema rejeita cruzamento consigo mesmo, entre pai e filho e entre irmãos
ou meios-irmãos. Não mantém uma árvore ancestral ilimitada nem detecta todos
os graus de parentesco.

`GrowthState` guarda duração, tempo restante e tamanho adulto. Filhotes
começam no tamanho 1 e crescem em degraus dentro do tamanho determinado
pelo genoma. Alimentação, conforto, energia e espaço condicionam o progresso.
As regras de nascimento e recuperação estão em [BREEDING.md](../guides/BREEDING.md).

NBT atual versão 7 preserva genoma, linhagem, crescimento, contadores reprodutivos,
histórico/exposição de metamorfose e lar ecológico, acrescentando os genes com
alteração verificada no nascimento. Histórico ausente em saves antigos permanece
indisponível. Regras: [GENETIC_RESEARCH.md](../guides/GENETIC_RESEARCH.md).
Saves anteriores sem lar continuam válidos. Grupos exigem ecologia social da
espécie; sociabilidade ajusta busca e espaçamento, com comportamento basal preservado.
Indivíduos antigos sem os campos adicionais carregam como adultos fundadores, sem
perder UUID, alelos, cuidador ou necessidades. A cápsula também preserva
esses dados e confere seu snapshot com o registro persistente do mundo.

O analisador recebe um snapshot de identificação, pais e alelos, além de
dados de necessidades e contadores sincronizados pelo menu. Ele é somente
leitura, mostra os 15 genes ativos e detalha o histórico de nascimento nos
tooltips. A aba Evolução mostra
origem e condições de metamorfose.

## Genética na evolução

Os híbridos iniciais recebem a espécie definida pela receita e os alelos dos
dois pais pelo mesmo serviço de herança. Metamorfoses mantêm todos os alelos e
a linhagem; o ambiente habilita uma troca de espécie sem reescrever o genoma.
As receitas consultam a expressão atual: Resistência ≥ 0,60 para Cristal,
Regeneração ≥ 0,50 para Floral, Potência elemental ≥ 0,60 para Magmático e
Estabilidade ≥ 0,80 para Ancestral.
A regeneração é recessiva, portanto os dois alelos precisam atingir o limiar.
Detalhes de ambiente, custos e identidade: [EVOLUTION.md](../guides/EVOLUTION.md).

**Planejado:** epistasia, expressão genética condicionada ao ambiente
e categorias raras de mutação. Os dois
cruzamentos e as quatro metamorfoses atuais são o primeiro incremento desses
sistemas; não completam toda a diversidade prevista na especificação.

## Estabilizador de mutação

Uma aplicação em um pai apto, antes da geleia, zera novas mutações do próximo
nascimento do par. A escolha de alelos e a expressão continuam as mesmas; valores
incomuns herdados não são apagados. O histórico do filhote é conhecido sem nova
alteração. A proteção só é removida após inserção aceita do filhote, não em
cancelamento, falta de espaço ou fim de prontidão. NBT atual 7 mantém a evidência
de mutações introduzida na versão 6. Regras: [MATERIALS.md](../guides/MATERIALS.md).
