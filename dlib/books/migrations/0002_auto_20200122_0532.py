# Generated by Django 2.2.9 on 2020-01-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.FileField(default='default.jpg', max_length=128, upload_to='static/uploads/'),
        ),
        migrations.AddField(
            model_name='book',
            name='filename',
            field=models.FileField(default='default.pdf', max_length=128, upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]