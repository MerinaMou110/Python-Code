#include <iostream>
#include <string>

using namespace std;
class Person {
protected:
    string name;
    int age;

public:
    Person(string name, int age) {
        this->name = name;
        this->age = age;
    }

    string getPersonDetails() const {
        return "Name: " + name + ", Age: " + to_string(age);
    }
};

class Student : public Person {
private:
    string student_id;

public:
    Student(string name, int age, string student_id) : Person(name, age) {
        this->student_id = student_id;
    }
    string getStudentDetails() const {
        return getPersonDetails() + ", Student ID: " + student_id;
    }
};

class GraduateStudent : public Student {
private:
    string thesis_title;

public:
    GraduateStudent(string name, int age, string student_id, string thesis_title)
        : Student(name, age, student_id) {
        this->thesis_title = thesis_title;
    }
    string getGraduateStudentDetails() const {
        return getStudentDetails() + ", Thesis Title: " + thesis_title;
    }
};

int main() {
    GraduateStudent grad_student("Mou", 25, "G12345", "Machine Learning in Healthcare");
    cout << grad_student.getGraduateStudentDetails() << endl;

    return 0;
}
