import json
import os
from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import (
    SiteSettings, NavigationItem, FooterLinkGroup, FooterLink, SearchedTerm,
    Course, Branch, Testimonial, HiringPartner, Certification,
)


class Command(BaseCommand):
    help = 'Import data from existing JSON files'

    def add_arguments(self, parser):
        parser.add_argument('data_dir', type=str, help='Path to admin/data directory')

    def handle(self, *args, **options):
        data_dir = options['data_dir']

        def read_json(filename):
            filepath = os.path.join(data_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None

        self.stdout.write('Importing data...')

        # Import Settings
        settings_data = read_json('settings.json')
        if settings_data:
            settings = SiteSettings.load()
            settings.site_name = settings_data.get('siteName', settings.site_name)
            settings.tagline = settings_data.get('tagline', settings.tagline)
            settings.phone = settings_data.get('phone', settings.phone)
            settings.email = settings_data.get('email', settings.email)
            settings.address = settings_data.get('address', settings.address)
            settings.google_maps_url = settings_data.get('googleMapsUrl', settings.google_maps_url)
            settings.student_portal_url = settings_data.get('studentPortal', settings.student_portal_url)
            settings.videos_url = settings_data.get('videosUrl', settings.videos_url)
            settings.social_media = settings_data.get('socialMedia', settings.social_media)
            settings.save()
            self.stdout.write(self.style.SUCCESS('Settings imported'))

        # Import Navigation
        nav_data = read_json('navigation.json')
        if nav_data:
            NavigationItem.objects.all().delete()
            for item in nav_data:
                NavigationItem.objects.create(
                    label=item.get('label', ''),
                    href=item.get('href', ''),
                    order=item.get('order', 0),
                    has_dropdown=item.get('hasDropdown', False),
                )
            self.stdout.write(self.style.SUCCESS('Navigation imported'))

        # Import Footer
        footer_data = read_json('footer.json')
        if footer_data:
            FooterLinkGroup.objects.all().delete()
            SearchedTerm.objects.all().delete()

            for i, group_data in enumerate(footer_data.get('linkGroups', [])):
                group = FooterLinkGroup.objects.create(
                    title=group_data.get('title', ''),
                    order=i,
                )
                for j, link_data in enumerate(group_data.get('links', [])):
                    FooterLink.objects.create(
                        group=group,
                        label=link_data.get('label', ''),
                        href=link_data.get('href', ''),
                        order=j,
                    )

            for i, term in enumerate(footer_data.get('searchedTerms', [])):
                SearchedTerm.objects.create(
                    label=term.get('label', ''),
                    href=term.get('href', '#'),
                    order=i,
                )
            self.stdout.write(self.style.SUCCESS('Footer imported'))

        # Import Courses
        courses_data = read_json('courses.json')
        if courses_data:
            Course.objects.all().delete()
            for item in courses_data:
                Course.objects.create(
                    name=item.get('name', ''),
                    slug=item.get('slug', ''),
                    fee=item.get('fee', ''),
                    duration=item.get('duration', ''),
                    image=item.get('image', ''),
                    description=item.get('description', ''),
                    features=item.get('features', []),
                    category=item.get('category', ''),
                    order=item.get('order', 0),
                )
            self.stdout.write(self.style.SUCCESS('Courses imported'))

        # Import Branches
        branches_data = read_json('branches.json')
        if branches_data:
            Branch.objects.all().delete()
            for item in branches_data:
                Branch.objects.create(
                    name=item.get('name', ''),
                    slug=item.get('slug', ''),
                    address=item.get('address', ''),
                    phone=item.get('phone', ''),
                    order=item.get('order', 0),
                )
            self.stdout.write(self.style.SUCCESS('Branches imported'))

        # Import Testimonials
        testimonials_data = read_json('testimonials.json')
        if testimonials_data:
            Testimonial.objects.all().delete()
            for item in testimonials_data:
                Testimonial.objects.create(
                    name=item.get('name', ''),
                    course=item.get('course', ''),
                    video_url=item.get('videoUrl', ''),
                    order=item.get('order', 0),
                )
            self.stdout.write(self.style.SUCCESS('Testimonials imported'))

        # Import Hiring Partners
        partners_data = read_json('hiringPartners.json')
        if partners_data:
            HiringPartner.objects.all().delete()
            for item in partners_data:
                HiringPartner.objects.create(
                    name=item.get('name', ''),
                    logo=item.get('logo', ''),
                    order=item.get('order', 0),
                )
            self.stdout.write(self.style.SUCCESS('Hiring Partners imported'))

        # Import Certifications
        certs_data = read_json('certifications.json')
        if certs_data:
            Certification.objects.all().delete()
            for item in certs_data:
                Certification.objects.create(
                    name=item.get('name', ''),
                    image=item.get('image', ''),
                    order=item.get('order', 0),
                )
            self.stdout.write(self.style.SUCCESS('Certifications imported'))

        self.stdout.write(self.style.SUCCESS('All data imported successfully!'))
