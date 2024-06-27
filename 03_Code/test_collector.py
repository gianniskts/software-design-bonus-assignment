import pytest
from collector import Collector, Resource

def test_track_resource_collection():
    collector = Collector()
    resource = Resource("Plant_test", 5)
    collector.track_resource_collection(resource)
    assert len(collector.resources_collected) == 1

def test_get_resource_statistics():
    collector = Collector()
    resource1 = Resource("test1", 5)
    resource2 = Resource("test2", 3)
    collector.track_resource_collection(resource1)
    collector.track_resource_collection(resource2)
    stats = collector.get_resource_statistics()
    assert stats.total_resources_collected == 8
    assert stats.resource_breakdown["test1"] == 5
    assert stats.resource_breakdown["test2"] == 3