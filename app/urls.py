from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name='double'),
    path('multiply/', views.MultThree.as_view(), name='multiply'),
    path('earnings/', views.Earnings.as_view(), name='earnings'),
    path('t_or_f/', views.TrueOrFalse.as_view(), name='t_or_f'),
    path('walk_or_drive/', views.WalkOrDrive.as_view(), name='walk_or_drive'),
    path('population/', views.HowPopulated.as_view(), name='population'),
    path('gold_star/', views.GoldStar.as_view(), name='gold_star'),
    path(
        'scoring_action/',
        views.ScoringAction.as_view(),
        name='scoring_action')
]
