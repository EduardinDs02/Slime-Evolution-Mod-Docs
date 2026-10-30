# Species and Datapacks

<a id="condições-ambientais-opcionais-de-metamorfose"></a>
<a id="definições-de-espécie"></a>
<a id="espécies-e-datapacks"></a>
<a id="habitats-e-recarregamento"></a>
<a id="marcos-de-metamorfose"></a>
<a id="metamorfoses"></a>
<a id="reprodução"></a>

## Species definitions

Each `data/<namespace>/slime_species/<name>.json` defines a species. Its `id` must match `<namespace>:<name>`. The mod includes 47 definitions.

| Field | Format |
|---|---|
| `id`, `family` | Namespaced IDs |
| `color` | Integer RGB, 0–16,777,215 |
| `min_size`, `max_size` | Integers 1–4, minimum ≤ maximum |
| `stats` | Health 1–200, speed 0.01–0.6, damage 0–30, armor 0–20, elasticity 0.5–1.5 |
| `temperament` | `docile`, `neutral`, or `hostile` |
| `ecology` | `solitary`, `social`, or `territorial`; default `solitary` |
| `diet` | Existing item IDs |
| `biomes` | Explicit existing biome IDs |
| `natural_spawn` | Boolean; default `true` |
| `ability` | Registered mod ability ID |
| `ability_cooldown_ticks` | 20–12,000 ticks |
| `ability_energy_cost` | 0–100 |

Base species attributes correspond to size 2 before genetic expression. The 26 included derived species use `natural_spawn: false`. For additional spawn biomes, also extend `slimeevolution:spawns_evolution_slimes` with `replace: false`.

New species can reuse the entity and existing abilities; new abilities need Java implementation and registration. New IDs are not automatically allowed by basic capsules.

## Breeding

Define pairs under `data/<namespace>/slime_breeding/<name>.json`:

```json
{
  "first": "slimeevolution:common",
  "second": "slimeevolution:common",
  "offspring": "slimeevolution:common"
}
```

Parent order does not matter. Duplicate or reversed duplicate pairs are rejected. Missing recipes block a combination. Caretaker, needs, relatedness, and space checks still apply.

## Metamorphoses

Files under `data/<namespace>/slime_metamorphosis/` define source, result, catalyst, environment, gene, age, exposure, and costs. Use the 14 included recipes as complete examples. See [evolution](../guides/EVOLUTION.md).

## Habitats and reloading

Preferred floors use `data/<namespace>/tags/block/habitat/<species>.json`. Add the appropriate tag for habitat evaluation. Run `/reload` and inspect the log after editing a datapack.

Species, breeding, and metamorphoses are validated as one snapshot; invalid data keeps the previous snapshot. Changed routes can invalidate incompatible exposure.

```mcfunction
/summon slimeevolution:evolution_slime ~ ~ ~ {Species:"yournamespace:your_species"}
```

Test appearance, attributes, persistence, and breeding in a test world.

## Optional environmental conditions

These fields belong inside `conditions`; old recipes remain valid without them.

| Field | Values / default |
|---|---|
| `cycle` | `any`, `day`, `night`; default `any` |
| `weather` | `any`, `clear`, `rain`, `thunder`; default `any` |
| `sky_visible` | Boolean; default `false` |
| `min_y`, `max_y` | Inclusive integers −2048 to 2048; defaults −2048 / 2048 |
| `moon_phase` | −1 for any, 0 for full moon, up to 7; default −1 |
| `submerged` | Requires eyes underwater when true; default `false` |

Day, night, moon, and sky checks require a dimension with skylight. The analyzer displays these conditions in its biome-line tooltip.

## Metamorphosis milestones

Optional `milestone` values are `storm_charges`, `biome_journey`, and `celestial_observations`. An empty value preserves old recipes; unknown values are rejected. Milestones supplement rather than replace care, genes, exposure, and catalyst checks. See [ascension requirements](../guides/ASCENSION.md).
