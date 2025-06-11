from scripts.src.WoundedPreyMarker import LOGIC_MARKER_CLASSES

class MarkerSetWrapper:
    def __init__(self, targeting_card, targeted_card, logic_registry=LOGIC_MARKER_CLASSES):
        self.targeting_card = targeting_card
        self.targeted_card = targeted_card
        self._targeting_raw = targeting_card.markers
        self._targeted_raw = targeted_card.markers
        self._wrapped = {}
        self._registry = logic_registry

    def get_wrapped(self, name):
        if name in self._wrapped:
            return self._wrapped[name]

        targeting_count = self._targeting_raw[name] if name in self._targeting_raw else 0
        targeted_count = self._targeted_raw[name] if name in self._targeted_raw else 0

        cls = self._registry.get(name)
        self._wrapped[name] = cls(targeting_count, targeted_count) if cls else None
        return self._wrapped[name]




    def adjust_dice(self, attack, targeting_card, targeted_card, attacker_traits):
        total = 0
        all_marker_names = set(list(self._targeting_raw) + list(self._targeted_raw))
        for name in all_marker_names:
            marker = self.get_wrapped(name)
            if marker:
                total += marker.adjust_dice_from_tokens(
                    attack, targeting_card, targeted_card, attacker_traits
                )
        return total


