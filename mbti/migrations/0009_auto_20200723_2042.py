# Generated by Django 3.0.3 on 2020-07-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0008_auto_20200723_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputclient',
            name='password',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='mbtiresult',
            name='password',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
