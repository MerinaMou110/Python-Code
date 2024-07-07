def get_student_details(self):
        person_details = self.get_person_details()
        academic_details = self.get_academic_details()
        return f"{person_details}, {academic_details}, Student ID: {self.student_id}"