# Generated by Django 4.2.16 on 2024-12-17 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="hr",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_posts",
                to="users.user",
            ),
        ),
        migrations.AddField(
            model_name="jobpost",
            name="industry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobs.industry"
            ),
        ),
        migrations.AddField(
            model_name="jobpost",
            name="wilaya",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobs.wilaya"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="job_post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="jobs.jobpost",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="job_seeker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="users.user",
            ),
        ),
    ]