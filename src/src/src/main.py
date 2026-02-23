# src/main.py

from watcher import Watcher
from decider import Decider
from actuator import Actuator
from rollback import Rollback


class AdaptiveSystem:
    """Main system that orchestrates Watch-Decide-Act-Rollback"""
    
    def __init__(self):
        self.watcher = Watcher()
        self.decider = Decider()
        self.actuator = Actuator()
        self.rollback = Rollback()
    
    def run(self, module_name):
        """Run full cycle: Watch → Decide → Act → Verify"""
        
        print(f"\n{'='*50}")
        print(f"🚀 Starting adaptive cycle for: {module_name}")
        print(f"{'='*50}\n")
        
        # 1. WATCH
        print("👁️  STEP 1: Watching...")
        metrics = self.watcher.watch_module(module_name)
        print(f"   CPU: {metrics['cpu']}%")
        print(f"   Memory: {metrics['memory']}%\n")
        
        # 2. DECIDE
        print("🤔 STEP 2: Deciding...")
        should_migrate, reason = self.decider.should_migrate(metrics)
        print(f"   Should migrate: {should_migrate}")
        print(f"   Reason: {reason}\n")
        
        if not should_migrate:
            print("✅ No action needed. System healthy.")
            return
        
        # Save state before migration
        self.rollback.save_state(module_name, {"status": "before_migration"})
        
        # 3. ACT
        print("⚙️  STEP 3: Acting...")
        try:
            result = self.actuator.extract_module(module_name)
            print(f"   Result: {result}\n")
            
            # 4. VERIFY
            print("✅ STEP 4: Verifying...")
            is_healthy = self.rollback.verify_health(module_name)
            
            if is_healthy:
                print("   Migration successful!")
            else:
                print("   Migration failed! Rolling back...")
                self.rollback.rollback(module_name)
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            print("   Rolling back...")
            self.rollback.rollback(module_name)


# Run example
if __name__ == "__main__":
    system = AdaptiveSystem()
    
    # Test with a module
    system.run("payment_module")
