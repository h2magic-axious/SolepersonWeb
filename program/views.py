import markdown
from django.db.models import Q

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render

from program.models import ProgramName, ProgramJournal

from pure_pagination.mixins import PaginationMixin


class ProgramNameView(PaginationMixin, ListView):
    model = ProgramName
    template_name = 'program/programs.html'
    context_object_name = 'program_list'
    paginate_by = 5


class ProgramJournalView(PaginationMixin, ListView):
    model = ProgramJournal
    template_name = 'program/journals.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        c = get_object_or_404(ProgramName, pk=self.kwargs.get('pk'))
        return super(ProgramJournalView, self).get_queryset().filter(program_name=c)


class ProgramJournalDetail(DetailView):
    model = ProgramJournal
    template_name = 'program/detail.html'
    context_object_name = 'journal'

    def get_object(self, queryset=None):
        journal = super(ProgramJournalDetail, self).get_object(queryset=None)
        MARKDOWN = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        journal.body = MARKDOWN.convert(journal.body)
        journal.toc = MARKDOWN.toc
        return journal
