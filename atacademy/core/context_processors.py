from datetime import date
from .models import (
    SiteSettings, NavigationItem, FooterLinkGroup, SearchedTerm,
    Course, Branch, Certification, HiringPartner,
)


def site_context(request):
    settings = SiteSettings.load()
    return {
        'settings': settings,
        'current_year': date.today().year,
        'nav_items': NavigationItem.objects.all(),
        'footer_groups': FooterLinkGroup.objects.prefetch_related('links').order_by('order'),
        'searched_terms': SearchedTerm.objects.all(),
        'nav_courses': Course.objects.all().order_by('order'),
        'nav_branches': Branch.objects.all().order_by('order'),
        'certifications': Certification.objects.all().order_by('order'),
        'hiring_partners': HiringPartner.objects.all().order_by('order'),
    }
