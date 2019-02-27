import sqlite3
import time
from Student import Student

conn = sqlite3.connect('Students')
c = conn.cursor()
class DbFunctions:

    def displayStudents(self):
        c.execute("SELECT * FROM Students")
        rows = c.fetchall()
        for row in rows:
            print(row)
            print('')
        time.sleep(1)

    def createStudent(self):
        inputCheck = True
        newFirst = raw_input("Please enter the Student's First Name: ")
        newLast = raw_input("Please enter the Student's Last Name: ")
        while (inputCheck):
            newGPA = input("Please enter the Student's GPA: ")
            try:
                val = float(newGPA)
                inputCheck = False
            except ValueError:
                print("Enter a proper GPA")
        newMajor = raw_input("Please enter the Student's Major: ")
        newFac = raw_input("Please enter the Student's Faculty Advisor: ")
        tempStudent = Student(newFirst, newLast, newGPA, newMajor, newFac)
        c.execute("INSERT INTO Students (FirstName,LastName,GPA,Major,FacultyAdvisor) VALUES (?, ?, ?, ?, ?)",
                  (tempStudent.getStudentTuple()))
        conn.commit()
        print("Student Added!")
        time.sleep(1)

    def updateStudent(self):
        print("This is the current table: ")
        DbFunctions.displayStudents(self)
        sidEdit = int(input("Enter the desired StudentID you want to edit: "))
        if(DbFunctions.checkIfStudentExists(self, sidEdit)== True):
            newMajor = raw_input("Please input the updated Major for this Student: ")
            newAdvisor = raw_input("Please input the updated Advisor for this Student: ")
            c.execute("UPDATE Students SET Major = ? WHERE StudentId = ?", (newMajor, sidEdit,))
            c.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentId = ?", (newAdvisor, sidEdit,))
            conn.commit()
        else:
            print("Invalid student ID. ")
            time.sleep(1)

    def checkIfStudentExists(self, SID):
        c.execute("SELECT StudentId FROM Students WHERE StudentId = ?", (SID,))
        idArray = c.fetchall()
        if (idArray == []):
            return False;
        return True;

    def deleteStudent(self):
        print("This is the current table: ")
        DbFunctions.displayStudents(self)
        sidDelete = int(input("Enter the desired StudentID you want to Remove: "))
        if (DbFunctions.checkIfStudentExists(self, sidDelete) == True):
            c.execute("DELETE FROM Students WHERE StudentId = ?", (sidDelete,))
            conn.commit()
            print("Student Deleted.")
            time.sleep(1)
        else:
            print("Invalid student ID. ")
            time.sleep(1)


    def searchStudents(self):
        print("Enter what you would like to display the students by: ")
        inputCheck = True
        while (inputCheck):
            try:
                sidDisplay = int(input("1) By Major  2) By GPA  3) By Advisor: "))
                inputCheck = False
            except NameError:
                print("Enter a proper number (1, 2, or 3)")
                print('')
                time.sleep(0.5)
        if (sidDisplay == 1):
            majorSelection = raw_input("What major would you like to sort by: ")
            c.execute("SELECT * FROM Students WHERE Major = ?", (majorSelection,))
            rows = c.fetchall()
            if (rows == []):
                print("No students Found")
                time.sleep(0.5)
            else:
                for row in rows:
                    print(row)
                time.sleep(0.5)
        elif (sidDisplay == 2):
            inputCheck = True
            while(inputCheck):
                try:
                    GPASelection = int(input("Do you want to sort by 1) an upper bound or 2) a lower bound? "))
                    inputCheck = False
                except NameError:
                    print("Enter a proper number (1 or 2)")
                    print('')
                    time.sleep(0.5)
            if (GPASelection == 1):
                inputCheck = True
                while (inputCheck):
                    try:
                        upperBound = float(input("What is your upper bound? "))
                        inputCheck = False
                    except NameError:
                        print("Enter a proper GPA")
                        print('')
                        time.sleep(0.5)
                c.execute("SELECT * FROM Students WHERE GPA < ? ", (upperBound,))
                rows = c.fetchall()
                if (rows == []):
                    print("No Students found")
                    time.sleep(0.5)
                else:
                    for row in rows:
                        print(row)
                    time.sleep(0.5)
            elif (GPASelection == 2):
                inputCheck = True
                while (inputCheck):
                    try:
                        lowerBound = float(input("What is your lower bound? "))
                        inputCheck = False
                    except NameError:
                        print("Enter a proper GPA")
                        print('')
                        time.sleep(0.5)
                c.execute("SELECT * FROM Students WHERE GPA > ? ", (lowerBound,))
                rows = c.fetchall()
                if(rows==[]):
                    print("No Students found")
                    time.sleep(0.5)
                else:
                    for row in rows:
                        print(row)
                    time.sleep(0.5)
        elif (sidDisplay == 3):
            advisorSelection = raw_input("What is the advisor you want to sort by: ")
            c.execute("SELECT * FROM Students WHERE FacultyAdvisor = ? ", (advisorSelection,))
            rows = c.fetchall()
            if (rows == []):
                print("No Students found")
                time.sleep(0.5)
            else:
                for row in rows:
                    print(row)
                time.sleep(0.5)
        else:
            print("Invalid number inputted.")
            time.sleep(1)