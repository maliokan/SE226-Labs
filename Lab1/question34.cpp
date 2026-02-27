#include <cmath>
#include <iostream>

using namespace std;

int main() {
    double x1, x2, y1, y2;
    cout<<"Enter the value of x1:"<<endl;
    cin>>x1;
    cout<<"Enter the value of y1:"<<endl;
    cin>>y1;
    cout<<"Enter the value of x2:"<<endl;
    cin>>x2;
    cout<<"Enter the value of y2:"<<endl;
    cin>>y2;
    double dist = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
    cout<<"The distance between two points is "<<dist<<endl;

    cout<<"*******"<<endl<<
          " *****"<<endl<<
          "  ***"<<endl<<
          "   *"<<endl;
}