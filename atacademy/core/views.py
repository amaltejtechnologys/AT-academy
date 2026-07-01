import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Course, Branch, Testimonial, SuccessStory, Blog, GalleryImage,
    Programme, Technology,
)
from .forms import EnquiryForm, CallbackForm, RecruiterForm


def home(request):
    context = {
        'featured_courses': Course.objects.all().order_by('order')[:4],
        'testimonials': Testimonial.objects.all().order_by('order'),
        'success_stories': SuccessStory.objects.all().order_by('order'),
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
        'categories': Course.objects.values_list('category', flat=True).distinct(),
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
    return render(request, 'discover/gallery.html')


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
    return render(request, 'placements/recruiters.html')


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


@csrf_exempt
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
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


@csrf_exempt
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
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


@csrf_exempt
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
        return JsonResponse({'success': False, 'message': str(e)}, status=500)
