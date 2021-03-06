from django.test import TestCase
from dojo.tools.nikto.parser import NiktoXMLParser
from dojo.models import Test, Engagement, Product


class TestNiktoParser(TestCase):

    def test_parse_without_file_has_no_findings(self):
        parser = NiktoXMLParser(None, Test())
        self.assertEqual(0, len(parser.items))

    def test_parse_file_with_old_format(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-old-format.xml")
        parser = NiktoXMLParser(testfile, test)
        self.assertEqual(1, len(parser.items))

    def test_parse_file_with_no_vuln_has_no_findings(self):
        testfile = open("dojo/unittests/scans/nikto/nikto-report-zero-vuln.xml")
        parser = NiktoXMLParser(testfile, Test())
        self.assertEqual(0, len(parser.items))

    def test_parse_file_with_one_vuln_has_one_finding(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-one-vuln.xml")
        parser = NiktoXMLParser(testfile, test)
        self.assertEqual(1, len(parser.items))

    def test_parse_file_with_multiple_vuln_has_multiple_findings(self):
        test = Test()
        engagement = Engagement()
        engagement.product = Product()
        test.engagement = engagement
        testfile = open("dojo/unittests/scans/nikto/nikto-report-many-vuln.xml")
        parser = NiktoXMLParser(testfile, test)
        self.assertTrue(len(parser.items) == 10)
