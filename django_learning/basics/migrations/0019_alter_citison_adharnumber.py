# Generated by Django 4.2.4 on 2023-11-03 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0018_alter_adharnumber_adhar_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citison',
            name='adharnumber',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='human', to='basics.adharnumber'),
        ),
    ]