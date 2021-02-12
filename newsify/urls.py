from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from core.views import signup
from story.views import frontpage, submit, newest, vote, story, search

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('submit/', submit, name='submit'),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('s<int:story_id>/vote/', vote, name='vote'),
    path('s<int:story_id>/', story, name='story'),

    path('u/', include('userprofile.urls')),
]
