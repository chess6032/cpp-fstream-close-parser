#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    ifstream inputFile(argv[1]);
    ofstream outputFile(argv[2]);

    string firstName;
    string lastName;
    int points;
    double factor;

    while (inputFile >> firstName >> lastName >> points >> factor) {
        double recalculatedPoints = points * factor;
        outputFile << lastName << ", " << firstName << ": " << recalculatedPoints << endl;

    }
    return 0;
}