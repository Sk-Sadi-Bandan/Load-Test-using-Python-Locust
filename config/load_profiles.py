from locust import LoadTestShape

class HeavyLoad(LoadTestShape):
    """
    Profile for heavy load test with significant server pressure
    """
    stages = [
        {"duration": 15, "users": 10, "spawn_rate": 10},
        {"duration": 30, "users": 15, "spawn_rate": 15},
        {"duration": 45, "users": 20, "spawn_rate": 20},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])

        return None
