# src/watcher.py

import psutil
import time


class Watcher:
    """Watch system metrics and detect heavy modules"""
    
    def __init__(self):
        self.metrics = {}
    
    def get_cpu_usage(self):
        """Get current CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """Get current memory usage percentage"""
        return psutil.virtual_memory().percent
    
    def watch_module(self, module_name):
        """Watch a specific module and return metrics"""
        self.metrics[module_name] = {
            'cpu': self.get_cpu_usage(),
            'memory': self.get_memory_usage(),
            'timestamp': time.time()
        }
        return self.metrics[module_name]
    
    def is_overloaded(self, module_name, threshold=70):
        """Check if module is overloaded"""
        if module_name not in self.metrics:
            return False
        
        metric = self.metrics[module_name]
        return metric['cpu'] > threshold or metric['memory'] > threshold


# Example usage
if __name__ == "__main__":
    watcher = Watcher()
    print("CPU:", watcher.get_cpu_usage())
    print("Memory:", watcher.get_memory_usage())
