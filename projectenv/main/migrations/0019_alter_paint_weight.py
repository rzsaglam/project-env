# Generated by Django 3.2.3 on 2021-06-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_paint_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='weight',
            field=models.CharField(choices=[('20 KG', '20 KG'), ('5 KG', '5 KG')], default='20 KG', max_length=200),
        ),
    ]
