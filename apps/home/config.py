# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.apps import AppConfig


class MyConfig(AppConfig):
    name = 'apps.home'
    label = 'apps_home'

    def get(self, *args, **kwargs):
        return 'HELLO'
