from django.views import generic
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import Form, CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/all_posts.html'


def PostDetail(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Creates the Comment object
            new_comment = comment_form.save(commit=False)
            # Assigns the post to the comment
            new_comment.post = post
            # Saves the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


@login_required
def add_post(request):
    """
    Add a new post to the blog
    """
    # A message to say that posts can only be added by admin
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        blog_form = Form(request.POST, request.FILES)
        if blog_form.is_valid():
            # Creates the Blog object
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


@login_required
def delete_comment(request, comment_id):
    """
    Admin can delete a comment posted by a user
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, only admin can do that.')
        return redirect(reverse('home'))
    comment = get_object_or_404(Comment, pk=comment_id)
    slug = comment.post.slug
    comment.delete()

    if 'last_item' in request.session:
        del request.session['last_item']

    messages.success(request, 'Successfully deleted your comment.')
    return redirect(reverse('home'))
