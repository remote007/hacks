# Generated by Django 2.0.7 on 2021-06-13 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_register.Position'),
        ),
    ]