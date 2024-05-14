from django.test import TestCase

from employees.models.workers import Worker


class WorkerModelTest(TestCase):

    def test_string_representation(self):
        worker = Worker(name='Иван', surname='Иванов', patronymic='Иванович')
        self.assertEqual(str(worker), 'Иванов И. И.')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Worker._meta.verbose_name_plural), 'Сотрудники')

    def test_verbose_name(self):
        self.assertEqual(str(Worker._meta.verbose_name), 'Сотрудника')
