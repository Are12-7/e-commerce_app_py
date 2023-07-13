# Generated by Django 4.1.4 on 2023-07-13 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_remove_product_prodapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('mobile', models.IntegerField(max_length=11)),
                ('city', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=150)),
                ('province', models.CharField(choices=[('Alberta', 'AL'), ('British Columbia', 'BC'), ('Manitoba', 'MB'), ('New Brunswick', 'NB'), ('Newfoundland and Labrador', 'NL'), ('Nova Scotia', 'NS'), ('Ontario', 'ON'), ('Prince Edward Island', 'PE'), ('Quebec', 'QC'), ('Saskatchewan', 'SK'), ('Northwest Territories', 'NT'), ('Nunavut', 'NU'), ('Yukon', 'YT')], max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]