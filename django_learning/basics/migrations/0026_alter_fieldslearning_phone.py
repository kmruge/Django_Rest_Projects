# Generated by Django 4.2.4 on 2023-11-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0025_alter_fieldslearning_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldslearning',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
