import subprocess
import time

# Path to the ETL script
script_path = r'path\to\ETL.py'

# Number of times to run the script
num_iterations = 100 #to add 100 records

# Running the script in a loop
for i in range(num_iterations):
    subprocess.run(['python', script_path])
    time.sleep(1)  # delay between iterations
