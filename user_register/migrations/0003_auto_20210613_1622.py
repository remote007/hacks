# Generated by Django 2.0.7 on 2021-06-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0002_details_utype'),
    ]

    operations = [
        migrations.CreateModel(
            name='evnts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edate', models.CharField(max_length=20)),
                ('etime', models.CharField(max_length=20)),
                ('eloct', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
