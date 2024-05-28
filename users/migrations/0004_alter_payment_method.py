# Generated by Django 5.0.6 on 2024-05-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="method",
            field=models.CharField(
                choices=[("CASH", "cash"), ("TRAN", "transfer to account")],
                default="TRAN",
                max_length=4,
                verbose_name="method",
            ),
        ),
    ]