import django.dispatch 

tags_add = django.dispatch.Signal(providing_args=['instance', 'tags'])
tags_remove = django.dispatch.Signal(providing_args=['instance', 'tags'])
tags_clear = django.dispatch.Signal(providing_args=['instance'])
