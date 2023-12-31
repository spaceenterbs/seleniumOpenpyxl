# Generated by Django 4.2.2 on 2023-06-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('like_num', models.PositiveIntegerField()),
                ('review_num', models.PositiveBigIntegerField()),
                ('write_date', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
