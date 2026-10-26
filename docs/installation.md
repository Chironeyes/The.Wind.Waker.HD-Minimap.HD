# Installation

## Requirements

- Cemu; Minimap HD 1.3 has been tested with Cemu 2.6.
- Either the European v0 release of The Legend of Zelda: The Wind Waker HD, title ID `0005000010143600`, module `B7E748DE`, or American v0, title ID `0005000010143500`, module `475BD29F`.

Both regional patches are included. Cemu selects the matching module automatically. Other regions, executable revisions and emulator versions have not been validated. No build tools, external scripts or Xbox graphics pack are needed to play.

## Installation ZIP

1. Close Cemu.
2. Download and extract `WindWakerHD_MinimapHD-1.3.zip` from the repository's release page or `dist` directory.
3. Copy the extracted `WindWakerHD_MinimapHD` folder into the `graphicPacks` directory used by the active Cemu installation.
4. Confirm that the final path ends in `graphicPacks/WindWakerHD_MinimapHD/rules.txt`.
5. Open Cemu, select **Options -> Graphic packs**, and enable **The Legend of Zelda: The Wind Waker HD -> Mods -> Minimap HD**.
6. Choose the settings and launch the game. Restart the game after changing pack settings.

A portable installation normally uses `portable/graphicPacks`; other installations may use a different data directory. Custom packs belong outside `downloadedGraphicPacks`.

The ZIP includes English installation, configuration and asset-provenance documentation, notices and the license. It contains Minimap HD only. Controller profiles, saves and original game files are not included or replaced.

## Repository ZIP or Git checkout

Copy only `graphicPacks/WindWakerHD_MinimapHD` into Cemu's active `graphicPacks` directory. The whole repository does not need to be placed inside Cemu.

Keep these four core files together:

```text
graphicPacks/WindWakerHD_MinimapHD/
    rules.txt
    patch_map.asm
    patch_map_us.asm
    VERSION.txt
```

Keep both assembly files; regional selection is automatic. The installation ZIP also adds documentation inside the pack folder.

## Updating

Close Cemu and move the previous Minimap HD folder outside `graphicPacks`. Install the new folder without merging versions. Keep only one active copy.

Legacy folder names include `WindWakerHD_NativeLocalMap` and `WWHD_NativeLocalMap`. Cemu may require the pack to be enabled again and its saved settings checked after a name or version change. Historical 1.2.1 ZIPs are EU-only; use 1.3 for EU/US support.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Pack is missing from the list | Confirm the active Cemu directory and the path to `rules.txt`; restart Cemu |
| Pack is listed but the minimap is absent | Check region/revision and module hash, discovery, local coverage and possession of the dungeon Map item |
| Multiple copies or unexpected behavior | Move older pack folders outside `graphicPacks` and check for conflicting HUD layout mods |
| Setting changes have no immediate effect | Restart the game |
| Inputs do not match the displayed control | Check Cemu's mapping to the emulated Wii U controller |

No map is shown when no native map is available. An undiscovered island can display a faded availability icon; that icon does not unlock the map. Dungeon markers retain native Compass and opened-chest rules. The minimap's controlled-character and airborne floor selection does not alter the original map menu's floor policy.

See [configuration](configuration.md) for view controls and opacity, and the repository's [validation record](validation-1.3.md) for tested scenarios and limitations.

## Removal

Disable Minimap HD, close Cemu and remove its folder from `graphicPacks`. Game files and saves do not require restoration because the pack does not replace them.
