# Generated by Django 4.1.5 on 2023-01-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture', '0010_rename_amount_crops_amt_bags_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=122, null=True)),
                ('date', models.DateField(null=True)),
                ('amount_bags', models.IntegerField(null=True)),
                ('price_crops', models.IntegerField(null=True)),
            ],
        ),
    ]
