# Generated by Django 2.1.3 on 2020-05-31 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=200)),
                ('tz', models.CharField(default='UTC', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='real_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='populate_data.User'),
        ),
    ]
