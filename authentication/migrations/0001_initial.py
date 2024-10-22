# Generated by Django 5.1.2 on 2024-10-22 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('ADM', 'Admin'), ('BUY', 'Buyer'), ('SEL', 'Seller')], default='BUY', max_length=3)),
                ('region', models.CharField(choices=[('JAKUT', 'Jakarta Utara'), ('JAKBAR', 'Jakarta Barat'), ('JAKSEL', 'Jakarta Selatan'), ('JAKTIM', 'Jakarta Timur'), ('JAKPUS', 'Jakarta Pusat')], max_length=6)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
