# Care and Capture

<a id="alimentador"></a>
<a id="alimentação-e-necessidades"></a>
<a id="cuidado-e-captura"></a>
<a id="cuidador-e-confiança"></a>
<a id="cápsula"></a>
<a id="receitas"></a>
<a id="recinto"></a>

[Species and diets](SLIMES.md) · [Breeding](BREEDING.md) · [Companions](COMPANIONS.md)

## Feeding and needs

Use a food from the species' diet directly on a slime. An accepted meal consumes one item in Survival, reduces hunger by 20, and restores 10 energy. The slime must have at least 20 hunger and wait five seconds between meals.

Crouch and interact with an empty hand to inspect needs. Values range from 0 to 100: low hunger is good; high energy, comfort, and trust are good. Metabolism and habitat affect hunger and energy recovery.

## Caretaker and trust

The first player to feed a slime manually becomes its caretaker. Other players may feed it, but do not take over the bond.

| Temperament | Trust per meal from caretaker | Trust required for capture |
|---|---:|---:|
| Docile | 20 | 20 |
| Neutral | 15 | 40 |
| Hostile | 10 | 70 |

Hostile slimes stop selecting their caretaker as a target at 20 trust. Hurting your own slime removes 20 trust and can provoke retaliation. A bond supports care and capture; [training](COMPANIONS.md) unlocks commands and cooperation.

## Enclosures

Preferred biomes, suitable flooring, moisture, and nearby population influence comfort. Avoid overcrowding. Fire suffers in water; Ice is vulnerable to fire. Build barriers and roofs appropriate to the species. Habitat tags can be changed with [datapacks](../reference/SPECIES_DATA.md).

## Feeder

![SolarPunk Feeder](../assets/blocks/feeder.png)

The Feeder has **nine slots** and supports hoppers. Every two seconds it tries to feed a hungry slime within four blocks and clear line of sight, using compatible food and respecting the individual's meal cooldown. It neither assigns a caretaker nor increases trust. Its reservoir and tray face you when placed.

## Capsules

Use an empty capsule on a **size-1 or size-2** slime with sufficient caretaker trust, at least half health and 10 energy, no combat or damage in the last five seconds, and no leash, mount, or passengers.

Only the caretaker can capture and release it. Use an occupied capsule on solid, dry ground with free space. A rejected release keeps the slime in its capsule. Bosses and minions cannot be captured.

Capsules preserve identity, genes, health, age, trust, and cooldowns. The individual is suspended while captured. Losing its occupied capsule makes it inaccessible through normal gameplay. Captures belong to their original world: [back up the entire world](../INSTALLATION.md).

Recipes unlock after obtaining a slimeball. A second capsule recipe uses **one Slime Core and one glass block**. See [materials](MATERIALS.md).
