# Generated by Django 2.0.1 on 2018-03-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcularPDB', '0007_auto_20180307_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='MouseProtein',
            fields=[
                ('ens_id', models.CharField(default='x', max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('tissue', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
            ],
        ),
    ]