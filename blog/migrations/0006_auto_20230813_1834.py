# Generated by Django 3.2.20 on 2023-08-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230813_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Write your comment here'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='Email', max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Name', max_length=80),
        ),
    ]
