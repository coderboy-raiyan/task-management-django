# Generated by Django 4.2.7 on 2023-12-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=500)),
                ('task_description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('task_assign', models.DateTimeField(auto_now_add=True)),
                ('task_categories', models.ManyToManyField(to='category.categorymodel')),
            ],
        ),
    ]
