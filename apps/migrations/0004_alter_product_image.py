# Generated by Django 5.2.1 on 2025-06-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productImage/'),
        ),
    ]
