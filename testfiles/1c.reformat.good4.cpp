#include <iostream>
using std::cout, std::cerr, std::endl;
#include <fstream>
using std::ifstream, std::ofstream;
#include <string>
using std::string;


int main(int argc, char* argv[]) {
    if (argc < 3) {
        cout << "This function needs two arguments, an input file name, and an output file name." << endl;
        return 1;
    }

    ifstream infile(argv[1]);
    if (!infile.is_open()) {
        cout << "Input file failed to open" << endl;
    }
    ofstream outfile(argv[2]);
    if (!outfile.is_open()) {
        cout << "Output file failed to open" << endl;
    }
    string first_name;
    string last_name;
    int score;
    double factor;

    while (infile >> first_name, infile >> last_name, infile >> score, infile >> factor) {
        outfile << last_name << ", " << first_name << ": " << score * factor << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}