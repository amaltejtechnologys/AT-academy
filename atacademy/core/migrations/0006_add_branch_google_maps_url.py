from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_course_brochure_brochurerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='google_maps_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
