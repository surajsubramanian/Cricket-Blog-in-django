from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', PostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('calendars/', views.calendars, name='calendars'),
    path('statistics/', views.statistics, name='statistics'),
    path('announcements/', views.announcements, name='announcements'),
    path('ipl/', views.ipl, name='blog-ipl'),
    path('ipl/purple_cap/', views.purple_cap, name='purple-cap'),
    path('ipl/orange_cap/', views.orange_cap, name='orange-cap'),
    path('ipl/most_successfulteam/', views.most_successfulteam, name='most_successfulteam'),
    path('ipl/bowler_vs_batsman/', views.bowler_vs_batsman, name='bowler_vs_batsman'),
    path('ipl/result_prediction/', views.result_prediction, name='Result-Prediction'),
    path('ipl/toss/', views.toss, name='toss')
]

admin.site.site_header = _("Crictics Administration")
admin.site.site_title = _("Admin")
