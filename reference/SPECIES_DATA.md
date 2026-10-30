# Espécies e datapacks

[Documentação](../README.md) · [Galeria e dietas](../guides/SLIMES.md) · [Genética](GENETICS.md)

## Definições de espécie

Cada arquivo `data/<namespace>/slime_species/<nome>.json` descreve uma espécie.
O campo `id` deve coincidir com `<namespace>:<nome>`. As 47 definições incluídas
estão em `src/main/resources/data/slimeevolution/slime_species/`.

| Campo | Formato |
|---|---|
| `id`, `family` | IDs com namespace |
| `color` | RGB inteiro de 0 a 16.777.215 |
| `min_size`, `max_size` | Inteiros entre 1 e 4; mínimo ≤ máximo |
| `stats` | Vida 1–200, velocidade 0,01–0,6, dano 0–30, armadura 0–20 e elasticidade 0,5–1,5 |
| `temperament` | `docile`, `neutral` ou `hostile` |
| `ecology` | `solitary`, `social` ou `territorial`; padrão `solitary` |
| `diet` | IDs de itens existentes |
| `biomes` | IDs explícitos de biomas existentes |
| `natural_spawn` | Booleano; padrão `true` |
| `ability` | ID de uma habilidade registrada no mod |
| `ability_cooldown_ticks` | 20–12.000 ticks |
| `ability_energy_cost` | 0–100 |

Os atributos-base de espécie correspondem ao tamanho 2, antes da expressão
genética. As 26 espécies derivadas incluídas usam `natural_spawn: false`.
Para permitir spawn em biomas adicionais, inclua-os também na tag
`slimeevolution:spawns_evolution_slimes`, com `replace: false`.

Novas espécies podem reutilizar a entidade e as habilidades existentes.
Habilidades novas exigem implementação e registro em Java. A cápsula básica
aceita as 47 espécies incluídas; novos IDs não recebem permissão de captura
implicitamente.

## Reprodução

`data/<namespace>/slime_breeding/<nome>.json` define o resultado de um par:

```json
{
  "first": "slimeevolution:common",
  "second": "slimeevolution:common",
  "offspring": "slimeevolution:common"
}
```

A ordem dos pais não altera o par. Duplicatas, inclusive em ordem inversa,
são recusadas. Ausência de receita bloqueia a combinação. Cuidador,
necessidades, parentesco e espaço continuam sendo verificados pelo servidor.

## Metamorfoses

Arquivos em `data/<namespace>/slime_metamorphosis/` definem origem, destino,
catalisador, condições de ambiente/gene/idade/exposição e custos.
As 14 receitas incluídas oferecem exemplos completos. O uso em jogo está
no [guia de evolução](../guides/EVOLUTION.md).

## Habitats e recarregamento

Pisos preferidos usam tags em
`data/<namespace>/tags/block/habitat/<espécie>.json`. Adicione a tag correspondente
a uma nova espécie para que o recinto seja avaliado corretamente.

Após alterar o datapack, execute `/reload` e confira o log. O catálogo de
espécies, reprodução e metamorfoses é validado antes de ser publicado em conjunto;
um pacote inválido conserva o estado anterior. Alterar uma rota pode invalidar
exposição incompatível já acumulada.

Com comandos habilitados, uma definição pode ser conferida com:

```mcfunction
/summon slimeevolution:evolution_slime ~ ~ ~ {Species:"seunamespace:sua_especie"}
```

Revise aparência, atributos, salvamento e reprodução em um mundo de teste.

## Condições ambientais opcionais de metamorfose

Receitas antigas continuam válidas sem os campos abaixo, que ficam dentro de
`conditions`. O analisador mostra essas condições no tooltip da linha de biomas.

| Campo | Valores / padrão |
|---|---|
| `cycle` | `any`, `day`, `night`; padrão `any` |
| `weather` | `any`, `clear`, `rain`, `thunder`; padrão `any` |
| `sky_visible` | Booleano; padrão `false` |
| `min_y`, `max_y` | Inteiros de −2048 a 2048, limites inclusivos; padrão −2048/2048 |
| `moon_phase` | −1 para qualquer fase, 0 para lua cheia, até 7; padrão −1 |
| `submerged` | Booleano; exige olhos sob água quando `true`; padrão `false` |

Dia, noite, lua e céu aberto exigem dimensão com iluminação celeste. A receita
`glacial_aquatic_to_abyssal` demonstra profundidade/submersão; `fire_to_solar`,
`luminous_to_lunar` e `storm_to_supercell` demonstram horário, lua e clima.

## Marcos de metamorfose

Receitas de `slime_metamorphosis` podem declarar o campo opcional `milestone`:
`storm_charges`, `biome_journey` ou `celestial_observations`. O padrão vazio
mantém receitas antigas. Valores desconhecidos são rejeitados no carregamento.
O marco complementa as condições de cuidado, genes, exposição e catalisador;
não substitui essas verificações. Consulte [os requisitos](../guides/ASCENSION.md).
