# Balance Reference

<a id="chefes"></a>
<a id="circuitos-sonar-e-vitrine"></a>
<a id="crescimento-e-custos"></a>
<a id="funções-individuais"></a>
<a id="referências"></a>
<a id="treinamento-e-simbiose"></a>
<a id="valores-de-balanceamento"></a>

Values describe loaded gameplay ticks, normally 20 per second. Actual survival difficulty and economy depend on play conditions.

## Growth and incubation

Default natural growth needs **12,000 loaded ticks** under valid care conditions. Each manual incubator cycle takes **200 ticks**, charging one food and one supplement only at completion.

| Supplement | Growth per cycle | Cycles for a default newborn | Processing time | Foods / supplements |
|---|---:|---:|---:|---:|
| Breeding Gel | 1,200 | 10 | 100 seconds | 10 / 10 |
| Genetic Catalyst | 2,400 | 5 | 50 seconds | 5 / 5 |
| Royal Gel | 3,600 | 4 | 40 seconds | 4 / 4 |

These totals exclude gathering, crafting, menu use, and intervals between clicks. Chronological age increases by only 2,000 / 1,000 / 800 ticks respectively. New `growthTicks` settings affect future births; existing juveniles retain their duration.

## Bosses

Health is measured in points; two points equal one heart. All encounters announce attacks and check distance, height, and cover. Rituals prevent overlapping bosses within 96 blocks.

| Boss | Health | Armor | Attack families | Raw damage by phase |
|---|---:|---:|---:|---|
| Gelatinous King | 290 | 7 | 4 | 9 / 12.6 |
| Magmatic Heart | 320 | 6 | 4 | 9 / 12.6; eruptions 7.5 / 10.5 |
| Crystalline Colossus | 400 | 10 | 4 | 7.5 / 10.5 |
| Primordial Slime | 540 | 8 | 5 | 7.5 / 10.5 / 14.7 |

Damage uses `base × 1.5 × 1.4^phase × setting`. At multiplier 2, the largest hit reaches 29.4 before defenses. Water halves Magmatic Heart damage after this calculation. Prepared attacks keep their starting phase parameters.

The King maintains up to six minions: guards have 24 health and four base damage with Weakness II; healers have 18 health and restore nine health per 80 ticks; spitters have 20 health and three base damage with Slowness I and Poison I. The Heart supports up to four fire/magma servants; Primordial supports up to three flying echoes.

A player-credited victory yields two boss materials: Royal Gel, Igneous Fragment, Prismatic Shard, or Primordial Essence. Minions do not drop loot or XP or split. See [boss encounters](guides/BOSSES.md).

## Training and symbiosis

| Action | Cost | Recovery |
|---|---|---|
| Lesson | 5 energy, +3 hunger, up to +1 trust | 200 ticks |
| Water + Moss crop growth | 6 energy, +3 hunger per partner | Shared 400 ticks |
| Electric + Iron processing | 2 energy, +1 hunger per partner | Shared 20 ticks |

Lessons grant `4 + floor(sociability × 4) + floor(stability × 2)` points, capped at 100. Wait needs 20, Follow 40, Return home 60. Symbiosis adds up to four machine ticks or one crop stage without bypassing materials or permissions. See [companions](guides/COMPANIONS.md).

## Jobs and circuits

Fire adds up to 20 furnace ticks per 20-tick helper cooldown for 2 energy and +1 hunger. Fungal converts eight compostables to one bone meal in 200 work ticks for 6 energy and +3 hunger. Abyssal restores up to 60 air and 300 ticks of Night Vision within six blocks for 2 energy and +1 hunger, recovering for 40 ticks. Amber holds three compartments of up to 16 items with no storage cost.

Electric pulses need training 20 and cost 2 energy and +1 hunger, with strength 15, intervals 20/40/80/160 ticks, and durations 2/4/8/10. Crystal sonar needs training 20, reaches 12 blocks, and costs 4 energy and +2 hunger only on an echo, with 200-tick recovery even without one. Energized Crystal needs training 40 and one energy initially and per active second, relaying analog 0–15 across 4–32 blocks. Glass displays one item with free 1.5× visual enlargement.

[Job details](guides/SPECIALIZATIONS.md) · [Additional jobs](guides/WORK_JOBS.md) · [Signal jobs](guides/SIGNAL_JOBS.md) · [Configuration](CONFIGURATION.md)
