# Generated by Django 5.0.6 on 2024-06-20 21:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('problem_resolution_time', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('timely_update_information', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('technical_skill_service_engineer', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('communication_attire_behavior', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('response_backend_team', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('overall_experience', models.IntegerField(choices=[(5, 'Excellent / Appreciable'), (4, 'Very Good / More than expectations'), (3, 'Good / As expected'), (2, 'Poor / Below average or below than expectations'), (1, 'Very Poor / Needed improvement')])),
                ('suggestions', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('otp', models.CharField(max_length=50, verbose_name='OTP')),
            ],
        ),
    ]
