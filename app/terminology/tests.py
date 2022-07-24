from django.test import TestCase
from .models import Term
from freezegun import freeze_time
import datetime


@freeze_time("2022-01-14")
class TerminologyTest(TestCase):

    def setUp(self):
        term = Term.objects.create(
            definition='Co to CORS', description='CORS description')

    def test_term_was_created_successully(self):
        self.assertEqual(Term.objects.first().definition, 'Co to CORS')
        self.assertEqual(Term.objects.first().description, 'CORS description')
        self.assertEqual(Term.objects.first().slug, 'co-to-cors')
        self.assertEqual(
            Term.objects.first().created_at, datetime.datetime(2022, 1, 14, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Term.objects.first().modified_at, datetime.datetime(2022, 1, 14, 0, 0, tzinfo=datetime.timezone.utc))

    def test_create_term_with_missing_definition_raises_error(self):
        with self.assertRaises(Exception):
            Term.objects.create(
                definition=None, description='CORS description')

    def test_update_term_with_existing_definition_raises_error(self):
        with self.assertRaises(Exception):
            Term.objects.create(
                definition=Term.objects.first().definition, description='CORS description')

    def test_term_update_successfully(self):
        term = Term.objects.first()
        term.definition = 'HTTP wyjaśnienie'
        term.description = 'HTTP description'
        term.save()
        self.assertEqual(Term.objects.first().definition, 'HTTP wyjaśnienie')
        self.assertEqual(Term.objects.first().description, 'HTTP description')
        self.assertEqual(Term.objects.first().slug, 'http-wyjasnienie')
        self.assertEqual(
            term.created_at, datetime.datetime(2022, 1, 14, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            term.modified_at, datetime.datetime(2022, 1, 14, 0, 0, tzinfo=datetime.timezone.utc))

    def test_delete_term_successfully(self):
        Term.objects.first().delete()
        self.assertEqual(Term.objects.all().count(), 0)
