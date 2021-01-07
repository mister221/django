# Generated by Django 3.1.5 on 2021-01-05 04:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=20)),
                ('dept_mgr', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Others')], max_length=6)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='invalid phone number', regex='^[6789]\\d{9}$')])),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employees.employee')),
                ('date', models.DateField()),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.role'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('login_time', models.TimeField(auto_now_add=True)),
                ('logout_time', models.TimeField(blank=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
