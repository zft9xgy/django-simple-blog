from django.urls import path
from blog.views import views, views_users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('demo/',views.demo,name='demo'),
    path('blog/',views.blog,name='blog'),
    path('robots.txt',views.robots),
   
    path('create-single/',views.createSingle,name='create-single'),
    path('delete-single/<str:slug>',views.deleteSingle,name='delete-single'),
    path('edit-single/<str:slug>',views.editSingle,name='edit-single'),

    path('tag/<str:slug>',views.tagView,name='tag-view'),
    path('create-tag/',views.createTag,name='create-tag'),
    path('delete-tag/<str:slug>',views.deleteTag,name='delete-tag'),
    path('edit-tag/<str:slug>',views.editTag,name='edit-tag'),

    path('dj-admin/',views.adminPanel,name='admin-panel'),

    path('login/',views_users.userLogin,name='user-login'),
    path('logout/',views_users.userLogout,name='user-logout'),
    path('register/',views_users.userRegister,name='user-register'),
    path('edit-profile/',views_users.userEditProfile,name='user-edit-profile'),
    path('profile/<str:username>',views_users.userPublicProfile,name='user-public-profile'),
    path('profiles/',views_users.listProfiles,name='profiles-listing'),


    # this view is for post single entries and its on the last position to avoid urls resolve conflict
    path('<str:slug>',views.single,name='single'),


    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)