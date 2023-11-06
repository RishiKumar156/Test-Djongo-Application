# Generated by Django 4.2.7 on 2023-11-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.EmailField(db_index=True, max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('create', models.DateField()),
            ],
        ),
    ]
