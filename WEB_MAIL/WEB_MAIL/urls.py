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
    path('', views.acceuil, name="acceuil"),
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
#******************************Fin URLS Fifi*************************************
]
