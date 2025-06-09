import AbstractMarker

class AegisMarker(AbstractMarker):
    def adjust_dice_from_tokens(self, *args, **kwargs):
        return -1 if self.count > 0 else 0