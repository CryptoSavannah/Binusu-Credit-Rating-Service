# Generated by Django 2.2.5 on 2019-09-25 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_auto_20190924_1002'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('hashed_nin', 'user_number')},
        ),
    ]
