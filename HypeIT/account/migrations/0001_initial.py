# Generated by Django 4.0.2 on 2022-02-21 15:56

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=50)),
                ('email', models.EmailField(default='@hype.de', max_length=254)),
                ('comment', models.TextField(blank=b'I01\n')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.city')),
                ('department', models.ForeignKey(on_delete=django.db.models.query.Prefetch, to='account.department')),
            ],
        ),
    ]
