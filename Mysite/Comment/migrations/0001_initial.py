# Generated by Django 3.1.1 on 2020-10-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Overview', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('Date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
