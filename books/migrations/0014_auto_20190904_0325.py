# Generated by Django 2.1.7 on 2019-09-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_kitablar_janr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitablar',
            name='icare_ucun',
            field=models.CharField(choices=[('Mövcud', 'mövcud'), (
                'Mövcud deyil', 'mövcud deyil')], max_length=20, verbose_name='Kirayə üçün mövcudluğu'),
        ),
        migrations.AlterField(
            model_name='kitablar',
            name='veziyyet',
            field=models.CharField(choices=[('Yeni', 'yeni'), (
                'İşlənmiş', 'işlənmiş')], default='', max_length=20, verbose_name='Vəziyyəti'),
        ),
    ]