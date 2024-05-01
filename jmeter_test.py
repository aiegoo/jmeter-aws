import requests
import time
import concurrent.futures
import psutil

# Define the base URL for your API
base_url = "http://your-api-url.com"

# Define the number of user sessions
num_sessions = 2000

# Define variables to keep track of performance metrics
start_time = time.time()
success_count = 0
total_count = 0
cpu_percent = psutil.cpu_percent()

# Define the function to simulate a user session
def user_session(session_id):
    global success_count, total_count
    # Send an HTTP request
    response = requests.get(f"{base_url}/endpoint")
    # Check if the request was successful
    if response.status_code == 200:
        success_count += 1
    # Record the response time
    response_time = time.time() - start_time
    # Print the performance metrics
    print(f"Session {session_id}: Response time = {response_time}s, CPU usage = {psutil.cpu_percent() - cpu_percent}%, Success = {response.status_code == 200}")
    # Update the total count
    total_count += 1

# Simulate the user sessions using a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=num_sessions) as executor:
    executor.map(user_session, range(num_sessions))

# Calculate the average availability and success rate
avg_availability = success_count / total_count
success_rate = (success_count / num_sessions) * 100

# Print the final performance metrics
print(f"Total time = {time.time() - start_time}s")
print(f"CPU usage = {psutil.cpu_percent() - cpu_percent}%")
print(f"Average availability = {avg_availability}")
print(f"Success rate = {success_rate}%")
