from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import TestCase
from django.test.client import RequestFactory

from misago.core.middleware.exceptionhandler import ExceptionHandlerMiddleware


class ExceptionHandlerMiddlewareTests(TestCase):
    def setUp(self):
        self.request = RequestFactory().get(reverse('misago:index'))
        self.request.preloaded_ember_data = {}

    def test_middleware_returns_response_for_supported_exception(self):
        """Middleware returns HttpResponse for supported exception"""
        exception = Http404()
        middleware = ExceptionHandlerMiddleware()

        self.assertTrue(middleware.process_exception(self.request, exception))

    def test_middleware_returns_none_for_non_supported_exception(self):
        """Middleware returns None for non-supported exception"""
        exception = TypeError()
        middleware = ExceptionHandlerMiddleware()

        self.assertFalse(middleware.process_exception(self.request, exception))
