# Generated by Django 3.2.3 on 2021-06-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_paint_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paint',
            name='choice',
            field=models.CharField(choices=[('Boya', 'Boya'), ('Tiner', 'Tiner')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paint',
            name='location',
            field=models.CharField(choices=[('İstanbul', 'İstanbul'), ('Yalova', 'Yalova')], max_length=200),
        ),
        migrations.AlterField(
            model_name='paint',
            name='weight',
            field=models.CharField(choices=[('20 KG', '20 KG'), ('12 KG', '12 KG'), ('5 KG', '5 KG')], max_length=200),
        ),
    ]
