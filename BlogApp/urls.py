from django.urls import path
from .views import loginView,register,welcome,main,logout_view,create,blog,update,delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',loginView,name="login"),
    path('registration',register , name="registration"),
    path('', welcome, name="welcome"),
    path('main', main, name="main"),
    path('logout', logout_view, name="logout"),
    path('create',create,name='create'),
    path('blog/<int:pk>',blog, name='blog'),
    path('update/<int:pk>',update, name='update'),
    path('delete/<int:pk>',delete,name='delete')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)