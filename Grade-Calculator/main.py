'''
    Title:          Course Score Calculator
    Description:    Assignment 2
    Author:         Quinn Bromley-Hough
'''
'''
    Imported Functions
'''
from tabulate import tabulate
'''
    Global Variables
'''
repeat = 0

assign_names = []
assign_weightings = []
assign_max_marks = []
assign_actual_marks = []
assign_percent = []
assign_grade = []
overall_percent = 0

"""
Functions
""" 
    #Print Table Function
def print_table():
    try:    
        print(tabulate([[str(assign_names[0]), str(assign_weightings[0]), str(assign_actual_marks[0]), str(assign_max_marks[0]), str(assign_percent[0])], [str(assign_names[1]), str(assign_weightings[1]), str(assign_actual_marks[1]), str(assign_max_marks[1]), str(assign_percent[1])]], 
        headers=["Assignments Name:", "Weighting:", "Actual Mark:", "Max Marks:", "Assignment %:",]))
    except:
        print(tabulate([[str(assign_names[0]), str(assign_weightings[0]), str(assign_actual_marks[0]), str(assign_max_marks[0]), str(assign_percent[0])]], 
        headers=["Assignments Name:", "Weighting:", "Actual Mark:", "Max Marks:", "Assignment %:"]))

    #Percentage Calculator Function
def percent_calculator(overall_percent):
    try:
        overall_percent = (assign_percent[0] + assign_percent[1])
        return overall_percent
    except:
        overall_percent = (assign_percent)
        return overall_percent

#################################### Main Program ###################################
    #Name of Course
course_name = input("What is the name of your course?")

    #Assignment Information input - Loop
while repeat <= 1:
    names_input = assign_names.append(input("Assignment Name: "))
    weightings_input = assign_weightings.append(int(input("Assignment Weighting % : ")))
    max_marks_input = assign_max_marks.append(int(input("Assignment Max Marks: ")))
    actual_marks_input = assign_actual_marks.append(int(input("Assignment Actual Marks: ")))  

        #Ask if user wants to add a second assignment 
    while repeat <= 1:
        if repeat <= 0:
            user_input_stop_loop = input("Would you like to add a second assignment? (Y/N)")
        if user_input_stop_loop == "Y":
            repeat += 1
            break
        elif user_input_stop_loop == "N":
            repeat += 2
            break
        else:
            print("Invalid Option")
     
#print("*** DEBUG *** You pushed 'N'")

    #Percentage Calculator
try:        #This will get used if there are more than 1 item in array
    assign_percent = [(assign_weightings[0] * assign_actual_marks[0] / assign_max_marks[0]), (assign_weightings[1] * assign_actual_marks[1] / assign_max_marks[1])]
except:     #This will get used if there is only 1 item in array
    assign_percent = [(assign_weightings[0] * assign_actual_marks[0] / assign_max_marks[0])]
    
    #Prints Course name as title
print(course_name)

    #Prints Table
print_table()

    #Prints Total %
print("Total Percent: " + str(percent_calculator(overall_percent)))

    #Prints overall grade
print("Overall Grade:")

    #Calculates Grade
if percent_calculator(overall_percent) >= 90:
    print("A+")
elif percent_calculator(overall_percent) >= 85:
    print("A")
elif percent_calculator(overall_percent) >= 80:
    print("A-")
elif percent_calculator(overall_percent) >= 75:
    print("B+")
elif percent_calculator(overall_percent) >= 70:
    print("B")
elif percent_calculator(overall_percent) >= 65:
    print("B-")
elif percent_calculator(overall_percent) >= 60:
    print("C+")
elif percent_calculator(overall_percent) >= 55:
    print("C")    
elif percent_calculator(overall_percent) >= 50:
    print("C-")
elif percent_calculator(overall_percent) >= 45:
    print("D")
else:
    print("E")

"""
OLD CODE:

'''
    Title:          Course Score Calculator
    Description:    Assignment 2
    Author:         Quinn Bromley-Hough
'''
'''
    Imported Functions
'''
from tabulate import tabulate
'''
    Global Variables
'''
assign_names = ["a", "b", "c"]
assign_weightings = [30, 30, 40]
assign_max_marks = [50, 100, 50]
assign_actual_marks = [32, 93, 33]
assign_percent = [(assign_weightings[0] * assign_actual_marks[0] / assign_max_marks[0]), (assign_weightings[1] * assign_actual_marks[1] / assign_max_marks[1]), (assign_weightings[2] * assign_actual_marks[2] / assign_max_marks[2])]

'''
    Functions
'''
def ask_for_assign_name():
    userInput = input("Name of Assignment: ")
    assign_names.append(str(userInput))
    



#################################### Main Program ###################################



print("*** DEBUG ***")
print("Assignment Name:   " + "Weighting:     " + "Max Marks:     " + "Assignment %:")
print(assign_names[0] + ": " + str(assign_weightings[0]) + " " + str(assign_max_marks[0]) + " " + str(assign_percent[0]))
print(assign_names[1] + ": " + str(assign_weightings[1]) + " " + str(assign_max_marks[1]) + " " + str(assign_percent[1]))
print(assign_names[2] + ": " + str(assign_weightings[2]) + " " + str(assign_max_marks[2]) + " " + str(assign_percent[2]))
print("*** DEBUG ***")


ask_for_assign_name()

if assign_names[len] <= 4:
    print("*** DEBUG *** This works")

#This is good

print(tabulate([[str(assign_names[0]), str(assign_weightings[0]), str(assign_actual_marks[0]), str(assign_max_marks[0]), str(assign_percent[0])], [str(assign_names[1]), str(assign_weightings[1]), str(assign_actual_marks[1]), str(assign_max_marks[0]), str(assign_percent[1])], [str(assign_names[2]), str(assign_weightings[2]), str(assign_actual_marks[2]), str(assign_max_marks[0]), str(assign_percent[2])]], 
headers=["Assignments Name:", "Weighting:", "Actual Mark:", "Max Marks:", "Assignment %:"]))

print(assign_names[0])













################################## Old Code ###########################################

def write_assignment_names():
    length = len(assign_names)
    index = 0
    while index < length:
        print(str(assign_names[index]))
        index = index + 1

#Function to calculate the percentage of each Assignment:
def calc_percent():
    length = len(assign_weightings)
    index = 0
    while index < length:
        percent = (assign_weightings[index] * assign_actual_marks[index] / assign_max_marks[index])
        print("***DEBUG*** assign_name: " + str(write_assignment_names()) + " assign_percent: " + str(percent))
        print(write_assignment_names([index]) + str(percent))
        #assign_percent.append(19)
        #assign_percent.append(percent)
        #return(percent)
        index = index + 1
"""

