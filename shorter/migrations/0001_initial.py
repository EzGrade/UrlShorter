# Generated by Django 5.0.7 on 2024-07-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=16)),
                ('initial_url', models.URLField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('auto_delete_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
