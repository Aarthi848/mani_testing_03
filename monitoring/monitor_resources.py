import psutil
import time
import logging

# Setup logging
class ResourceMonitor:
    def __init__(self, interval=5):
        self.interval = interval
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [ResourceMonitor] %(message)s',
            handlers=[
                logging.FileHandler("resource_usage.log"),
                logging.StreamHandler()
            ]
        )

    def log_usage(self):
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            logging.info(f"CPU: {cpu}% | "
                         f"Memory: {memory.percent}% ({memory.used//1024//1024}MB/{memory.total//1024//1024}MB) | "
                         f"Disk: {disk.percent}% ({disk.used//1024//1024}GB/{disk.total//1024//1024}GB)")

            time.sleep(self.interval)

if __name__ == "__main__":
    monitor = ResourceMonitor(interval=10)  # Log every 10 seconds
    monitor.log_usage()