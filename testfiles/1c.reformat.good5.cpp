#include <string>
using std::string, std::stoi;
#include <iostream>
using std::cout, std::cerr, std::cin, std::endl, std::getline;
#include <fstream>
using std::ifstream, std::ofstream;
#include <sstream>
using std::istringstream, std::ostringstream;

int main(int argc, char *argv[]) {
    ifstream infile(argv[1]);
    if (!infile.is_open()) {
        cerr << "Unable to open file: " << argv[1] << endl;
    }
    ofstream outfile(argv[2]);
    if (!outfile.is_open()) {
        cerr <<"Unable to open file: " << argv[2] << endl;
    }
    string name;
    string last;
    int points;
    double factor;
    string line;
    while (getline(infile, line)) {
        istringstream ss(line);
        ss >> name >> last >> points >> factor;
        outfile << last << ", " << name << ": " << factor * points << endl;

    }




    infile.close();
    outfile.close();
}