# from abc import ABC, abstractmethod

class AbstractMarker:
    def __init__(self, count):
        self.count = count

    # @abstractmethod
    def adjust_dice_from_tokens(self, attack, targeting_card, targeted_card, attacker_traits):
        """Return dice adjustment value (can be positive, negative, or zero)."""
        pass
