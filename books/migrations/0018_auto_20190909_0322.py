# Generated by Django 2.1.7 on 2019-09-08 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20190909_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitablar',
            options={'ordering': ['-tarix']},
        ),
    ]
