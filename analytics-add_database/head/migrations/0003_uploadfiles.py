# Generated by Django 5.0.2 on 2024-05-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
    ]

