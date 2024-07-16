import subprocess
import time

# Path to your separate script
script_path = r'C:\Users\elmal\Downloads\Bosta Assesment\ETL.py'

# Number of times to run the script
num_iterations = 100 #to add 100 record

# Run the script in a loop
for i in range(num_iterations):
    subprocess.run(['python', script_path])
    time.sleep(1)  # Optional: add a delay between iterations
