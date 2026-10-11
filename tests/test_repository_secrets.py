import unittest
from scripts.check_repository_secrets import findings


class PublicationScanTests(unittest.TestCase):
    def test_google_key_in_embedded_html(self):
        value = 'AIza' + 'A' * 35
        self.assertEqual(findings('<script>{"apiKey":"' + value + '"}</script>'), ['Google API key'])

    def test_redacted_html(self):
        self.assertEqual(findings('<script>{"apiKey":"[REDACTED_GOOGLE_API_KEY]"}</script>'), [])

    def test_other_credentials_and_plain_docs(self):
        self.assertIn('Databricks token', findings('dapi' + 'a' * 32))
        self.assertIn('GitHub token', findings('ghp_' + 'A' * 36))
        self.assertEqual(findings('Google API key must be restricted; no credential here.'), [])
