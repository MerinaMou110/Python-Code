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
    string getDetails() const {
        return "Name: " + name + ", Age: " + to_string(age);
    }
};


class Student : public Person {
private:
    string student_id;

public:
    Student(string name, int age, string student_id)
        : Person(name, age) {
            this->student_id=student_id;
        }

   
    string getStudentDetails() const {
        string person_details = getDetails();
        return person_details + ", Student ID: " + student_id;
    }
};

class Teacher : public Person {
private:
    string employee_id;

public:
    Teacher(string name, int age, string employee_id)
        : Person(name, age) {
            this->employee_id=employee_id;
        }


    string getTeacherDetails() const {
        string person_details = getDetails();
        return person_details + ", Employee ID: " + employee_id;
    }
};

int main() {
  
    Student student("Nitu", 20, "S19");
    Teacher teacher("sadia", 35, "T89");

    cout << student.getStudentDetails() << endl;
    cout << teacher.getTeacherDetails() << endl;

    return 0;
}
