from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render
from .models import (
    SiteSettings, NavigationItem, FooterLinkGroup, FooterLink, SearchedTerm,
    Technology, Course, Branch, Programme, Testimonial, SuccessStory,
    HiringPartner, Certification, Blog, GalleryImage,
    Enquiry, CallbackRequest, RecruiterContact, BrochureRequest, CourseBrochure,
    LiveProject, Internship,
)


class ATAdminSite(AdminSite):
    site_header = 'AT Academy Admin'
    site_title = 'AT Academy'
    index_title = 'Dashboard'
    index_template = 'admin/data_export.html'


admin_site = ATAdminSite(name='atacademy_admin')


@admin.register(SiteSettings, site=admin_site)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = (
        ('Basic Info', {'fields': ('site_name', 'tagline')}),
        ('Footer', {'fields': ('phone', 'email', 'address', 'google_maps_url'), 'description': 'These values appear in the footer section of the website.'}),
        ('Home Page Settings', {'fields': ('career_guidance_icon', 'materials_icon', 'interview_prep_icon', 'placement_icon', 'excel_banner'), 'description': 'Upload images for the "Excel with AT Academy" section on the homepage.'}),
        ('Nutshell / Career Services', {'fields': ('nutshell_illustration', 'nutshell_1', 'nutshell_2', 'nutshell_3', 'nutshell_4', 'nutshell_5', 'nutshell_6'), 'description': 'Upload images for the "Career Services in a Nutshell" section on the homepage.'}),
        ('Links', {'fields': ('student_portal_url', 'videos_url')}),
        ('Social Media', {'fields': ('social_media',)}),
        ('Branding', {'fields': ('header_logo', 'footer_logo')}),
    )


@admin.register(NavigationItem, site=admin_site)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ['label', 'href', 'order', 'has_dropdown']
    list_editable = ['order', 'has_dropdown']
    ordering = ['order']


@admin.register(FooterLinkGroup, site=admin_site)
class FooterLinkGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


@admin.register(FooterLink, site=admin_site)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['label', 'group', 'href', 'order']
    list_editable = ['order']
    list_filter = ['group']


@admin.register(SearchedTerm, site=admin_site)
class SearchedTermAdmin(admin.ModelAdmin):
    list_display = ['label', 'href', 'order']
    list_editable = ['order']


@admin.register(Technology, site=admin_site)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


class BrochureInline(admin.TabularInline):
    model = CourseBrochure
    extra = 1


@admin.register(Course, site=admin_site)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'fee', 'duration', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'category']
    list_filter = ['category']
    fields = ['name', 'slug', 'fee', 'duration', 'image', 'image_file', 'description', 'features', 'category', 'order', 'meta_title', 'meta_description', 'technologies']
    inlines = [BrochureInline]


@admin.register(Branch, site=admin_site)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Programme, site=admin_site)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['course', 'institution_name', 'mode', 'duration', 'fee_range', 'order']
    list_editable = ['order']
    list_filter = ['course', 'mode']


@admin.register(Testimonial, site=admin_site)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'order']
    list_editable = ['order']


@admin.register(SuccessStory, site=admin_site)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'order']
    list_editable = ['order']


@admin.register(LiveProject, site=admin_site)
class LiveProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'order']
    list_editable = ['order']


@admin.register(Internship, site=admin_site)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'company', 'order']
    list_editable = ['order']


@admin.register(HiringPartner, site=admin_site)
class HiringPartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Certification, site=admin_site)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Blog, site=admin_site)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'date']
    search_fields = ['title']


@admin.register(GalleryImage, site=admin_site)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']


@admin.register(Enquiry, site=admin_site)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'branch', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at', 'course', 'branch']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone', 'course', 'branch', 'qualification', 'created_at']


@admin.register(CallbackRequest, site=admin_site)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'branch', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone', 'course', 'branch', 'created_at']


@admin.register(RecruiterContact, site=admin_site)
class RecruiterContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'company_name', 'designation', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone', 'company_name', 'designation', 'created_at']


@admin.register(BrochureRequest, site=admin_site)
class BrochureRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at', 'course']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['name', 'email', 'phone', 'course', 'created_at']
