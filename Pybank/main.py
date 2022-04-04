#import modules
import os
import csv 

#import path to CSV and READ
csvpath=os.path.join('Pybank', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #working directory
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_chnage = []   
    #print(f"Header: {csv_header}") 

# The total number of months included in the data set
    for row in csvreader:
       month.append(row[0]) #indentify which row containign months
       revenue.append(row[1]) #identify row containing revenue(profit or loss)
    #print(len(month)) # len function sums up the number of specified months as previous


# Calculating net total revenue (profit or loss) over entire dataset
    revenue_integer = map(int,revenue) # change current string value of profit or loss row into integers
    revenue_total = (sum(revenue_integer)) # sum all values
    #print(revenue_total)

# Average change in profit or loss over enitre period
    i = 0
    for i in range(len(revenue)-1):
        profit_loss= int(revenue[i+1])- int(revenue[i])
        revenue_change.append(profit_loss) #append profit or loss

    Total = sum(revenue_change)
    monthly_change = Total/ len(revenue_change)
    #print(monthly_change)

# Calculating greatest incresae in profits (date and amount) over entire period
    profit_increase = max(revenue_change)
    #print(profit_increase)
    K = revenue_change.index(profit_increase) #index string that corrolates to the greatest increase in profit (month)
    month_increase = month[K + 1]

#Calculating greatest decrease in  profits (date and amount) over entire period
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    J = revenue_change.index(profit_decrease)
    month_decrease = month[J + 1]

#final print statements
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total months: " + str(len(month)))

print("Total Revenue in period: $ " + str(revenue_total))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

#creating output txt
g = open('Pybank/Analysis/Pybank_Result.txt', "a")
print((f'Financial Analysis'+'\n'), file = g)
print((f'----------------------------'+'\n'), file = g)
print(("Total months: " + str(len(month))), file = g)   
print(("Total Revenue in period: $ " + str(revenue_total)), file = g)    
print(("Average monthly change in Revenue : $" + str(monthly_change)), file = g)
print((f"Greatest Increase in Profits: {month_increase} (${profit_increase})"), file = g)
print((f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})"), file = g)
g.close()
