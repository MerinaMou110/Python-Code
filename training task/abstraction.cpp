#include <iostream>
using namespace std;

// Abstract base class
class Student {
public:
    virtual void displayDetails() = 0; // do nothing function-->Pure virtual function
};

class UndergraduateStudent : public Student {
private:
    string name;
    int year;

public:
    UndergraduateStudent( string name, int year) : name(name) {
        this->year=year;
    }

    void displayDetails() override {
        cout << "Undergraduate Student:" << endl;
        cout << "Name: " << name << endl;
        cout << "Year: " << year << endl;
    }
};

class GraduateStudent : public Student {
private:
    string name;
    string thesisTitle;

public:
    GraduateStudent(const string& name, const string& thesisTitle) : name(name), thesisTitle(thesisTitle) {}

    void displayDetails() override {
        cout << "Graduate Student:" << endl;
        cout << "Name: " << name << endl;
        cout << "Thesis Title: " << thesisTitle << endl;
    }
};

int main() {
    UndergraduateStudent undergrad("Alice", 3);
    GraduateStudent grad("Bob", "Machine Learning in Healthcare");
    grad.displayDetails();

    return 0;
}
