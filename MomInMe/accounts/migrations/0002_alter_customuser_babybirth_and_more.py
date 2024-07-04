# Generated by Django 5.0.6 on 2024-07-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='babyBirth',
            field=models.DateField(blank=True, null=True, verbose_name='아기 생일'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='babyGender',
            field=models.CharField(max_length=10, verbose_name='아기 성별'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='babyNickname',
            field=models.CharField(max_length=10, verbose_name='아기 별명'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='motherBirth',
            field=models.DateField(blank=True, null=True, verbose_name='엄마 생일'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='motherNickname',
            field=models.CharField(max_length=10, verbose_name='엄마 별명'),
        ),
    ]