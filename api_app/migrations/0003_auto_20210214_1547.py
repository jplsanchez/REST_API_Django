# Generated by Django 3.1.2 on 2021-02-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20210214_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
