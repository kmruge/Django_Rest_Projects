# Generated by Django 4.2.4 on 2023-10-29 06:21

import basics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0010_modellearning2_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='modellearning3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(error_messages={'invalid': 'Enter a valid age'}, validators=[basics.models.age_validator])),
            ],
        ),
    ]
