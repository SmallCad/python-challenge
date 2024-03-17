import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('Pypoll', 'Resources', 'election_data.csv')



# Open and Read in the CSV file
with open(poll_csv, 'r') as pollcsv:

    # Spliting the data using ',' as columns 
    csvreader = csv.reader(pollcsv, delimiter=',')

    #Read the header row first and storing it as a list to remove it from the data.
    header = next(csvreader)

    #Declaring variables given my objectives to find (1)total votes, (2)A complete list of
    #   candidates who received votes, (3)The total number of votes each candidate won. this
    #   can be stored along side candidates in a dictionary. (4) The winner of the election 
    #   based on popular vote

    totalv = 0
    dict_candidates = {}  
    winner = ""
        

    #appending the data in csvreader to a list for data access and manipulation
    #   using lst_ballot to hold the data of ballot entries
    lst_ballot = []

    for row in csvreader:
        lst_ballot.append(row)


    #total votes should equal the total number of ballots entered
    totalv = len(lst_ballot)

    #to create a dictionary of candidates, we loop through lst_ballots and record
    #   unique names as candidates which will be the dictionary's keys. then we
    #   count 1 vote for every time the candidate name appears.
    candidate = ''
    for row in lst_ballot:
        if candidate != row[2]:
            candidate = row[2]  
            if dict_candidates.get(candidate) == None:
                   dict_candidates[candidate] = 1
            else: dict_candidates[candidate] = int(dict_candidates[candidate]) + 1
                


        else: dict_candidates[candidate] = int(dict_candidates[candidate]) + 1
    

    #selecting the winner by most votes. initializing variable votes. assumes no draws.
    votes = 0
        
    for key in dict_candidates:
         if int(dict_candidates[key]) > votes:
              winner = key
              votes = int(dict_candidates[key])
            
    
    
    #printing election results  
              
    print(f'Election Results \n ')
    print(f'------------------------- \n')
    print(f'Total Votes: {totalv} \n')
    print(f'------------------------- \n')
    
    for key in dict_candidates:
         print(f'{key}: {round(100*(int(dict_candidates[key])/totalv),3)}% ({(dict_candidates[key])}) \n')

    print(f'------------------------- \n')
    print(f'Winner: {winner} \n')
    print(f'------------------------- \n')
               

#Exporting the results to a text file. Code provided by Xpert Learning Assistant - NEW!
pypoll_txt = os.path.join('Pypoll', 'analysis', 'pypoll_results.txt') 
    
with  open(pypoll_txt, 'w') as txtfile:
    txtfile.write(f'Election Results\n ')
    txtfile.write(f'------------------------- \n')
    txtfile.write(f'Total Votes: {totalv} \n')
    txtfile.write(f'------------------------- \n')
    
    for key in dict_candidates:
         txtfile.write(f'{key}: {round(100*(int(dict_candidates[key])/totalv),3)}% ({(dict_candidates[key])}) \n')

    txtfile.write(f'------------------------- \n')
    txtfile.write(f'Winner: {winner} \n')
    txtfile.write(f'------------------------- \n')
          


    