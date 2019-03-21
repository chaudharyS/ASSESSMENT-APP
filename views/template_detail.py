from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from assessment.forms import ResponseForm
from assessment.models import Template, Category

class TemplateDetail(View):
    def get(self, request, *args, **kwargs):
        template = get_object_or_404(Template, id=kwargs["id"])
        template_name = "assessment/template.html"
        context = {"template":template}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        template = get_object_or_404(Template, id=kwargs["id"])
        categories = Category.objects.filter(template=template).order_by("order")
        form = ResponseForm(
            request.POST, template=template, user=request.user, step=kwargs.get("step", 0)
        )
        context = {"response_form": form, "template": template, "categories": categories}
        if form.is_valid():
            session_key = "template_%s" % (kwargs["id"],)
            if session_key not in request.session:
                request.session[session_key] = {}
            for key, value in list(form.cleaned_data.items()):
                request.session[session_key][key] = value
                request.session.modified = True

            next_url = form.next_step_url()
            response = None
            response = form.save()

            if next_url is not None:
                return redirect(next_url)
            else:
                del request.session[session_key]
                if response is None:
                    return redirect("/")
                else:
                    next_ = request.session.get("next", None)
                    if next_ is not None:
                        if "next" in request.session:
                            del request.session["next"]
                        return redirect(next_)
                    else:
                        return redirect(
                            "template-confirmation", uuid=response.interview_uuid
                        )
        template_name = "assessment/template.html"
        return render(request, template_name, context)
