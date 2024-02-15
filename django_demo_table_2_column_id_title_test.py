from django.test import TestCase
from .models import DemoTable

class DemoTableTest(TestCase):
    def setUp(self):
        DemoTable.objects.create(id=1, title='Test Title')

    def test_title_content(self):
        demo_table = DemoTable.objects.get(id=1)
        expected_object_name = f'{demo_table.title}'
        self.assertEqual(expected_object_name, 'Test Title')