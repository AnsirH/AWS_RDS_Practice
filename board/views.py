from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.
def board_lists(request):
    posts = Post.objects.order_by("-created_at") # -: 내림차순
    return render(request, "board/lists.html", {"posts": posts})

def board_new(request):
    if request.method == "POST":
        Post.objects.create(title=request.POST["title"], content=request.POST["content"])
        return redirect("board_lists")
    return render(request, "board/new.html")

def board_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("board_lists")
    return render(request, "board/update.html", {"post": post})

def board_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("board_lists")
    
    return render(request, "board/delete.html", {"post": post})