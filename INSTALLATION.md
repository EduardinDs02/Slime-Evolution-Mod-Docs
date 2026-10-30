# Installation and Updates

<a id="atualização-e-backup"></a>
<a id="compatibilidade-e-diagnóstico"></a>
<a id="instalar-e-atualizar"></a>
<a id="licença"></a>

## Requirements

| Component | Required version |
|---|---|
| Minecraft Java Edition | 1.21.1 |
| NeoForge | 21.1.264 |
| Java | 21 |
| GeckoLib | 4.9.3 for NeoForge / Minecraft 1.21.1 |

Install **Slime Evolution and GeckoLib on both the client and server**, using matching versions for every participant. GeckoLib is a required external dependency; the game cannot load the mod without it.

## Install

1. Install compatible Minecraft and NeoForge in a separate profile.
2. Close the game or stop the server.
3. Place the Slime Evolution and GeckoLib `.jar` files in `mods/`.
4. Start a test world and check the items, species, and recipes.
5. Read [getting started](guides/GETTING_STARTED.md) and [configuration](CONFIGURATION.md).

The release ZIP includes the official GeckoLib JAR under `dependencies/`. Put the JARs in `mods/`, not the documentation ZIP. Compare transferred files against the release's `SHA256SUMS`. GeckoLib keeps its MIT license, supplied under `licenses/GECKOLIB_LICENSE` in the bundle.

## Update and back up

Stop the server and make a complete, consistent backup of the world, including player data, saved data, dimensions, and server configuration. Keep the previous mod JAR and your mod list. Replace the JAR and test a copy of your world before continuing. Do not downgrade a world after opening it with a newer version.

Capsules depend on `data/slimeevolution_captures.dat`, inventories, and world entities. The Slimepedia uses `data/slimeevolution_research.dat` in the Overworld. Restoring only an inventory or only a ledger can invalidate capsules or reintroduce old tokens. Minecraft world files do not form a single atomic transaction.
