# Generated by Django 3.2.5 on 2021-07-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('option1', models.CharField(max_length=256)),
                ('option2', models.CharField(max_length=256)),
                ('option3', models.CharField(max_length=256)),
                ('option1_count', models.IntegerField(default=0)),
                ('option2_count', models.IntegerField(default=0)),
                ('option3_count', models.IntegerField(default=0)),
            ],
        ),
    ]