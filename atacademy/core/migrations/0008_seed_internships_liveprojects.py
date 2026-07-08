from django.db import migrations


def seed_data(apps, schema_editor):
    Internship = apps.get_model('core', 'Internship')
    LiveProject = apps.get_model('core', 'LiveProject')

    # Only seed if empty (avoid duplicates on repeated migrations)
    if not Internship.objects.exists():
        Internship.objects.bulk_create([
            Internship(
                name='Priya Sharma',
                role='Software Engineering Intern',
                company='Google',
                course='Full Stack Development',
                description='Completed a 6-month internship at Google working on cloud-based web applications. Gained hands-on experience with React, Node.js, and Google Cloud Platform.',
                intern_image_url='https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&crop=face',
                company_logo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/200px-Google_2015_logo.svg.png',
                order=1,
            ),
            Internship(
                name='Rahul Verdata',
                role='Data Analyst Intern',
                company='Microsoft',
                course='Data Science',
                description='Worked with the Azure data analytics team to build dashboards and predictive models. Utilized Python, SQL, and Power BI for data visualization.',
                intern_image_url='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop&crop=face',
                company_logo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/200px-Microsoft_logo.svg.png',
                order=2,
            ),
            Internship(
                name='Sneha Patel',
                role='Cyber Security Intern',
                company='Amazon',
                course='Cyber Security',
                description='Assisted the security team in vulnerability assessments and penetration testing. Learned about AWS security services and compliance frameworks.',
                intern_image_url='https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200&h=200&fit=crop&crop=face',
                company_logo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/200px-Amazon_logo.svg.png',
                order=3,
            ),
            Internship(
                name='Amit Kumar',
                role='Cloud Engineer Intern',
                company='Infosys',
                course='Cloud Computing',
                description='Deployed and managed cloud infrastructure on AWS and Azure. Gained experience with Docker, Kubernetes, and CI/CD pipelines.',
                intern_image_url='https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200&h=200&fit=crop&crop=face',
                company_logo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Infosys_logo.svg/200px-Infosys_logo.svg.png',
                order=4,
            ),
        ])

    if not LiveProject.objects.exists():
        LiveProject.objects.bulk_create([
            LiveProject(
                title='E-Commerce Platform',
                client='RetailHub',
                description='A full-stack e-commerce solution with payment integration, inventory management, and admin dashboard. Built for a mid-size retail business.',
                tech_stack='Python, Django, React, Stripe',
                duration='3 months',
                image_url='https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&h=400&fit=crop',
                order=1,
            ),
            LiveProject(
                title='Healthcare Dashboard',
                client='MedCare',
                description='Real-time patient monitoring dashboard with appointment scheduling, medical records management, and telemedicine integration.',
                tech_stack='Python, Django, Vue.js, PostgreSQL',
                duration='4 months',
                image_url='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600&h=400&fit=crop',
                order=2,
            ),
            LiveProject(
                title='Student Management System',
                client='EduTech',
                description='End-to-end student lifecycle management covering admissions, attendance, grades, fee management, and parent communication portal.',
                tech_stack='Python, Django, Bootstrap, MySQL',
                duration='2 months',
                image_url='https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=600&h=400&fit=crop',
                order=3,
            ),
        ])


def reverse_seed(apps, schema_editor):
    Internship = apps.get_model('core', 'Internship')
    LiveProject = apps.get_model('core', 'LiveProject')
    Internship.objects.filter(company__in=['Google', 'Microsoft', 'Amazon', 'Infosys']).delete()
    LiveProject.objects.filter(client__in=['RetailHub', 'MedCare', 'EduTech']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_internship_liveproject'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
