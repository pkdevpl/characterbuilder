# Generated by Django 4.2.7 on 2023-11-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='create_date',
        ),
        migrations.AddField(
            model_name='character',
            name='characterClass',
            field=models.CharField(default='wojownik', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='człowiek', max_length=50),
            preserve_default=False,
        ),
    ]