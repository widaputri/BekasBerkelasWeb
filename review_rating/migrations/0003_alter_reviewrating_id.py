# Generated by Django 5.1.2 on 2024-10-23 08:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_rating', '0002_reviewrating_reviewee_alter_reviewrating_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
