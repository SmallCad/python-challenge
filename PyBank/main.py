import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')



# Open and Read in the CSV file
with open(budget_csv, 'r') as budgetcsv:

    # Spliting the data using ',' as columns 
    csvreader = csv.reader(budgetcsv, delimiter=',')
    
    # Read the header row first and storing it as a list to remove it from the data.
    header = next(csvreader)

    #initializing variables to hold items such as total profit, average change in profit
    #   greatest increase in profits (and its month), and greatest decrease in profits  
    #    (and its month). Lists containing each month's profits and change in profits are 
    #    initialized here as well.

    totalp = 0
    avchange = 0
    GIP = []
    GDP = []
    lst_of_profit = []
    lst_of_changes = []

    # looping through CSV file. totalp should equal sum of all profits.
    #  lst_of_profits should store rows in the csv file in a "Date , Profit" format

    for row in csvreader:
        totalp = totalp + int(row[1])
        lst_of_profit.append(row)


    #looping through lst_of_profit and calculating the difference in profits between
    #   months. the differences are stored in  lst_of_changes.
    for i in range(0, len(lst_of_profit) - 1):
         lst_of_changes.append(int(lst_of_profit[i+1][1]) - int(lst_of_profit[i][1]))
    
   
    #To get the average of changes, totalchange and length are initialized and then looped
    totalchange = 0
    length = len(lst_of_changes)

    for changes in lst_of_changes:
       totalchange += changes
       avchange = round(totalchange / length, 2)

    
    
    #initializing variables to be looped through the lst_of_changes. the variables will
    #   store the greatest change in profit and losses. trackers will track in 
    #   which month the greatest changes occured.
    GIPamount = 0
    GDPamount = 0  
    GIPtracker = 0
    GDPtracker = 0

    for i in range(0,length):
        if GIPamount < int(lst_of_changes[i]):
            GIPtracker = i
            GIPamount = int(lst_of_changes[i])
        
        elif GDPamount > int(lst_of_changes[i]):
            GDPtracker = i
            GDPamount = int(lst_of_changes[i])
    
    #appending the date the greatest changes occured and their
    #   values to their respective variables
    GIP.append(lst_of_profit[GIPtracker + 1][0])
    GIP.append(GIPamount)

    GDP.append(lst_of_profit[GDPtracker + 1][0])
    GDP.append(GDPamount)





   #Printing the financial analysis    
    
    print('Financial Analysis \n ')
    print('-------------------------------------------- \n')
    print(f'Total Months: {len(lst_of_profit)}\n')    
    print(f'Average Change: ${avchange} \n')
    print(f'Greatest Increase in Profits: {GIP[0]} ${GIP[1]} \n')
    print(f'Greatest Decrease in Profits: {GDP[0]} ${GDP[1]}')



#Exporting the results to a text file. Code provided by Xpert Learning Assistant - NEW!
results_txt = os.path.join('analysis', 'pybank_results.txt') 
    
with  open(results_txt, 'w') as txtfile:
    txtfile.write('Financial Analysis \n')
    txtfile.write('---------------------------- \n')
    txtfile.write(f'Total Months: {len(lst_of_profit)} \n')  
    txtfile.write(f'Average Change: ${avchange} \n') 
    txtfile.write(f'Greatest Increase in Profits: {GIP[0]} ${GIP[1]} \n')
    txtfile.write(f'Greatest Decrease in Profits: {GDP[0]} ${GDP[1]}')


