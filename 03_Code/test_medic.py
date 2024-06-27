import pytest
from medic import Medic, Player

def test_add_healing_record():
    medic = Medic()
    player = Player()
    medic.add_healing_record(player)
    assert len(medic.get_healing_history()) == 1

def test_increase_energy():
    player = Player()
    initial_energy = player.energy[0]
    medic = Medic()
    medic.increase_energy(player)
    assert player.energy[0] == initial_energy + 1
