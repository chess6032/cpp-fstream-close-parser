#include <iostream>
#include <fstream>
#include <string>

using std::string, std::cout, std::cin, std::endl, std::getline, std::cerr, std::ifstream;

int main(int argc, char* argv[]) {
    ifstream inFile(argv[1]);
    std::ofstream outFile(argv[2]);

    string first, last;
    int points;
    double factor;

    while (inFile >> first >> last >> points >> factor) {
        double score = points * factor;
        outFile << last << ", " << first << ": " << score << endl;

    }
    inFile.close();
    outFile.close();

    return 0;
}

