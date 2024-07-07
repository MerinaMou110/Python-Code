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

    string getStudentDetails() const {
        string person_details =getPersonDetails();
        string academic_details = getAcademicDetails();
        return person_details + ", " + academic_details + ", Student ID: " + student_id;
    }
};

int main() {
    Student student("Mou", 20, "NWU", "Computer Science", "S12345");
    cout << student.getStudentDetails() << endl;

    return 0;
}
