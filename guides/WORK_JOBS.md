# Production, Transport, and Auras

<a id="almas-localizar-a-última-morte"></a>
<a id="aurora-acalmar-o-curral"></a>
<a id="colmeia-mel-favos-e-polinização"></a>
<a id="comum-transportar-entre-estações"></a>
<a id="cáustico-reciclar-metal"></a>
<a id="end-viajar-entre-âncoras"></a>
<a id="ferro-reparar-equipamento"></a>
<a id="luminoso-iluminar-o-caminho"></a>
<a id="lunar-benefício-da-fase"></a>
<a id="produção-transporte-e-auras"></a>
<a id="transporte-e-controle"></a>
<a id="void-recolher-itens"></a>
<a id="água-irrigar-e-encher-frascos"></a>

Crouch and use the analyzer on your slime, then open **Job**. Work starts paused. Workers need calm adulthood, trust 40, energy 30, hunger at most 60, and comfort 40. Training requirements below refer to lesson experience points.

| Species | Job | Training | Cost per useful action |
|---|---|---:|---|
| Iron | Smith | 0 | Repair material; 6 energy, +3 hunger |
| Common | Courier | 20 | Linked containers; 2 energy, +1 hunger per pickup or delivery |
| Water | Irrigator | 0 | Stored water; 2 energy, +1 hunger |
| Luminous | Light guide | 0 | Glowstone dust; 1 energy per pulse |
| Soul | Memory keeper | 20 | Recorded last death; 1 energy every two seconds |
| End | Passage keeper | 60 | One pearl; 12 energy, +4 hunger per trip |
| Void | Spatial collector | 40 | Linked container or Amber; 2 energy, +1 hunger |
| Caustic | Recycler | 20 | Equipment and slimeball; 6 energy, +3 hunger |
| Lunar | Lunar tides | 20 | A useful phase effect; 3 energy, +1 hunger |
| Hive | Beekeeper | 0 | Flower and optional bottle; 6 energy, +3 hunger |
| Aurora | Peacekeeper | 20 | Nearby companions; 3 energy, +1 hunger |

## Iron: repair equipment

Place a tool or armor piece in the first slot and a compatible repair material in the second. After **ten seconds**, one material restores **25% of maximum durability**, preserving name and enchantments. The equipment stays in its slot for withdrawal or another cycle. Wrong materials and fully repaired equipment do not charge.

Supported materials follow the equipment's normal repair rules, including iron, gold, diamond, netherite, cobblestone, planks, leather, turtle scutes, and phantom membrane.

## Common: deliver between stations

Select **Source** in the panel, then crouch and use the analyzer on a nearby chest or barrel. Repeat for **Destination**, enable the job, and choose Free.

Containers must share a dimension and be within **32 blocks** of each other. The slime navigates normally, picks up up to **16 items** per operation, and delivers within three blocks. Full output preserves its cargo. Withdraw cargo through the panel. Follow, Wait, and Return home pause the route; the clear button removes links without deleting cargo.

## Water: irrigation and bottles

A water bucket in the first slot fills the reservoir with **1,000 units** and returns an empty bucket. Once per second it can hydrate visible farmland within four blocks, spending **25 units**.

Bottles in slot two and space in slot three allow one water bottle per **100 units**. Bottling takes priority over irrigation. Stored water persists through saves and capsules.

## Luminous: light the way

Glowstone dust supplies **20 pulses per item**, one per second, lighting the slime's path and its caretaker's path within six blocks. A pulse costs one energy. Temporary lights do not replace existing blocks and expire within three loaded seconds without renewal. Capturing or losing the slime does not create permanent lighting.

## Soul: find the last death

Enable the job near the caretaker. It shows the dimension and coordinates of the player's last death, points with particles in the same dimension, and highlights up to three nearby stacks identified as that player's lost belongings. **Track** checks the same point with a two-second cooldown. It locates surviving items; it does not recreate missing ones.

## End: travel between anchors

Link source and destination floors through the analyzer, in the same dimension and within **32 blocks**. Supply ender pearls, enable the job, stand within four blocks of an anchor, and press **Travel**.

The caretaker and slime travel together. Each accepted trip consumes one pearl, 12 energy, and +4 hunger, with ten seconds of recovery. Both need safe, clear landing space. Blocked, hazardous, or unloaded destinations do not consume a pearl.

## Void: collect loose items

Link a nearby chest, barrel, or Amber belonging to the same caretaker. Once per second, transfer up to **16 items** from a visible loose stack within six blocks to the visible destination. Excess remains on the ground.

Capsules, embedded inventories, stacks with pickup delay, and other players' identified belongings are excluded. No capacity means no charge.

## Caustic: recycle metal

Insert iron, gold, or chainmail equipment, a slimeball, and leave output space. After ten seconds, consume both inputs and return up to **25% of the metal as nuggets**, proportional to remaining durability and capped at 16 nuggets. Enchantments are not transferred. Insufficient yield or output room consumes nothing.

## Lunar: phase benefits

An enabled Lunar supports its caretaker within six blocks and clear line of sight according to its individual phase.

| Phase | Benefit |
|---|---|
| Full | Regeneration I when injured |
| Waning gibbous | Resistance I |
| Last quarter | Haste I |
| Waning crescent | Removes Poison and Hunger |
| New | Invisibility |
| Waxing crescent | Jump Boost I |
| First quarter | Speed I |
| Waxing gibbous | Night Vision |

Effects last 15 seconds, with five seconds between actions. Useful refreshes cost three energy and +1 hunger. Stronger existing effects are preserved. See [individual phases](CELESTIAL_VISUALS.md).

## Hive: honey and pollination

Maintain a visible planted flower within four blocks. Under Free, the slime can seek nearby flowers. A flower in the first slot becomes honeycomb after ten seconds; a bottle in the second produces bottled honey instead. Output uses slot three.

A cycle can also advance a nearby crop one stage when permitted. Full output or missing flowers stops processing without charging.

## Aurora: calm the enclosure

Every five seconds, help up to **three slimes of the same caretaker** within six blocks and clear line of sight. Each receives four comfort and seven seconds of calm, reducing spontaneous aggression and retaliation between companions without disabling self-defense. Useful actions cost three energy and +1 hunger.

## Persistence and permissions

Materials, cargo, water, cooldowns, and links persist through saves and capsules. Metamorphosis pauses the previous job; withdraw belongings and configure the new species. Death drops stored items.

Work follows server settings, caretaker permissions, protection events, and `mobGriefing` where applicable. Only loaded entities and regions are used.
