import pytest

from django.urls import reverse
from django.test import Client, TestCase
from pytest_django.asserts import assertTemplateUsed
from ..models import Letting, Address


@pytest.mark.django_db
class TestLettingsView(TestCase):
    def setUp(self):
        Address.objects.create(number=10,
                               street="Madisson Avenue",
                               city="New York",
                               state="NY",
                               zip_code=11554,
                               country_iso_code="USA")
        Address.objects.create(number=30,
                               street="Statue of liberty",
                               city="New York",
                               state="NY",
                               zip_code=11554,
                               country_iso_code="USA")
        Letting.objects.create(title="Campaign Retreat",
                               address=Address.objects.get(
                                   number=10,
                                   street="Madisson Avenue"))
        Letting.objects.create(title="Beach Retreat",
                               address=Address.objects.get(
                                   number=30,
                                   street="Statue of liberty"))

    def test_letting_view(self):
        client = Client()
        path = reverse('letting', kwargs={'letting_id': 1})
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<title>Campaign Retreat</title>"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "letting.html")

    def test_lettings_index_view(self):
        client = Client()
        path = reverse('lettings_index')
        response = client.get(path)
        content = response.content.decode()
        expected_title = "<title>Lettings</title>"
        excepted_letting_1 = "Campaign Retreat"
        excepted_letting_2 = "Beach Retreat"

        assert expected_title in content
        assert excepted_letting_1 in content
        assert excepted_letting_2 in content

        assert response.status_code == 200
        assertTemplateUsed(response, "lettings_index.html")
