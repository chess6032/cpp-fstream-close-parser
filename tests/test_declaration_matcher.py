# test_declaration_matcher.py

import sys
import os

import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from filecloseparser import FileCloseParser


class TestDeclarationMatcher(unittest.TestCase):
    def setUp(self):
        self.match_decl = FileCloseParser.declaration_matcher()

    def assertDeclares(self, statement: str, name: str, opened: bool = False):
        result = self.match_decl(statement)

        self.assertIsNotNone(result, msg=f"Expected declaration match: {statement!r}")
        self.assertEqual(result.name, name)
        self.assertEqual(result.opened, opened)
        self.assertFalse(result.closed)

    def assertDoesNotDeclare(self, statement: str):
        result = self.match_decl(statement)
        self.assertIsNone(result, msg=f"Expected no declaration match: {statement!r}")

    def test_unopened_declarations(self):
        cases = [
            ("fstream uF1;", "uF1"),
            ("std::fstream uF2;", "uF2"),
            ("fstream uF3{};", "uF3"),
            ("std::fstream uF4{};", "uF4"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name, opened=False)

    def test_opened_parentheses_initializations(self):
        cases = [
            ('fstream oF1("hello.txt");', "oF1"),
            ("fstream oF2(filepath);", "oF2"),
            ('std::fstream oF3("hello.txt");', "oF3"),
            ("std::fstream oF4(filepath);", "oF4"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name, opened=True)

    def test_opened_brace_initializations(self):
        cases = [
            ('fstream oF5{"hello.txt"};', "oF5"),
            ("fstream oF6{filepath};", "oF6"),
            ('std::fstream oF7{"hello.txt"};', "oF7"),
            ("std::fstream oF8{filepath};", "oF8"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name, opened=True)

    def test_multi_statement_lines_if_split_before_matching(self):
        cases = [
            ("std::fstream u_multi_stmt1;", "u_multi_stmt1"),
            ("std::fstream u_multi_stmt2;", "u_multi_stmt2"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name)

    def test_multi_declaration_line_current_expected_behavior(self):
        result = self.match_decl("std::fstream u_multi_dec1, u_multi_dec2;")

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "u_multi_dec1")
        self.assertFalse(result.opened)

    def test_ifstream_and_ofstream_also_match(self):
        cases = [
            ("ifstream in_file;", "in_file", False),
            ("std::ifstream std_in_file;", "std_in_file", False),
            ('ifstream in_opened("input.txt");', "in_opened", True),
            ("ofstream out_file;", "out_file", False),
            ("std::ofstream std_out_file;", "std_out_file", False),
            ('ofstream out_opened("output.txt");', "out_opened", True),
        ]

        for statement, name, opened in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name, opened)

    def test_qualifiers(self):
        cases = [
            ("const std::fstream const_file;", "const_file"),
            ("static std::fstream static_file;", "static_file"),
            ("extern std::fstream extern_file;", "extern_file"),
            ("const static std::fstream const_static_file;", "const_static_file"),
            ("static const std::fstream static_const_file;", "static_const_file"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertDeclares(statement, name)

    def test_negative_cases(self):
        cases = [
            "string filepath;",
            'string filepath = "hello.txt";',
            "int argc;",
            "file.open(filepath);",
            "file.close();",
            "std::string not_a_stream;",
            "fstream;",
            "std::fstream;",
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertDoesNotDeclare(statement)


if __name__ == "__main__":
    unittest.main()