# Companions, Training, and Symbiosis

<a id="abrir-o-painel"></a>
<a id="ativar-uma-simbiose"></a>
<a id="elétrico--ferro-nas-máquinas"></a>
<a id="ensinar-comandos"></a>
<a id="funções-individuais"></a>
<a id="marcar-um-lar"></a>
<a id="persistência-e-configuração"></a>
<a id="vínculo-treinamento-e-simbiose"></a>
<a id="água--musgo-na-horta"></a>

## Open the companion panel

Manually feed a slime to become its caretaker. Then **crouch and use the Genetic Analyzer on your slime**. Normal analyzer use still opens genetic inspection. Control requires a nearby caretaker, clear line of sight, and building permission.

## Teach commands

Training requires trust ≥40, energy ≥40, hunger ≤60, comfort ≥40, a calm slime with at least half health, and no recent damage, breeding, leash, mount, or passengers.

Each lesson costs **5 energy and +3 hunger**, adds up to one trust, and grants **4–10 training points**, depending on sociability and stability. Both genes at 0.50 grant seven points. Lessons require **200 loaded ticks** of recovery. Training caps at 100 and does not change alleles.

| Command | Training points | Behavior |
|---|---:|---|
| Free | 0 | Resume natural movement and feeding |
| Wait | 20 | Guard the chosen point and return if displaced |
| Follow | 40 | Follow the available caretaker in the same dimension, within 32 blocks |
| Return home | 60 | Navigate to the marked home, then wait |

Learned commands require 40 trust; Free remains available below that threshold. Self-defense takes priority. Commands suspend loose-food seeking, so maintain manual feeding or a nearby Feeder.

Movement uses normal navigation and jumping: it does not teleport, pass through walls, or load chunks. Follow waits when its caretaker is unavailable, too far away, or in another dimension. Movement pauses below 20 energy for rest.

## Mark a home

**Mark home here** uses the caretaker's current position. Choose solid, dry ground inside the world border with room for the entire slime. A home can be marked before learning Return home. Return requires the same dimension and a loaded, unblocked location.

## Enable symbiosis

Open each partner's panel and enable cooperation. Both must be adults with the **same caretaker**, within six blocks and mutual line of sight, calm, with trust ≥40, energy ≥30, hunger ≤60, and comfort ≥40. Recent damage, breeding, leashes, mounts, or passengers prevent cooperation.

Partners cooperate while Free or Waiting. Follow and Return home suspend work. Cooperation starts disabled for new and existing individuals.

| Partners | Work | Cost per participant | Shared recovery |
|---|---|---|---|
| Water + Moss | Advance one compatible crop by one growth stage | 6 energy, +3 hunger | 400 ticks / 20 seconds |
| Electric + Iron | Add up to four processing ticks to a station or incubator | 2 energy, +1 hunger | 20 ticks / 1 second |

No valid work means no charge. Both participants receive recovery, preventing immediate reuse in another pair.

### Water + Moss

Keep partners within four blocks of crops and clear line of sight. Wheat, carrots, potatoes, beetroot, and other compatible `CropBlock` plants are supported. Cooperation does not plant or harvest. The caretaker must be online in the same dimension with permission to alter the location. Work respects `mobGriefing` and NeoForge protection events.

### Electric + Iron

Keep partners within four blocks of the machine, with clear line of sight. The capsule must belong to their caretaker. Assistance occurs only after the machine accepts a valid processing tick; it reduces processing time without bypassing ingredients or changing results, genes, growth rewards, identities, or token rules.

## Persistence and settings

Training, commands, home, cooperation preferences, and recovery persist through saves, capsules, and metamorphoses. Recovery pauses while captured or unloaded. Offspring start untrained and do not inherit commands or homes.

Server options `companions.training` and `companions.symbiosis` can pause these features without deleting progress. Canceling commands and disabling cooperation remain available. See [individual jobs](SPECIALIZATIONS.md).
