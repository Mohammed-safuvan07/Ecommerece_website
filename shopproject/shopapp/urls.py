from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'shopapp'
urlpatterns = [

    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodetail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)