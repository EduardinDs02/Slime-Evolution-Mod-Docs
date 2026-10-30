# Genetic Research

<a id="descobrir-variantes"></a>
<a id="mutações-verificadas-no-nascimento"></a>
<a id="persistência-e-compatibilidade"></a>
<a id="pesquisa-genética"></a>

The Slimepedia records observed expression bands and genes with verified changes at birth. An unusual trait alone does not prove a mutation.

## Discover variants

Analyze a reachable, visible live slime or complete a valid capsule analysis at a Genetic Station. The Slimepedia's **Genes** tab accumulates expression bands observed in analyzed members of that species.

| Band | Calculated gene expression |
|---|---|
| Low | 0 through 0.25, inclusive |
| Intermediate | Above 0.25 and below 0.75 |
| High | 0.75 through 1, inclusive |

Expression respects additive, dominant, or recessive rules. Gameplay effects still follow species rules. The bands apply to all 15 existing genes and accumulate per species and player. Repeating the same analysis does not inflate counts. Storage holds up to three bands per gene rather than an expanding list of genomes or UUIDs.

Observation, feeding, and witnessing births unlock their own facts; genetic findings require analysis. Books show their current reader's progress. Spectators do not advance research.

## Verified birth mutations

Inheritance records genes where at least one allele actually changed after mutation and clamping. Zero-step, zero-delta, or clamped unchanged results do not register false mutations. A real allele change can occur even if the average additive expression stays the same.

After analyzing a descendant, the journal distinguishes:

- **Verified mutations:** genes changed in analyzed births with recorded provenance.
- **Birth without new changes:** a known birth record with no new allele changes.
- **Unavailable history:** a descendant without verifiable birth provenance.

Founder variation and inherited parental alleles are not evidence of a new mutation in that child. Findings concern the individual's direct birth, not a reconstruction of every ancestor. Hover over genes in the analyzer for provenance, expression, and gameplay effect details.

## Persistence and compatibility

`BirthMutationsKnown` and `BirthMutationGenes` store bounded birth evidence using stable gene enum names. Missing or invalid history loads as unavailable; old saves are not retroactively assigned mutations based on rare values.

Evidence persists through capsules, station readings, incubation, and metamorphosis. Incubation cannot modify genome, lineage, or birth evidence. A changed birth record invalidates an open inspection.

Older journals retain species, stages, and routes; new analysis fills missing findings. Invalid optional genetic data is discarded without erasing other valid facts. Journals are shared across dimensions by player UUID. The current journal schema is 4 as of version 0.15.0, which also stores first-login book delivery.

The server sends only the player's discoveries and selected species details. Client and server must use matching mod versions.
