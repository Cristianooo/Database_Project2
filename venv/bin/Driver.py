import sqlite3

from Student import Student
from DbFunctions import DbFunctions
conn = sqlite3.connect('Students')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Students(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(25) NOT NULL,LastName VARCHAR(25) NOT NULL,GPA NUMERIC NOT NULL ,Major VARCHAR(10) NOT NULL,FacultyAdvisor VARCHAR(25) NOT NULL)")

myFunctions = DbFunctions()
keepLoop = True
while(keepLoop):

    print(
        '''
        1) Display ALL Students
        2) Create/Add a Student
        3) Update Student Info
        4) Delete Student by SID
        5) Search for Student (GPA, Major, Advisor)
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
        print("Enter what you would like to display the students by: ")
        sidDisplay = int(input("1) By Major  2) By GPA  3) By Advisor: "))
        if (sidDisplay == 1):
            majorSelection = raw_input("What major would you like to sort by: ")
            c.execute("SELECT * FROM Students WHERE Major = ?", (majorSelection,))
            rows = c.fetchall()
            for row in rows:
                print(row)
        elif (sidDisplay == 2):
            GPASelection = int(input("Do you want to sort by 1) an upper bound or 2) a lower bound? "))
            if (GPASelection == 1):
                upperBound = float(input("What is your upper bound? "))
                c.execute("SELECT * FROM Students WHERE GPA < ? ", (upperBound,))
                rows = c.fetchall()
                for row in rows:
                    print(row)
            elif(GPASelection == 2):
                lowerBound = float(input("What is your lower bound? "))
                c.execute("SELECT * FROM Students WHERE GPA > ? ", (lowerBound,))
                rows = c.fetchall()
                for row in rows:
                    print(row)
        elif(sidDisplay == 3):
            advisorSelection = raw_input("What is the advisor you want to sort by: ")
            c.execute("SELECT * FROM Students WHERE FacultyAdvisor = ? ", (advisorSelection,))
            rows = c.fetchall()
            for row in rows:
                print(row)
    else:
        keepLoop = False
        c.close()



