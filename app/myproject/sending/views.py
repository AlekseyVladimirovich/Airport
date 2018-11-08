from django.shortcuts import render
from arriving.models  import Arriving

def sending(request):
	posts = Arriving.objects.filter(status__iexact='departure')
	return render(request, 'sending/sending_html.html', context = {'posts': posts})


