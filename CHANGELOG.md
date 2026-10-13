# Changelog

## 1.2.1 — 2026-10-13

- Fix island/dungeon map switching at Forsaken Fortress with a Pro Controller when the pause menu remains on Items and the Maps tab has never been opened.
- Refresh the map family through the game's native world classifier during visible gameplay, independently of the map menu.
- Preserve dungeon maps aboard in the Tower of the Gods, native chart and floor selection, existing artwork, controls and settings.
- Retain the ending-crash protection introduced in 1.2.0 without changing its panel attachment and cleanup routines.
- Clarify native map availability and visibility rules in the README.

The player confirmed both Fortress transition directions after a fresh Pro Controller launch without opening Maps, and confirmed that the Tower of the Gods keeps its dungeon plan aboard. The new helper passed ten focused guard/ABI checks, and its compiled code was verified in the development Cemu using European v0 and Cemu 2.6. The ending protection was verified unchanged; the full ending cinematic was not replayed for this update.

## 1.2.0 — 2026-10-12

- Fix a crash after the final dialogue with the King of Hyrule during the ending sequence.
- Reject detached or inconsistent UI links before moving minimap and treasure-chart panels between their native parents.
- Validate the treasure-chart frame before updating its geometry and clear cached chart pointers before native destruction.
- Preserve normal panel attachment, frame drawing order, artwork, controls, and settings.

The crash was traced to a null-link write in the pack's panel attachment routine. The correction passed 70 focused routine checks, and its compiled code was verified in the development Cemu. The player confirmed that the previously failing ending sequence now passes with European v0 and Cemu 2.6. This update was not validated through a complete replay of every dungeon and event.

## 1.1.3 — 2026-10-08

- Add internal padding equal to 4% of the frame width on each side of dungeon minimaps, in compact and expanded views.
- Scale dungeon plans and their markers together while retaining the existing frame position, size, clipping, and animations.
- Preserve native map projection, the companion marker correction from 1.1.2, and existing settings and artwork.

Both map sizes were checked in the Earth Temple with European v0 and Cemu 2.6; the player confirmed the visual result. Other dungeons and event scenarios were not replayed for this update.

## 1.1.2 — 2026-10-08

- Fix dungeon companion markers remaining at an old position after the companion moves or is carried and put down.
- Refresh companion position and facing through the game's native map update before calculating the minimap projection.
- Preserve native marker visibility, existing settings, artwork, and layouts.

The player confirmed the correction with Medli in the Earth Temple and Makar in the Wind Temple, using European v0 and Cemu 2.6. Other dungeon and event scenarios were not replayed for this update.

## 1.1.1 — 2026-10-06

- Select the map type from the game's native map state instead of relying on the stage name or a blanket boat condition.
- Fix simultaneous island and dungeon plans at Forsaken Fortress.
- Follow native map changes when boarding, disembarking, swimming, and crossing the Fortress map boundaries.
- Retain the dungeon map and its shortcuts aboard Lion Rouge inside the Tower of the Gods.
- Preserve existing presets, map textures, and layouts.

The Fortress transitions were confirmed in game by the player; the Tower of the Gods dungeon map was checked aboard. The Ganon's Tower portal has been researched but was not replayed as part of this update.

## 1.0.1 — 2026-10-04

- Rename the pack from Native Local Map to Minimap HD.
- Fix empty pixel lines at the right and bottom edges of dungeon maps, including at 3840 × 2160.
- Make the parchment border permanent and remove its separate visibility setting.
- Adjust the dungeon compass shortcut position.
- Synchronize treasure-chart title and artwork between L3 cycling and the GamePad menu.
- Add undiscovered-area hints using a native-font question mark and HUD-dependent attenuation.
- Hide sailing availability hints outside local map coverage.
- Preserve native dungeon marker visibility, including Compass requirements and opened chests.

Testing has covered selected island, dungeon, sailing, HUD, and transition scenarios. A complete playthrough of every dungeon and event is not claimed.
