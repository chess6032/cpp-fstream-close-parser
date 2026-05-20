#include <iostream>
using std::cout, std::cerr, std::endl;

#include <fstream>
using std::ifstream, std::ofstream;

#include <string>
using std::string, std::getline;

#include <sstream>
using std::istringstream;

int main(int argc, char *argv[]) {
    ifstream inFile(argv[1]);
    if (!inFile.is_open()) {
        cerr << "Unable to open file for reading: " << argv[1] << endl;
        return 1;
    }
    ofstream outFile(argv[2]);
    if (!outFile.is_open()) {
        cerr << "Unable to open file for writing: " << argv[2] << endl;
        return 2;
    }
    string line;
    string firstName;
    string lastName;
    int points;
    double factor;
    while (getline(inFile, line)) {
        istringstream is(line);
        is >> firstName >> lastName >> points >> factor;
        outFile << lastName << ", " << firstName << ": " << points * factor << endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}