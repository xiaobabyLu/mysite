from django.contrib import admin
from polls.models import Question,Choice,User
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['question_type']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text','question_type','pub_date' ,'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question,QuestionAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')


admin.site.register(User,UserAdmin)


# admin.site.register(Choice)