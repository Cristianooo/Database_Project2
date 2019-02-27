import sqlite3

from Student import Student
from DbFunctions import DbFunctions

conn = sqlite3.connect('Students')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Students(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(25) NOT NULL,LastName VARCHAR(25) NOT NULL,GPA NUMERIC NOT NULL ,Major VARCHAR(10) NOT NULL,FacultyAdvisor VARCHAR(25) NOT NULL)")
class Driver:




    def run(self):
        myFunctions = DbFunctions()
        keepLoop = True
        while(keepLoop):

            print(
                '''
                1) Display ALL Students
                2) Create/Add a Student
                3) Update Student Info
                4) Delete Student by SID
                5) Search for Student (Major, GPA, Advisor)
                6+) Exit
                '''
            )

            print("What would you like to do?")
            userChoice = int(input("# "))

            if(userChoice == 1):
                myFunctions.displayStudents()

            elif(userChoice == 2):
                myFunctions.createStudent()


            elif(userChoice == 3):
                myFunctions.updateStudent()

            elif(userChoice == 4):
                myFunctions.deleteStudent()
            elif (userChoice == 5):
                myFunctions.searchStudents()
            else:
                keepLoop = False
                c.close()



