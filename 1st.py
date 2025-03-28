# Student grade calculator
def calculate_grade(avg):
    '''The function calculate the grade of students marks'''
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "F"
def main():
    '''Main function to get student details and calculate results.'''
    name=int(input("Enter the number of students:"))
    subject=int(input("Enter the number of subjects:"))
    students=[] # list to store student data
    for i in range(name):
        num_std=input("\n Enter the student name: ")
        marks=[]
        for i in range(subject):
            mark=float(input(f"Enter marks for subject {i+1}:"))
            marks.append(mark)
            total = sum(marks)
        avg = total / subject
        grade = calculate_grade(avg)

        students.append((name, total, avg, grade))  # Store as a tuple

    print("\n--- Student Results ---")
    for student in students:
        name, total, avg, grade = student
        print(f"Student: {name}, Total: {total}, Average: {avg:.2f}, Grade: {grade}")

if __name__ == "__main__":
    main()
        
