#constructing pathway to csv file
import os
import csv

# Path to collect data from the Resources folder
Bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Lists to store data
profit = []
monthly_changes = []
date = []

# Variables to track data
total_months = 0
sum_of_profit = 0
sum_of_change = 0
starting_profit = 0

# Read in the CSV file
with open(Bank_csv, encoding='UTF-8') as budget:
    csvreader = csv.reader(budget, delimiter=",")
    csv_header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        total_months = total_months + 1
        profit.append(row[1])
        sum_of_profit = sum_of_profit + int(row[1])
        final_profit = int(row[1])
        
        # Calculating the change in profits
        if total_months > 1:
            
            # Calculating the change in profits
            monthly_change_in_profits = final_profit - starting_profit
            sum_of_change = sum_of_change + monthly_change_in_profits
            monthly_changes.append(monthly_change_in_profits)
            
            # Calculating the date
            date.append(row[0])
        
        # Setting the profit to the next row
        starting_profit = final_profit
        
        # Calculating the average change in profits
    average_of_profit_changes = (sum_of_change/(total_months - 1))

    # Calculating the greatest increase and decrease in profits
    greatest_increase_in_prof = max(monthly_changes)
    greatest_decrease_in_prof = min(monthly_changes)
    
    # Calculating the date of the greatest increase and decrease in profits
    increase_by_date = date[monthly_changes.index(greatest_increase_in_prof)]
    decrease_by_date = date[monthly_changes.index(greatest_decrease_in_prof)]

# Storing the analysis results in a dictionary
analysis = {
    "Total Months": total_months,
    "Total Profits": sum_of_profit,
    "Average Change": int(average_of_profit_changes),
    "Greatest Increase": {
        "Date": increase_by_date,
        "Amount": greatest_increase_in_prof
    },
    "Greatest Decrease": {
        "Date": decrease_by_date,
        "Amount": greatest_decrease_in_prof
    }
}

# Here I print the analysis results
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {analysis['Total Months']}")
print(f"Total: ${analysis['Total Profits']}")
print(f"Average Change: ${analysis['Average Change']}")
print(f"Greatest Increase in Profits: {analysis['Greatest Increase']['Date']} (${analysis['Greatest Increase']['Amount']})")
print(f"Greatest Decrease in Profits: {analysis['Greatest Decrease']['Date']} (${analysis['Greatest Decrease']['Amount']})")

# outputting the analysis results to a text file
with open('Analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------------------------\n")
    text.write(f"Total Months: {analysis['Total Months']}\n")
    text.write(f"Total Profits: ${analysis['Total Profits']}\n")
    text.write(f"Average Change: ${analysis['Average Change']}\n")
    text.write(f"Greatest Increase in Profits: {analysis['Greatest Increase']['Date']} (${analysis['Greatest Increase']['Amount']})\n")
    text.write(f"Greatest Decrease in Profits: {analysis['Greatest Decrease']['Date']} (${analysis['Greatest Decrease']['Amount']})\n")




