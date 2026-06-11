from faker import Faker
from django.core.management.base import BaseCommand
from students.models import Student

fake = Faker()

class Command(BaseCommand):
    help = "Create random students"

    def handle(self, *args, **kwargs):

        for _ in range(5):

            Student.objects.get_or_create(
                email=fake.email(),
                defaults={
                    "name": fake.name()
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Students Created Successfully")
        )