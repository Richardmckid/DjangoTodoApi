# Generated by Django 3.2.5 on 2021-07-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
    ]