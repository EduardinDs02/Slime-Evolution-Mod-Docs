# Slime Levels and Experience

[Player guide](../README.md) · [Companions](COMPANIONS.md)

Bonded slimes have an **individual level from 1 to 10**, replacing practice lessons. **Follow, Wait, and Return home are available at level 1**. Keep at least 40 trust, mark a home before returning, and respect the five-follower limit.

## Earn experience

| Completed action | XP |
|---|---:|
| Eat one item from the slime's own diet | 2 |
| Kill a passive mob | 8 |
| Kill a hostile mob | 20 |
| Kill one of the four bosses | 160 |

Meals must actually be accepted, respecting hunger, diet, and the five-second feeding interval. Hand-feeding, feeders, and feed bags use the same rule. Wrong foods, repeated attempts during cooldown, analyzer clicks, and defeating another companion award no XP. Boss summons award no XP.

Kill XP belongs to the slime that finishes the target, including when Minecraft loot and experience are credited to its caretaker. Projectiles retain that credit. Delayed unattributed damage, such as poison, also counts when the target took actual damage from that slime within the last ten seconds. Direct player kills do not award slime XP. Experience is not automatically shared with the party.

## Attribute growth

Level 1 retains the current species, size, and genetic attributes. Each additional level adds **20% of base health**, **18% of base damage**, and **1 armor**. Both basic attacks and offensive companion skills benefit from damage growth. Armor is capped at 30.

At level 10, a slime has **2.8× health**, **2.62× damage**, and **+9 armor** compared with level 1. Species rarity and their original attributes still matter. Leveling preserves the current health percentage rather than fully healing the slime.

| Level | Total XP | Health | Damage | Extra armor |
|---|---:|---:|---:|---:|
| 1 | 0 | 1× | 1× | 0 |
| 2 | 30 | 1.2× | 1.18× | 1 |
| 3 | 90 | 1.4× | 1.36× | 2 |
| 4 | 180 | 1.6× | 1.54× | 3 |
| 5 | 300 | 1.8× | 1.72× | 4 |
| 6 | 450 | 2× | 1.9× | 5 |
| 7 | 630 | 2.2× | 2.08× | 6 |
| 8 | 840 | 2.4× | 2.26× | 7 |
| 9 | 1080 | 2.6× | 2.44× | 8 |
| 10 | 1350 | 2.8× | 2.62× | 9 |

The analyzer panel shows level, XP progress, and attributes. Jobs that previously required 20, 40, or 60 training points now require levels 2, 3, or 4.

## Saves and migration

XP and level stay with the individual through saves, capture, release, and metamorphoses. Offspring start at level 1 without inherited XP. Wild slimes start at level 1 and gain XP after bonding.

Old training is converted once: each complete twenty points grants one level above the first. For example, 60 points become level 4 and 100 points become level 6. Home, posture, commands, and symbiosis consent are retained. The practice button has been removed.

## Creative Slime Wand

Find the **Creative Slime Wand** in Slime Evolution's creative tab. Right-click a mod slime to set **100 trust and level 10**. The wand is reusable, has no recipe or loot source, and only works in Creative mode, even if obtained by command in another mode.

Wild slimes bond to you; already bonded individuals keep their existing caretaker. Genes, identity, orders, inventory, hunger, comfort, and energy remain intact. Promotion preserves the current health percentage and does not wake a defeated companion. Bosses and vanilla mobs are unaffected.

```mcfunction
/give @s slimeevolution:creative_slime_wand
```
