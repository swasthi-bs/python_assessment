import unittest
from format_paragraph import justify_index, create_arrays


class TestParagraph(unittest.TestCase):

    def test_create_array(self):
        paragraph = "This is a sample text but a complicated problem to solved"
        width = 20

        expected_output = ['This is a sample', 'text but a', 'complicated problem', 'to solved']

        assert create_arrays(paragraph, width) == expected_output

    def test_justify_index(self):
        sentence = "text but a"
        page_width = 20

        expected_output = "text      but      a"

        assert justify_index(sentence, page_width).strip() == expected_output

    def test_create_array(self):
        paragraph = ""
        width = 20

        expected_output = ['']

        assert create_arrays(paragraph, width) == expected_output

    def test_justify_index(self):
        sentence = ""
        page_width = 20

        expected_output = ""

        assert justify_index(sentence, page_width).strip() == expected_output

    def test_create_array(self):
        paragraph = "Paragraph justification aligns text evenly between margins"
        width = 25

        expected_output = ['Paragraph justification', 'aligns text evenly', 'between margins']

        assert create_arrays(paragraph, width) == expected_output

    def test_justify_index(self):
        sentence = "Paragraph justification aligns text evenly between margins"
        page_width = 25

        expected_output = "Paragraphjustificationalignstextevenlybetween  margins"

        assert justify_index(sentence, page_width).strip() == expected_output

    def test_create_array(self):
        paragraph = "Left justification,   aligns text to the left margin"
        width = 15

        expected_output = ['Left', 'justification,', ' aligns text to', 'the left margin']

        assert create_arrays(paragraph, width) == expected_output

    def test_justify_index(self):
        sentence = "Left justification,   aligns text to the left margin"
        page_width = 15

        expected_output = "Leftjustification,alignstexttotheleft    margin"

        assert justify_index(sentence, page_width).strip() == expected_output

    def test_create_array(self):
        paragraph = "  This is the unit test case with leading space   and multiple spaces"
        width = 20

        expected_output = ['  This is the unit', 'test case with', 'leading space   and', 'multiple spaces']

        assert create_arrays(paragraph, width) == expected_output

    def test_justify_index(self):
        sentence = "  This is the unit test case with leading space   and multiple spaces"
        page_width = 20

        expected_output = "Thisistheunittestcasewithleadingspaceandmultiple        spaces"

        assert justify_index(sentence, page_width).strip() == expected_output

    

if __name__ == '__main__':
    unittest.main()