from django.test import TestCase
from terminology.models import Term


class TerminologyTest(TestCase):
    fixtures = ['./fixtures/fixtures.json']

    def test_inserted_fixtures(self):
        self.assertEqual(Term.objects.all().count(), 3)
        self.assertEqual(Term.objects.get(id=1).definition, 'What is 1')
        self.assertEqual(Term.objects.get(id=2).definition, 'What is 2')
        self.assertEqual(Term.objects.get(id=3).definition, 'What is 3')
        self.assertEqual(Term.objects.get(id=1).slug, 'what-is-1')
        self.assertEqual(Term.objects.get(id=2).slug, 'what-is-2')
        self.assertEqual(Term.objects.get(id=3).slug, 'what-is-3')
        self.assertEqual(Term.objects.get(id=1).description, 'Term 1 is')
        self.assertEqual(Term.objects.get(id=2).description, 'Term 2 is')
        self.assertEqual(Term.objects.get(id=3).description, 'Term 3 is')

    def test_create_term_with_missing_definition_raises_error(self):
        with self.assertRaises(Exception):
            Term.objects.create(
                definition=None, description='Some description')

    def test_create_term_with_exsiting_definition_raises_error(self):
        with self.assertRaises(Exception):
            Term.objects.create(
                definition='What is 1', description='Some description')

    def test_create_term_with_success(self):

        Term.objects.create(definition='What is 4', description='Term 4 is')
        self.assertEqual(Term.objects.all().count(), 4)
        self.assertEqual(Term.objects.last().definition, 'What is 4')
        self.assertEqual(Term.objects.last().slug, 'what-is-4')
        self.assertEqual(Term.objects.last().description, 'Term 4 is')

    def test_update_term_with_success(self):
        term_last = Term.objects.last()
        term_last.definition = 'What is 5'
        term_last.description = 'Term 5 is'
        term_last.save()
        self.assertEqual(Term.objects.last().definition, 'What is 5')
        self.assertEqual(Term.objects.last().slug, 'what-is-5')
        self.assertEqual(Term.objects.last().description, 'Term 5 is')

    def test_delete_term_with_success(self):
        Term.objects.last().delete()
        self.assertEqual(Term.objects.all().count(), 2)
