# Generated by Django 4.2.2 on 2023-06-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_writer', models.CharField(max_length=50)),
                ('review_writer_date', models.CharField(max_length=50)),
                ('content_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
