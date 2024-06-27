import pytest
from medic import Medic, Player

def test_add_healing_record(self):
    medic = Medic()
    player = Player()
    medic.add_healing_record(player)
    self.assertEqual(len(medic.get_healing_history()), 1)

def test_increase_energy(self):
    player = Player()
    initial_energy = player.energy[0]
    medic = Medic()
    medic.increase_energy(player)
    self.assertEqual(player.energy[0], initial_energy + 1)
