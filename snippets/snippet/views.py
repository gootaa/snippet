from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SnippetForm
from .models import Snippet
from django.core.exceptions import PermissionDenied


@login_required
def new_snippet(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			snippet = form.save(commit=False)
			snippet.author = request.user
			snippet.save()
			return redirect('snippet_detail', snippet_id=snippet.id)
	else:
		form = SnippetForm()
	return render(request, 'new-snippet.html', {'form':form})


def snippet_detail(request, snippet_id):
	snippet = get_object_or_404(Snippet, id=snippet_id)
	if snippet.exposure == 'public' or snippet.author == request.user:
		return render(request, 'snippet-detail.html', {'snippet':snippet})
	else:
		raise PermissionDenied







