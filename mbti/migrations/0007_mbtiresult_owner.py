# Generated by Django 3.0.3 on 2020-07-23 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0006_auto_20200723_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbtiresult',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mbti.inputClient'),
        ),
    ]