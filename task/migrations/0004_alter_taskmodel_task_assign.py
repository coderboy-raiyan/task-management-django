# Generated by Django 4.2.7 on 2023-12-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_taskmodel_task_assign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_assign',
            field=models.DateTimeField(),
        ),
    ]
