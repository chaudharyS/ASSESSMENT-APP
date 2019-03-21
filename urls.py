from django.conf.urls import url

from assessment.views import IndexView, TemplateDetail, ConfirmView

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="assessment-list"),
    url(r"^assessment/template/(?P<id>\d+)/", TemplateDetail.as_view(), name="template-detail"),
    url(r"^assessment/confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="template-confirmation"),
]
