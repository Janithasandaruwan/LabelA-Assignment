from api.category.models import Category
from django.db import migrations


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        cat1 = Category(name="Toyota", description="Toyota Car Parts")
        cat1.save()
        cat2 = Category(name="BMW", description="BMW Car Parts")
        cat2.save()
        cat3 = Category(name="Ford", description="Ford Car Parts")
        cat3.save()
        cat4 = Category(name="Porsche", description="Porsche Car Parts")
        cat4.save()
        cat5 = Category(name="Mercedes-Benz", description="Mercedes-Benz Car Parts")
        cat5.save()
        cat6 = Category(name="Bentley", description="Bentley Car Parts")
        cat6.save()
        cat7 = Category(name="KIA", description="KIA Car Parts")
        cat7.save()
        cat8 = Category(name="Audi", description="Audi Car Parts")
        cat8.save()
        cat9 = Category(name="NISSAN", description="NISSAN Car Parts")
        cat9.save()
        cat10 = Category(name="Tesla", description="Tesla Car Parts")
        cat10.save()

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]
