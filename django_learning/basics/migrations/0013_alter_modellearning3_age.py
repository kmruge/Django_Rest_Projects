# Generated by Django 4.2.4 on 2023-10-29 06:28

import basics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0012_alter_modellearning3_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modellearning3',
            name='age',
            field=models.IntegerField(error_messages={'invalid': 'Age field is required'}, validators=[basics.models.age_validator]),
        ),
    ]
