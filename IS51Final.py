"""
The program is attempting to show student grades on a final exam.
The grades of 24 students are from a text file called "final.txt."
It will show the number of grades, the average grade, and the percentage of hrades that are above the average grade
Three different functions will be used to obtain three different grades.
"""

"""
main()
to open file and retrieve data, we use infile = open(file, 'r')
for line in infile = To obtain the lines of the file 
[line.rstrip() for line in infile] = Creates a list of strings where each item of the list of the file minus its newline character
grades = [line.rstrip()]

grades[i] = int(grades[i]), to change the list into integers
to get average grade = sum(grades) / len(grades)

to retrieve grades that are above the average, if the grade is above average then increase counter by 1 

to get percentage of grages above average, take number of grades that are above average divided by the total grades in the list 

Then
print total number of grades
print average grade
print percentage of grades that are above the average 
"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0 
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print ("Percentafe of grade above average: {0:.2f}%".format(100 * num / len(grades)))