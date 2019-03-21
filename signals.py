# -*- coding: utf-8 -*-

import django.dispatch

template_completed = django.dispatch.Signal(providing_args=["instance", "data"])

