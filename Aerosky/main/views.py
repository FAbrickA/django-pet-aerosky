from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

from main.forms import MessageForm


def index(request):
    context = {
        'title': 'Aerosky',
    }
    return render(request, "main/index.html", context)


def page_about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, "main/about.html", context)


def page_services(request):
    context = {
        'title': 'Services'
    }
    return render(request, "main/services.html", context)


def page_price(request):
    context = {
        'title': 'Price',
    }
    return render(request, "main/price.html", context)


def page_projects(request):
    context = {
        'title': 'Projects',
    }
    return render(request, "main/projects.html", context)


def page_contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Message sent successfully!")
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error("Something went wrong. Check if form data is correct.")
    else:
        form = MessageForm(request.POST)

    context = {
        'title': 'Contact',
        'form': form,
    }
    return render(request, "main/contact.html", context)


def page_right_sidebar(request):
    context = {
        'title': 'Right Sidebar',
    }

    return render(request, "main/sidebar-right.html", context)

