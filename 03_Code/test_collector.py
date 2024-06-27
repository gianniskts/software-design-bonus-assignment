import pytest
from collector import Collector, Resource

class TestCollector(pytest.TestCase):
    def test_track_resource_collection(self):
        collector = Collector()
        resource = Resource("Plant_test", 5)
        collector.track_resource_collection(resource)
        self.assertEqual(len(collector.resources_collected), 1)

    def test_get_resource_statistics(self):
        collector = Collector()
        resource1 = Resource("test1", 5)
        resource2 = Resource("test2", 3)
        collector.track_resource_collection(resource1)
        collector.track_resource_collection(resource2)
        stats = collector.get_resource_statistics()
        self.assertEqual(stats.total_resources_collected, 8)
        self.assertEqual(stats.resource_breakdown["test1"], 5)
        self.assertEqual(stats.resource_breakdown["test2"], 3)

if __name__ == '__main__':
    pytest.main()
