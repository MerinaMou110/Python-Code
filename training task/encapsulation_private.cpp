#include <iostream>
#include <string>

using namespace std;

class StudentPrivate {
private:
    string name;
    int age;

public:
    StudentPrivate(string name, int age){
         this->name = name;
    this->age = age;
    }   
    string getName() ;
    void setName(string name);
    int getAge();
    void setAge(int age);
    void displayDetails() ;
};



string StudentPrivate::getName(){
    return name;
}


void StudentPrivate::setName(string name) {
    this->name = name;
}


int StudentPrivate::getAge(){
    return age;
}


void StudentPrivate::setAge(int age) {
    this->age = age;
}


void StudentPrivate::displayDetails() {
    cout << "Name: " << name << ", Age: " << age << endl;
}

int main() {
    StudentPrivate student("Sadia", 20);

    cout << "Original Details:" << endl;
    student.displayDetails();

    student.setName("Mohua");
    student.setAge(22);

    cout << "Modified Details:" << endl;
    student.displayDetails();

    return 0;
}
