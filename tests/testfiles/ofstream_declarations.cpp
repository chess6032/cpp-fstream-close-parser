#include <fstream>
using std::ofstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::ofstream.
*/

int main() {
    string filepath = "hello.txt";

    ofstream uF1;
    std::ofstream uF2;
    ofstream uF3{};
    std::ofstream uF4{};

    ofstream oF1("hello.txt");
    ofstream oF2(filepath);
    std::ofstream oF3("hello.txt");
    std::ofstream oF4(filepath);

    ofstream oF5{"hello.txt"};
    ofstream oF6{filepath};
    std::ofstream oF7{"hello.txt"};
    std::ofstream oF8{filepath};

    std::ofstream fine1; // std::ofstream line_commented_1;
    // std::ofstream line_commented_2;
    std::ofstream fine2; /* std::ofstream comment1; */
    /* std::ofstream comment2; */
}