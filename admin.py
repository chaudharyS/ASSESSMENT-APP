from django.contrib import admin
from  assessment.models import Customer, Template, Answer, Category, Question, Response
# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ("order", "category")
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name","template")
    search_fields = ["customer_name"]
#    change_form_template = "admin/template_button.html"

class TemplateAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    search_fields = ["name"]
    inlines=[CategoryInline, QuestionInline]

class AnswerBaseInline(admin.StackedInline):
    fields = ("question", "body")
    readonly_fields = ("question",)
    extra = 0
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("interview_uuid", "template", "created", "user")
    list_filter = ("template", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ("template", "created", "updated", "interview_uuid", "user")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Template,TemplateAdmin)
admin.site.register(Response, ResponseAdmin)
