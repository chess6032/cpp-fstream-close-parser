#include <fstream>
using std::fstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::fstream.
*/

int main(int argc, char *argv[]) {
    string filepath = "hello.txt";

    fstream uF1;
    std::fstream uF2;
    fstream uF3{};
    std::fstream uF4{};

    fstream oF1("hello.txt");
    fstream oF2(filepath);
    std::fstream oF3("hello.txt");
    std::fstream oF4(filepath);

    fstream oF5{"hello.txt"};
    fstream oF6{filepath};
    std::fstream oF7{"hello.txt"};
    std::fstream oF8{filepath};

    std::fstream u_cmt_test1; // std::fstream line_commented_1;
    // std::fstream line_commented_2;
    std::fstream u_cmt_test2; /* std::fstream comment1; */
    /* std::fstream comment2; */

    // different indentations
std::fstream u_indent0;
 std::fstream u_indent1;
  std::fstream u_indent2;
   std::fstream u_indent3;
    std::fstream u_indent4;
                                std::fstream u_indent_many;
	std::fstream u_indent_t1;
				std::fstream u_indent_t4;

    { std::fstream u_inbrackets; }
    if (argc > 1) {
        std::fstream u_ifstatement1;
    }
    if (argc > 2) { std::fstream u_ifstatement2; }
    if (argc > 3) std::fstream u_ifstatement3;

    std::fstream u_multi_stmt1; std::fstream u_multi_stmt2;
    std::fstream u_multi_dec1, u_multi_dec2;

    return 0;
}