import json
import logging
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_POST
from .models import (
    Course, Branch, Testimonial, SuccessStory, Blog, GalleryImage,
    Programme, Technology, HiringPartner, BrochureRequest, CourseBrochure,
)
from .forms import EnquiryForm, CallbackForm, RecruiterForm

logger = logging.getLogger(__name__)


def home(request):
    context = {
        'featured_courses': Course.objects.all().order_by('order')[:4],
        'testimonials': Testimonial.objects.all().order_by('order'),
        'success_stories': SuccessStory.objects.all().order_by('order'),
        'hiring_partners': HiringPartner.objects.all().order_by('order'),
    }
    return render(request, 'index.html', context)


def course_list(request):
    category = request.GET.get('category', '')
    courses = Course.objects.all().order_by('order')
    if category:
        courses = courses.filter(category=category)
    context = {
        'courses': courses,
        'current_category': category,
        'categories': sorted(set(Course.objects.exclude(category='').values_list('category', flat=True))),
    }
    return render(request, 'course/list.html', context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course,
        'programmes': course.programmes.all().order_by('order'),
        'technologies': course.technologies.all().order_by('order'),
    }
    return render(request, 'course/detail.html', context)


def branch_detail(request, slug):
    branch = get_object_or_404(Branch, slug=slug)
    context = {
        'branch': branch,
        'courses': Course.objects.all().order_by('order'),
    }
    return render(request, 'branch/detail.html', context)


def about(request):
    return render(request, 'discover/about.html')


def contact(request):
    return render(request, 'discover/contact.html')


def gallery(request):
    context = {
        'gallery_images': GalleryImage.objects.all().order_by('order'),
    }
    return render(request, 'discover/gallery.html', context)


def videos(request):
    return render(request, 'discover/videos.html')


def blog_list(request):
    context = {
        'blogs': Blog.objects.all().order_by('-date'),
    }
    return render(request, 'blogs/list.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog': blog}
    return render(request, 'blogs/detail.html', context)


def alumni(request):
    context = {
        'testimonials': Testimonial.objects.all().order_by('order'),
    }
    return render(request, 'placements/alumni.html', context)


def recruiters(request):
    context = {
        'hiring_partners': HiringPartner.objects.all().order_by('order'),
    }
    return render(request, 'placements/recruiters.html', context)


def success_stories(request):
    context = {
        'stories': SuccessStory.objects.all().order_by('order'),
    }
    return render(request, 'success_stories.html', context)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_service(request):
    return render(request, 'terms_of_service.html')


def apply_jobs(request):
    return render(request, 'apply_for_jobs.html')


def find_course(request):
    return render(request, 'find_my_course.html')


def custom_404(request, exception):
    return HttpResponseNotFound(render(request, '404.html').content)


@require_POST
def submit_enquiry(request):
    try:
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        form = EnquiryForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Enquiry submitted successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        logger.exception("Error in submit_enquiry")
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)


@require_POST
def submit_callback(request):
    try:
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        form = CallbackForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Callback request submitted successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        logger.exception("Error in submit_callback")
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)


@require_POST
def submit_recruiter(request):
    try:
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        form = RecruiterForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Contact submitted successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        logger.exception("Error in submit_recruiter")
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)


@require_POST
def download_brochure(request, slug):
    try:
        course = get_object_or_404(Course, slug=slug)
        data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
        name = data.get('name', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        if not all([name, email, phone]):
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)
        BrochureRequest.objects.create(name=name, email=email, phone=phone, course=course)
        brochures = list(course.brochures.values_list('id', flat=True))
        if brochures:
            return JsonResponse({'success': True, 'brochure_ids': brochures})
        if course.brochure:
            return JsonResponse({'success': True, 'download_url': course.brochure.url})
        return JsonResponse({'success': False, 'message': 'Brochure not available yet.'}, status=404)
    except Exception as e:
        logger.exception("Error in download_brochure")
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)


def download_brochure_file(request, brochure_id):
    try:
        brochure = get_object_or_404(CourseBrochure, id=brochure_id)
        if brochure.file:
            return JsonResponse({'success': True, 'download_url': brochure.file.url})
        return JsonResponse({'success': False, 'message': 'File not available.'}, status=404)
    except Exception as e:
        logger.exception("Error in download_brochure_file")
        return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)
