from django.test import RequestFactory, SimpleTestCase
from django_htmx_extras.views.generic import HtmxTemplateView


class TestHtmxTemplateView(HtmxTemplateView):
    template_name = 'template.html'
    htmx_template_name = 'partials/htmx_template.html'


class HtmxTemplateViewTests(SimpleTestCase):
    request_factory = RequestFactory()

    def test_htmx_template_view_uses_htmx_template_for_htmx_request(self):
        request = self.request_factory.get("/")
        request.htmx = True
        view = TestHtmxTemplateView.as_view()(request)
        assert view.template_name == ['partials/htmx_template.html']

    def test_htmx_template_view_uses_template_for_request(self):
        request = self.request_factory.get("/")
        request.htmx = False
        view = TestHtmxTemplateView.as_view()(request)
        assert view.template_name == ['template.html']
