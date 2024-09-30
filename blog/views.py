from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all()
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments})

@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        category = Category.objects.get(pk=category_id)
        blog = Blog.objects.create(
            title=title, content=content, category=category, author=request.user
        )
        return redirect('blog_detail', pk=blog.pk)
    categories = Category.objects.all()
    return render(request, 'blog/create_blog.html', {'categories': categories})

@login_required
def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        content = request.POST['content']
        author = request.POST['author']
        Comment.objects.create(blog=blog, content=content, author=author)
        return redirect('blog_detail', pk=pk)
    return HttpResponse("Comment could not be added.")
