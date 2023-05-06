from .models import Course 
# BASE VIEW CLass = VIEW


class CourseDeleteView(View):
    template_name = "courses/course_delete.html" # DetailView
class CourseObjectMixin:
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            return get_object_or_404(self.model, id=id)
        return None


from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class CourseDeleteView(CourseObjectMixin, DeleteView):
    model = Course
    template_name = "courses/course_delete.html"
    success_url = reverse_lazy('course-list')



from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, FormView
from .forms import CourseForm

class CourseUpdateView(CourseObjectMixin, UpdateView):
    model = Course
    template_name = "courses/course_update.html"
    form_class = CourseForm
    success_url = reverse_lazy('course-list')

class CourseUpdateFormView(CourseObjectMixin, FormView):
    template_name = "courses/course_update.html"
    form_class = CourseForm
    success_url = reverse_lazy('course-list')

    def get_initial(self):
        initial = super().get_initial()
        course = self.get_object()
        initial['name'] = course.name
        initial['description'] = course.description
        return initial

    def form_valid(self, form):
        course = self.get_object()
        course.name = form.cleaned_data['name']
        course.description = form.cleaned_data['description']
        course.save()
        return super().form_valid(form)



class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"

    def get(self, request, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})
# HTTP METHODS
from django.http import HttpResponse

def my_fbv(request, *args, **kwargs):
    print(request.method)
    return HttpResponse('Hello, World!')

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Couldn't import Django. Did you forget to activate a virtual environment?") 
    execute_from_command_line()

    

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
"""
WSGI config for trydjango project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango.settings")

application = get_wsgi_application()