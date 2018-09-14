# Generated by Django 2.0.6 on 2018-09-14 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180828_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='tickets', to='events.Booking'),
        ),
    ]
