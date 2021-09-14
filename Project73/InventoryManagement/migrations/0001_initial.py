# Generated by Django 3.2.7 on 2021-09-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Provider', models.CharField(max_length=30)),
                ('Product_name', models.CharField(max_length=60)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Amount', models.FloatField()),
                ('Stock', models.IntegerField()),
            ],
        ),
    ]
