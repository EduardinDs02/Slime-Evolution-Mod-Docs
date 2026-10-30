# Valores de balanceamento

Esta referência reúne os custos de crescimento e os parâmetros de chefes da
versão 0.5.0. Dificuldade percebida e economia de uma campanha survival
continuam sujeitas a feedback de jogo; não são garantidas por uma simulação.

## Crescimento e custos

O crescimento natural padrão exige 12.000 ticks carregados e em boas condições
(dez minutos). O tempo para obter e cuidar dos pais é adicional.
Cada ciclo manual da incubadora leva 200 ticks e cobra um alimento e um suplemento
apenas na conclusão. Não há ciclo automático, e o token da cápsula é renovado.

| Suplemento | Crescimento por ciclo | Ciclos para um recém-nascido padrão | Tempo carregado | Alimentos/suplementos |
|---|---:|---:|---:|---:|
| Geleia | 1.200 | 10 | 100 s | 10 / 10 |
| Catalisador | 2.400 | 5 | 50 s | 5 / 5 |
| Geleia Real | 3.600 | 4 | 40 s | 4 / 4 |

Esses resultados vêm da aplicação repetida das regras de produção, com
necessidades válidas. Não incluem coleta, fabricação, abertura de menus ou
intervalos entre cliques. Crescimento adicional não envelhece o indivíduo na
mesma proporção: os três casos acrescentam 2.000/1.000/800 ticks de idade.
Mudar growthTicks afeta os próximos nascimentos; filhotes existentes conservam
sua duração. O suplemento real recompensa o Rei e é opcional.

## Chefes

Valores em pontos de vida, antes de armadura/efeitos: dois pontos são um coração.
Os quatro encontros anunciam ataques e verificam distância, altura e cobertura.
Os interiores dos anéis, cruzes e orbitais foram preenchidos na 0.5.0.
O ritual consome o item após inserir o chefe e impede sobreposição em 96 blocos.

| Chefe | Vida em 0.5.0 | Armadura | Famílias de ataque | Dano bruto por fase |
|---|---:|---:|---:|---|
| Rei Gelatinoso | 290 | 7 | 4 | 9 / 12,6 |
| Coração Magmático | 320 | 6 | 4 | 9 / 12,6; erupções 7,5 / 10,5 |
| Colosso Cristalino | 400 | 10 | 4 | 7,5 / 10,5 |
| Primordial | 540 | 8 | 5 | 7,5 / 10,5 / 14,7 |

O cálculo é `base × 1,5 × 1,4^fase × configuração`. Não há o antigo teto de
12 pontos: com configuração dois, o maior golpe é 29,4. Água reduz o dano do
Coração pela metade depois desse cálculo. Preparações conservam a fase inicial.
Os corpos físicos e visuais dos quatro chefes são 1,5 vez maiores.

O Rei conserva seis lacaios: guardas (24 de vida, dano quatro/Fraqueza II),
curandeiros (18, cura nove a cada 80 ticks) e cuspidores (20, dano três,
Lentidão I/Veneno I). Os avanços têm no máximo sete fragmentos. O Primordial
chama até três ecos voadores e o Coração até quatro lacaios de fogo/magma;
reservas e expiração impedem duplicação por descarregamento. Invocações novas
usam o multiplicador geral e a fase do dono em seu dano de base três/quatro.
[Efeitos e comportamento dos bosses](guides/BOSSES.md).

As recompensas de vitória creditada a jogador são duas unidades por chefe.
Rei: Geleia Real; Coração: Fragmento Ígneo; Colosso: Estilhaço Prismático;
Primordial: Essência Primordial. Lacaios não geram loot/XP nem se dividem.
Os amuletos têm usos finitos cobrados em dano aceito. A progressão do selo final
exige recompensas dos chefes anteriores, Essência Ancestral e Tabuleta Antiga;
as formas raras preservam a identidade em metamorfose, sem gerar um clone.

## Referências

[Bosses](guides/BOSSES.md) · [Reprodução](guides/BREEDING.md) ·
[Incubadora](guides/INCUBATOR.md) · [Configurações](CONFIGURATION.md)

## Treinamento e simbiose

| Ação | Custo | Condições e recuperação |
|---|---|---|
| Lição | 5 energia, +3 fome, até +1 confiança | Confiança 40, energia 40, fome até 60, conforto 40; 200 ticks |
| Horta de Água + Musgo | 6 energia e +3 fome de cada parceiro | Um estágio de uma planta por ação; recuperação compartilhada de 400 ticks |
| Pesquisa de Elétrico + Ferro | 2 energia e +1 fome de cada parceiro | Até quatro ticks de progresso extra; recuperação compartilhada de 20 ticks |

Lições concedem `4 + piso(sociabilidade × 4) + piso(estabilidade × 2)` pontos,
com limite 100. Esperar exige 20, Seguir 40 e Voltar ao lar 60. A simbiose exige
adultos calmos, confiança 40, energia 30, fome até 60 e conforto 40, com consentimento
e cuidador comum. Custos de receitas e resultados das máquinas permanecem iguais.

[Uso e limites](guides/COMPANIONS.md).

## Funções individuais

| Função | Recurso/resultado | Custo | Intervalo |
|---|---|---|---|
| Fogo | Até +20 ticks em uma fornalha que esteja processando, a até 4 blocos | 2 energia, +1 fome | 20 ticks por ajudante |
| Fúngico | 8 compostáveis → 1 farinha de osso | 6 energia, +3 fome | 200 ticks de trabalho |
| Abyssal | Até +60 de ar e 300 ticks de visão noturna ao cuidador submerso a até 6 blocos | 2 energia, +1 fome | 40 ticks |
| Âmbar | 3 compartimentos de até 16 itens cada | Sem custo de armazenamento | Respeita o limite natural de cada item |

As funções ativas exigem adulto calmo, confiança 40, energia 30, fome até 60 e
conforto 40. Depósitos exigem confiança 40; a retirada dos pertences não exige
essa confiança. [Condições e limites](guides/SPECIALIZATIONS.md).

## Circuitos, sonar e vitrine

| Função | Custo e alcance | Parâmetros |
|---|---|---|
| Elétrico | 2 energia e +1 fome por pulso; saída a até 6 blocos | Treino 20; força 15; intervalo 20/40/80/160 ticks e duração 2/4/8/10 ticks |
| Cristal | 4 energia e +2 fome ao encontrar eco; raio 12 | Treino 20; concentração de pelo menos 4 minerais por setor; recuperação de 200 ticks mesmo sem eco |
| Cristal Energizado | 1 energia no início e por 20 ticks de sinal ativo | Treino 40; entrada/saída separadas por 4–32 blocos; intensidade analógica 0–15 |
| Vidro | Um objeto; exposição e ampliação sem custo | Depósito exige confiança 40; zoom visual de 1,5× |

[Uso e limites](guides/SIGNAL_JOBS.md). Os onze trabalhos anteriores estão
em [produção, transporte e auras](guides/WORK_JOBS.md).
