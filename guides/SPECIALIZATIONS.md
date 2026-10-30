# Individual Slime Jobs

<a id="abyssal-guia-submarino"></a>
<a id="acessar-a-função"></a>
<a id="fogo-aquecedor"></a>
<a id="funções-individuais-dos-slimes"></a>
<a id="fúngico-compostador"></a>
<a id="persistência-retirada-e-configuração"></a>
<a id="âmbar-conservador"></a>

The companion panel offers **19 individual jobs**. Crouch and use the Genetic Analyzer on your slime, then open **Job**. See also [production, transport, and auras](WORK_JOBS.md) and [circuits, sonar, and displays](SIGNAL_JOBS.md).

## Requirements

Active workers must be calm adults with trust ≥40, energy ≥30, hunger ≤60, comfort ≥40, and no recent damage, combat, breeding, leash, mount, or passengers. Jobs start disabled. The nearby caretaker needs clear line of sight and appropriate permissions. Hover over information icons for costs.

## Fire: furnace assistant

Keep Fire within four blocks and clear line of sight of a furnace, blast furnace, or smoker, under Free or Wait. The caretaker must be online in the same dimension with permission to alter the location.

Every second, an available slime adds up to **20 cooking ticks** to processing that has already accepted fuel, ingredients, and output space. Each pulse costs **2 energy and +1 hunger**, with a 20-tick worker cooldown. Multiple furnaces cannot reuse the same helper simultaneously, and multiple slimes do not multiply that furnace's pulse in the same second.

Normal fuel, recipes, output, and XP remain in effect. Invalid or blocked work does not charge. Work respects `mobGriefing` and NeoForge permissions.

## Fungal: composter

Place **eight identical compostable items** in the first slot. Vanilla composting inputs such as seeds, leaves, plants, and plant foods are accepted. After **200 loaded work ticks**, eight inputs become **one bone meal**, costing **6 energy and +3 hunger**.

Slots hold up to 16 items. Invalid input or full output resets the cycle without charging. Pausing or losing care conditions preserves progress, as do saving and capture. Processing can continue while following. Output can be withdrawn with Shift; inputs cannot be placed in the output slot.

## Abyssal: underwater guide

Enable the job while both the slime's and caretaker's eyes are submerged, within six blocks and clear line of sight. It also works while following.

When useful, an action restores up to **60 air** and grants or refreshes **15 seconds of Night Vision**. It costs **2 energy and +1 hunger**, with **40 ticks** of recovery. Full air and sufficiently recent Night Vision do not charge; longer existing effects are preserved. Granted effects expire normally after leaving water, but further assistance requires both participants to remain submerged.

## Amber: storage keeper

Amber offers **three compartments of up to 16 items**, respecting each item's normal stack limit. Deposits require 40 trust. Stored objects appear inside its resin body; empty Amber retains its decorative inclusions.

Storage requires no processing cycle or energy. Capsules, bags, shulker boxes, and items with embedded inventories are rejected. Shift transfers preserve excess items in the player's inventory.


## Persistence and withdrawal

Items, job preferences, cooldowns, and composting progress persist through saves and capsules. Capture preserves belongings; death drops them once. Offspring begin with empty storage and jobs disabled.

Metamorphosis preserves belongings. If the new species lacks that job, withdrawal remains available until its inventory is empty. `companions.specializations` can pause jobs and deposits without preventing withdrawal or disabling stored work preferences. Jobs do not load chunks; cooldowns advance only while loaded.
