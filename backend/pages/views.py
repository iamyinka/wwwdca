from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, FreeTaster
from .forms import FreeTasterForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, "pages/about-us.html")

def courses(request):
    courses = Course.objects.all()
    print(courses)
    context = {
        'courses': courses
    }
    return render(request, "pages/courses.html", context)

def wpe_form(request):
    return render(request, "pages/contact-us.html")

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, "pages/course-detail.html", context)

def contact_us(request):
    return render(request, "pages/contact-us.html")

def enrolment_form(request):
    return render(request, "pages/enrolment-form.html")

def faqs(request):
    return render(request, "pages/faqs.html")

def freetaster(request):
    form = FreeTasterForm()
    if request.method == "POST":
        form = FreeTasterForm(request.POST)
        if form.is_valid():
            freetaster_form = form.save(commit=False)
            email = freetaster_form.email
            course = freetaster_form.course
            freetaster_form.save()
            messages.info(request, "Your free taster request has been submitted successfully! blah blah blah")
            send_mail(
                "Free Taster Confirmation",
                "Thank you for signing up for our free taster!",
                "from@example.com",
                [email],
                fail_silently=False,
            )
            return redirect(course.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "pages/freetaster.html", context)

def work_experience_program(request):
    return render(request, "pages/work-experience.html")