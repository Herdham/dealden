# Generated by Django 5.2.1 on 2025-06-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_product_user_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BOOK', 'Book'), ('HLT & WLN', 'Health & Wellness'), ('FASHION', 'FASHION')], default='', max_length=100),
            preserve_default=False,
        ),
    ]
