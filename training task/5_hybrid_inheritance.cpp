#include <iostream>
#include <string>

using namespace std;
class Person {
private:
    string name;
    int age;

public:
    Person(string name, int age) {
        this->name = name;
        this->age = age;
    }
    string getDetails() const {
        return "Name: " +name + ", Age: " + to_string(age);
    }
};


class Academic {
protected:
    string institution;
    string major;

public:
    Academic(string institution, string major) {
        this->institution = institution;
        this->major = major;
    }

    
    string getAcademicDetails() const {
        return "Institution: " + institution + ", Major: " + major;
    }
};

class Student : public Person, public Academic {
private:
    string student_id;

public:
    Student(string name, int age, string institution, string major, string student_id)
        : Person(name, age), Academic(institution, major) {
        this->student_id = student_id;
    }

    // Method to get student details
    string getStudentDetails() const {
        string person_details = this->getDetails();
        string academic_details = this->getAcademicDetails();
        return person_details + ", " + academic_details + ", Student ID: " + student_id;
    }
};

class GraduateStudent : public Student {
private:
    string thesis_title;

public:
    GraduateStudent(string name, int age, string institution, string major, string student_id, string thesis_title)
        : Student(name, age, institution, major, student_id) {
        this->thesis_title = thesis_title;
    }

    string getGraduateStudentDetails() const {
        string student_details = getStudentDetails();
        return student_details + ", Thesis Title: " + thesis_title;
    }
};

int main() {
    GraduateStudent grad_student("Mou", 23, "NWU", "Computer Science", "G12345", "Machine Learning in Healthcare");

    cout << grad_student.getGraduateStudentDetails() << endl;

    return 0;
}
