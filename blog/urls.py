from django.urls import path

from . import views


handler404 = views.error_404

urlpatterns = [
    path('orders/', views.home, name='home'),
]

#re_path('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),