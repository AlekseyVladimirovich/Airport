from django.shortcuts import render
from arriving.models import Arriving
def thedetainees(request):
	posts = Arriving.objects.filter(status__iexact='thedetainees')
	return render(request, 'thedetainees/thedetainees_html.html', context = {'posts': posts})
