from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="admin", email="adminuser@gmail.com", is_staff=True, is_superuser=True, phone="0112345567", gender="Male")
        user.set_password("root")
        user.save()

    dependencies = [
    
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]