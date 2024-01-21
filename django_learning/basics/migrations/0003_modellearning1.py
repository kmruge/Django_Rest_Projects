# Generated by Django 4.2.4 on 2023-10-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0002_fieldslearning_personal_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='modellearning1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=200, unique=True)),
                ('choisce', models.CharField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')], default='1', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
