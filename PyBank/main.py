
import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#Store the content 
date = []
profit = []

total_amount = 0
change = 0
greatestInc = 0
greatestDec = 0

#Iterare through the csv file 
with open(budget_csv, "r", encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])

    #The total number of months is the lenght of the list
    total_months = len(date)
    
    for i in range(len(profit)):
        #Total amount of Profit/Losses.
        total_amount += int(profit[i])
        #average of changes in Profit/Losses
        if i < len(profit)-1:
            change += int(profit[i+1]) - int(profit[i])
            increase = int(profit[i+1]) - int(profit[i])
        #Greatest Increase value
        if increase >= greatestInc:
            greatestInc = increase
            date_gratestInc = date[i+1]
        #Greatest Decrease value
        if increase <= greatestDec:
            greatestDec = increase
            date_gratestDec = date[i+1]

    #This is part for the average calculation        
    avg_change = round(change / (len(profit)-1),2)
    
#Analysis results
analysis = f"""
Financial Analysis
-------------------------------------------------
Total Months: {total_months}
Total: ${total_amount}
Average Change: ${avg_change}
Greatest Increase in Profits: {date_gratestInc} (${greatestInc})
Greatest Decrease in Profits: {date_gratestDec} (${greatestDec})
 """
print(analysis)

#Creation of txt file with the analysis results
output_file = os.path.join("analysis", "analysis_file.txt")

with open(output_file, "w") as textfile:
    textfile.write(analysis)