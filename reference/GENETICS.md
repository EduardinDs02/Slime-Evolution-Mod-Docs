# Genetics and Inheritance

<a id="estabilizador-de-mutação"></a>
<a id="fundadores-e-descendentes"></a>
<a id="genes-com-efeito-nesta-versão"></a>
<a id="genética-e-herança"></a>
<a id="genética-na-evolução"></a>
<a id="linhagem-crescimento-e-consulta"></a>

Each immutable genome contains **15 genes**, each with two finite alleles in `[0, 1]`. Additive expression uses the average, dominant expression the maximum, and recessive expression the minimum. These are fictional gameplay rules; expression does not replace stored alleles.

## Founders and offspring

Natural and spawn-egg founders receive 30 random alleles in `[0.25, 0.75)`. Directly created entities without spawn finalization retain baseline `0.5/0.5` until assigned a genome. Loading or releasing a capsule preserves existing genes.

For each gene, offspring inherit one equally likely allele from each parent. Each inherited allele can mutate independently. Effective probability is:

```text
min(0.25, mutationChance × (1.5 - average parental stability)
    × (1 + 0.5 × unstable parents))
```

Default `mutationChance` is 0.02: stability gives 1%–3% per allele without unstable parents. One parent with `unstable_touch` adds a 1.5 factor; two give a factor of 2. Setting chance to zero disables mutations even for Corrupted parents. There are no spontaneous lifetime mutations or genetic infection from attacks.

Mutation adds a random delta between `-mutationStep` and `+mutationStep`, clamped to `[0, 1]`. Default step is 0.1; configurable chance and step cap at 0.25. Parents are unchanged.

## Gene effects

`e` is expressed value, between zero and one. Species baselines apply at size 2; health and damage use current size divided by two.

| Gene | Expression | Effect |
|---|---|---|
| Size | Additive | Adult size: `min(max, min + floor(e × (max - min + 1)))` |
| Elasticity | Additive | Jump factor `0.75 + 0.5e`; Common offensive knockback `0.35 × (0.5 + e)` |
| Vitality | Additive | Base health × size factor × `0.75 + 0.5e` |
| Speed | Additive | Base speed × `0.8 + 0.4e` |
| Metabolism | Additive | Hunger +`0.1 × (0.5 + e)` each loaded second |
| Resistance | Dominant | Armor `base + (e - 0.5) × 4`, clamped 0–20; mineral reduction `min(0.75, setting × (0.5 + e))` |
| Fertility | Additive | Breeding recovery × `1.25 - 0.5e` |
| Stability | Additive | Adjusts mutation probability using parental average |
| Regeneration | Recessive | Moss healing `(0.5 + e) × setting`, capped at six health |
| Elemental potency | Additive | Fire, mud, and chill duration × `0.5 + e` and setting, capped at 200 ticks |
| Aggression | Dominant | Retaliation `100 + 200e` ticks; docile flee threshold `0.4 - 0.2e` health fraction |
| Sociability | Additive | Social search radius `4 + 8e`; stopping distance `4 - 2e` blocks |
| Transparency | Additive | Base gel alpha `round(255 - 102e)` combined with species material |
| Luminosity | Recessive | Luminous body visual light `round(8 + 7e)`; other species do not gain this emission |
| Pigmentation | Dominant | Species RGB channels × `0.85 + 0.3e`, capped at 255 |

All 15 genes have expression implemented. Transparency is not invisibility. Genetic luminosity is visual emission, not block lighting or a spawn-rule change. At baseline, gel alpha is 204 and Luminous visual emission is 12. Species still determines temperament and ability selection.

## Lineage, growth, and inspection

Lineage stores both parent UUIDs and generation. Founders start at zero; children use the higher parental generation plus one, capped at one million. Self-pairing, parent–child, siblings, and half-siblings are rejected; there is no unlimited ancestral tree.

Juveniles begin at size 1 and grow toward their genome-determined adult size, subject to food, comfort, energy, and space. See [breeding](../guides/BREEDING.md).

Individual NBT version 7 preserves genes, lineage, growth, breeding counters, transformation history and exposure, ecological home, and birth mutation evidence. Old saves retain identities and alleles; unavailable mutation history remains unavailable rather than being inferred. Capsules preserve this state and validate it against the world's capture ledger.

The analyzer is read-only and shows identification, ancestry, alleles, needs, counters, birth evidence, and evolution requirements.

## Evolution and stabilization

Hybrids inherit alleles using the normal service and receive the recipe's species. Metamorphoses preserve every allele and the lineage: environmental conditions allow a species change without rewriting the genome. Recessive thresholds require both alleles to qualify.

A Mutation Stabilizer applied to an eligible parent before gel prevents **new mutations in the next accepted birth**. Allele selection and inherited unusual values remain unchanged. Protection persists through failed or canceled births and expires only on accepted offspring insertion. See [materials](../guides/MATERIALS.md) and [verified genetic research](../guides/GENETIC_RESEARCH.md).

Epistasis, environmentally conditioned gene expression, and rare mutation categories are planned rather than current features.
