from api.product.models import Product
from django.db import migrations


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        prod1 = Product(name="Toyota Break Pad",
                        description="Brake rotors of disc brakes rotate with the wheels, and brake pads, which are fitted to the brake calipers, clamp on these rotors to stop or decelerate the wheels.",
                        price="800",
                        stock=500)
        prod1.save()
        prod2 = Product(name="Winker Mirror",
                        description="One is the mirror installed inside the car, called the rearview mirror or back mirror. The rearview mirror is attached to the upper center of the car's windshield and serves to check directly behind the car.",
                        price="350",
                        stock=200)
        prod2.save()
        prod3 = Product(name="Gear Lever",
                        description="Gears can be classified by shape as involute, cycloidal and trochoidal gears.",
                        price="750",
                        stock=300)
        prod3.save()
        prod4 = Product(name="Senota Windscreen",
                        description="A cracked windscreen can impede a driver's vision, making it difficult to see approaching traffic and other road hazards.",
                        price="900",
                        stock=100)
        prod4.save()

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]
