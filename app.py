# api_server.py
from flask import Flask, jsonify
import time
import concurrent.futures
import psutil

app = Flask(__name__)

# Define variables to keep track of performance metrics
start_time = time.time()
success_count = 0
total_count = 0
cpu_percent = psutil.cpu_percent()

# Define the function to simulate a user session
def user_session(session_id):
    global success_count, total_count
    # Simulate processing time
    time.sleep(0.1)
    success_count += 1
    total_count += 1

@app.route('/endpoint')
def endpoint():
    user_session(0)  # Simulate a user session
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
