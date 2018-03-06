from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse


from core import models

# Create your tests here.
HTTP_OK_STATUS = 200
HTTP_NOT_FOUND_STATUS = 404
HTTP_REDIRECT_STATUS = 302


class UrlsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_wrong_url_return_http_NOT_FOUND_status(self):
        url = '/profile/gogopowerrangers'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_show_return_http_OK_status(self):
        profile = models.Profile.objects.create()
        url = reverse('account:profile_show', kwargs={'pk': profile.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_OK_STATUS, msg='Not OK')

    def test_wrong_show_id_return_http_NOT_FOUND_status(self):
        url = reverse('account:profile_show', kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_NOT_FOUND_STATUS, msg='Not OK')

    def test_edit_profile_return_http_REDIRECT_status(self):
        profile = models.Profile.objects.create()
        url = reverse('account:profile_edit', kwargs={'pk': profile.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTP_REDIRECT_STATUS, msg='Not OK')


# class TestProfileModels(TestCase):
#     model = models.Profile

    # def test_create(self):
    #     description = 'Description'
    #     set_quantity = 3
    #     repeats = 12
    #     exercise = self.model.objects.create(
    #         description=description,
    #         set_quantity=set_quantity,
    #         repeats=repeats,
    #     )
    #     self.assertEqual(exercise.description, description)
    #     self.assertEqual(exercise.set_quantity, set_quantity)
    #     self.assertEqual(exercise.repeats, repeats)

