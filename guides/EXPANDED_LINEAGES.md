# Expanded lineages


**0.25.0:** Reef, Boreal and Abyssal Beacon were removed; existing specimens migrate to Coral, Blizzard and Bioluminescent. [New concepts](../updates/0.25.0.md).
[Player guide](../README.md) · [Evolution](EVOLUTION.md) · [Companion combat](COMPANION_COMBAT.md)

Version **0.24.0** adds **16 acquired species**, for a total of **60**. None of these sixteen spawns naturally. Breeding creates a new child at level 1; metamorphosis preserves the individual, UUID, genes, keeper, level, orders and inventory.

## Six new crosses

| Parents, in either order | Child |
|---|---|
| Coral Slime + Luminous Slime | Bioluminescent Slime |
| Floral Slime + Hive Slime | Pollinator Slime |
| Ice Slime + Wind Slime | Blizzard Slime |
| Iron Slime + Crystal Slime | Geode Slime |
| Obsidian Slime + Soul Slime | Ash Guardian Slime |
| Sand Slime + Electric Slime | Fulgurite Slime |

The complete registry has **79 breeding pairs**: 62 same-species pairs and 20 crosses. Phoenix cannot breed; each specimen must complete its own ritual. Existing care, ancestry, population, food and cooldown checks apply.

## Seven metamorphoses

| Route | Catalyst | Floor | Level / trust | Exposure |
|---|---|---|---|---|
| Ash Guardian Slime → Phoenix Slime | `slimeevolution:primordial_essence` | `minecraft:gold_block` | 10 / 90 | 300 s |
| Geode Slime → Adamantine Slime | `slimeevolution:prismatic_shard` | `minecraft:diamond_block` | 8 / 80 | 300 s |
| Iron Slime → Steel Slime | `minecraft:iron_block` | `minecraft:blast_furnace` | 4 / 40 | 120 s |
| Mycelium Slime → Cordyceps Slime | `minecraft:spore_blossom` | `minecraft:moss_block` | 4 / 40 | 120 s |
| Obsidian Slime → Volcanic Slime | `slimeevolution:igneous_fragment` | `minecraft:magma_block` | 5 / 40 | 120 s |
| Sand Slime → Mirage Slime | `minecraft:phantom_membrane` | `minecraft:glass` | 4 / 40 | 120 s |
| Sculk Slime → Resonant Slime | `minecraft:echo_shard` | `minecraft:sculk` | 5 / 40 | 120 s |

All ordinary routes require age 48,000 ticks and the listed gene at 0.65 or higher; advanced routes require age 96,000 ticks and gene 0.85 or higher. Minimum needs: comfort 60, energy 60, hunger at most 40, an adult with a keeper and no combat. Catalyst use rechecks all conditions before spending one item. Exposure advances only while valid and pauses otherwise.

- **Phoenix Slime**: `minecraft:basalt_deltas`, `minecraft:nether_wastes`; `regeneration`.
- **Adamantine Slime**: `minecraft:dripstone_caves`, `minecraft:stony_peaks`; `resistance`.
- **Steel Slime**: `minecraft:stony_peaks`, `minecraft:jagged_peaks`, `minecraft:windswept_hills`; `resistance`; lit blast furnace.
- **Cordyceps Slime**: `minecraft:lush_caves`; `regeneration`; light 7 or less.
- **Volcanic Slime**: `minecraft:basalt_deltas`, `minecraft:nether_wastes`; `resistance`.
- **Mirage Slime**: `minecraft:desert`; `elasticity`; daytime, clear weather and open sky.
- **Resonant Slime**: `minecraft:deep_dark`; `elemental_power`; light 7 or less and an active sculk sensor within 4 blocks; generate vibrations while the slime remains calm.

## Abilities and limits

- **Geode Slime**: Stores received impacts and releases a fragment shockwave.
- **Pollinator Slime**: Healing pollen restores nearby allies and weakens its marked target.
- **Blizzard Slime**: Frost bolts build chill; three hits briefly root ordinary enemies.
- **Fulgurite Slime**: A focused glass lance exposes armour without chaining to other enemies.
- **Bioluminescent Slime**: Living light marks a target, increasing damage from companions of the same keeper.
- **Ash Guardian Slime**: An ash shield retaliates against its attacker when its absorption breaks.
- **Mirage Slime**: Creates a short-lived decoy that distracts ordinary attackers; bosses resist it.
- **Steel Slime**: Reduces physical damage and fractures the armour of its target.
- **Cordyceps Slime**: Implants spores that burst after three further allied companion hits.
- **Resonant Slime**: A vibration pulse interrupts ordinary enemies and exposes a weak point.
- **Volcanic Slime**: Received impacts build pressure for a concentrated eruption.
- **Adamantine Slime**: A slow fortress with reinforced armour and an impact-powered shockwave.
- **Phoenix Slime**: Prevents one nearby ally’s defeat per boss encounter, with a five-minute cooldown shared by the keeper.

Light marks add 5%, 10% or 15% damage according to their source and apply only to companions with the same keeper. Cordyceps requires three further accepted companion hits; rejected hits and other keepers do not advance the implant. Frost control has shared immunity; the new freeze and interrupt abilities do not hard-stun bosses. Mirage decoys last three seconds and cannot be saved, captured, bred or looted. Boreal reduces incoming projectile damage by 25% while its ward lasts.

**Phoenix:** an adult following its keeper can prevent a nearby player or bonded slime from dying, within eight blocks and line of sight, with 24 energy. The victim returns at 30% health with two seconds of resistance. The five-minute cooldown belongs to the keeper, is shared by all Phoenix copies, survives saving and player respawn, and does not reset when a guardian is captured. A living boss that already triggered this protection cannot trigger it again, even after the timer. Administrative damage bypasses this protection.
