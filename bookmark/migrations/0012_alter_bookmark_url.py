# Generated by Django 4.1.1 on 2022-09-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0011_alter_bookmark_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
