from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SnippetForm
from .models import Snippet


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


@login_required
def edit_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)

    if snippet.author == request.user:
        if request.method == 'POST':
            form = SnippetForm(instance=snippet, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('snippet_detail', snippet_id=snippet.id)
        else:
            form = SnippetForm(instance=snippet)
        return render(request, 'new-snippet.html', {'form':form})
    else:
        raise PermissionDenied


@login_required
def delete_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)

    if snippet.author == request.user:
        snippet.delete()
        messages.success(request, 'Your snippet was deleted successfully!')
        return redirect('home')
    else:
        raise PermissionDenied
