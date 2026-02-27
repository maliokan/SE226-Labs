#include <iostream>
using namespace std;

int main() {
    cout<<"Enter time by seconds: ";
    int input;
    cin>>input;
    int hours = input/3600;
    int minutes = (input - hours*3600)/60;
    int seconds = (input - hours*3600 - minutes*60);
    cout<<input<<"seconds is " <<hours <<" hours, " << minutes<< " minutes, and " << seconds<< " seconds."<<endl;
}