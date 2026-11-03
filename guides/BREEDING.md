# Breeding, Growth, and Inspection

<a id="analisador-genético"></a>
<a id="configuração-do-servidor"></a>
<a id="crescimento-e-persistência"></a>
<a id="nascimento-e-recuperação"></a>
<a id="preparar-os-pais"></a>
<a id="preparação-com-estabilizador"></a>
<a id="receitas"></a>
<a id="reprodução-crescimento-e-inspeção"></a>

Breed compatible adults to produce offspring with inherited genetics. The 60 species use **79 breeding pairs**, including 20 cross-species combinations.

## Prepare the parents

1. Manually feed two compatible adults, binding both to the same caretaker. Required trust is 20 for docile, 40 for neutral, and 70 for hostile species. Feeders maintain hunger but do not increase trust.
2. Each adult needs hunger at most 40, comfort and energy at least 60, and at least half health. Combat, recent damage, breeding recovery, leashes, mounts, or passengers prevent breeding.
3. The caretaker uses **Breeding Gel** on each parent. A successful preparation consumes one gel in Survival and lasts **1,200 ticks**, normally 60 seconds. Repeated clicks while ready neither consume more gel nor extend readiness. Invalid attempts do not consume it.
4. Keep the parents within four blocks and clear line of sight. The server checks for solid, dry, unoccupied ground near their midpoint. Parents do not automatically seek partners.

Parent order does not matter. Parent–offspring, sibling, and half-sibling pairings are rejected. The record stores both parent UUIDs and generation; more distant ancestry is not detected. See [all breeding combinations](EVOLUTION.md).

The default population cap is **12 loaded living slimes** in a 32-block region around the birth, including parents and other species. This uses a spatial box.

## Birth and recovery

A successful birth creates one individual with a new UUID, inherited genome, parent IDs, and one generation above the higher parental generation. It inherits the caretaker and starts at size 1, hunger 60, comfort 60, trust 20, and energy 70. Juveniles do not deal contact damage. Parental metamorphosis history and exposure are not inherited.

Only after the server accepts the child do both parents spend **30 energy**, gain **30 hunger**, and begin recovery. Base recovery is **6,000 ticks**, multiplied by `1.25 - 0.5 × fertility`: normally 3 minutes 45 seconds to 6 minutes 15 seconds.

Blocked space, incompatibility, population limits, or another mod canceling entity insertion do not apply birth costs or recovery. Parents remain ready until their timer expires. Preparation gel is not refunded; expiration does not create offspring.

## Growth and persistence

Base growth takes **12,000 loaded ticks**, ten minutes under suitable conditions. It advances once per second while hunger is below 80, comfort at least 40, and energy at least 20. Growth that increases size also requires space. Chronological age and growth progress are separate counters.

The size gene determines adult size within species limits. A size-1 adult is still an adult. Size changes preserve health ratio. Genome, parents, generation, life stage, progress, and recovery persist through saves and capsules. Captured or unloaded individuals do not advance their growth or timers. Older individuals without growth fields load as generation-zero adults, preserving identity and genetics.

## Genetic Analyzer

Use `slimeevolution:genetic_analyzer` on a reachable, visible slime to inspect species, generation, UUID, parents, ability, health, size, stage, age, needs, growth, recovery, and readiness.

The 15 genes show both alleles and their expression. Scroll or use arrows; tooltips explain expression and genes without active gameplay effects. Inspection neither edits the slime nor consumes the analyzer. Losing the slime, line of sight, or eight-block access closes the menu. The **Evolution** tab shows transformation history and environmental requirements.

## Recipes

Breeding Gel: wheat (W), glow berries (B), slimeball (S).

```text
.W.
BSB
.W.
```

Genetic Analyzer: iron ingots (I), glass (G), slimeball (S).

```text
.IG
ISI
.I.
```

Both recipes unlock after obtaining a slimeball and produce one item.

## Server settings

| Setting in `[breeding]` | Default | Range / purpose |
|---|---|---|
| `enabled` | `true` | Player-initiated breeding |
| `localPopulationLimit` | `12` | 2–64 loaded slimes |
| `recoveryTicks` | `6000` | 200–240000; adjusted by fertility |
| `growthTicks` | `12000` | 200–240000; new juveniles |
| `mutationChance` | `0.02` | 0–0.25 per allele; affected by stability |
| `mutationStep` | `0.1` | 0–0.25 maximum allele change |

Existing juveniles and active recovery retain their stored durations. Timings assume 20 ticks per second and do not advance while unloaded.

## Mutation Stabilizer

Apply a stabilizer to an eligible parent in your care before Breeding Gel. One unit protects the pair's next accepted birth against new mutations without changing inherited alleles or bypassing breeding conditions. Protection persists through saves, capsules, failed births, and readiness expiration. An accepted birth consumes protection from treated parents; offspring do not inherit it.

Eclipse requires its additional [solar and lunar ritual](ASCENSION.md). See [genetics](../reference/GENETICS.md), [materials](MATERIALS.md), and [advanced lineages](ADVANCED_LINEAGES.md).


Phoenix requires an individual ritual and cannot breed. See [expanded lineages](EXPANDED_LINEAGES.md).
