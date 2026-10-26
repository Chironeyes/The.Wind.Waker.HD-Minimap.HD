# Boat / foot presentation transitions

Scope: Minimap HD 1.3, based on 1.2.1. The requested US candidate scenario campaign is accepted. EU evidence combines the earlier presentation campaign with targeted later feature checks; see the validation record for source scopes.

## Forsaken Fortress: native island / dungeon family change

Each family keeps its own user preference. Marine states are Compass, Local, and Local + Treasure. Foot dungeon states are Hidden, Small, and Large. Hidden retains its stored size and orientation.

| Remembered foot dungeon state | Remembered marine mode | Boarding | Disembarking |
| --- | --- | --- | --- |
| Hidden | Compass | Remain hidden; no map entrance or exit | Remain hidden; no map entrance or exit |
| Hidden | Local | Enter the local map from outside the viewport | Exit to the hidden foot state |
| Hidden | Local + Treasure | Enter the local and treasure panels | Exit both panels to the hidden foot state |
| Small | Compass | Exit the visible map before the compass returns | Enter the small dungeon map |
| Small | Local | Remain visible at the compact size | Remain visible at the small size |
| Small | Local + Treasure | Retain local map; enter treasure panel | Retain dungeon map; exit treasure panel |
| Large | Compass | Exit the visible map before the compass returns | Enter the large dungeon map |
| Large | Local | Resize continuously from large to compact | Resize continuously from compact to large |
| Large | Local + Treasure | Resize to compact and enter treasure panel | Resize to large and exit treasure panel |

The native game selects the island/dungeon artwork. The handoff changes presentation geometry, not native classification. The large/compact preference in this table belongs to the Fortress dungeon renderer. Ordinary island boating keeps its native compact-only policy.

## Shared presentation rules

- Hidden to hidden never creates an active close animation or a visible map.
- Hidden to visible starts at the fully closed position. Visible to hidden exits from the last displayed fraction. Visible to visible retains that fraction and interpolates the square width if required.
- Interrupted slides and resizes start from actual geometry, including reversals. Native family and riding changes may occur together or on adjacent ticks.
- Marine request, selected chart, foot visibility, dungeon stored size and orientation remain preferences. Automatic coverage/discovery/resource fallback does not overwrite them.
- The final snapshot is taken after marine cleanup. Inactive island fields and the frame's earlier declared-visible flag are not evidence that a map was displayed.
- Activity opacity does not redefine geometric visibility or discard a partially completed slide.
- Snapshot HUD identity is compared only; pane pointers are never retained. HUD/stage replacement or genuine native suppression clears pending resize ownership.
- Existing 200 ms entrances/resizes, 250 ms smooth exits, and 200 ms compass return delay remain in use.
- A captured treasure panel completes its 250 ms exit across the Fortress's marine-to-dungeon change, including a hidden foot map. This tail depends on its captured HUD/pane and the current sea/HUD lifetime, not local-map eligibility, chart ownership/count, or the foot visibility preference. It never creates or selects a chart on foot.
- When boarding restores Local or Local + Treasure from a foot/dungeon HUD, a fresh marine compass starts hidden. It must not be invented behind the entering island panel. Ordinary aboard Compass-to-chart changes retain their existing departure animation. Snapshot provenance distinguishes a genuinely absent compass during suppression from a native compass already present in an undiscovered sector.

## Other contexts and gates

| Context | Required behavior |
| --- | --- |
| Tower of the Gods, native dungeon both on foot and aboard | One shared visibility/size/orientation state; boarding does not reinitialize it. Down cycles compact/large/hidden; L3 changes orientation/zoom when visible; Left/Right remain native tools. |
| Ordinary island, same native family | Existing native island sizing and input policy remain active; preference changes drive the existing slide. |
| Discovered island outside its bounds | No new entrance; an already displayed discovered image may complete its existing exit. Return uses the remembered request. |
| Undiscovered local plan | No new local image or markers. Marine request remains stored for a later eligible plan. |
| Marine treasure temporarily unavailable | Fall back to local presentation without overwriting the requested Local + Treasure state. |
| Dungeon Map missing | Native eligibility rejects the dungeon renderer before any handoff; no new plan, frame or markers. |
| HUD/menu/loading suppression | Native suppression still controls drawing; no stale pane or delayed resize survives replacement. |
| First marine use after foot HUD suppression | Inherit the last actual foot family's preference, rather than the unrelated island visibility field. |

## Verification

The following script names identify the local development harness retained with the private QA archive; the harness and native fixtures are not shipped as runtime dependencies or included in the installation pack. See [validation-1.3.md](validation-1.3.md) for counts, limitations and candidate identities.

`test_presentation_matrix.py` executes emitted prepare, slide, visibility, and snapshot PPC across successive synthetic HUD ticks. It covers both directions for all nine visible-state pairs, both hidden stored sizes, both orientations, partial reversals, adjacent family/riding orderings, unavailable coverage, cleanup, opacity, and suppression/replacement. Native layout construction/matrix publication is represented by private pane fixtures; runtime gameplay remains a separate confirmation.

The existing family, coverage, marine preference, compass, map-exit, ownership/ending and regional address checks remain separate evidence. They must not be substituted for the integration matrix or manual gameplay.

`test_treasure_exit_present.py` additionally executes the actual boat transition, tail capture, presentation, and final reset. It tests hidden/small/large foot maps, partially entered treasure panels, canceled exits, null HUD children, and the formerly rejected dungeon-family context. Native layout lookup and matrix publication are stubbed; the tail control flow and easing are emitted PPC.

`test_compass_boarding.py` checks the first and subsequent compass frames for both marine map modes, visible/hidden foot maps, suppressed/unknown contexts, stale identity/stage/tick, the Compass target, and subsequent deliberate switching with the unchanged delay and easing.

Regression reproduced on the previous candidate: the inactive island target was open with offset zero while the foot dungeon was hidden. Restoring marine Compass then started a 250 ms close and briefly displayed that stale island. The integrated hidden-to-hidden cases explicitly reproduce those inactive field values before boarding.
