from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        cat1 = CustomUser(name="admin", email="jsjweerasinghe@gmail.com", phone="+94761223443", gender="Male", is_superuser=True)
        cat1.save()
        cat2 = CustomUser(name="John", email="johnwrick@gmail.com", phone="+94761223123", gender="Male", is_superuser=False)
        cat2.save()
        cat3 = CustomUser(name="Smith", email="devsmith@gmail.com", phone="+94761223456", gender="Male", is_superuser=False)
        cat3.save()
        cat4 = CustomUser(name="Finch", email="aronfinch@gmail.com", phone="+94761223789", gender="Male", is_superuser=False)
        cat4.save()
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]
