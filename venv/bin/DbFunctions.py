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
        time.sleep(2)

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
    def updateStudent(self):
        sidEdit = int(input("Enter the desired StudentID you want to Edit: "))
        if(DbFunctions.checkIfStudentExists(self, sidEdit)== True):
            newMajor = raw_input("Please input the updated Major for this Student: ")
            newAdvisor = raw_input("Please input the updated Advisor for this Student: ")
            c.execute("UPDATE Students SET Major = ? WHERE StudentId = ?", (newMajor, sidEdit,))
            c.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentId = ?", (newAdvisor, sidEdit,))
            conn.commit()
        else:
            print("Invalid student ID. ")
            time.sleep(2)

    def checkIfStudentExists(self, SID):
        c.execute("SELECT StudentId FROM Students WHERE StudentId = ?", (SID,))
        idArray = c.fetchall()
        if (idArray == []):
            return False;
        return True;

    def deleteStudent(self):
        sidDelete = int(input("Enter the desired StudentID you want to Remove: "))
        if (DbFunctions.checkIfStudentExists(self, sidDelete) == True):
            c.execute("DELETE FROM Students WHERE StudentId = ?", (sidDelete,))
            conn.commit()
        else:
            print("Invalid student ID. ")
            time.sleep(2)