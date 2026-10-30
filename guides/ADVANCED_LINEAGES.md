# Híbridos avançados e metamorfoses raras

O mod tem **47 espécies, 61 receitas de reprodução e 14 metamorfoses**.
As 26 espécies derivadas ficam fora do spawn natural e não recebem ovos.
Herdam os quinze genes, pais e geração pelo fluxo normal de reprodução; filhotes
crescem com comida, conforto e espaço. Cápsulas, estação, incubadora e diário
continuam usando NBT 7 e diário 3, sem apagar saves antigos.

## Cruzamentos avançados

| Pais, em qualquer ordem | Filhote | Características |
|---|---|---|
| Fogo + Água | Vapor (`steam`) | Véu de cegueira limitado a cinco segundos; dieta de alga e pó de blaze |
| Água + Gelo | Aquático Glacial (`glacial_aquatic`) | Jato que empurra/apaga e resfria, respiração aquática, imunidade a congelamento, fraqueza a fogo |
| Cristal + Elétrico | Cristal Energizado (`energized_crystal`) | Estilhaços/refração, guarda mineral e descarga ao contato com condução limitada |
| Vento + Fogo | Chama Volátil (`volatile_flame`) | Rajada e ignição, queda reduzida, imunidade ao fogo e dano por água |
| Musgo + Água | Pantanoso (`bog`) | Caminho alternativo; Musgo + Lama continua válido |

Efeitos compostos compartilham **um custo de energia e uma recarga** do
indivíduo. Aliados/cuidadores ficam protegidos. Custo só ocorre se alguma
parte do efeito for aceita. Todos os novos resultados podem reproduzir com
sua própria espécie, inclusive as formas raras depois da primeira aquisição.
Não há cruzamento genérico que transforme qualquer par em uma espécie rara.

## Rotas raras

| Rota | Substrato / bioma | Requisitos mínimos | Catalisador / custo |
|---|---|---|---|
| Cristal → Prismático (`prismatic`) | Ametista / Picos Rochosos ou Cavernas de Espeleotemas | Adulto; 48.000 ticks de idade; luminosidade expressa ≥0,85; 12.000 ticks de exposição válida | 1 Estilhaço Prismático; 40 energia; +30 fome |
| Ancestral → Celestial (`celestial`) | Púrpura / Terras Altas do End | Adulto; 96.000 ticks de idade; estabilidade expressa ≥0,90; 18.000 ticks de exposição válida | 1 Essência Primordial; 50 energia; +35 fome |

Ambas exigem cuidador, confiança suficiente, calma, fome até 40, conforto a
partir de 60 e energia a partir de 60, além do custo. Exposição conta somente
em ticks carregados nas condições certas e pausa fora delas; não cresce dentro
da cápsula ou em chunks descarregados. Use o catalisador agachado. O analisador
mostra a rota e o progresso, sem editar dados. Gene expressa é o fenótipo:
luminosidade é recessiva e exige os dois alelos elevados.

Prismático mantém projéteis/refração e defesa mineral, com vida/mobilidade
moderadamente maiores; Celestial mantém a proteção ancestral ao cuidador,
com recarga menor e custo maior. São metamorfoses de uma criatura existente,
sem criar outra entidade, curar por completo ou mudar alelos. Preservam UUID,
linhagem, cuidador, confiança, idade, proporção de vida, recargas, proteção
reprodutiva e proveniência de mutação; o histórico registra a transformação.
A Slimepedia registra apenas o nascimento ou transformação realmente observado
pelo cuidador, sem conceder a descoberta por obter um troféu.

Requisitos, custos e habitats são JSON/tags recarregáveis. Falha na validação
mantém o snapshot anterior; mudar requisitos invalida exposição incompatível.
Os dados dos indivíduos são preservados.

Regras gerais: [BREEDING.md](BREEDING.md), [EVOLUTION.md](EVOLUTION.md).
Recompensas dos catalisadores: [bosses e recompensas](BOSSES.md).

## Novas linhagens adquiridas

A 0.7.0 acrescenta 15 espécies em três grupos. Elas usam o mesmo cuidado,
parentesco, crescimento, captura e herança genética das demais.

### Breeding

| Pais | Filhote | Característica |
|---|---|---|
| Elétrico + Vento | Tempestade | Nuvem com chuva, tornado escuro e descargas/rajadas com energia compartilhada |
| Água + Floral | Coral | Aglomerado de dezoito árvores ramificadas; recupera aliados na água, enquanto molhado |
| Areia + Fogo | Vidro | Gel transparente com bordas, sem cristais, refração de flechas e camuflagem breve quando ameaçado |
| Ferro + Água | Ferrofluido | Atrai até oito itens metálicos lançados pelo cuidador, com visão livre e alcance de seis blocos |
| Fúngico + Musgo | Micélio | Esporos recuperam aliados próximos |
| Venenoso + Magma | Cáustico | Poças de três segundos aplicam veneno e fraqueza |

### Metamorfoses

Estas cinco rotas exigem 24.000 ticks de idade, 6.000 ticks de exposição válida,
30 de energia e +25 de fome na conclusão, além do cuidado geral.

| Origem → destino | Ambiente e piso | Catalisador / gene |
|---|---|---|
| Musgo → Âmbar | Floresta Florida ou Planície de Girassóis; bloco de musgo | Favo de mel; regeneração ≥0,65 |
| Aquático Glacial → Abissal | Oceano Frio Profundo ou Oceano Congelado Profundo; prismarinho; totalmente submerso em Y ≤40 | Bolsa de tinta brilhante; luminosidade ≥0,65 |
| Corrompido → Sculk | Profundezas Sombrias; sculk | Fragmento de eco; potência elemental ≥0,70 |
| Fogo → Solar | Planície, Planície de Girassóis ou Deserto; bloco de ouro; dia, tempo limpo e céu aberto | Catalisador Solar; potência elemental ≥0,65 |
| Luminoso → Lunar | Planície, Prado ou Planície Nevada; calcita; noite de lua cheia e céu aberto | Fragmento de ametista; luminosidade ≥0,65 |

Âmbar aplica lentidão; Abissal combina escuridão e lentidão. Sculk responde ao
movimento de inimigos com pulsos de eco. Solar recupera vida sob o sol e aplica
ignição; Lunar concede visão noturna ao cuidador próximo durante a noite.

O Catalisador Solar é fabricado com um lingote de ouro, dois girassóis,
um fragmento de ametista e um pó de blaze: ouro acima, `girassol / ametista /
girassol` no meio e pó de blaze abaixo.

### Evoluções avançadas

As três metamorfoses abaixo exigem 96.000 ticks de idade, 12.000 ticks de
exposição, 40 de energia e +25 de fome. Eclipse nasce por cruzamento.

| Linha | Condições finais | Característica |
|---|---|---|
| Elétrico + Vento → Tempestade → Supercélula | Picos Ventosos ou Picos Pedregosos Ventosos; para-raios; tempestade e céu aberto; carga de vento; potência elemental ≥0,90 | Rajadas e descargas encadeadas em até dois alvos adicionais |
| Musgo → Âmbar → Colmeia | Floresta Florida ou Planície de Girassóis; bloco de favo de mel; favo de mel; regeneração ≥0,85 | Dois pequenos polinizadores temporários e coleta de mel |
| Pedra → Cristal → Prismático → Aurora | Picos Congelados ou Espigões de Gelo; gelo azul; noite de céu aberto; Estilhaço Prismático; estabilidade ≥0,90 | Faixas luminosas e resistência para aliados próximos |
| Solar + Lunar → Eclipse | Solar carregado + Lunar de Lua Nova; ritual ao entardecer com Estilhaço Prismático | Alterna ignição e lentidão a cada ativação aceita; conserva o ciclo ao salvar |

A Colmeia produz um frasco de mel ao usar uma garrafa de vidro, com os
[requisitos de coleta](PROGRESSION.md): 20 de energia, +10 de fome e 6.000 ticks
de recuperação. Os polinizadores vivem até 200 ticks, recuperam slimes aliados
e desaparecem ao perder a Colmeia. O limite é dois por Colmeia.

Efeitos ofensivos preservam as proteções de cuidador, colônia e aliados.
As poças e os polinizadores têm duração limitada; energia, recargas e as opções
de habilidades, dano, cura, partículas e sons continuam valendo.

As aparências raras acompanham seus temas: Ferrofluido tem uma cobertura de
36 espinhos; Cáustico borbulha e solta fumaça; Abissal tem cauda, nadadeiras
e uma grande isca luminosa; Sculk tem chifres inspirados no Warden. Solar
exibe raios e Lunar, lua cheia e crateras. O Âmbar conserva objetos decorativos
na resina — graveto, pedregulho e uma picareta com seis materiais possíveis,
fixada para cada indivíduo. A Colmeia apresenta favos, mel e abelhas; Aurora
tem gradiente no corpo e faixas animadas; Eclipse tem silhueta escura e corona.

## Marcos adicionais de conquista

Os requisitos da tabela se somam aos [cinco rituais de conquista](ASCENSION.md):
três cargas conduzidas para Supercélula, três biomas para Aurora, Selo
Primordial para Ancestral e vínculo, pesquisa e três observações para Celestial.
Aurora também exige tempo limpo. Consulte esse guia antes de consumir catalisadores.
