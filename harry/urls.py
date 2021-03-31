from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('analyze/',views.analyze,name='analyze'),
    path('about/',views.about,name='aboutus'),
    path('addition/',views.addition,name='add'),
    path('nav/',views.nav,name='nav')


    
    # path('capfirst/',views.capfirst,name='capfirst'),
    # path('newlineremove/',views.newlineremove,name='newlineremove'),
    # path('spaceremove/',views.spaceremove,name='spaceremove'),
    # path('charcount/',views.charcount,name='charcount')
]
