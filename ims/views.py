# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.conf import settings


import logging
logger = logging.getLogger(__name__)


def home(request):
    context = {
        'ajax_count': settings.AJAX_COUNT,
    }
    return render(request, 'home.html', context)


def ajax_fragment(request, param):
    context = {'param': param}
    logger.info(f'Fetched ajax fragment with param {param}')
    return render(request, 'ajax_fragment.html', context)

