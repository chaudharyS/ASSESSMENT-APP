from django.views.generic import TemplateView


class ConfirmView(TemplateView):

    template_name = "assessment/completed.html"

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        context["uuid"] = kwargs["uuid"]
        return context
