with open('webserver.log', 'r') as log_file:
    lines = log_file.readlines()

error_500 = {}

for line in lines:
    parts = line.split()
    status = parts[8]
    endpoint = parts[6]

    # only care about 500s
    if status == '500':
        error_500[endpoint] = error_500.get(endpoint, 0) + 1

print("\n=== Endpoints with 500 errors ===")
for endpoint, count in error_500.items():
    print(f"{endpoint} -> {count} times")