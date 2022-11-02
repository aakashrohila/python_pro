# Generated by Django 4.0 on 2022-10-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classroom1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=20)),
                ('fid', models.IntegerField()),
                ('CR', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'classroom',
            },
        ),
        migrations.CreateModel(
            name='faculty1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('doj', models.DateField()),
                ('sub_id', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('M_no', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='guardian1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian_id', models.CharField(max_length=20)),
                ('guardian_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'guardian',
            },
        ),
        migrations.CreateModel(
            name='student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prn_no', models.IntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('standard', models.CharField(max_length=20)),
                ('guardian_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='subject1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=20)),
                ('sub_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
    ]