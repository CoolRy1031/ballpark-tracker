# Generated by Django 4.1 on 2022-08-07 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_concession'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concession',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='stadium',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='concession',
            name='date',
            field=models.DateField(verbose_name='Purchase Date'),
        ),
    ]
