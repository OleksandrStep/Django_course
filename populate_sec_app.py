import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_course.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from sec_app.models import Users
from faker import Faker


fakegen = Faker()


def creat_users(n=5):
    for _ in range(n):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()
        try:
            Users.objects.create(first_name=first_name,
                                 last_name=last_name,
                                 email=email)
        except django.db.utils.IntegrityError as e:
            print(e)
            n += 1


if __name__ == "__main__":
    creat_users(n=20)
