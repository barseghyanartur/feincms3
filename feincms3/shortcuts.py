"""
For me, the most useful part of Django's generic class based views is
the template name generation and the context variable naming for list
and detail views, and maybe later also the pagination.

The rest of the CBV is less flexible than I'd like them to be, i.e.
integrating forms on detail pages can be a hassle.

Because of this, ``render_list`` and ``render_detail``.
"""

from __future__ import unicode_literals

from django.shortcuts import render


__all__ = ('render', 'render_list', 'render_detail')


def template_name(model, template_name_suffix):
    return '%s/%s%s.html' % (
        model._meta.app_label,
        model._meta.model_name,
        template_name_suffix,
    )


def render_list(request, queryset, context, template_name_suffix='_list'):
    context.update({
        'object_list': queryset,
        '%s_list' % queryset.model._meta.model_name: queryset,
    })
    return render(
        request,
        template_name(queryset.model, template_name_suffix),
        context,
    )


def render_detail(request, object, context, template_name_suffix='_detail'):
    context.update({
        'object': object,
        object._meta.model_name: object,
    })
    return render(
        request,
        template_name(object, template_name_suffix),
        context,
    )