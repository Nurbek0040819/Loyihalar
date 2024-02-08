from django.urls import path
from .views import homepageview, AboutView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', homepageview.as_view, name='home'),
]


from django.urls import path
from .views import homepageview, AboutView, korinishView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('korinish/', korinishView.as_view(), name='korinish'),
    path('', homepageview.as_view(), name='home'),


]