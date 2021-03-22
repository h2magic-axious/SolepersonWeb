from django.contrib import admin

from program.models import ProgramJournal, ProgramName


# Register your models here.

class ProgramNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'document_url', 'github_url']
    fields = ['name', 'document_url', 'github_url', 'excerpt']


class ProgramJournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'program_name']
    fields = ['title', 'excerpt', 'body', 'program_name']


admin.site.register(ProgramName, ProgramNameAdmin)
admin.site.register(ProgramJournal, ProgramJournalAdmin)
