# Generated by Django 3.0.3 on 2020-07-17 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import subscriptions.states


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'TRIAL_ACTIVE'), (3, 'TRIAL_ENDED'), (4, 'ACTIVE'), (5, 'DEACTIVATED')], default=subscriptions.states.SubscriptionState['ACTIVE'], help_text='current subscription status of the user')),
                ('trial_limit', models.IntegerField(default=5, help_text='default search limit for trials', null=True)),
                ('search_limit', models.IntegerField(default=0, help_text='search limit for the subscription')),
                ('searches_completed', models.IntegerField(default=0, help_text='searches completed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_subscription', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-searches_completed',),
            },
        ),
    ]