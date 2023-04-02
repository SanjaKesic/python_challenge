# import libraries
import os
import csv
# set the file path
budget_csv = os.path.join("budget_data.csv")


# set up variables
total_months = 0
total_profit = 0
last_profit = None
changes = []
max_increase = 0
max_increase_date = ""
max_decrease = 0
max_decrease_date = ""

#read the file and loop through rows
with open (budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    #skip the header
    next(csv_reader)
    for row in csv_reader:
        date = row[0]
        

    # add the profit
        profit = float(row[1])
        total_profit += profit

    # calculate change in each profit
        if last_profit is not None:
            change = profit - last_profit
            changes.append(change)

        # if this is the max increase
            if change > max_increase:
                max_increase = change
                max_increase_date = date

        # if this is the max decrease
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date
                
        last_profit = profit
        total_months +=0

# average change calculation

avg_change = sum(changes) / len(changes)

#print

print("Financial Analysis")
print("---------------------")
print(f"Total months: {total_months}")
print(f"Total profit: ${total_profit}")
print(f"Average change: ${avg_change:.2f}")
print(f"Greatest increase in profits: {max_increase_date} (${max_increase})")
print(f"Greatest decrease in profits: {max_decrease_date} (${max_decrease})")


