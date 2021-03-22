from django.urls import path

from program.views import ProgramNameView, ProgramJournalView, ProgramJournalDetail

app_name = 'program'
urlpatterns = [
    path('program/index', ProgramNameView.as_view(), name='program_index'),
    path('program/journal/index/<int:pk>', ProgramJournalView.as_view(), name='program_item'),
    path('program/journal/detail/<int:pk>', ProgramJournalDetail.as_view(), name='program_detail')

]
