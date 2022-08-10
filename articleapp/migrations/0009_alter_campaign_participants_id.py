# Generated by Django 4.0.2 on 2022-08-10 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0008_article_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='Participants_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaign', to=settings.AUTH_USER_MODEL),
        ),
    ]