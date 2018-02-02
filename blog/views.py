from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from .models import Subject

# Create your views here.
def home(request):
	subjects = Subject.objects.all()
	return render(request, 'blog/home.html', {"subjects" : subjects})

def post(request, subject, category=None, subcategory=None, pk=None):
	subject = Subject.objects.get(url_name=subject)
	posts = Post.objects.filter(subject=subject.pk)
	if posts.count() == 0:
		post = get_object_or_404(Post, pk=pk, subject=subject.pk)
	else:
		if pk==None:
			pk = posts[0].pk
		post = get_object_or_404(Post, pk=pk, subject=subject.pk)

	return render(request, 'blog/post.html', {"posts" : posts, 
											  "post" : post, 
											  "subject" : subject})