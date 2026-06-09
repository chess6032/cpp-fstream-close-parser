#include <fstream>
using std::fstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::fstream.
*/

int main() {
    string filepath = "hello.txt";

    fstream uF1;
    std::fstream uF2;
    fstream uF3{};
    std::fstream uF4{};

    fstream oF1("hello.txt");
    fstream oF2(filepath);
    std::fstream oF3("hello.txt");
    std::fstream oF4(filepath);

    fstream oF5{"hello.txt"};
    fstream oF6{filepath};
    std::fstream oF7{"hello.txt"};
    std::fstream oF8{filepath};
}