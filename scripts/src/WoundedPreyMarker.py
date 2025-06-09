# from AbstractMarker import AbstractMarker

class WoundedPreyMarker(AbstractMarker):
    def adjust_dice_from_tokens(self, attack, targeting_card, targeted_card, attacker_traits):
        if (
            self.targeted_count > 0
            and 'Mage' not in targeted_card.Subtype
            and ('Animal' in targeting_card.Subtype or 'Johktari Beastmaster' in targeting_card.name)
            and attack['range type'] == 'Melee'
            and attack.get('strikes', 1) <= 1
            and 'Infernia' not in attacker_traits
            and 'Debilitate' not in attacker_traits
        ):
            return 1
        return 0

class ScoutTokenMarker(AbstractMarker):
    def adjust_dice_from_tokens(self, attack, targeting_card, targeted_card, attacker_traits):
        if self.targeted_count > 0:
            return 1
        return 0

    
    # if defender attacker has ScouToken:
    #     attacker attack +1 attack[dice]

def build_logic_marker_classes():
    return {
        WoundedPrey: WoundedPreyMarker,
        ScoutToken: ScoutTokenMarker,
    }

# Then call it later when needed
LOGIC_MARKER_CLASSES = build_logic_marker_classes()


# class WeakMarker(Marker):
#     def adjust_dice_from_tokens(self, attack, targeting_card, targeted_card, attacker_traits):
#         if self.count > 0 and 'Spell' not in attack:
#             return -self.count
#         return 0

# class StaggerMarker(Marker):
#     def adjust_dice_from_tokens(self, *args, **kwargs):
#         return -2 if self.count > 0 else 0
