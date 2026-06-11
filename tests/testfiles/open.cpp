#include <fstream>
using std::fstream, std::ifstream, std::ofstream;

#include <string>
using std::string;

int main() {
    string filepath;

    fstream file;
    file.open("literal");

    if (1) {
        file.open("literal");
    }

    if (1) file.open("literal");

    if (1) { file.open("literal"); }

    if (1) 
        file.open("literal");

file.open("literal");
 file.open("literal");
  file.open("literal");
   file.open("literal");
	file.open("literal");
		file.open("literal");

    file.open("literal");        

    return 0;
}