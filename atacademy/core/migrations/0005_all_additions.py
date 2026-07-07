import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sitesettings_nutshell_1_sitesettings_nutshell_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='google_maps_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='brochure',
            field=models.FileField(blank=True, help_text='PDF brochure for this course', upload_to='brochures/'),
        ),
        migrations.CreateModel(
            name='BrochureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brochure_requests', to='core.course')),
            ],
            options={
                'verbose_name_plural': 'Brochure Requests',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseBrochure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='e.g. Full Stack Python Syllabus 2026', max_length=200)),
                ('file', models.FileField(help_text='PDF brochure', upload_to='brochures/')),
                ('order', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brochures', to='core.course')),
            ],
            options={
                'verbose_name_plural': 'Course Brochures',
                'ordering': ['order'],
            },
        ),
    ]
