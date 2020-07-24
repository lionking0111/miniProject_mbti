# Generated by Django 3.0.3 on 2020-07-24 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inputClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('password', models.IntegerField(default=0, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MbtiResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('password', models.IntegerField(default=0, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('extraScore', models.IntegerField(default=0)),
                ('introScore', models.IntegerField(default=0)),
                ('senseScore', models.IntegerField(default=0)),
                ('intuiScore', models.IntegerField(default=0)),
                ('thinkScore', models.IntegerField(default=0)),
                ('feelScore', models.IntegerField(default=0)),
                ('judgeScore', models.IntegerField(default=0)),
                ('perceiScore', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mbti.inputClient')),
            ],
        ),
    ]
