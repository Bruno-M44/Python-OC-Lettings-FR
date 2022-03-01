import pytest

from django.urls import reverse
from django.test import Client, TestCase
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
class TestIndexView(TestCase):

    def test_index_view(self):
        client = Client()
        path = reverse('index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<title>Holiday Homes</title>"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")
