import datetime

from django.test import TestCase

from .models import Reservations



class ReservationsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservations.objects.create(
            property_name='PropertyName1',
            city='Oradea',
            net_income=420.69,
            date = datetime.datetime(2020,7,16)
        )

    def test_if_information_is_correct(self):
        self.assertIsInstance(self.reservation.property_name, str)
        self.assertIsInstance(self.reservation.city, str)
        self.assertIsInstance(self.reservation.net_income, float)
        self.assertIsInstance(self.reservation.date, datetime.datetime)


    def test_if_information_is_not_correct(self):
        self.assertNotIsInstance(self.reservation.property_name, int)
        self.assertNotIsInstance(self.reservation.city, int)
        self.assertNotIsInstance(self.reservation.net_income, str)
        self.assertNotIsInstance(self.reservation.date, str)
    
