#include <fstream>
using std::ifstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::ifstream.
*/

int main(int argc, char *argv[]) {
    string filepath = "hello.txt";

    ifstream uF1;
    std::ifstream uF2;
    ifstream uF3{};
    std::ifstream uF4{};

    ifstream oF1("hello.txt");
    ifstream oF2(filepath);
    std::ifstream oF3("hello.txt");
    std::ifstream oF4(filepath);

    ifstream oF5{"hello.txt"};
    ifstream oF6{filepath};
    std::ifstream oF7{"hello.txt"};
    std::ifstream oF8{filepath};

    std::ifstream u_cmt_test1; // std::ifstream line_commented_1;
    // std::ifstream line_commented_2;
    std::ifstream u_cmt_test2; /* std::ifstream comment1; */
    /* std::ifstream comment2; */

    // different indentations
std::ifstream u_indent0;
 std::ifstream u_indent1;
  std::ifstream u_indent2;
   std::ifstream u_indent3;
    std::ifstream u_indent4;
                                std::ifstream u_indent_many;
	std::ifstream u_indent_t1;
				std::ifstream u_indent_t4;

    { std::ifstream u_inbrackets; }
    if (argc > 1) {
        std::ifstream u_ifstatement1;
    }
    if (argc > 2) { std::ifstream u_ifstatement2; }
    if (argc > 3) std::ifstream u_ifstatement3;

    return 0;
}