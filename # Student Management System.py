# Student Management System

students = []

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("✅ Student added successfully!")

    # View all students
    elif choice == "2":
        if len(students) == 0:
            print("⚠️ No students found!")
        else:
            print("\n--- Student List ---")
            for s in students:
                print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

    # Search student
    elif choice == "3":
        search_roll = input("Enter roll number to search: ")
        found = False

        for s in students:
            if s["roll"] == search_roll:
                print("\n🎯 Student Found!")
                print(f"Name: {s['name']}")
                print(f"Roll: {s['roll']}")
                print(f"Marks: {s['marks']}")
                found = True
                break

        if not found:
            print("❌ Student not found!")

    # Exit
    elif choice == "4":
        print("👋 Exiting program... Bye!")
        break

    else:
        print("❌ Invalid choice! Try again.")