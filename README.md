# python-challenge
 
 
 ## Using Python to analyze financial information and election votes results.
 In this assignment, I'll use the concepts learnt in class to complete two Python challenges, PyBank and PyPoll.

 For PyBank, I will be given a csv data set made up of two coloums; Dates and Profit/Losses. I must prepare a python script that reads in the csv file and prints out an analysis containing the number of months within the dataset, the net profit/loss, the average change in profit/loss from month to month, the greatest increase in profits (date and amount), as wells as the greatest decrease in profits (date and amount) over the entire period.

 For Pypoll, I will be given a csv data set made up of three columns; "Voter ID", "County", and "Candidate". The python script I prepare must read in the data set and print out the the total number of votes cast, a list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won, and the winner of the election based on popular vote.

## How did I approach these challenges?
Both challengese heavily relied on me reading in their csv file into python and storing their information in variables. 

For PyBank, i opted to use a list that stores the [Date and Profit/Loss] pairs as a list (a list of lists). Example: [['Jan-17', '607208'], ['Feb-17', '382539']]. With this list of dates and profits, i run various loops utilizing the fact that this_list[index I][1] will return the profits/loss made during period index I. 

For Pypoll, I managed to recognize that a data set made up of candidates in an election will have repeating data information. I.e. the candidates names will repeat. this allowed me to read in the csv file, loop through its rows, and store needed information in a dictionary using the candidates names as keys. Given the challenge objectives, I decided the only thing needed to be stored in the dictionary was a count tracking how many times a candidates name appear in the csv file. So my script emphasized looping through the data and adding 1 to each candidates count tracker which should equal their total votes.   


## Credits and in closing
I ran into a few challenges completing assignment.

Firstly, I know that in class we discussed how to unpack a list for printing purposes, but i could not recall how to.
Thanks to users Jianru Shi and Steve Bennett for answering and providing the edit (respectively) to how to print an unpacked list.
 https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row

 
 Secondly, I wasn't sure how to go about exporting results to a text file. Slides for class go over how to exporting to a csv file and i tried following along the slides but the formatting did not seem presentable. I believe we did exporting to a .txt as a class example but I did not know which example file to check to confirm. --> Xpert Learning Assistant - NEW! was used to generate script for  exporting and my results to a .txt. The code below was pretty much used as is:
 
    with open('output.txt', 'w') as file:

    file.write("Hello, this is some text that will be written to the file.\n")s

Lastly, in my Pypoll script, i ran into a road block trying to test an if condition. initially, my code ran fine in a sorted list where a candidates name did not show up again after an initial iteration. however, candidates could be voted for in different counties so their could be reiterations after a break. I needed a way to check if a given key for my dictionary already had stored data. I am not sure if this was covered in class but using the youtube link below, I came accross dictionary.get() function that was a safe way of returning a value assigned to a key or returning 'None' if that key did not exist within the dictionary.
thus checking for a key not yet established became:
    if dictionary.get(new_key) == None

https://www.youtube.com/watch?v=daefaLgNkw0 -- Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs by Corey Schafer