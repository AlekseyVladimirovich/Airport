from django.shortcuts import render
from .models import Arriving

def arriving(request):
	posts = Arriving.objects.filter(status__iexact='arriving')
	return render(request, 'arriving/arriving_html.html',context = {'posts': posts})
