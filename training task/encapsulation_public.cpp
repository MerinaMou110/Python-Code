#include <iostream>
#include <string>

using namespace std;

class StudentPublic {
public:
    string name;
    int age;
    StudentPublic(string name, int age) {
        this->name = name;
        this->age = age;
    }
   void displayDetails();
    
    
};
void StudentPublic:: displayDetails(){
        cout << "Name: " << name << ", Age: " << age << endl;
    }

int main() {
    StudentPublic student("Mohua", 20);
    cout << "Original Details:" << endl;
    student.displayDetails();

    student.name = "Nasima";
    student.age = 22;

    cout << "Modified Details:" << endl;
    student.displayDetails();

    return 0;
}
