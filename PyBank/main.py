import csv 
import os 

# Define variables for end result clarification
total_months = 0 
total_profit = 0
monthly_average_change = 0 
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
previous_pl = None
changes = []

# Open the CSV file and read it 
with open ("budget_data.csv") as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)
    # Loop through each row in the CSV reader and perform the following analysis:
    for row in csvreader:
        # Define where date and P&L within the CSV file, ensure that P&L is defined as an integer
        date = row[0]
        profit_loss = int(row[1])
        # Calculate total profit off the P&L
        total_profit += profit_loss
        # Calculate and add one to total month counter
        total_months += 1
        # Calculate the greatest increase and greatest decrease with months 
        if previous_pl is not None:
            change = profit_loss-previous_pl
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = date
            if change < greatest_decrease:
                greatest_decrease = change 
                greatest_decrease_month = date
        # Define previous Pl- needed to calculate greatest increase and decrease
        previous_pl = profit_loss
        
# Define the Monthly Average Change 
monthly_average_change = round(sum(changes)/len(changes))

analysis = f"""
Financial Analysis
__________________
Total Profit: ${total_profit}
Total Months: {total_months}
Monthly Average Change: {monthly_average_change}
Greatest Increase: {greatest_increase_month}, ${greatest_increase}
Greatest Decrease: {greatest_decrease_month}, ${greatest_decrease}
"""
print(analysis)

save_final = input("Do you want to save the final results? (y/n)\n ")
if save_final =="y":
    with open ("output_file.txt","w") as doc:
        doc.write(analysis)
