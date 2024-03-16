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
    GIP = []
    GDP = []

    ## looping through CSV file 


    for row in csvreader:
        totalp = totalp + int(row[1])
        lst_of_profit.append(row)

    for i in range(0, len(lst_of_profit) - 1):
         lst_of_changes.append(int(lst_of_profit[i+1][1]) - int(lst_of_profit[i][1]))
    
   
    totalchange = 0
    length = len(lst_of_changes)

    for changes in lst_of_changes:
       totalchange += changes
       avchange = round(totalchange / length, 2)

    
    
    #initializing a variable to be looped through the list of changes in profit
       #the variables will store the greatest change in profit and losses
    GIPamount = 0
    GDPamount = 0
    
    
    #initializing a variable to be looped through the list of changes in profit
       #the variable will track when the greatest change in profit occurs
    GIPtracker = 0
    GDPtracker = 0

    for i in range(0,length):
        if GIPamount < int(lst_of_changes[i]):
            GIPtracker = i
            GIPamount = int(lst_of_changes[i])
        
        elif GDPamount > int(lst_of_changes[i]):
            GDPtracker = i
            GDPamount = int(lst_of_changes[i])
    
    GIP.append(lst_of_profit[GIPtracker + 1][0])
    GIP.append(GIPamount)

    GDP.append(lst_of_profit[GDPtracker + 1][0])
    GDP.append(GDPamount)





        
     #declaring a variable named changes to record changes between months.

    print(*GDP, sep=", ")

    


       






#Defining a function that analyzes a financial dataset composed of 2
#   columns: "Date" and "Profit/Losses"

#def pybanking(budget):
