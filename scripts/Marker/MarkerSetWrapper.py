from MarkerMap import LOGIC_MARKER_CLASSES

class MarkerSetWrapper:
    def __init__(self, card, logic_registry=LOGIC_MARKER_CLASSES):
        self.card = card
        self._raw = card.markers  # Raw OCTGN dict
        self._wrapped = {}
        self._registry = logic_registry

    def get_wrapped(self, name):
        if name in self._wrapped:
            return self._wrapped[name]
        count = self._raw.get(name, 0)
        cls = self._registry.get(name)
        self._wrapped[name] = cls(count) if cls else None
        return self._wrapped[name]

    def adjust_dice(self, attack, targeting_card, targeted_card, attacker_traits):
        total = 0
        for name in self._raw:
            marker = self.get_wrapped(name)
            if marker:
                total += marker.adjust_dice_from_tokens(
                    attack, targeting_card, targeted_card, attacker_traits
                )
        return total
