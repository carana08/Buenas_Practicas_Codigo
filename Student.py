class student:

    def __init__(s, id, name):
        if not id or not name:
            raise ValueError("Student ID and name cannot be empty.")
        s.id = id
        s.name = name
        s.grades = []
        s.isPassed = "NO"
        s.honor = False

    def addGrades(self, g):
        if isinstance(g, (int, float)) and 0 <= g <= 100:
            self.grades.append(g)
        else:
            print("Grade must be a float value.")

    def calcAverage(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def determineLetterGrade(self):
        avg = self.calcAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def checkHonor(self):
        self.honor = self.calcAverage() >= 90

    def deleteGrade(self, index):
        try:
            del self.grades[index]
        except IndexError:
            print("Index out of range. Unable to delete grade.")

    def removeGradeByValue(self, grade):
        try:
            self.grades.remove(grade)
        except ValueError:
            print(f"Grade {grade} not found in the list.")

    def removeGradeByIndex(self, index):
        try:
            del self.grades[index]
        except IndexError:
            print("Index out of range. Unable to delete grade.")

    def determinePassFail(self):
        self.is_passed = "YES" if self.calcAverage() >= 60 else "NO"

    def report(self):
        avg = self.calcAverage()
        letter_grade = self.determineLetterGrade()
        self.determinePassFail()
        self.checkHonor()
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Pass/Fail: {self.is_passed}")
        print(f"Honor Roll: {'YES' if self.honor else 'NO'}")


def startrun():
    a = student("x", "Jose")
    a.addGrades(100)
    a.addGrades(50)
    a.calcAverage()
    a.checkHonor()
    a.deleteGrade(1)
    a.report()


startrun()
