# Generated by Django 4.1.1 on 2022-09-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0010_alter_bookmark_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
    ]