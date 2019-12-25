# Import dependencies
import os
import csv
import datetime
import math
import statistics
import string

# Safe message
print("imports were correct")

# Path to collect the data (indicate where the data is)
budget_file = os.path.join("Resources", "budget_data.csv")

# Safe message
print("budget file path was found")

# Read the file using the CSV module (to take advantage of it, otherwise, you are reading it as text)
with open(budget_file, newline="") as budget_csv:

    # This stores and print a reference to the file location (also known as file stream), not to the file content
    # It is useful for debugging
    print(budget_csv)

    # CSV reader specifies delimiter and variable that holds contents
    budget_csv_reader = csv.reader(budget_csv, delimiter=",") 

    #If you want to know where the object is, you print the address (this will not print the content of the file)
    print(budget_csv_reader)

    # Print the header row first
    whateveriwant_header = next(budget_csv_reader)
    print(f"CSV Header: {whateveriwant_header}")

    # Read each row of data after the header
    for row in budget_csv_reader:
        print(row)
    




# # Define the function
# def financial_analysis(financial_data)
    
#     # For readibility, assign values to varialbes with descriptive names
#     date = str(financial_data[0])
#     p_l = int(financial_data[1])
    
#     # Calculate the total number of months included in the dataset
#     total_months = date.count(:)
#     print(total_months)

#     # Calculate the net total amount of "Profit/Losses" over the entire period
#     total_p_l = p_l.sum(:)
#     print(total_p_l)

#     # The average of the changes in "Profit/Losses" over the entire period
#     ave_p_l = p_l.mean(:)
#     print(ave_p_l)
    
#     # The greatest increase in profits (dates and amount) over the entire period
#     #greatest_inc = 
        
        #greatest_to_print = [XXX for XXX in p_l if XXX == {greatest_inc}]
        #print(greatest_to_print)
    
        # The greatest decrease in losses (date and amount) over the entire period
        #greatest_dec = 
        
        #greatest_dec_to_print = [XXX for XXX in p_l if XXX == {greatest_dec}]
        #print(greatest_dec_to_print)


    
    

# # Final script should both print the analysis to the terminal and export a text 
# # file with the results

#print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#print(f"
# Financial Analysis
# - - - - - - - - - - - - - - - - - - - - 
# Total Months:{}
# Total: ${}
# Average Change: ${}
# Greatest Increase in Profits: {} (${})
# Greatest Decrease in Profits: {} (${})
# - - - - - - - - - - - - - - - - - - - -")

#print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
