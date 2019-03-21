from django.views.generic import TemplateView

from assessment.models import Customer, Template

class IndexView(TemplateView):
    template_name = "assessment/assessment.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
