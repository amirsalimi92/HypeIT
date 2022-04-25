# Generated by Django 4.0.2 on 2022-02-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0002_inuse_warehouse_comment_alter_warehouse_serialnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not delivered'), (2, 'Got it'), (3, 'Idle'), (4, 'Wait for the upgrade'), (5, 'Wait for repairs'), (6, 'Other')], default=1),
        ),
    ]
