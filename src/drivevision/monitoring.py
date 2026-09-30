from collections import deque
import statistics

class RuntimeMonitor:
    def __init__(self,window=200):self.latencies=deque(maxlen=window);self.failures=0;self.frames=0
    def record(self,latency_ms,ok=True):
        self.frames+=1;self.latencies.append(float(latency_ms));self.failures+=0 if ok else 1
    def snapshot(self):
        vals=list(self.latencies)
        return {"frames":self.frames,"mean_latency_ms":statistics.mean(vals) if vals else 0.0,"failure_rate":self.failures/max(self.frames,1)}
