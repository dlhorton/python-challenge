import csv

# Path to the CSV file
csv_path = "/Users/demetriahorton/Downloads/Starter_Code 4/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Track the total number of votes
        total_votes += 1

        # Track the votes for each candidate
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Track the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    # Calculate and write the percentage of votes each candidate won
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
