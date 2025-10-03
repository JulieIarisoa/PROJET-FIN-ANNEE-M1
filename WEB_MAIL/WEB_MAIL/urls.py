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

      # 🏠 Page d'accueil
    path('', views.base, name="base"),

    # 🏠 Page d'accueil
    path('acceuil/', views.acceuil, name="acceuil"),
    
#*********************************URLS Fifi*************************************
    # 📩 Inbox
    path('inbox/', views.inbox_view, name="inbox"),
    path('inbox/unread_count/', views.unread_count_view, name="unread_count"),

    # 📨 Messages envoyés
    path('sent/<int:user_id>/', views.sent_view, name="sent"),

    # 📝 Brouillons
    path('drafts/<int:user_id>/', views.drafts_view, name="drafts"),

    # ⏰ Planifiés
    path('scheduled/<int:user_id>/', views.scheduled_view, name="scheduled"),

    # 📂 Archivés
    path('archive/<int:user_id>/', views.archive_view, name="archive"),

    # 🗑️ Corbeille
    path('trash/<int:user_id>/', views.trash_view, name="trash"),

    # 👁️ Marquer comme lu/non lu
    path('toggle_read/<int:message_id>/', views.toggle_read_status_view, name="toggle_read"),

    # ✍️ Composer un nouveau message
    path('compose/', views.compose_view, name="compose"),

    # 📑 Détail d’un email
    path('email/<int:message_id>/', views.email_detail_view, name="email_detail"),

   
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
]
