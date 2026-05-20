#include <fstream>
using std::ifstream, std::ofstream;

#include <string>
using std::string;

#include <iostream>
using std::cout, std::endl, std::cerr;

int main(int argc, char* argv[]) {
    ifstream input_file(argv[1]);
    if (!input_file.is_open()) {
        cerr << "Unable to open file for reading: " << argv[1] << endl;
        return 1;
    }

    ofstream output_file(argv[2]);
    if (!output_file.is_open()) {
        cerr << "Unable to open file for writing: " << argv[2] << endl;
        return 2;
    }

    string first_name, last_name;
    double points, factor;
    while (input_file >> first_name >> last_name >> points >> factor)
        output_file << last_name << ", " <<first_name << ": " << points * factor << endl;

    input_file.close();
    output_file.close();
    return 0;
}