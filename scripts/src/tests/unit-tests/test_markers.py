from scripts.src.tests.MockCard import MockCard
from scripts.constants import ScoutToken

import builtins
class MockPlayer:
    def __init__(self, _id):
        self._id = _id

builtins.me = MockPlayer(_id=12345)

from scripts.src.attackCalcs import adjustDiceFromTokens, adjustFromDefenderTraits
from unittest.mock import patch

builtins.mute = lambda: None

builtins.notify = lambda s: print(s)
builtins.getGlobalVariable = lambda s: "[['Attack', [65543, 65557, 'Basic Melee Attack', 3]], ['Attack', [65543, 65557, 'Basic Melee Attack', 2]]]"



def test_adjust_dice_from_scout_tokens():
    attacker = MockCard(Name="Attacker")
    defender = MockCard(name="Defender", markers={ScoutToken: 2})
    attack = {"dice": 3}

    updated = adjustDiceFromTokens(attack, attacker, defender, attackerTraits=[])

    assert updated["dice"] == 5

@patch("builtins.getGlobalVariable", return_value="[]")
def test_adjust_from_defender_traits_aegis(a):
    attacker = MockCard(Name="Attacker", attachedTraits='')
    defender = MockCard(name="Defender", attachedTraits="{'markedForDeath': True}")
    print(defender.attachedTraits)
    attack = {"dice": 3}
    builtins.me = MockPlayer(_id=12345)
    updated = adjustFromDefenderTraits(attack, attacker, defender)

    assert updated["dice"] == 4

@patch("builtins.getGlobalVariable", return_value="[['Attack', [65543, 65557, 'Basic Melee Attack', 3]]]")
def test_adjust_from_defender_traits_aegis(a):
    attacker = MockCard(_id=65543,Name="Attacker", attachedTraits='')
    defender = MockCard(_id=65557 ,name="Defender", attachedTraits="{'markedForDeath': True}")
    print(defender.attachedTraits)
    attack = {"dice": 3}
    builtins.me = MockPlayer(_id=12345)
    updated = adjustFromDefenderTraits(attack, attacker, defender)

    assert updated["dice"] == 3