from django.test import TestCase

from employees.models.workers import Worker


class WorkerModelTest(TestCase):

    def test_string_representation(self):
        worker = Worker(name='Иван', surname='Иванов', patronymic='Иванович')
        self.assertEqual(str(worker), 'Иванов И. И.')
