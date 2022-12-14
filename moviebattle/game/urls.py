from django.urls import path

from . import views


urlpatterns = [
    path('run', views.postGame, name='run'),
    path('start', views.index, name='index'),
    path('runAudience', views.postAudienceGame, name='runAudience'),
    path('post', views.runPost, name='post'),
    path('audience', views.postAudience, name='audience'),
    path('changeAudience', views.changeAudienceRounds, name='changeAudience'),
    path('send/<gameId>/', views.GameIndex.as_view(), name='sendGame'),
    path('postMovie', views.postMovie, name='postMovie'),
    path('reload', views.reload, name='reload'),
    path('vote/<gameId>/', views.VoteView.as_view(), name='voteView'),
    path('vote', views.vote, name="vote"),
    path('check', views.checkVotes, name="check"),
    path('checkVote', views.canVote, name="checkVote"),
    path('host/<setId>/', views.HostIndex.as_view(), name="hostIndex"),
    path('postHost', views.postHostGame, name='postHost'),
    path('marketplace', views.marketplaceView, name='marketplace'),
    path('ownsets', views.ownsetsView, name='ownsets')
]