class Student:

    def __init__(self, first_name, last_name, major, gpa, facAdv):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.facAdv = facAdv

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getMajor(self):
        return self.major

    def getGPA(self):
        return self.gpa

    def getFacAdv(self):
        return self.facAdv

    def getStudentTuple(self):
        return (self.getFirstName(), self.getLastName(), self.getMajor(), self.getGPA(), self.getFacAdv())
