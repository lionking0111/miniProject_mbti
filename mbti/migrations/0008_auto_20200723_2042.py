# Generated by Django 3.0.3 on 2020-07-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0007_mbtiresult_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputclient',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputclient',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='inputclient',
            name='nickname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inputclient',
            name='password',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mbtiresult',
            name='nickname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mbtiresult',
            name='password',
            field=models.IntegerField(default=0),
        ),
    ]
