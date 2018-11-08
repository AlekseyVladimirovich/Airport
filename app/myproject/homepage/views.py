from django.shortcuts import render
from arriving.models  import Arriving



def index(request):
	return render(request, 'homepage/startPage.html')


def posts_list_url(request):
	search_query = request.GET.get('search', '')

	if search_query:
		posts = Arriving.objects.filter(boardNumber__icontains=search_query)
		return render(request, 'homepage/basec.html', context = {'posts': posts})
	else:
		return render(request, 'homepage/basec.html')