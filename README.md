# django-htmx-extras
Extra functionality for [django-htmx](https://github.com/adamchainz/django-htmx/)

`django-htmx` provides very useful tools to integrate htmz with Django. It does not
include anything related to Django Class Based Views on purpose. `django-htmx-extras` provides *some* additional functionality for CBVs. 

This package is not meant to *complete* `django-htmx` but to extend it.

# Usage

The main functionality of `django-htmx-extras` is found in the `HtmxTemplateResponseMixin` found in `django_htmx_extras.views.generic.base`. This mixin simply inherits the Django `TemplateResponseMixin` and adds a check to identify when a request is an htmx request. This is used to provide a mechanism through which a view can respond with either of two templates. Example:

You have a view that returns a Queryset and renders it into a template. By using htmx, you can request a **template partial** and update the page without reloading. The `HtmxTemplateResponseMixin` provides a way to define what template to return when a request is of type htmx.

```
Template Partials

A template partial is simply a piece of an HTML template that is meant to be included
within another.
```

The library includes multiple htmx enabled CBVs, but does not implement them all. The reason is that I did not have use for them. However, it is straightforward for you to create your own. To do so, create a new class based view and inherit the `HtmxTemplateResponseMixin` and the CBV you wish to extend. Example:

`class HtmxTemplateView(HtmxTemplateResponseMixin, TemplateView):`

Using the provided CBVs does not change any of the underlying Django functionality. Everything works as it should.

The path to import the Htmx CBVs mimics that of Django to make things a little more familiar. 

Instead of `from django.views.generic import TemplateView` you would do `from django_htmx_extras.views.generic import TemplateView`.


# License

MIT

# Requirements

`Django`
`django-htmx`

# Run tests

`python -m pytest --verbose -s`