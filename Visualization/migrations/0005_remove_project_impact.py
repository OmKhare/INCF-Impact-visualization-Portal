# Generated by Django 4.2.10 on 2024-03-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Visualization', '0004_organization_impact_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='impact',
        ),
    ]