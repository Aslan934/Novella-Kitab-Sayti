# Generated by Django 2.1.7 on 2019-09-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20190905_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitablar',
            name='dil',
            field=models.CharField(choices=[('Azərbaycan', 'Azərbaycan'), ('Türk', 'Türk'), (
                'Rus', 'Rus'), ('İngilis', 'İngilis')], default='', max_length=100, verbose_name='Dil'),
        ),
        migrations.AlterField(
            model_name='kitablar',
            name='janr',
            field=models.CharField(choices=[('Dedektiv', 'dedektiv'), ('Fantastik', 'fantastik'), ('Psixoloji', 'psixoloji'), ('Hüquq', 'hüquq'), (
                'Roman', 'roman'), ('Dünya Ədəbiyyatı', 'dünya ədəbiyyatı'), ('Fəlsəfə', 'fəlsəfə')], default='', max_length=100, verbose_name='Janr'),
        ),
    ]