# Generated by Django 4.1.5 on 2023-01-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture', '0005_alter_machinery_machinery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinery',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
