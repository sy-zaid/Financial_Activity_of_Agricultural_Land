# Generated by Django 4.1.5 on 2023-01-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture', '0006_alter_machinery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinery',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
