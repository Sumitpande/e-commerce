# Generated by Django 3.0.8 on 2020-07-15 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200715_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='blisting_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidlist', to='auctions.Listing'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='buyer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='clisting_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.Listing'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commenters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='watchuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='wlisting_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.Listing'),
        ),
    ]