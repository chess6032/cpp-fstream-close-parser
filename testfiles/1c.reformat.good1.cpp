#include <iostream>
using std::endl;

#include <fstream>
using std::ifstream, std::ofstream;

#include <string>
using std::string, std::getline;

#include <sstream>

int main(int argc, char **argv) {
    ifstream infile(argv[1]);
    ofstream outfile(argv[2]);
    string line;
    while (getline(infile, line)) {
        string lastname;
        string firstname;
        int points;
        double factor;
        std::istringstream line_stream(line);
        line_stream >> firstname >> lastname >> points >> factor;
        double recalculated = points * factor;
        outfile << lastname << ", " << firstname << ": " << recalculated << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}