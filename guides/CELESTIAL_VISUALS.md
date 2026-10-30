# Celestial Appearances and Lunar Phases

<a id="aparências-e-fases-lunares"></a>
<a id="as-oito-luas-do-lunar"></a>
<a id="invocar-para-comparar"></a>

**Eclipse** has a spherical aura and two celestial bodies orbiting above it. **Ferrofluid** wears a covering of small spikes. **Steam** releases smoke from its crown, shoulders, and sides, rising and dissipating.

## Lunar's eight moons

Each Lunar is born with one of eight individual phases. Its moon floats and gently orbits above its head. The phase persists through saving and capsule transport and does not follow the world's calendar. It also determines the [Lunar job's benefit](WORK_JOBS.md).

| Value | Phase |
|---|---|
| 0 | Full moon |
| 1 | Waning gibbous |
| 2 | Last quarter |
| 3 | Waning crescent |
| 4 | New moon |
| 5 | Waxing crescent |
| 6 | First quarter |
| 7 | Waxing gibbous |

## Summon for comparison

With commands enabled:

```mcfunction
/summon slimeevolution:evolution_slime ~ ~ ~ {Species:"slimeevolution:lunar"}
```

To select a phase, add `LunarPhase` from 0 to 7. For a new moon:

```mcfunction
/summon slimeevolution:evolution_slime ~ ~ ~ {Species:"slimeevolution:lunar",LunarPhase:4}
```

Other species IDs include `slimeevolution:eclipse`, `slimeevolution:ferrofluid`, and `slimeevolution:steam`. Substitute the `Species` value in the first command.
