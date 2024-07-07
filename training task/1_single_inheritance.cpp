#include <iostream>
#include <string>

using namespace std;
class Student {
private:
    string name;
    string student_id;

protected:
    string getName() const {
        return name;
    }

    string getStudentId() const {
        return student_id;
    }

public:
    
    Student(string name, string student_id) {
        this->name = name;
        this->student_id = student_id;
    }

    string getDetails() const {
        return "Name: " + name + ", Student ID: " + student_id;
    }
};


class GraduateStudent : public Student {
private:
    string thesis_title;

public:
    GraduateStudent(string name, string student_id, string thesis_title)
        : Student(name, student_id) {
        this->thesis_title = thesis_title;
    }

    string getDetails() const {
        string base_details = Student::getDetails(); 
        return base_details + ", Thesis Title: " + thesis_title;
    }
};

int main() {

    GraduateStudent grad_student("Mou", "43", "Object oriented program");
    cout << grad_student.getDetails() << endl;

    return 0;
}
