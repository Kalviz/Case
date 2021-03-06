# Generated by Django 2.1.1 on 2018-11-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caseoverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseid', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=125)),
                ('owner', models.CharField(max_length=125)),
                ('catagory', models.CharField(max_length=20)),
                ('subcatagory', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('progress', models.CharField(max_length=100)),
                ('progressDetails', models.TextField()),
                ('incidentReporter', models.CharField(max_length=50)),
                ('incidentOwner', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=10)),
            ],
        ),
    ]
