from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
# from django.http import Http404

# Create your views here.
# Retrieving all the posts with published status.
def post_list(request):
    posts = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    
    return render (
        request,
        'blog/post/list.html',
        {'posts' : posts}
    )

# Displays a single post.
# 1st way.
# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
    
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post' : post})

# 2nd way.
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                 {'post' : post})