from django.urls import path

from decider import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:campaign_code>', views.campaign, name='campaign'),
    path('vote/<int:item_id>/<slug:vote_val>', views.vote, name='vote'),
    path('add/<int:camp_id>', views.add_item, name='add'),
    path('clear/<int:item_id>', views.clear_vote, name='clear_vote'),
]
