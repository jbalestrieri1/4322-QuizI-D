'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

infile = open('employee_data.csv')

variable = csv.reader(infile)

# create an empty dictionary

csr = {}

# use a loop to iterate through the csv file

for x in variable:
    FullName = (x[1] + x[2])
    Salary = int(x[5])
    Title = (x[4])

print('FullName', 'Salary')

# check if the employee fits the search criteria
if x[4] == 'CSR':
    NewSalary = 1.1('Salary')
    print('FullName', 'NewSalary')


print()
print('================================')
print()

# iternate through the dictionary and print out the key and value as per printout
