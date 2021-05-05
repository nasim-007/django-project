from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def blog_list(request):

    posts = Post.objects.all()
    
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
       'posts': posts,
       'page_obj': page_obj
    }

    return render(request, 'blog/index.html', context)





def blog_details(request, slug):

    post = Post.objects.get(slug=slug)
    similar_post = post.tags.similar_objects()[:4]
    comments = post.comments.all()

    if request.method == 'POST':
        
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            
            new_comment = comment_form.save(commit=False)
            
            new_comment.post = post
            
            new_comment.save()
            # redirect to a new URL:
            
            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)

    
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        
        comment_form = CommentForm()
    
    
    
    
    context = {
       'post': post,
       'similar_post': similar_post,
       'comments': comments
    }

    return render(request, 'blog/details.html', context)


def search_blog(request):
    
    queryset = Post.objects.all()
    query = request.GET.get('q')
    
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) |
            Q(description__icontains=query)


        ).distinct()
    context = {
        'queryset': queryset,
        'query': query


    }
    return render(request, 'blog/search.html', context)