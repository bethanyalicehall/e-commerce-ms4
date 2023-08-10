from django.views import generic
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import Form, FormComment


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/all_posts.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


@login_required
def add_post(request):
    """
    Add a new post to the blog
    """
    # Ensures only admin can add new post
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        blog_form = Form(request.POST, request.FILES)
        if blog_form.is_valid():
            # Create Blog object but don't save to database yet
            blog = blog_form.save()
            messages.success(request, 'Successfully posted your blog.')
        else:
            messages.error(request, 'Failed to add the blog. \
                           Please ensure the form is valid.')

    else:
        blog_form = Form()

    template = 'blog/add_post.html'
    context = {
        'blog_form': blog_form,
    }

    return render(request, template, context)

