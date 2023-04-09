# Generated by Django 3.2.16 on 2023-01-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]
