with open("webserver.log", "r") as log_file:
    lines = log_file.readlines()

error_counts = {}
for line in lines:
    parts = line.split()
    status = parts[8]
    
    if status.startswith('4') or status.startswith('5'):
        error_counts[status] = error_counts.get(status, 0) + 1

total_errors = sum(error_counts.values())
print("\nError Counts:", total_errors)
total_requests = len(lines)
print("Total Requests:", total_requests)
error_rate = (total_errors / total_requests) * 100

print(f"Error Rate: {error_rate:.2f}%")