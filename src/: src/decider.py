# src/decider.py


class Decider:
    """Decide if module should be extracted to microservice"""
    
    def __init__(self, cpu_threshold=70, memory_threshold=80):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
    
    def should_migrate(self, metrics):
        """
        Decide if migration is needed based on metrics
        
        metrics = {
            'cpu': 75,
            'memory': 60,
            'timestamp': 1234567890
        }
        """
        cpu = metrics.get('cpu', 0)
        memory = metrics.get('memory', 0)
        
        # If CPU or Memory is above threshold, migrate
        if cpu > self.cpu_threshold:
            return True, f"CPU high: {cpu}%"
        
        if memory > self.memory_threshold:
            return True, f"Memory high: {memory}%"
        
        return False, "Metrics normal"
    
    def calculate_cost(self, module_name):
        """
        Calculate migration cost (simplified)
        Lower cost = easier to migrate
        """
        # TODO: Add real cost calculation
        return {
            'module': module_name,
            'estimated_time': '2 hours',
            'risk': 'low',
            'downtime': '30 seconds'
        }


# Example usage
if __name__ == "__main__":
    decider = Decider()
    
    test_metrics = {'cpu': 75, 'memory': 60}
    should_migrate, reason = decider.should_migrate(test_metrics)
    
    print(f"Should migrate: {should_migrate}")
    print(f"Reason: {reason}")
