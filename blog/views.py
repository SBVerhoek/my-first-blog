from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'posts': posts})

def about(request,):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/about.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            #post.docfile = request.FILES.get('Title_image', None)
            #post.h1image = request.FILES.get('First_paragraph_image', None)
            #post.subtitle = request.Post.get('subtile', None)
            #post.intro = request.Post.get('intro', None)
            #post.h1 = request.Post.get('h1', None)
            #post.h1date = request.Post.get('h1date', None)
            #post.h1text = request.Post.get('h1text', None)

            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        documents = Document.objects.all()
    return render(request, 'blog/post_edit.html', {'documents': documents, 'form': form})
        # Handle file upload


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_new2():
    me = User.objects.get(username='s155185')
    post = Post.objects.create(author=me, text=textvalue)
    return redirect('post_detail', pk=post.pk)
                #return redirect('post_detail', pk=post.pk)

            #form = PostForm()
        #return render(request, 'blog/post_edit.html', {'form': form})
def document_list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            #return render(request, 'blog/document_list.html', {'documents': documents, 'form': form})
            return HttpResponseRedirect(reverse('document_list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'blog/post_list.html', {'documents': documents, 'form': form, 'posts':posts})
    #return render_to_response(
    #    'blog/base.html',
    #    {'documents': documents, 'form': form},
    #    context_instance=RequestContext(request)
    #)
