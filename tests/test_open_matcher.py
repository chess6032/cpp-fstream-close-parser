# Big thanks to the big GPT for these.

import sys
import os

import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from filecloseparser import FileCloseParser


class TestOpenMatcher(unittest.TestCase):
    def setUp(self):
        self.match_open = FileCloseParser.open_matcher()

    def assertOpens(self, statement: str, name: str = "file"):
        result = self.match_open(statement)
        self.assertIsNotNone(result, msg=f"Expected match: {statement!r}")
        self.assertEqual(result, name)

    def assertDoesNotOpen(self, statement: str):
        result = self.match_open(statement)
        self.assertIsNone(result, msg=f"Expected no match: {statement!r}")

    def test_basic_literal_open(self):
        self.assertOpens('file.open("literal");')

    def test_basic_variable_open(self):
        self.assertOpens("file.open(filepath);")

    def test_open_with_extra_args(self):
        cases = [
            'file.open("literal", std::ios::in);',
            'file.open("literal", std::ios::out);',
            'file.open("literal", std::ios::app);',
            "file.open(filepath, std::ios::in);",
            "file.open(filepath, std::ios::out);",
            "file.open(filepath, std::ios::app);",
            "file.open(filepath, std::ios::in | std::ios::out);",
            'file.open("literal", std::ios::in | std::ios::binary);',
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertOpens(statement)

    def test_different_stream_names(self):
        cases = [
            ('in_file.open("literal");', "in_file"),
            ("in_file.open(filepath);", "in_file"),
            ("in_file.open(filepath, std::ios::in);", "in_file"),
            ('out_file.open("literal");', "out_file"),
            ("out_file.open(filepath);", "out_file"),
            ("out_file.open(filepath, std::ios::out);", "out_file"),
            ("std_file.open(filepath, std::ios::in | std::ios::out);", "std_file"),
        ]

        for statement, expected_name in cases:
            with self.subTest(statement=statement):
                self.assertOpens(statement, expected_name)

    def test_spacing_variations(self):
        cases = [
            'file . open("literal");',
            'file.open ( "literal" );',
            "file.open( filepath );",
            ' file.open("literal");',
            '  file.open("literal");',
            '\tfile.open("literal");',
            '\t\tfile.open("literal");',
            'file.open("literal");        ',
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertOpens(statement)

    def test_control_flow_same_statement(self):
        cases = [
            'if (1) file.open("literal");',
            'if (1) { file.open("literal"); }',
            'while (1) file.open(filepath);',
            'for (int i = 0; i < 1; ++i) file.open("literal");',
            "{ file.open(filepath); }",
            "{ file.open(filepath, std::ios::binary); }",
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertOpens(statement)

    def test_negative_cases(self):
        cases = [
            "file.close();",
            'open("literal");',
            "file.is_open();",
            "file.opened();",
            "file;",
            "fstream file;",
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertDoesNotOpen(statement)


if __name__ == "__main__":
    unittest.main()