# Generated by Django 4.2.4 on 2023-12-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0035_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
