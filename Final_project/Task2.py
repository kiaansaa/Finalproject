import sys

# Initialize variables to track statistics
total_runners = 0
total_time = 0
fastest_time = float("inf")
fastest_runner = None
slowest_time = 0

# Read input from the user
print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
while True:
  line = input("> ")
  if line == "END":
    break

  # Split the line into the runner number and time
  parts = line.split("::")
  if len(parts) != 2:
    print("Error in data stream. Ignorning. Carry on.")
    continue

  # Try to parse the runner number and time
  try:
    runner_number = int(parts[0])
    time = int(parts[1])
  except ValueError:
    print("Error in data stream. Ignorning. Carry on.")
    continue

  # Update statistics
  total_runners += 1
  total_time += time
  if time < fastest_time:
    fastest_time = time
    fastest_runner = runner_number
  if time > slowest_time:
    slowest_time = time

# Calculate average time
if total_runners == 0:
  print("No data found. Nothing to do. What a pity.")
  sys.exit()
else:
  average_time = total_time / total_runners

# Convert times to minutes and seconds
def to_minutes_seconds(time):
  minutes = time // 60
  seconds = time % 60
  return f"{minutes} minutes, {seconds} seconds"

fastest_time = to_minutes_seconds(fastest_time)
slowest_time = to_minutes_seconds(slowest_time)
average_time = to_minutes_seconds(average_time)

# Print results
print(f"\nTotal Runners: {total_runners}")
print(f"Average Time:  {average_time}")
print(f"Fastest Time:  {fastest_time}")
print(f"Slowest Time:  {slowest_time}")
print(f"Best Time Here: Runner #{fastest_runner}")