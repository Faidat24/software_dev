"""
Faidat Fahm
April 30, Lab 11, class in Python (extra points)
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = {} 
    
    def add_grade(self, subject, grade):
        self.grade[subject] = grade
    
    def get_average_grade(self):
        if not self.grade:
            return 0.0
        return sum(self.grade.values()) / len(self.grade)

# Example usage
if __name__ == "__main__":
    # Create a student instance
    student1 = Student("John Doe", 18)
    
    # Add grades for different subjects
    student1.add_grade("Math", 85.5)
    student1.add_grade("Science", 92.0)
    student1.add_grade("History", 78.5)
    
    # Print student information
    print(f"Student Name: {student1.name}")
    print(f"Age: {student1.age}")
    print("Grades:")
    for subject, grade in student1.grade.items():
        print(f"  {subject}: {grade}")
    print(f"Average Grade: {student1.get_average_grade():.2f}")
    
    # Create another student instance
    student2 = Student("Jane Smith", 17)
    student2.add_grade("Math", 90.0)
    student2.add_grade("Science", 88.5)
    
    print("\nSecond Student:")
    print(f"Student Name: {student2.name}")
    print(f"Age: {student2.age}")
    print("Grades:")
    for subject, grade in student2.grade.items():
        print(f"  {subject}: {grade}")
    print(f"Average Grade: {student2.get_average_grade():.2f}")
