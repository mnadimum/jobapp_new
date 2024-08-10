from django.contrib import admin
from app.models import JobPost, Location, Author,Skills

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = [ 'id','title', 'date', 'description', 'salary', '__str__']
    list_filter = ['date', 'title', 'salary', 'expiry']
    search_fields = ['title', 'date', 'salary']
    search_help_text = "Write your query here and hit enter"
    #fields = (('title', 'description'), 'expiry')
    #exclude = ('title',)
    fieldsets = (
        ('Basic information', {
            'fields': ('title', 'description')
        }),
        ('More Information', {
            'classes': ('collapse',),
            'fields': ('salary', 'expiry','slug')
        }),
    )
    
    


# created empty class
    

admin.site.register(JobPost)
#admin.site.register(JobPost, JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)






