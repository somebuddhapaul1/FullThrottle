# Generated by Django 2.1.3 on 2020-05-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('populate_data', '0002_auto_20200531_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='3DF3995E', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
