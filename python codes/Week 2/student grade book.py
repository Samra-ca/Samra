students = {}

# Load file
if "students.txt" in __import__("os").listdir():
    f = open("students.txt", "r")
    for line in f:
        data = line.strip().split(",")
        roll = data[0]
        name = data[1]
        marks = [int(data[2]), int(data[3]), int(data[4])]
        students[roll] = {"name": name, "marks": marks}
    f.close()

# Grade function
def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

while True:
    print("\n1. Add Student  2. Show All  3. Search  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        m1 = int(input("Math Marks: "))
        m2 = int(input("Science Marks: "))
        m3 = int(input("English Marks: "))
        students[roll] = {"name": name, "marks": [m1, m2, m3]}
        f = open("students.txt", "a")
        f.write(f"{roll},{name},{m1},{m2},{m3}\n")
        f.close()
        print("Student added!")

    elif choice == "2":
        print("\n🎓 Student Records:")
        for roll in students:
            name = students[roll]["name"]
            marks = students[roll]["marks"]
            avg = sum(marks) / 3
            grade = get_grade(avg)
            print(f"{roll} - {name} | Marks: {marks} | Avg: {avg:.1f} | Grade: {grade}")

    elif choice == "3":
        roll = input("Enter Roll No: ")
        if roll in students:
            name = students[roll]["name"]
            marks = students[roll]["marks"]
            avg = sum(marks) / 3
            grade = get_grade(avg)
            print(f"\nName: {name}\nMarks: {marks}\nAverage: {avg:.1f}\nGrade: {grade}")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")