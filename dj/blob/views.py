from django.shortcuts import render

from blob.forms import CommentsForm
from blob.models import Post, Comments # <==

# мой проект/blob/views.py



def post_list(request):
    posts = Post.objects.all()# <==
    return render(request,
                  'blob/post_list.html',
                  {'posteki':posts})# <==

def post_detail(request, pk):
    this_post = Post.objects.get(id=pk)
    comments = Comments.objects.filter(post=this_post).all()
    if request.method == 'GET':
        form = CommentsForm()
    elif request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = this_post
            comment.save()

    page = render(request,
                  'blob/post_one.html',
                  {'post':this_post,
                   'comments':comments,
                   'form':form})
    return page