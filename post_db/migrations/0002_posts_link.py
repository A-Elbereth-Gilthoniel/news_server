# Generated by Django 5.0.4 on 2024-04-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]