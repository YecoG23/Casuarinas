from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Buzon


class HomeTemplateView(TemplateView):
	template_name = "index.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['list_buzones'] = Buzon.objects.all()
		print(Buzon.objects.all())
		return context