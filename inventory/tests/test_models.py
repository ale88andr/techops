from django.test import TestCase

from inventory.models.equipment_type import EquipmentType


class EquipmentTypeModelTest(TestCase):

    def test_string_representation(self):
        equipment_type = 'Printer'
        worker = EquipmentType(name=equipment_type)
        self.assertEqual(str(worker), equipment_type)

    def test_verbose_name_plural(self):
        self.assertEqual(str(EquipmentType._meta.verbose_name_plural), 'Типы оборудования')

    def test_verbose_name(self):
        self.assertEqual(str(EquipmentType._meta.verbose_name), 'Тип оборудования')
