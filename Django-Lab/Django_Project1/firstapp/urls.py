from django.urls import path  # type: ignore[import-untyped]
from . import views  # type: ignore[import-untyped]
urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('hello-class/', views.HelloWorldView.as_view(), name='hello_world_class'),  # type: ignore[attr-defined]
]