# Structures and Natural Arenas

<a id="estruturas-e-arenas-naturais"></a>
<a id="exploração-e-frequência"></a>
<a id="invocar-no-altar"></a>
<a id="proteção-das-arenas"></a>

Six structures generate in **new chunks** when structure generation is enabled. Each has its own architecture, materials, lighting, and SolarPunk details.

| Structure ID after `slimeevolution:` | Allowed biomes | Contents |
|---|---|---|
| `royal_court` | Plains, Sunflower Plains, Swamp | 39×23×39 court, towers, battlements, green banners, crown crest, moat; Gelatinous King altar |
| `elemental_sanctuary` | Plains, Desert, Savanna | 39×23×39 sanctuary, colonnades, four elemental gardens; Magmatic Heart altar |
| `crystal_cavern` | Stony Peaks, Dripstone Caves, Plains, Forest | 35×24×35 underground cavern, calcite arches, dome, amethyst clusters; Crystalline Colossus altar |
| `ancestral_chamber` | End Highlands, End Midlands | 39×25×39 chamber, buttresses, vaults, halo, glass; Primordial Slime altar |
| `gelatinous_lake` | Swamp, Mangrove Swamp, Plains | 29×16×29 lake, organic banks, walkways, trees, copper pavilions |
| `researcher_ruins` | Plains, Forest, Taiga | 31×20×31 ruins, two-story library, mezzanine, laboratory, overgrown copper greenhouse |

![Royal Court](../assets/sites/royal_court.png)

## Summon at an altar

The four arenas have central engraved pedestals and **17×17 floor space with six clear blocks above**.

| Arena | Ritual item | Boss |
|---|---|---|
| Royal Court | Gelatinous Crown | Gelatinous King |
| Elemental Sanctuary | Magma Brazier | Magmatic Heart |
| Crystal Cavern | Crystal Sigil | Crystalline Colossus |
| Ancestral Chamber | Primordial Seal | Primordial Slime |

Structures start without bosses. An accepted Survival summon consumes one item. The altar remains reserved until that boss dies, including across unloading and server restarts. Rejected uses do not consume ritual items. After victory, the altar can be reused. Ordinary floors cannot start rituals.

## Arena protection

All four boss arenas remain protected before, during, and after fights, including in Creative. Protection covers the structure, foundations, and an outer margin. It blocks breaking, placement, fluid changes, explosion damage to blocks, pistons, and indirect terrain changes from fire, dispensers, falling blocks, fluids, or mobs.

Altars, chests, and reward collection remain accessible. Attacks and explosions can still affect entities. Protection persists independently of structure-generation settings. Lakes and researcher ruins are unprotected exploration sites.

## Exploration and frequency

Each structure contains one finite loot chest; opening, emptying, or reloading it does not refill it. The Ancestral Chamber supplies an **Ancient Tablet** for the Primordial Seal. Loot does not automatically reveal Slimepedia entries.

Crystal caverns are underground without an excavated entrance tunnel. Surface sites reject unsuitable oceans, steep terrain, and low islands. There is no retroactive generation: explore new terrain for updated structures and altars.

Structure sets use `random_spread`, spacing 32 and separation 12 chunks; the chamber uses 24 and 8. Biome, height, slope, and rarity filter candidates, so spacing does not guarantee a structure at every interval. Server settings control overall and individual generation plus rarity.

With commands enabled, use `/locate structure slimeevolution:royal_court` in the Overworld or `/locate structure slimeevolution:ancestral_chamber` in the End. Substitute other IDs as needed. Datapack `has_<id>` tags can extend allowed biomes.

[Bosses](BOSSES.md) · [Configuration](../CONFIGURATION.md)
