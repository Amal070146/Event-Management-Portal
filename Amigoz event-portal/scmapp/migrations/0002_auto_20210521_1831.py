# Generated by Django 3.2.3 on 2021-05-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default=7994043754, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_ground',
            name='regevent',
            field=models.CharField(max_length=40),
        ),
    ]
