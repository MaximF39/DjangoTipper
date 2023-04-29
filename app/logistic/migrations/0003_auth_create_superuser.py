from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create_superuser('root', '', '123')


class Migration(migrations.Migration):
    dependencies = [
        ('logistic', '0002_data_create_cars_and_models_car'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
