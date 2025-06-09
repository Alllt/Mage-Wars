from . import (
    WoundedPreyMarker,
    AegisMarker,
    WeakMarker,
    StaggerMarker,
    ScoutTokenMarker,
)

LOGIC_MARKER_CLASSES = {
    WoundedPrey[0]: WoundedPreyMarker,
    AegisToken[0]: AegisMarker,
    Weak[0]: WeakMarker,
    Stagger[0]: StaggerMarker,
    ScoutToken[0]: ScoutTokenMarker,
}
