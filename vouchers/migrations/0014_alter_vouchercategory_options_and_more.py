# Generated by Django 4.2.19 on 2025-02-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vouchers", "0013_alter_voucheruser_date_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vouchercategory",
            options={
                "verbose_name": "VoucherCategory",
                "verbose_name_plural": "VoucherCategories",
            },
        ),
        migrations.AlterModelOptions(
            name="voucherfile",
            options={
                "ordering": ["-date_created"],
                "verbose_name": "VoucherFile",
                "verbose_name_plural": "VoucherFiles",
            },
        ),
        migrations.AlterModelOptions(
            name="voucherlogs",
            options={
                "ordering": ["-date_created"],
                "verbose_name": "VoucherLogs",
                "verbose_name_plural": "VoucherLogs",
            },
        ),
        migrations.AlterModelOptions(
            name="vouchers",
            options={
                "ordering": ["-date_created"],
                "verbose_name": "Vouchers",
                "verbose_name_plural": "Vouchers",
            },
        ),
        migrations.AlterModelOptions(
            name="voucheruser",
            options={
                "verbose_name": "VoucherUser",
                "verbose_name_plural": "VoucherUsers",
            },
        ),
        migrations.AddField(
            model_name="voucheruser",
            name="email",
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
