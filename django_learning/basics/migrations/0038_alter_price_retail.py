# Generated by Django 4.2.4 on 2023-12-24 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0037_price_retail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='retail',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='retails', to='basics.retaildetails'),
        ),
    ]
