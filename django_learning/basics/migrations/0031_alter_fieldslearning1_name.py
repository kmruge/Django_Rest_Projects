# Generated by Django 4.2.4 on 2023-11-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0030_alter_fieldslearning1_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldslearning1',
            name='name',
            field=models.CharField(error_messages={'null': 'Name field is required custom'}, max_length=20),
        ),
    ]
