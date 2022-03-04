import pytest

from django.urls import reverse
from django.test import Client, TestCase
from pytest_django.asserts import assertTemplateUsed
from ..models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestProfilesView(TestCase):
    def setUp(self):
        User.objects.create(username="Bruno",
                            first_name="Bruno",
                            last_name="Smith",
                            email="bruno.smith@mail.com",
                            password="django123!")
        User.objects.create(username="John",
                            first_name="John",
                            last_name="Smith",
                            email="john.smith@mail.com",
                            password="django123!")
        Profile.objects.create(user=User.objects.get(username="Bruno"),
                               favorite_city="Chicago")
        Profile.objects.create(user=User.objects.get(username="John"),
                               favorite_city="Los Angeles")

    def test_profile_view(self):
        client = Client()
        path = reverse('profiles:profile', kwargs={'username': "Bruno"})
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<title>Bruno</title>"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

    def test_index_view(self):
        client = Client()
        path = reverse('profiles:index')
        response = client.get(path)
        content = response.content.decode()
        expected_title = "<title>Profiles</title>"
        excepted_profile_1 = "Bruno"
        excepted_profile_2 = "John"

        assert expected_title in content
        assert excepted_profile_1 in content
        assert excepted_profile_2 in content

        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")
