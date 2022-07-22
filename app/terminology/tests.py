from django.test import TestCase
from .models import Term

# Create your tests here.


class TerminologyTest(TestCase):

    def setUp(self):
        term = Term.objects.create(
            definition='CORS', description='CORS description')

    def test_term_create_success(self):
        term = Term.objects.first()

        self.assertEqual(term.definition, 'CORS')
        self.assertEqual(term.description, 'CORS description')

    def test_term_update_success(self):
        term = Term.objects.first()
        term.definition = 'HTTP'
        term.description = 'HTTP description'
        term.save()

        self.assertEqual(Term.objects.first().definition, 'HTTP')
        self.assertEqual(Term.objects.first().description, 'HTTP description')
