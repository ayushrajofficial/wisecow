import psutil

# Thresholds (adjust these as needed)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Function to check CPU usage
def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")
    if cpu_percent > CPU_THRESHOLD:
        print("CPU usage is above threshold!")

# Function to check memory usage
def check_memory():
    memory_percent = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory_percent}%")
    if memory_percent > MEMORY_THRESHOLD:
        print("Memory usage is above threshold!")

# Function to check disk space
def check_disk():
    disk_percent = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk_percent}%")
    if disk_percent > DISK_THRESHOLD:
        print("Disk space usage is above threshold!")

# Function to check running processes
def check_processes():
    process_count = len(psutil.pids())
    print(f"Running Processes: {process_count}")

# Main function
def main():
    print("System Health Monitoring Script")
    
    print("")
    check_cpu()

    print("")
    check_memory()

    print("")
    check_disk()

    print("")
    check_processes()

# Run the main function
if __name__ == "__main__":
    main()
