# Combat and Abilities

<a id="combate-e-habilidades"></a>
<a id="energia-recarga-e-configurações"></a>
<a id="principais-efeitos"></a>
<a id="quando-uma-habilidade-funciona"></a>
<a id="reações-elementais"></a>

## Bonded companions in 0.17.0

Bonded slimes use the new [47-species companion combat system](COMPANION_COMBAT.md). It defines their roles, attacks, support, energy, and recovery. The ecological examples below describe wild species and general elemental traits. Companion-specific rules take precedence for bonded slimes.

## Activation requirements

Offensive slime abilities require an adult, a valid target, sufficient energy, and an available cooldown. Physical contact must be accepted before contact effects apply. Juveniles do not deal contact damage.

Genes affect strength, duration, regeneration, and defense. Species values are baselines; individuals may perform differently. Inspect the slime you are raising with the analyzer.

## Main effects

| Group | Examples |
|---|---|
| Mobility and knockback | Common attacks with jumps; Water pushes and extinguishes; Wind creates gusts and cushions falls |
| Fire and cold | Fire ignites; Ice chills and extinguishes burning targets; Magma recovers in lava |
| Recovery | Moss and Floral regenerate under favorable conditions; Fungal benefits from nearby mushrooms |
| Control | Mud slows; Sand blinds; Fungal weakens; Venom leaves a toxic cloud |
| Mineral defense | Stone, Iron, and Obsidian offer different impact defenses |
| Crystals and electricity | Crystal fires shards; Electric can chain discharges through wet targets; Amethyst reveals threats |
| Dimensional forms | End teleports away; Void pulls threats; Ancestral protects an injured caretaker |

Browse all 47 species in the [gallery](SLIMES.md). [Hybrids and metamorphoses](EVOLUTION.md) have their own ability, cost, and cooldown combinations.

## Elemental reactions

Water, rain, and bubbles hinder Fire's ignition, and Fire takes damage when wet. Ice extinguishes burning targets, resists freezing, and is vulnerable to fire. Electrical discharges are stronger against wet targets and have limited propagation. Suitable terrain supports regeneration, resonance, and magmatic recovery.

Line of sight, allies, caretaker relationships, and target conditions are checked. Damage, healing, status, and knockback cancellations preserve their respective protections. Slime abilities do not alter terrain.

## Energy and configuration

Valid activations use the species' energy cost and cooldown. Passive defenses follow their own conditions. Hunger and comfort influence energy recovery: maintain a suitable [habitat](CARE.md).

[Server settings](../CONFIGURATION.md) control abilities, costs, damage, duration, sounds, and particles. [Bosses](BOSSES.md) have separate patterns, contact effects, and summons; see [balance values](../BALANCE.md).
