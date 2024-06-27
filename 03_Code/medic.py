from datetime import datetime

class Medic:
    def __init__(self):
        self.energy = [100]
        self.healing_history = []

    def heal_player(self, player):
        if self.energy[0] > 0:
            self.increase_energy(player)
            self.add_healing_record(player)
            self.energy[0] -= 1

    def activate_medic(self):
        # I assume that it's always night for simplicity
        player = self.select_team_member_with_least_energy()
        if player:
            self.heal_player(player)

    def select_team_member_with_least_energy(self):
        pass

    def increase_energy(self, player):
        player.energy[0] += 1

    def add_healing_record(self, player):
        record = HealingRecord(datetime.now(), self, player)
        self.healing_history.append(record)

    def get_healing_history(self):
        return self.healing_history

class HealingRecord:
    def __init__(self, timestamp, healer, healed):
        self.timestamp = timestamp
        self.healer = healer
        self.healed = healed

class Player:
    def __init__(self):
        self.energy = [100]
