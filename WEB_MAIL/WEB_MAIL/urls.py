"""
URL configuration for WEB_MAIL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Appli_WEB_Mail import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌐 Pages HTML
    path('', views.base, name="base"),
    path('acceuil/', views.accueil, name="acceuil"),
    path('inbox/page/', views.inbox_page, name="inbox_page"),
    path('sent/page/', views.sent_page, name="sent_page"),
    path('drafts/page/', views.drafts_page, name="drafts_page"),
    path('scheduled/page/', views.scheduled_page, name="scheduled_page"),
    path('archive/page/', views.archive_page, name="archive_page"),
    path('trash/page/', views.trash_page, name="trash_page"),
    path('email/page/', views.email_detail_page, name="email_detail_page"),

    # 🧠 API (pour Postman)
     path('search/', views.search_view, name='search_page'),
    path('inbox/', views.inbox_api, name="inbox_api"),
    path('inbox/unread_count/', views.unread_count_api, name="unread_count_api"),
    path('sent/<str:user_id>/', views.sent_api, name="sent_api"),
    path('drafts/<str:user_id>/', views.drafts_api, name="drafts_api"),
    path('scheduled/<str:user_id>/', views.scheduled_api, name="scheduled_api"),
    path('archive/<str:user_id>/', views.archive_api, name="archive_api"),
    path('trash/<str:user_id>/', views.trash_api, name="trash_api"),
    path('toggle_read/<int:message_id>/', views.toggle_read_status_api, name="toggle_read_status_api"),

]


   
# Fonctionnalité	                    Méthode HTTP	URL à tester dans Postman
# Inbox (boîte Principale)	            GET	            http://127.0.0.1:8000/inbox/
# Nombre de messages non lus	        GET	            http://127.0.0.1:8000/inbox/unread_count/
# Messages envoyés d’un utilisateur	    GET	            http://127.0.0.1:8000/sent/<user_id>/ → exemple : http://127.0.0.1:8000/sent/U001/
# Brouillons d’un utilisateur	        GET	            http://127.0.0.1:8000/drafts/<user_id>/
# Messages planifiés	                GET	            http://127.0.0.1:8000/scheduled/<user_id>/
# Messages archivés	                    GET	            http://127.0.0.1:8000/archive/<user_id>/
# Messages corbeille	                GET	            http://127.0.0.1:8000/trash/<user_id>/
# Marquer un message comme lu/non lu	POST ou GET	    http://127.0.0.1:8000/toggle_read/<message_id>/ → exemple : http://127.0.0.1:8000/toggle_read/M001/
#******************************Fin URLS Fifi*************************************

