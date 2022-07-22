from django.test import TestCase

# Create your tests here.


class TestTest(TestCase):
    """
    Something should happen
    """

    def test_first_test_is_OK(self):
        x = None
        self.assertIsNone(x)

    def test_first_test_is_not_OK(self):
        x = False
        self.assertFalse(x)
