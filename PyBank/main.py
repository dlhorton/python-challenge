import csv

# Path to the CSV file
csv_path = "/Users/demetriahorton/Downloads/Starter_Code 4/PyBank/Resources/budget_data.csv"

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Track the total number of months
        total_months += 1

        # Track the total profit/loss
        total_profit_loss += int(row[1])

        # Track the profit/loss changes
        if total_months > 1:
            profit_loss_changes.append(int(row[1]) - previous_profit_loss)

        # Track the dates
        dates.append(row[0])

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change
average_change = sum(profit_loss_changes) / (total_months - 1)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
