from datetime import datetime

class Collector:
    def __init__(self):
        self.energy = [100]
        self.resources_collected = []

    def collect_items(self, plants):
        if self.energy[0] > 0:
            for plant in plants:
                self.track_resource_collection(plant)
                self.energy[0] -= 1

    def activate_collector(self):
        # I assume it's always day for simplicity
        # Example plants list
        plants = [Resource("Plant 1", 5), Resource("Plant 2", 3)]
        self.collect_items(plants)

    def track_resource_collection(self, resource):
        resource.timestamp = datetime.now()
        self.resources_collected.append(resource)

    def get_resource_statistics(self):
        stats = ResourceStats()
        for resource in self.resources_collected:
            stats.total_resources_collected += resource.quantity
            if resource.type in stats.resource_breakdown:
                stats.resource_breakdown[resource.type] += resource.quantity
            else:
                stats.resource_breakdown[resource.type] = resource.quantity
        return stats

class Resource:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity
        self.timestamp = None

class ResourceStats:
    def __init__(self):
        self.total_resources_collected = 0
        self.resource_breakdown = {}
