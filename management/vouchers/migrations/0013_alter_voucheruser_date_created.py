# Generated by Django 4.2.2 on 2023-08-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0012_alter_voucheruser_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucheruser',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]