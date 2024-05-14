from django.test import TestCase
from employees.models.workers import Worker
from employees.models.positions import Position
from employees.models.locations import Location
from employees.models.departments import Department
from employees.models.buildings import Building
from employees.models.structures import Structure
from employees.models.organisations import Organisation

class WorkerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестовые объекты для тестирования
        position = Position.objects.create(name='Тестовая должность')
        building = Building.objects.create(
            city='Севастополь',
            street='Улица Тестовая',
            number='123',
            index='123456'
        )
        location = Location.objects.create(
            room='Тестовое помещение',
            cabinet=1,
            floor=1,
            building=building
        )
        organisation = Organisation.objects.create(name='Тестовая организация')
        structure = Structure.objects.create(name='Тестовая структура', organisation=organisation)
        department = Department.objects.create(name='Тестовый отдел', structure=structure)
        # Создаем тестового сотрудника
        Worker.objects.create(
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            position=position,
            location=location,
            department=department
        )

    def test_string_representation(self):
        # Проверяем, что строковое представление сотрудника корректно возвращает ФИО в формате "Фамилия И. О."
        worker = Worker.objects.get(id=1)
        self.assertEqual(str(worker), 'Иванов И. И.')

    def test_verbose_name_plural(self):
        # Проверяем, что множественное наименование модели сотрудника отображается корректно
        self.assertEqual(str(Worker._meta.verbose_name_plural), 'Сотрудники')

    def test_verbose_name(self):
        # Проверяем, что наименование модели сотрудника отображается корректно
        self.assertEqual(str(Worker._meta.verbose_name), 'Сотрудника')

    def test_full_name_property(self):
        # Проверяем, что свойство full_name возвращает правильное полное имя сотрудника
        worker = Worker.objects.get(id=1)
        self.assertEqual(worker.full_name, 'Иванов Иван Иванович')

    def test_short_name_property(self):
        # Проверяем, что свойство short_name возвращает короткое имя сотрудника в формате "Фамилия И. О."
        worker = Worker.objects.get(id=1)
        self.assertEqual(worker.short_name, 'Иванов И. И.')

    def test_department_relationship(self):
        # Проверяем, что отношение между сотрудником и его отделом установлено корректно
        worker = Worker.objects.get(id=1)
        self.assertEqual(worker.department.name, 'Тестовый отдел')

    def test_position_relationship(self):
        # Проверяем, что отношение между сотрудником и его должностью установлено корректно
        worker = Worker.objects.get(id=1)
        self.assertEqual(worker.position.name, 'Тестовая должность')

    def test_location_relationship(self):
        # Проверяем, что отношение между сотрудником и его местоположением установлено корректно
        worker = Worker.objects.get(id=1)
        self.assertEqual(worker.location.room, 'Тестовое помещение')
