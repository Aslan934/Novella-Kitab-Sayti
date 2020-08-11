# Generated by Django 2.1.7 on 2019-09-01 19:09

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20190901_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitablar',
            old_name='Yazichi',
            new_name='Yazar',
        ),
        migrations.RenameField(
            model_name='kitablar',
            old_name='Icare_ucun',
            new_name='icare_ucun',
        ),
        migrations.AddField(
            model_name='kitablar',
            name='shekil',
            field=models.FileField(blank=True, null=True,
                                   upload_to='', verbose_name='Şəkil'),
        ),
        migrations.AddField(
            model_name='kitablar',
            name='tarix',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name='Əlavə edildiyi tarix'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitablar',
            name='veziyyet',
            field=models.CharField(choices=[('Yeni', 'yeni'), (
                'İşlənmiş', 'işlənmiş')], default='', max_length=10, verbose_name='Vəziyyəti'),
        ),
        migrations.AlterField(
            model_name='kitablar',
            name='Mezmun',
            field=ckeditor.fields.RichTextField(
                default='', verbose_name='Məzmun'),
        ),
    ]