from django.shortcuts import render


def home(request):
    course_names = [
        'Database Management Systems',
        'Operating Systems',
        'Web Technologies',
        'Computer Networks',
        'Software Engineering',
    ]

    return render(
        request,
        'students/home.html',
        {'course_names': course_names}
    )


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    return render(request, 'students/contact.html')
