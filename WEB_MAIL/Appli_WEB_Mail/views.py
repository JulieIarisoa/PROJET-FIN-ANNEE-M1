from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Message, Utilisateur
#**************************************View FIFI************************
# ------------------------------
# 📩 Boîte de réception (Inbox)
# ------------------------------
def inbox_view(request):
    """
    Retourne tous les messages de la boîte de réception (catégorie = Principale).
    On peut filtrer par lu/non lu côté front si nécessaire.
    """
    messages = Message.objects.filter(categorie='Principale').values()
    return JsonResponse(list(messages), safe=False)


def unread_count_view(request):
    """
    Retourne le nombre de messages non lus (est_lu = False).
    Sert pour les notifications (badge sur l'icône mail).
    """
    unread = Message.objects.filter(est_lu=False, categorie='Principale').count()
    return JsonResponse({"unread_count": unread})


# ------------------------------
# 📨 Messages envoyés
# ------------------------------
def sent_view(request, user_id):
    """
    Retourne la liste des messages envoyés par un utilisateur précis.
    """
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    sent_messages = Message.objects.filter(expediteur=expediteur).values()
    return JsonResponse(list(sent_messages), safe=False)


# ------------------------------
# 📝 Brouillons
# ------------------------------
def drafts_view(request, user_id):
    """
    Retourne les brouillons d’un utilisateur.
    """
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    drafts = Message.objects.filter(expediteur=expediteur, status='Brouillons').values()
    return JsonResponse(list(drafts), safe=False)


# ------------------------------
# ⏰ Messages planifiés
# ------------------------------
def scheduled_view(request, user_id):
    """
    Retourne les messages planifiés pour un utilisateur.
    """
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    scheduled = Message.objects.filter(expediteur=expediteur, status='Planifié').values()
    return JsonResponse(list(scheduled), safe=False)


# ------------------------------
# 📂 Archivage
# ------------------------------
def archive_view(request, user_id):
    """
    Retourne les messages archivés d’un utilisateur.
    """
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    archives = Message.objects.filter(expediteur=expediteur, status='Archiver').values()
    return JsonResponse(list(archives), safe=False)


# ------------------------------
# 🗑️ Corbeille
# ------------------------------
def trash_view(request, user_id):
    """
    Retourne les messages supprimés (corbeille) d’un utilisateur.
    """
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    trash = Message.objects.filter(expediteur=expediteur, status='Corbeille').values()
    return JsonResponse(list(trash), safe=False)


# ------------------------------
# 👁️ Marquer comme lu / non lu
# ------------------------------
def toggle_read_status_view(request, message_id):
    """
    Change le statut "lu / non lu" d’un message.
    """
    try:
        message = Message.objects.get(id_message=message_id)
        message.est_lu = not message.est_lu
        message.save()
        return JsonResponse({"success": True, "est_lu": message.est_lu})
    except Message.DoesNotExist:
        return JsonResponse({"success": False, "error": "Message introuvable"}, status=404)


# ------------------------------
# ✍️ Composer un nouvel email
# ------------------------------
def compose_view(request):
    """
    Affiche la page de composition d'email (formulaire).
    """
    return render(request, 'mail/compose.html')


# ------------------------------
# 📑 Détail d’un email
# ------------------------------
def email_detail_view(request, message_id):
    """
    Affiche le détail d’un message.
    """
    message = get_object_or_404(Message, id_message=message_id)
    return render(request, 'mail/email_detail.html', {"message": message})
#***************************Fin View Fifi*******************************

def acceuil(request):
   return render(request, "accueil.html")

def base(request):
   return render(request, "base.html")

def inbox_view(request):
   return render(request, "inbox.html")

def sent_view(request):
   return render(request, "sent.html")

def drafts_view(request):
   return render(request, "drafts.html")

def scheduled_view(request):
   return render(request, "scheduled.html")

def archive_view(request):
   return render(request, "archive.html")

def trash_view(request):
   return render(request, "trash.html")

def email_detail_view(request):
   return render(request, "email_detail.html")
