from django.urls import path
from .views import index,test,profile,get_post,search,sign_up,profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as av
urlpatterns = [
    path('',index,name='home'),
    path('test',test,name='test'),
    path('profile',profile,name='profile'),
    path('logout/',av.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('blog/<str:post_name>/<int:post_id>',get_post,name='get_post'),
    path('search/',search,name='search'),
    path('signup/',sign_up,name='signup'),
    path("login/",av.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path('profile/',profile,name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
