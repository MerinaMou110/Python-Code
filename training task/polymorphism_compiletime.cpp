#include <iostream>
using namespace std;

int mul(int a, int b) 
{ 
    return a + b;
}

float mul(float a, float b)
 { 
    return a + b;
}

int add(int b,int c){
    return b+c;
}

int main() { 
    int x = add(5, 10);
    cout<<x;
}