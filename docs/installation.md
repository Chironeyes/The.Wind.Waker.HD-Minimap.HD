# Installation

## Requirements

- Cemu; the pack has been tested with version 2.6.
- The European v0 release of The Legend of Zelda: The Wind Waker HD, title ID `0005000010143600`, module hash `B7E748DE`.

No build tools or external scripts are needed to play with the pack.

## Installation ZIP

1. Close Cemu.
2. Download and extract `dist/WindWakerHD_MinimapHD-1.2.1.zip`.
3. Copy the extracted `WindWakerHD_MinimapHD` folder into the `graphicPacks` directory used by the Cemu installation.
4. Confirm that the final path ends in `graphicPacks/WindWakerHD_MinimapHD/rules.txt`.
5. Open Cemu, select **Options → Graphic packs**, and enable **The Legend of Zelda: The Wind Waker HD → Mods → Minimap HD**.
6. Choose the settings and launch the game. Restart the game after changing pack settings.

A portable Cemu installation normally uses `portable/graphicPacks`. Other installations may use a different data directory. Use the active installation's graphic pack directory rather than an unrelated Cemu folder. Custom packs belong outside `downloadedGraphicPacks`.

## Repository ZIP or Git checkout

Copy only `graphicPacks/WindWakerHD_MinimapHD` from the repository into Cemu's active `graphicPacks` directory. The entire repository does not need to be placed inside Cemu.

The final structure is:

```text
graphicPacks/
└── WindWakerHD_MinimapHD/
    ├── rules.txt
    ├── patch_map.asm
    └── VERSION.txt
```

The installation ZIP also includes English notices and configuration information. Neither distribution requires the Xbox/GameCube HUD pack.

## Updating

Close Cemu and move the previous Minimap HD folder outside `graphicPacks`. Install the new folder without merging versions. Keep only one active copy.

Legacy folder names include `WindWakerHD_NativeLocalMap` and `WWHD_NativeLocalMap`. Cemu may require the pack to be enabled again and its saved settings checked after a name or version change.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Pack is missing from the list | Confirm the active Cemu directory and the path to `rules.txt`; restart Cemu |
| Pack is listed but the minimap is absent | Verify EU v0 compatibility, discovery, local coverage, and possession of the dungeon Map item |
| Multiple copies or unexpected behavior | Move older pack folders outside `graphicPacks` and check for HUD layout conflicts |
| Setting changes have no immediate effect | Restart the game |
| Inputs do not match the displayed control | Check Cemu's mapping to the emulated Wii U controller |

No map is shown when the native game context has no available map. An undiscovered island can display a faded availability icon; that icon does not unlock the map.

## Removal

Disable Minimap HD, close Cemu, and remove its folder from `graphicPacks`. Game files and saves do not need restoration because the pack does not replace them.

## Reference

[Cemu Wiki: graphic packs installation and usage](https://wiki.cemu.info/wiki/Graphic_packs_installation_and_usage).
