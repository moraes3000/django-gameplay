from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AdminTemplateView(TemplateView):
    template_name = "core/base-admin.html"