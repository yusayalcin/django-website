from django.shortcuts import render
#from personal.models import Question
#from account.models import Account
from blog.models import BlogPost
from operator import attrgetter
from blog.views import get_blog_queryset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOG_POSTS_PER_PAGE = 1

def home_screen_view(request):
	#print(request.headers)
	

    context ={}
	#context['some_string']="this is some string that I am passing to the view"
	#context['some_number']=1243242

	#context = {
	#			'some_string': "this is some string that I am passing to the view",
	#			'some_number': 1243242,
	#}

    '''
	list_of_values= []
	list_of_values.append("first entry")
	list_of_values.append("second entry")
	list_of_values.append("third entry")
	list_of_values.append("fourth entry")
	context['list_of_values'] = list_of_values
	'''

	#questions = Question.objects.all()
	#context["questions"]= questions

    #accounts = Account.objects.all()
    #context['accounts'] = accounts

    context = {}

    query = ""
    if request.GET:
       query = request.GET.get('q','')
       context['query'] = str(query)


    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)


    #####Pagination
    page = request.GET.get('page',1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
    	blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
    	blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
    	blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts


    return render(request, "personal/home.html", context)