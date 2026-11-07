"""Tests for the AI-assisted folder helper, not learner challenge solutions."""
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from new_challenge import create


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='challenge-scaffold-')
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(Path(tempfile.gettempdir()).resolve()))

    def tearDown(self):
        self.temp.cleanup()

    def test_empty_attempt_and_no_false_completion(self):
        p = create('leetcode', 'sample-problem', 'javascript', 'https://leetcode.com/problems/sample-problem/', self.root)
        self.assertEqual((p / 'attempt.js').read_text(), '// Write your independent attempt here.\n')
        self.assertIn('Status: Not started', (p / 'README.md').read_text())
        self.assertIn('No checks recorded.', (p / 'README.md').read_text())

    def test_existing_attempt_is_never_overwritten(self):
        p = create('coderbyte', 'sample', 'python', root=self.root)
        (p / 'attempt.py').write_text('my existing work')
        with self.assertRaises(FileExistsError):
            create('coderbyte', 'sample', 'python', root=self.root)
        self.assertEqual((p / 'attempt.py').read_text(), 'my existing work')

    def test_path_traversal_and_assessment_links_rejected(self):
        for slug in ['../escape', 'a/b', 'C:drive', 'A Name']:
            with self.assertRaises(ValueError):
                create('leetcode', slug, 'python', root=self.root)
        for url in ['https://coderbyte.com/assessment/private', 'https://coderbyte.com/challenges/public?token=private', 'https://other.example/problem']:
            with self.assertRaises(ValueError):
                create('coderbyte', 'sample', 'python', url, self.root)

    def test_sql_category(self):
        p = create('sql', 'joins', 'sql', root=self.root)
        self.assertTrue((p / 'attempt.sql').exists())
        with self.assertRaises(ValueError):
            create('sql', 'wrong-language', 'javascript', root=self.root)


if __name__ == '__main__':
    unittest.main()
