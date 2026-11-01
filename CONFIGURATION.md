# Configuration

<a id="configuração"></a>
<a id="visual-do-cliente"></a>
<a id="vínculo-e-simbiose"></a>

Server rules are authoritative NeoForge SERVER options synchronized on login. Stop the server before editing `<world>/serverconfig/slimeevolution-server.toml`. Use `defaultconfigs/` for new-world defaults and back up before changing versions. The Mods configuration screen uses NeoForge's editor; remote-server values are read-only for clients.

Twenty ticks normally equal one loaded second. Unloaded chunks do not advance growth or cooldowns. NeoForge corrects out-of-range values. Generated files include comments and limits; review them when upgrading. World-generation changes affect new terrain only.

## Server settings

| TOML key | Default; minimum; maximum | Purpose |
|---|---|---|
| `naturalSpawning` | `true` | Natural spawning; commands and eggs remain usable when disabled |
| `localPopulationLimit` | `8; 1; 64` | Natural-spawn population limit within 32 blocks; does not remove existing slimes |
| `spawnChance` | `0.25; 0; 1` | Additional spawn probability after normal checks |
| `damageMultiplier` | `1; 0; 4` | Ordinary slime contact and Crystal projectile damage; excludes bosses |
| `abilityParticles` | `true` | Server ability particles; boss ground warnings remain available |
| `combat.activeAbilities` | `true` | Active contact abilities and environmental regeneration; passive defenses remain |
| `combat.abilitySounds` | `true` | Ability activation sounds |
| `combat.thermalReactions` | `true` | Fire removes mod chill; icy contact extinguishes burning targets instead of chilling |
| `combat.effectDurationMultiplier` | `1; 0; 4` | Ignition, mud, and chill duration; capped at 200 ticks per application |
| `combat.healingMultiplier` | `1; 0; 4` | Healing combined with regeneration genetics; capped at six health |
| `combat.mineralImpactReduction` | `0.25; 0; 0.5` | Pre-armor projectile/explosion reduction, genetically adjusted; capped at 75% |
| `combat.metalMeleeReduction` | `0.2; 0; 0.5` | Iron melee reduction before genetics; excludes projectiles, explosions, and bypass damage |
| `combat.obsidianBlastReduction` | `0.5; 0; 0.5` | Genetically adjusted explosion reduction; capped at 75% |
| `combat.iceFireMultiplier` | `1.5; 1; 4` | Fire damage received by Ice slimes |
| `combat.wetFireDamage` | `1; 0; 4` | Fire slime damage per loaded second while wet |
| `combat.dischargeDamage` | `2; 0; 4` | Wild discharge base, doubled when wet and capped at six. Companion electrical attacks scale relative to default 2, with a 50% wet-target bonus |
| `combat.waterConduction` | `true` | Wet-target discharges may chain to two nearby visible wet targets |
| `breeding.enabled` | `true` | Caretaker-initiated breeding |
| `breeding.localPopulationLimit` | `12; 2; 64` | Loaded living slimes within 32 blocks of a birth |
| `breeding.recoveryTicks` | `6000; 200; 240000` | Parent recovery, adjusted by fertility |
| `breeding.growthTicks` | `12000; 200; 240000` | Growth duration for new juveniles; existing ones retain their duration |
| `breeding.mutationChance` | `0.02; 0; 0.25` | Per-allele chance adjusted by stability and unstable parents |
| `breeding.mutationStep` | `0.1; 0; 0.25` | Maximum absolute allele mutation; results clamped to 0–1 |
| `evolution.metamorphosis` | `true` | Environmental exposure and catalyst transformations |
| `ecology.foraging` | `true` | Seek loose diet items without gaining trust; respects `mobGriefing` |
| `ecology.grouping` | `true` | Compatible grouping by species and caretaker, adjusted by sociability |
| `ecology.territories` | `true` | Territorial defense with caretaker and boundary rules |
| `ecology.surfaceNests` | `true` | New-terrain surface nests and finite founders |
| `ecology.caveColonies` | `true` | New-terrain underground colonies and finite founders |
| `ecology.nestRarity` | `24; 1; 1000` | Additional one-in-N chance per nest attempt |
| `ecology.colonyRarity` | `12; 1; 1000` | Additional one-in-N chance per colony attempt |
| `structures.enabled` | `true` | Generate the six special sites in new chunks |
| `structures.crystalCaverns` | `true` | New Crystal Caverns |
| `structures.gelatinousLakes` | `true` | New Gelatinous Lakes |
| `structures.elementalSanctuaries` | `true` | New Elemental Sanctuaries |
| `structures.researcherRuins` | `true` | New Researcher Ruins |
| `structures.ancestralChambers` | `true` | New Ancestral Chambers |
| `structures.royalCourts` | `true` | New Royal Courts |
| `structures.rarity` | `1; 1; 1000` | Additional deterministic one-in-N generation filter |
| `bosses.enabled` | `true` | Start rituals; disabling does not remove existing encounters |
| `bosses.damageMultiplier` | `1; 0; 2` | Boss and servant damage; zero disables their damage |
| `companions.training` | `true` | Lessons and learned commands |
| `companions.symbiosis` | `true` | Water + Moss and Electric + Iron cooperation |
| `companions.specializations` | `true` | The 19 individual jobs and new storage deposits |

Disabling companion features preserves training, home, preferences, and belongings. Free, disabling cooperation, and item withdrawal remain accessible. Terrain work respects caretaker permissions and `mobGriefing`. Arena protection persists even when generation is disabled. Rarity filters do not replace datapack spacing and biome rules.

## Client visuals

Local `config/slimeevolution-client.toml` settings do not change server gameplay. NeoForge's screen provides English and Portuguese labels and help.

| Key | Default / range | Effect |
|---|---|---|
| `reducedMotion` | `false` | Reduces breathing, sway, pulses, and decorative flame, lightning, and steam motion; physical jumps remain visible |
| `visualParticleIntensity` | `0.75`, range 0–1 | Extra action and idle elemental particles; zero disables them |

Extra particles respect Minecraft's particle setting and server `abilityParticles`. Decorative animation is reduced after 24 blocks and stops after 48, without changing genetics, damage, collision, or world lighting.

Geometric flames, electrical arcs, and steam remain visible with minimal particles; their motion follows `reducedMotion`. The global extra-particle budget is four per five ticks, or two with reduced particles. Actions take priority over idle accents; reduced motion also disables idle accents.

[Companion rules](guides/COMPANIONS.md) · [Balance](BALANCE.md)
