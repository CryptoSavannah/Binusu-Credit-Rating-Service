# Generated by Django 2.2.5 on 2019-09-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
