from django.urls import path
from blog.views import views, views_users

urlpatterns = [
    path('', views.home,name='home'),
    path('demo/',views.demo,name='demo'),
    path('blog/',views.blog,name='blog'),

    path('<str:slug>',views.single,name='single'),
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
    

]