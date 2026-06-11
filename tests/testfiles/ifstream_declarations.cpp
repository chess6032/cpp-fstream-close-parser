#include <fstream>
using std::ifstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::ifstream.
*/

int main() {
    string filepath = "hello.txt";

    ifstream uF1;
    std::ifstream uF2;
    ifstream uF3{};
    std::ifstream uF4{};

    ifstream oF1("hello.txt");
    ifstream oF2(filepath);
    std::ifstream oF3("hello.txt");
    std::ifstream oF4(filepath);

    ifstream oF5{"hello.txt"};
    ifstream oF6{filepath};
    std::ifstream oF7{"hello.txt"};
    std::ifstream oF8{filepath};

    std::ifstream fine1; // std::ifstream line_commented_1;
    // std::ifstream line_commented_2;
    std::ifstream fine2; /* std::ifstream comment1; */
    /* std::ifstream comment2; */
}