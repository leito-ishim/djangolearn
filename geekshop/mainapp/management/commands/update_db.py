from django.core.management.base import BaseCommand
from authapp.models import User, UserProfile



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            UserProfile.objects.create(user=user)
