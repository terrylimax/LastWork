from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, verbose_name='Имя Пользователя')),
                ('password', models.CharField(blank=True, max_length=200, verbose_name='Пароль')),
            ],
        ),
    ]
