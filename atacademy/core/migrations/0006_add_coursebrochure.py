import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_all_additions'),
    ]

    operations = [
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
