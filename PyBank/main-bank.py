# Import dependencies
import os
import csv
import datetime
import math
import statistics
import string
import numpy 

# Safe message
print("dependencies were correctly imported")

# Path to collect the data (indicate where the data is)
budget_file = os.path.join("Resources", "budget_data.csv")

# Safe message
#print("budget file path was found")

# Create lists
date_list = []
p_l_list = []


# Read the file using the CSV module (to take advantage of it, otherwise, you are reading it as text)
with open(budget_file, "r", newline="") as budget_csv:
        # This stores and print a reference to the file location (also known as file stream), not to the file content
        # It is useful for debugging
        #print(budget_csv)
        #
        # CSV reader specifies delimiter and variable that holds contents
        budget_csv_reader = csv.reader(budget_csv, delimiter=",")
        #
        #If you want to know where the object is, you print the address (this will not print the content of the file)
        #print(budget_csv_reader)
        
        # Print the header row first
        #whateveriwant_header = next(budget_csv_reader)
        #print(f"CSV Header: {whateveriwant_header}")
        #
        # Get rid of the header (because it won't let you do the math b/c it is a string)
        header = next(budget_csv_reader)

        # Prompt the user, maybe this make the code to work
        #checking = input("Do you want to run the Financial Analysis? (y/n) ")

        # Start counting from zero
        total_months = 0
        total_p_l = 0

        # Found differences between consecutive elements in the list
        diff_p_l = numpy.diff(p_l_list)

        # Identify average change in p_l
        ave_p_l = statistics.mean(diff_p_l) 

        # Identify greatest increase in p_l
        increases = diff_p_l[diff_p_l > 0]
        greatest_inc = max(increases)
        
        # Identify greatest decrease in p_l
        decreases = diff_p_l[diff_p_l < 0]
        greatest_dec = min(decreases)
        
        # Append to the lists using the data from the dataset and reset the countings
        for row in budget_csv_reader:
                date_list.append([0])
                p_l_list.append([1])
                total_p_l=total_p_l+int(row[1])
                total_months = total_months + 1
      

# Final script should print the analysis to the terminal 
print(f"- - - - - - - - - - - - - - - - - - - -")
print(f"Financial Analysis") 
print(f"- - - - - - - - - - - - - - - - - - - -")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_p_l)}")
print(f"Average Change: ${str(ave_p_l)}")
print(f"Greatest Increase in Profits: (${str(greatest_inc)})")
#print(f"Greatest Increase in Profits: {str()} (${str()})")
#print(f"Greatest Decrease in Profits: {str()} (${str()})")
print("- - - - - - - - - - - - - - - - - - - -")

        
# Final script should export a text file with the results
#with open("main-bank.txt", "w") as text_file:
        #print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        #print(f"Financial Analysis") 
        #print(f"- - - - - - - - - - - - - - - - - - - -")
        #print(f"Total Months: {str(total_months)}")
        #print(f"Total: ${str(total_p_l)}")
        #print(f"Average Change: ${str(ave_p_l)}")
        #print(f"Greatest Increase in Profits: (${str(greatest_inc)})")
        #print(f"Greatest Increase in Profits: {str()} (${str()})")
        #print(f"Greatest Decrease in Profits: {str()} (${str()})")
        #print("- - - - - - - - - - - - - - - - - - - -")
        #print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        

# Say good bye (verifying that everything was done)
print("Done for today!")



# Define the function for average
#def average(numbers):
#        length = len(numbers)
#        total = 0.0
#        for number in numbers:
#                total += number
#        return total / lenght 

# Define the function
#def financial_function():
        # For readibility, assign values to varialbes with descriptive names
        #dates_f = (axis=0)
        #p_l = (axis=1)
        
        # Calculate the total number of months included in the dataset
        #total_months = (dates_f)

        # Calculate the net total amount of "Profit/Losses" over the entire period
        #total_p_l = math.fsum(p_l)

        # The average of the changes in "Profit/Losses" over the entire period
        #ave_p_l = statistics.mean(p_l) 
    
        # The greatest increase in profits (dates and amount) over the entire period
        #greatest_inc = max(p_l)
        #
        #greatest_to_print = [XXX for XXX in p_l if XXX == {greatest_inc}]
        #print(greatest_to_print)
        #
        # The greatest decrease in losses (date and amount) over the entire period
        #greatest_dec = 
        #
        #greatest_dec_to_print = [XXX for XXX in p_l if XXX == {greatest_dec}]
        #print(greatest_dec_to_print)

        #return 

        # Run the data
        #for row in budget_csv_reader:
                # If the user wants the analysis, that's OK
                #if checking == "y":
                        #financial_function()
        

