#include <iostream>
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;


#include <sstream>
using std::istringstream;

#include <string>
using std::string;


int main(int argc, char *argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    string line;

    while (getline(fin, line)) {
        istringstream linestream(line);
        string last_name;
        string first_name;
        int points;
        double factor;

        linestream >> first_name >> last_name >> points >> factor;

        fout << last_name << ", " << first_name << ": " << factor * points << endl;
    }
    return 0;
}