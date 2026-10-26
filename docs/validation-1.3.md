# Minimap HD 1.3 validation

Minimap HD 1.3 supports European v0 and American v0. Validation uses Cemu 2.6 in Wii U Pro Controller/XInput mode, with the separate Xbox graphics pack disabled. The [machine-readable record](validation-1.3.json) preserves hashes, source scopes and limitations.

## Manual coverage

| Scenario | EU evidence | US current R9 evidence |
| --- | --- | --- |
| Fishman discovery, island coverage, swimming HUD | Earlier presentation campaign accepted | Accepted; native discovery flag changed normally |
| Treasure charts and all three decoded Triforce charts | Earlier campaign accepted | Accepted; title, loaded chart and native menu agree |
| Fortress island/dungeon changes without opening Maps | Earlier campaign accepted | Accepted after fresh load and repeated swimming exits/returns |
| Tower controls, persistence and returning frame | Earlier campaign accepted | Accepted, including direct startup before an island pane existed |
| Dungeon Map/Compass gates and opened chests | Earlier campaign accepted | Accepted; temporary test item bits restored before the chest check |
| Medli control, camera, floors and gliding | Targeted R9 checks accepted | Targeted R9 checks and subsequent dungeon feedback accepted |
| Makar flight and character handoff | Fuller R7 replay accepted; R9 branch reviewed unchanged | Fuller R7 replay plus requested quick R9 regression accepted by the player |
| Critical final cinematic after marine chart use | Earlier presentation candidate accepted | Final R9 replay passed after all three Triforce choices |

The earlier full EU campaign retains its original candidate identity; it is not described as a fresh full R9 EU replay. Later targeted feature checks extend that evidence. The short current-R9 Makar trace did not capture flight, so acceptance of those actions relies on player feedback; fuller R7 flight traces remain separate evidence.

## Final US ending

The read-only observer collected 7,994 samples over 804.672 seconds without a read error. It observed the final Ganon stages and the sea ending (`ENDumi`). All 54 logged sea-ending rows had cleared island, dungeon and treasure objects, sources, panels and pending treasure exit. The player confirmed completion without blockage. The observer stopped on request; Cemu was not stopped or restarted during the trial, and the controller profile was unchanged.

This is not an independent rendered-credits detector or a guarantee for every game event.

## Offline and compiled checks

| Check group | Passing cases |
| --- | ---: |
| Existing presentation and static guards | 736 |
| Controlled-sage focus | 98 |
| Camera synchronization | 106 |
| Continuous geometry handoff | 88 |
| Vertical floor slides | 94 |
| Airborne floor selection | 120 |
| **Total** | **1,242** |

These are emitted-instruction/synthetic cases and static guards, separate from gameplay. Native construction and layout operations use fixtures or stubs where necessary. Actual Cemu compilation was verified for both regions: 7,005 assembled instructions, 16 hooks and 14 aligned image buffers per region; 1,509 feature instructions were compared against source in each region. The existing ending-ownership guard remains unchanged.

## Candidate identity

The released EU and US assembly files are byte-identical to the tested R9 candidate. Only the version/name/description metadata changes for release. Existing presets and embedded artwork remain unchanged.

| Assembly | SHA-256 |
| --- | --- |
| EU | `c5a414801d45919cb0576bde4daf0e31a92c399486baaa15fa5c42a8802718a2` |
| US | `9798ef3fc50bacaacede591de4453c49ebf579a6e6c4006cfb20a6d948e88ab0` |

Raw traces, native test fixtures and save files are retained in the private development archive. They are not runtime dependencies and are not included in the repository or installation ZIP. The archive contains the earlier EU campaign, later feature revisions and current US results separately.

The native distant Link projection at Forsaken Fortress was reproduced on the official map with the pack disabled in the tested setup. No original-hardware reproduction or projection correction is claimed. Original map-menu floor selection is preserved; the airborne floor feature changes only the minimap presentation.
