# Circuits, Sonar, and Displays

<a id="circuitos-sonar-e-vitrine"></a>
<a id="cristal-encontrar-concentrações-minerais"></a>
<a id="cristal-energizado-transmitir-um-sinal"></a>
<a id="elétrico-pulsos-ajustáveis"></a>
<a id="vidro-expor-um-objeto-real"></a>

Electric, Crystal, Energized Crystal, and Glass have dedicated jobs. Crouch and use the analyzer on your slime, then open **Job**.

| Species | Job | Level | Cost |
|---|---|---:|---|
| Electric | Living circuit | 2 | 2 energy, +1 hunger per accepted pulse |
| Crystal | Mineral sonar | 2 | 4 energy, +2 hunger when an echo is found |
| Energized Crystal | Crystal relay | 3 | 1 energy on activation and each second of active signal |
| Glass | Living display | 1 | No energy cost |

Active jobs need a calm adult, trust 40, energy 30, hunger ≤60, and comfort 40. They start paused. Circuits require building permission and an online caretaker in the same dimension.

## Electric: adjustable pulses

Select **Output**, use the analyzer on a floor with empty space above, and keep the slime within six blocks and clear line of sight. Set the interval and duration, then enable the job.

Intervals are **1, 2, 4, or 8 seconds**; durations are **2, 4, 8, or 10 ticks**. Defaults are two seconds and four ticks. Adjustments pause work. Output strength is **15**, supporting redstone, droppers, pistons, and nearby mechanisms. Occupied output space is not replaced and does not charge for rejected pulses. Clearing the link pauses the job.

## Crystal: mineral sonar

Enable the job and press **Search**. The panel closes to reveal a pulse and a direction with weak, medium, or strong intensity. Scans reach **12 blocks**, including through stone, seeking clusters of at least four mineral blocks in one directional sector. Ores and amethyst blocks are recognized; an isolated vein may not produce a useful echo.

Scans preserve terrain, respect protected regions, and use loaded chunks only. Recovery is **ten seconds**, even without an echo; unsuccessful scans preserve energy and hunger. The last echo indicator is temporary, while recovery persists through saves and capsules.

## Energized Crystal: relay a signal

Link a **Source** block such as a lever, pressure plate, or redstone wire, then a **Destination** floor with free output space. Keep the slime within six blocks of output and enable the job.

Input and output must be loaded, in the same dimension, and **4–32 blocks apart**. The relay preserves analog strength **0–15**. No input signal means no energy charge. Output turns off when paused, captured, removed, or when its caretaker becomes unavailable. Temporary output points do not retain power without a valid source after reloading. Circuits respect permissions, arena protection, and `mobGriefing`.

## Glass: display an item

Place **one item** in its display compartment. It rotates inside the transparent body. **Enlarge** increases visual scale; **Normal size** restores it. The core is hidden while an item is displayed.

Display storage needs 40 trust and no energy. Count, durability, name, and enchantments stay intact. Capsules and embedded inventories are rejected. Capture preserves the item and scale; death drops belongings. Existing cargo remains withdrawable.

[Other jobs](WORK_JOBS.md) · [Care and capture](CARE.md)
