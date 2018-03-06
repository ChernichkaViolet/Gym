from django.test import TestCase, Client
from django.urls import reverse
from django.utils import unittest

from . import models

# Create your tests here.
HTTP_OK_STATUS = 200
HTTP_NOT_FOUND_STATUS = 404
HTTP_REDIRECT_STATUS = 302


class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_wrong_url_return_http_NOT_FOUND_status(self):
        url = '/exercise/gogopowerrangers'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_list_return_http_OK_status(self):
        url = reverse('exercises:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_detail_return_http_OK_status(self):
        exercise = models.Exercise.objects.create()
        url = reverse('exercises:exercises_detail', kwargs={'pk': exercise.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_wrong_detail_id_return_http_NOT_FOUND_status(self):
        url = reverse('exercises:exercises_detail', kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_delete_return_http_REDIRECT_status(self):
        exercise = models.Exercise.objects.create()
        url = reverse('exercises:exercises_delete', kwargs={'pk': exercise.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTP_REDIRECT_STATUS, msg='Not OK')


# class TestExerciseModels(TestCase):
#     model = models.Exercise
#
#     def test_create(self):
#         description = 'Description'
#         set_quantity = 3
#         repeats = 12
#         exercise = self.model.objects.create(
#             description=description,
#             set_quantity=set_quantity,
#             repeats=repeats,
#         )
#         self.assertEqual(exercise.description, description)
#         self.assertEqual(exercise.set_quantity, set_quantity)
#         self.assertEqual(exercise.repeats, repeats)

