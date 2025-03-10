# Generated by Django 5.1.4 on 2025-01-25 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def rename_description_to_reason(apps, schema_editor):
    # Get the Transaction model
    Transaction = apps.get_model('tracker', 'Transaction')
    # Rename the column directly in the database
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("ALTER TABLE tracker_transaction RENAME COLUMN description TO reason;")

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', 'previous_migration_file'),
    ]

    operations = [
        migrations.RunPython(rename_description_to_reason),
    ]

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]


