# Generated by Django 4.1.1 on 2022-09-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0006_alter_bookmark_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.CharField(blank=True, default='None', max_length=255, null=True),
        ),
    ]
