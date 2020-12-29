from django.contrib import admin
from home.models import Contact,Recruitment,Profile,Enrollment
# Register your models here.
@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinymce.js',)
@admin.register(Recruitment)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinyinject.js',)
admin.site.register(Profile)
admin.site.register(Enrollment)