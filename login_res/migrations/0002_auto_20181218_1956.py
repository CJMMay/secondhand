# Generated by Django 2.1.1 on 2018-12-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_res', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='eml',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='jianjie',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=4),
        ),
    ]
