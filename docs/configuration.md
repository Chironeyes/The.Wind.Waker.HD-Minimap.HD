# Configuration

Settings are available under **The Legend of Zelda: The Wind Waker HD → Mods → Minimap HD** in Cemu's Graphic packs window. Set values before launching the game; changes take effect after a restart.

| Setting | Range | Default |
| --- | --- | --- |
| Overall opacity | 0–100%, in 5% steps | 100% |
| Faded opacity | 0–100%, in 5% steps | 70% |
| Fade on movement (Link + camera) | On / Off | On |
| Black background | On / Off | On |
| Background opacity (idle) | 0–100%, in 5% steps | 40% |
| Wind direction arrow | On / Off | On |

## Opacity and fading

Overall opacity applies to the complete minimap block: map artwork, markers, the wind arrow, the parchment frame, and the background. Shortcut icons remain native HUD elements and follow the HUD's own visibility and disabled-state animations.

Faded opacity is capped at overall opacity. Equal values produce constant opacity. With movement fading disabled, the block remains at its resting opacity.

Movement fading responds to directional input and camera input. Holding a direction against a wall also triggers it. The fade-out takes 60 ms. After 100 ms without activity, opacity returns over 200 ms.

The background starts at its configured resting opacity, capped at overall opacity, and follows the block's relative fading. For example, overall opacity 100%, faded opacity 70%, and background opacity 40% produce a 40% resting background and a 28% active background. At 0%, the background is transparent while the other elements retain their configured opacity.

## Frame and wind arrow

The parchment frame is always present when a map is shown. Its opacity follows the map even when the black background is disabled.

Dungeon map content has internal padding equal to 4% of the frame width on each side. Plans and markers are scaled together in compact and expanded views. The frame retains its existing position and dimensions; padding is fixed and requires no additional setting.

The wind direction arrow appears on island maps and follows the common opacity settings. It is never added to dungeon maps.

## Map availability

The game's native map type determines whether an island or dungeon plan is used. Its current world classification is refreshed independently of the Maps tab, including with a Pro Controller. Dungeon maps require the Map item; markers retain native Compass, floor, and opened-chest visibility rules.

For marine sailing, minimap and treasure-chart views require a discovered sector and Link within the local map's coverage. A treasure chart is always displayed beside a valid minimap, never by itself. All sailing maps remain compact. The Tower of the Gods keeps its dungeon map and dungeon controls aboard because the game's native map type remains a dungeon there.

Menus, cutscenes, first-person views, loading, and contexts without a native map retain priority over custom map visibility.
