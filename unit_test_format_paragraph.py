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


if __name__ == '__main__':
    unittest.main()