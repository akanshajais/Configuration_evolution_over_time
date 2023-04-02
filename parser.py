import csv
import subprocess
from datetime import datetime
# Define a data structure to hold the parsed data
data = []
filename = "cities_data.csv"
# Define a function to parse the CSV file
def parse_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

# Initialize a Git repository and commit the initial data file
subprocess.run(['git', 'init'])
subprocess.run(['git', 'add', "cities_data.csv"])
subprocess.run(['git', 'commit', '-m', 'Initial commit'])

# Loop over all Git commits and parse the data at each commit
for line in subprocess.check_output(['git', 'log', '--pretty=format:%H']).splitlines():
    commit_hash = line.decode('utf-8')
    subprocess.run(['git', 'checkout', commit_hash, '--', 'cities_data.csv'])
    parse_csv(filename)
    commit_timestamp = datetime.strptime(subprocess.check_output(['git', 'show', '-s', '--format=%ci', commit_hash]).decode('utf-8').strip(), '%Y-%m-%d %H:%M:%S %z')
    for row in data:
        row['commit_timestamp'] = commit_timestamp

# Export the sequence as a flat structure with the additional column for commit timestamp
with open('cities_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['City','Temperature','commit_timestamp'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
