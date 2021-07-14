from django.views.generic import FormView, UpdateView
from django_htmx_extras.views.generic.base import HtmxTemplateResponseMixin


class HtmxFormView(HtmxTemplateResponseMixin, FormView):
    """
    A view for displaying a form and rendering
    a htmx or regular template response.
    """


class HtmxUpdateView(HtmxTemplateResponseMixin, UpdateView):
    """
    A view for displaying a form and rendering
    a htmx or regular template response to update models
    """
