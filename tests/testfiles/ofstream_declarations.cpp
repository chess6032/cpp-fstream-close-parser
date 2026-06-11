#include <fstream>
using std::ofstream;

#include <string>
using std::string;

/*
This contains all possible ways we'd expect a student to format a
declaration or initialization of an std::ofstream.
*/

int main(int argc, char *argv[]) {
    string filepath = "hello.txt";

    ofstream uF1;
    std::ofstream uF2;
    ofstream uF3{};
    std::ofstream uF4{};

    ofstream oF1("hello.txt");
    ofstream oF2(filepath);
    std::ofstream oF3("hello.txt");
    std::ofstream oF4(filepath);

    ofstream oF5{"hello.txt"};
    ofstream oF6{filepath};
    std::ofstream oF7{"hello.txt"};
    std::ofstream oF8{filepath};

    std::ofstream u_cmt_test1; // std::ofstream line_commented_1;
    // std::ofstream line_commented_2;
    std::ofstream u_cmt_test2; /* std::ofstream comment1; */
    /* std::ofstream comment2; */

    // different indentations
std::ofstream u_indent0;
 std::ofstream u_indent1;
  std::ofstream u_indent2;
   std::ofstream u_indent3;
    std::ofstream u_indent4;
                                std::ofstream u_indent_many;
	std::ofstream u_indent_t1;
				std::ofstream u_indent_t4;

    { std::ofstream u_inbrackets; }
    if (argc > 1) {
        std::ofstream u_ifstatement1;
    }
    if (argc > 2) { std::ofstream u_ifstatement2; }
    if (argc > 3) std::ofstream u_ifstatement3;
    
    std::ofstream u_multi_stmt1; std::ofstream u_multi_stmt2;
    std::ofstream u_multi_dec1, u_multi_dec2;

    return 0;
}