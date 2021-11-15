from . import views

urlpatterns = [

    # Empty path shows its root url
    path('', views.view_bag, name='bag')
]