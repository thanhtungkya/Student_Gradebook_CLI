from gradebook_manager import GradebookManager
from user_manager import UserManager

gb = GradebookManager()
user_manager = UserManager()

# -----------------------------
# First-Time User Registration
# -----------------------------
username = user_manager.get_username()

if username is None:
    print("Welcome! It looks like this is your first time using the Gradebook App.")
    name = input("Please enter your name: ").strip()

    # Ensure non-empty name
    while not name:
        print("Name cannot be empty.")
        name = input("Please enter your name: ").strip()

    user_manager.save_user(name)
    username = name
    print(f"\nHello, {username}! Your profile has been created.\n")
else:
    print(f"Welcome back, {username}! 👋\n")


# -----------------------------
# CLI Menu
# -----------------------------
def menu():
    print(f"""
===== Student Gradebook CLI =====
User: {username}

1. Add course
2. Update course
3. Delete course
4. View gradebook
5. Calculate GPA
6. GPA by semester
7. Exit
""")
    return input("Choose: ")


# -----------------------------
# Main Program Loop
# -----------------------------
while True:
    option = menu()

    if option == "1":
        code = input("Course code: ")
        name = input("Course name: ")
        credits = int(input("Credits: "))
        semester = str(input("Semester: "))
        score = float(input("Score (0-10): "))

        success, message = gb.add_course(code, name, credits, semester, score)
        print(message)

    elif option == "2":
        code = input("Course code to update: ")
        print("Leave a field blank if you don't want to change it.")

        name = input("New name: ") or None
        credits = input("New credits: ")
        semester = input("New semester: ")
        score = input("New score: ")

        updates = {
            "name": name,
            "credits": int(credits) if credits else None,
            "semester": str(semester) if semester else None,
            "score": float(score) if score else None
        }

        success, message = gb.update_course(code, **updates)
        print(message)

    elif option == "3":
        code = input("Course code to delete: ")
        success, message = gb.delete_course(code)
        print(message)

    elif option == "4":
        print(gb.view_courses())

    elif option == "5":
        print("Overall GPA:", gb.calculate_gpa())

    elif option == "6":
        print("GPA by semester:", gb.gpa_by_semester())

    elif option == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.\n")
