# Generated by Django 2.2.5 on 2019-09-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_auto_20190918_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='actual_payment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loans',
            name='date_approved',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loans',
            name='date_requested',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='loans',
            name='expected_payment_date',
            field=models.DateField(),
        ),
    ]
