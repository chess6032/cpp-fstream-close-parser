# test_close_matcher.py


import sys
import os

import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from filecloseparser import FileCloseParser


class TestCloseMatcher(unittest.TestCase):
    def setUp(self):
        self.match_close = FileCloseParser.close_matcher()

    def assertCloses(self, statement: str, name: str = "file"):
        result = self.match_close(statement)
        self.assertIsNotNone(result, msg=f"Expected close match: {statement!r}")
        self.assertEqual(result, name)

    def assertDoesNotClose(self, statement: str):
        result = self.match_close(statement)
        self.assertIsNone(result, msg=f"Expected no close match: {statement!r}")

    def test_basic_close(self):
        self.assertCloses("file.close();")

    def test_different_stream_names(self):
        cases = [
            ("in_file.close();", "in_file"),
            ("out_file.close();", "out_file"),
            ("std_file.close();", "std_file"),
            ("uF1.close();", "uF1"),
            ("oF8.close();", "oF8"),
        ]

        for statement, name in cases:
            with self.subTest(statement=statement):
                self.assertCloses(statement, name)

    def test_spacing_variations(self):
        cases = [
            "file . close();",
            "file.close ();",
            "file.close( );",
            "file . close ( );",
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertCloses(statement)

    def test_negative_cases(self):
        cases = [
            "file.open(filepath);",
            "file.is_open();",
            "file.closed();",
            "close();",
            "std::fstream file;",
            "fstream file;",
            "file.close;",
            "file.close(filepath);",
            "file.close(1);",
            "file.close_all();",
            "not_a_call_to_close;",
        ]

        for statement in cases:
            with self.subTest(statement=statement):
                self.assertDoesNotClose(statement)


if __name__ == "__main__":
    unittest.main()