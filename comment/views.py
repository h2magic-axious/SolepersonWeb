from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from blogapp.models import Article
from comment.forms import BlogCommentForm

@require_POST
def comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = BlogCommentForm(request.POST)

    if form.is_valid():
        c = form.save(commit=False)
        c.article = article
        c.save()
        return redirect(article)

    return render(request, 'comment/preview.html', context={
        'article_item': article,
        'form': form
    })
