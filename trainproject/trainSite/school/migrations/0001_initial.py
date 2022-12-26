# Generated by Django 4.1.4 on 2022-12-26 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150)),
                ('grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('numberOfHours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150)),
                ('experience', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('quarter', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.subject')),
            ],
        ),
    ]
