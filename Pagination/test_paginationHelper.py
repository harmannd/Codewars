from unittest import TestCase
from PaginationHelper import PaginationHelper

class TestPaginationHelper(TestCase):
    collection = range(1,25)
    helper = PaginationHelper(collection, 10)

    def test_item_count(self):
        self.assertEqual(self.helper.item_count(), 24, 'item_count returned incorrect value')

    def test_page_count(self):
        self.assertEqual(self.helper.page_count(), 3, 'page_count is returning incorrect value.')

    def test_page_item_count(self):
        self.assertEqual(self.helper.page_item_count(2), 4, 'page_item_count returned incorrect value')

    def test_page_index(self):
        self.assertEqual(self.helper.page_index(23), 2, 'page_index returned incorrect value')
