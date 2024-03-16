import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')



# Open and Read in the CSV file
with open(budget_csv, 'r') as budgetcsv:

    # Spliting the data using ',' as columns 
    csvreader = csv.reader(budgetcsv, delimiter=',')
    
    # Read the header row first and storing it as a list
    header = next(csvreader)

    #initializing variables to hold items such as total profit, average change
    #   greatest increase in profits, and greatest decrease in profits

    totalp = 0
    avchange = 0
    lst_of_profit = []
    lst_of_changes = []
    GIP = 0
    GDP = 0

    # looping through CSV file 
    for row in csvreader:
        totalp = totalp + int(row[1])
        lst_of_profit.append(int(row[1]))

    for i in range(0, len(lst_of_profit) - 1):
         lst_of_changes.append(int(lst_of_profit[i+1]) - int(lst_of_profit[i]))
    
   
    totalchange = 0
    length = len(lst_of_changes)

    for changes in lst_of_changes:
       totalchange += changes
       avchange = round(totalchange / length, 2)

        
        

        
     #declaring a variable named changes to record changes between months.

    print(f'{avchange}')

    


       






#Defining a function that analyzes a financial dataset composed of 2
#   columns: "Date" and "Profit/Losses"

#def pybanking(budget):
