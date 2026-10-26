# Changelog

## 1.3 - 2026-10-26

Minimap HD 1.3 adds American v0 support and improves dungeon tracking, map transitions and remembered views. The installation ZIP contains Minimap HD only and includes both regional patches; Cemu selects the matching patch automatically.

## US support

- Support European v0 (`0005000010143600`, module `B7E748DE`) and American v0 (`0005000010143500`, module `475BD29F`) in one Cemu graphic pack. ([#1](https://github.com/Chironeyes/The.Wind.Waker.HD-Minimap.HD/issues/1))
- Keep the same artwork, presets and interface across regions, with individually mapped native code and data references.

## Bug fixes

- Fix the island minimap reappearing outside discovered-island boundaries when switching from sailing to swimming. Coverage checks now apply consistently while walking, swimming and sailing in both EU and US. Repeated boundary exits and returns at Forsaken Fortress animate correctly without another boarding cycle. ([#2](https://github.com/Chironeyes/The.Wind.Waker.HD-Minimap.HD/issues/2))
- Preserve independent foot and marine views, including the selected chart, when boarding, disembarking or temporarily leaving map coverage. Hidden-to-hidden transitions no longer flash a map.
- Animate compact/expanded size changes across island/dungeon transitions instead of snapping. A displayed treasure panel completes its exit when disembarking into a hidden foot map.
- Remove the compass return jump and prevent a brief compass flash behind entering maps.
- Keep the Tower of the Gods dungeon map, boat controls and frame functional on direct loading and after returning from marine treasure-chart views.
- Correct resource alignment that could shift the frame and expose a strip along its left edge.
- Keep camera-oriented dungeon views continuous across character and floor changes, without an overview flash, unwanted rotation or zoom reset.

## Quality-of-life improvements

- Follow Medli or Makar while controlled through the Command Melody, including their floor, map centering and camera orientation; return to Link when control changes.
- Update the displayed floor during flight with Link, Makar and Medli, including Medli's gliding phase, without waiting for landing. This is a deliberate minimap enhancement; the original map menu retains its native floor policy.
- Slide dungeon floors vertically with their markers while the frame stays fixed: ascending moves the plans downward, and descending moves them upward.
- Preserve dungeon visibility, size and orientation across walking, swimming and boating, including exits and returns to the Tower of the Gods.
- In dungeon-map boat contexts, use D-pad Down for compact/expanded/hidden and left-stick click (L3) for orientation/zoom. Left/right retain the native cannon/crane controls; only the custom bottom map shortcut is shown.
- Soften map-panel exits to 250 ms and refine compass timing with a 200 ms return delay, smooth reversals and continuous presentation.

## Validation and retained behavior

Tested with Cemu 2.6 in Wii U Pro Controller mode. The final US scenario campaign passed, including all three decoded Triforce charts and the critical ending cinematic after using the marine maps. EU coverage combines the earlier full campaign with later targeted companion/floor checks; the detailed validation record preserves those source scopes.

The candidate passed 1,242 synthetic instruction/guard checks, including 120 airborne cases, separately from manual gameplay. Both regional builds have 7,005 assembled instructions, 16 hooks and 14 aligned image buffers. The US ending observer collected 7,994 samples without a read error and confirmed native map/treasure cleanup.

Native discovery, dungeon Map/Compass requirements, opened-chest visibility, chart/menu synchronization and the existing ending protection are retained. The native distant-marker projection at Forsaken Fortress is unchanged; it was reproduced on the official map without Minimap HD in the tested setup.

Map resources come from the installed HD game alongside project-created interface elements. No save, controller profile, game executable, Xbox pack or separate original map texture is included. This validation does not claim every room, event, controller configuration or independently detected credits.

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
