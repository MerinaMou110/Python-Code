// #include <iostream>
// #include <string>
// using namespace std;


// class Student {
// protected:
//     string name;

// public:
//     Student(string name) {

//         this->name=name;
//     }
//     virtual void displayDetails() { 
//         cout << "Name: " << name << endl; 
//     }
// };

// class UndergraduateStudent : public Student {
// private:
//     int year;

// public:
//     UndergraduateStudent(const string& name, int year) : Student(name){
//         this->year=year;
//     }

   
//     void displayDetails() override {
//         cout << "Undergraduate Student Details:" << endl;
//         Student::displayDetails(); 
//         cout << "Year: " << year << endl; 
//     }
// };


// class GraduateStudent : public Student {
// private:
//     string thesisTitle;

// public:
//     GraduateStudent(const string& name, const string& thesisTitle) : Student(name) {
//         this->thesisTitle=thesisTitle;
//     }

   
//     void displayDetails() override {
//         cout << "Graduate Student Details:" << endl;
//         Student::displayDetails(); 
//         cout << "Thesis Title: " << thesisTitle << endl;
//     }
// };

// int main() {

//     UndergraduateStudent undergrad("Mohua", 3);
//     GraduateStudent grad("Sadia", "Machine Learning in Healthcare");
//     cout << "Displaying Undergraduate Student Details:" << endl;
//     undergrad.displayDetails();
//     cout << endl;
//     cout << "Displaying Graduate Student Details:" << endl;
//     grad.displayDetails();

//     return 0;
// }


