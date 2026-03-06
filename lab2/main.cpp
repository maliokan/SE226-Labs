#include <iostream>
using namespace std;

int main() {
    cout << "Task 1!" << endl;
    cout << "Please enter a positive integer greater than 9: ";
    int num;
    cin >> num;

    cout << num;

    int step = 0;
    while (num > 9) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        step++;
        num = sum;
        cout << " -> " << num;
    }
    cout << "\nFinal value: " << num;
    cout << "\nTotal steps: " << step;

    cout << "\n\nTask 2!" << endl;

    cout << "Please enter a number between 10 and 100: "<<endl;
    int n;
    cin >> n;
    while (n < 10 || n > 100) {
        cout<<"Invalid input. Please enter a number between 10 and 100:"<< endl;
        cin >> n;
    }

    int f= 0;
    int b=0;
    int fb=0;

    for (int i = 0; i <= n; i++) {
        if (i % 7 == 0) continue;
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fb++;
        }else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            f++;
        }else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            b++;
        }else {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---"<<endl;
    cout << "Fizz count :" << f <<endl;
    cout << "Buzz count :" << b <<endl;
    cout << "FizzBuzz count :" << fb <<endl;



    cout << "\n\nTask 3!" << endl;
    cout << "Please enter a number between 3 and 9:"<<endl;
    int m;
    cin >> m;
    for (int i = 1; i < 2*m; i++) {
        int k = m - abs(m - i);
        for (int j = 1; j <= k; j++) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}