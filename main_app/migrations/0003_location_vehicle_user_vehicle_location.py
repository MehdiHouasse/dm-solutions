# Generated by Django 4.2.5 on 2023-10-02 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_vehicle_year_alter_vehicle_msrp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('state_code', models.CharField(max_length=2, verbose_name='State')),
                ('zipcode', models.IntegerField(verbose_name='Zip Code')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.location'),
            preserve_default=False,
        ),
    ]
