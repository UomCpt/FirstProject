#include <iostream>

class Calculator {
public:
    // Function to add two numbers
    int add(int num1, int num2) {
        if (num2 == 0)
        {
            return -2;
        }
        return num1 / num2;
    }
};

int main() {
    Calculator calc;  // Create an object of Calculator
    int num1, num2;

    // User input
    std::cin >> num1 >> num2;

    // Call the function and display the result
    int result = calc.add(num1, num2);
    std::cout << result; 

    return 0;
}