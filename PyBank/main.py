# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import math

csvpath = os.path.join('budget_data.csv') 

output_path = os.path.join('pybanktxt.txt')

# Module used for reading csv files
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    total_months= 0
    totalamount= 0
    lastamount=0
    change=0
    totalchange=0
    averagechange=0
    greatest_decrease = 0
    greatest_increase = 0
    greatest_increase_month=[]
    greatest_decrease_month=[]


    # Read each row of data after the header
    for row in csvreader:

        total_months=total_months+1
        totalamount=totalamount+int(row[1])

        if total_months != 1:
            change=int(row[1])-lastamount

        totalchange = totalchange + change

        lastamount= int(row[1])

        if change > greatest_increase:
           greatest_increase= change
           greatest_increase_month= row[0]

        if totalchange < greatest_decrease:
           greatest_decrease= change
           greatest_decrease_month= row[0]     

averagechange = totalchange/((total_months)-1) 
print("Financial Analysis")  
print("-----------------------")
print("Total Months: "+str(total_months))
print("Total: "+"$"+str(totalamount))
print("Average Change: "+str(round(averagechange)))
print("Greatest Increase in Profits: "+str(greatest_increase_month)+" ($"+str(greatest_increase)+")")
print("Greatest Decrease in Profits: "+str(greatest_decrease_month)+" ($"+str(greatest_decrease)+")")

