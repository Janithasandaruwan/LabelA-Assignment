from django.db import migrations
from api.order.models import Order
from api.user.models import CustomUser
from api.product.models import Product
from api.category.models import Category

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user1 = CustomUser(name="Almatari", email="silvesteralmatari@gmail.com", phone="+94761223119", gender="Male",
                          is_superuser=False)
        user1.save()
        user2 = CustomUser(name="Dilshan", email="dilshanperera@gmail.com", phone="+94761223000", gender="Male",
                           is_superuser=False)
        user2.save()

        cat1 = Category(name="DATSUN", description="DATSUN Car Parts")
        cat1.save()

        prod1 = Product(name="Meter & Gauges",
                        description="Gauges are most often used in situations where the thing we are measuring changes all the time, such as in the measuring of volume of something we are using.",
                        price="450",
                        stock=100,
                        category=cat1)
        prod1.save()

        prod2 = Product(name="Fuel Filters",
                        description="A fuel filter is a filter used to screens out foreign particles or liquids from the fuel.",
                        price="100",
                        stock=500,
                        category=cat1)
        prod2.save()

        order1 = Order(user=user1,
                        product=prod1,
                        total_products="10",
                        total_amount="4500",
                        order_confirm="False",
                        delivery_date_time="2023-10-23T23:38:19.188Z")
        order1.save()
        order2 = Order(user=user1,
                       product=prod2,
                       total_products="10",
                       total_amount="4500",
                       order_confirm="False",
                       delivery_date_time="2023-10-23T23:38:19.188Z")
        order2.save()
        order3 = Order(user=user2,
                       product=prod2,
                       total_products="5",
                       total_amount="2250",
                       order_confirm="False",
                       delivery_date_time="2023-10-23T23:38:19.188Z")
        order3.save()



    dependencies = [
        ('order', '0002_order_user'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]