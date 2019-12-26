# Import dependencies
import os
import csv
import datetime
import math
import statistics
import string

# Safe message
#print("imports were correct")

# Path to collect the data (indicate where the data is)
budget_file = os.path.join("Resources", "budget_data.csv")

# Safe message
#print("budget file path was found")

# Define the function for average
#def average(numbers):
#        length = len(numbers)
#        total = 0.0
#        for number in numbers:
#                total += number
#        return total / lenght 

# Define the function
def financial_function():
        # For readibility, assign values to varialbes with descriptive names
        dates_f = (axis=0)
        p_l = (axis=1)
        
        # Calculate the total number of months included in the dataset
        total_months = (dates_f)

        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_p_l = math.fsum(p_l)

        # The average of the changes in "Profit/Losses" over the entire period
        ave_p_l = statistics.mean(p_l) 
    
        # The greatest increase in profits (dates and amount) over the entire period
        greatest_inc = max(p_l)
        #
        #greatest_to_print = [XXX for XXX in p_l if XXX == {greatest_inc}]
        #print(greatest_to_print)
        #
        # The greatest decrease in losses (date and amount) over the entire period
        #greatest_dec = 
        #
        #greatest_dec_to_print = [XXX for XXX in p_l if XXX == {greatest_dec}]
        #print(greatest_dec_to_print)

        # Final script should print the analysis to the terminal 
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print(f"Financial Analysis") 
        print(f"- - - - - - - - - - - - - - - - - - - -")
        print(f"Total Months: {str(total_months)}")
        print(f"Total: ${str(total_p_l)}")
        print(f"Average Change: ${str(ave_p_l)}")
        print(f"Greatest Increase in Profits: (${str(greatest_inc)})")
        #print(f"Greatest Increase in Profits: {str()} (${str()})")
        #print(f"Greatest Decrease in Profits: {str()} (${str()})")
        print("- - - - - - - - - - - - - - - - - - - -")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        
        # Final script should export a text file with the results
        return 

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
        #
        # Print the header row first
        #whateveriwant_header = next(budget_csv_reader)
        #print(f"CSV Header: {whateveriwant_header}")
        #
        # Get rid of the header (because it won't let you do the math b/c it is a string)
        header = next(budget_csv_reader)

        # Prompt the user, maybe this make the code to work
        checking = input("Do you want to run the Financial Analysis? (y/n) ")

        # Run the data
        for row in budget_csv_reader:
                # If the user wants the analysis, that's OK
                if checking == "y":
                        financial_function()
        
print("Done for today!")
