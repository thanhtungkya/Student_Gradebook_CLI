import json
import os


class GradebookManager:
    def __init__(self, filename="gradebook.json"):
        self.filename = filename
        self.gradebook = []
        self.load_data()

    # ----------------------------
    # Persistent Storage
    # ----------------------------
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    self.gradebook = json.load(f)
                except json.JSONDecodeError:
                    self.gradebook = []
        else:
            self.gradebook = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.gradebook, f, indent=4)

    # ----------------------------
    # CRUD Operations
    # ----------------------------
    def add_course(self, code, name, credits, semester, score):
        # Duplicate check
        for c in self.gradebook:
            if c["code"] == code:
                return False, "Course code already exists."

        course = {
            "code": code,
            "name": name,
            "credits": credits,
            "semester": semester,
            "score": score
        }
        self.gradebook.append(course)
        self.save_data()
        return True, "Course added successfully."

    def update_course(self, code, **updates):
        for course in self.gradebook:
            if course["code"] == code:
                for key, value in updates.items():
                    if value is not None:
                        course[key] = value
                self.save_data()
                return True, "Course updated."
        return False, "Course not found."

    def delete_course(self, code):
        for course in self.gradebook:
            if course["code"] == code:
                self.gradebook.remove(course)
                self.save_data()
                return True, "Course deleted."
        return False, "Course not found."

    # ----------------------------
    # View Function
    # ----------------------------
    def view_courses(self):
        if not self.gradebook:
            return "No courses found."

        output = "\n--- Gradebook ---\n"
        for c in self.gradebook:
            output += (f"Code: {c['code']} | Name: {c['name']} | Credits: {c['credits']} | "
                       f"Semester: {c['semester']} | Score: {c['score']}\n")
        return output

    # ----------------------------
    # GPA Calculation
    # ----------------------------
    def calculate_gpa(self):
        if not self.gradebook:
            return 0

        total_weight = 0
        total_credits = 0

        for c in self.gradebook:
            total_weight += c["score"] * c["credits"]
            total_credits += c["credits"]

        return round(total_weight / total_credits, 2) if total_credits else 0

    def gpa_by_semester(self):
        semesters = {}
        for c in self.gradebook:
            sem = c["semester"]
            if sem not in semesters:
                semesters[sem] = {"weight": 0, "credits": 0}
            semesters[sem]["weight"] += c["score"] * c["credits"]
            semesters[sem]["credits"] += c["credits"]

        result = {}
        for sem, data in semesters.items():
            result[sem] = round(data["weight"] / data["credits"], 2)

        return result