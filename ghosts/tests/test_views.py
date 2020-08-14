from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from ghosts.models import GhostUser, GhostName

# Create your tests here.
class HomePageTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class PostGhostUserTestCase(TestCase):

    def setUp(self):
        user_fields = {
            "username": "MikeGhost",
            "email": "mike@gamil.com",
            "password": "pass123"
        }
        User = get_user_model()
        self.user = User.objects.create_user(**user_fields)
        self.client = Client()
        self.client.login(username='MikeGhost', password='pass123')
        ghost_name_fields = {
            "name": "Casper",
            "description": "Animated cartoons in the mid-40s..."
        }
        self.ghost_name = GhostName.objects.create(**ghost_name_fields)

    def test_post_ghost_user_view(self):
        response = self.client.get(reverse("name_picker"))
        self.assertEqual(response.status_code, 200)

    def test_ghost_user_create(self):
        form_data = {
            'first_name': 'Mike',
            'last_name': 'George',
            'ghost_name': self.ghost_name.id
        }
        response = self.client.post(
            reverse('name_picker'),
            form_data
        )
        self.assertEqual(response.status_code, 302)
        gh_users = GhostUser.objects.all()
        self.assertEqual(gh_users.count(), 1)
        gh_user = gh_users.first()
        self.assertEqual(gh_user.user.first_name, 'Mike')
        self.assertEqual(gh_user.user.last_name, 'George')
        self.assertEqual(gh_user.ghost_name.name, 'Casper')

