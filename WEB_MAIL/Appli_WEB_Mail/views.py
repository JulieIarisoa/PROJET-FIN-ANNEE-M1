from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Message, Utilisateur

# ------------------------------
# 📩 API : Boîte de réception
# ------------------------------
from django.shortcuts import render
from django.db.models import Q
from .models import Message

def search_view(request):
    query = request.GET.get("query", "")
    filter_by = request.GET.get("filter", "all")

    if query:
        if filter_by == "subject":
            messages = Message.objects.filter(objet__icontains=query)
        elif filter_by == "sender":
            messages = Message.objects.filter(expediteur_id__icontains=query)
        elif filter_by == "body":
            messages = Message.objects.filter(body__icontains=query)
        else:
            messages = Message.objects.filter(
                Q(objet__icontains=query) |
                Q(expediteur_id__icontains=query) |
                Q(body__icontains=query)
            )
    else:
        messages = Message.objects.all()

    return render(request, "inbox.html", {"messages": messages})

def inbox_api(request):
    categorie = request.GET.get('categorie', 'Principale')
    messages = Message.objects.filter(categorie=categorie).values()
    return JsonResponse(list(messages), safe=False)

def unread_count_api(request):
    unread = Message.objects.filter(est_lu=False, categorie='Principale').count()
    return JsonResponse({"unread_count": unread})

def sent_api(request, user_id):
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    sent_messages = Message.objects.filter(expediteur=expediteur).values()
    return JsonResponse(list(sent_messages), safe=False)

def drafts_api(request, user_id):
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    drafts = Message.objects.filter(expediteur=expediteur, status='Brouillons').values()
    return JsonResponse(list(drafts), safe=False)

def scheduled_api(request, user_id):
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    scheduled = Message.objects.filter(expediteur=expediteur, status='Planifié').values()
    return JsonResponse(list(scheduled), safe=False)

def archive_api(request, user_id):
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    archives = Message.objects.filter(expediteur=expediteur, status='Archiver').values()
    return JsonResponse(list(archives), safe=False)

def trash_api(request, user_id):
    expediteur = get_object_or_404(Utilisateur, id_utilisateur=user_id)
    trash = Message.objects.filter(expediteur=expediteur, status='Corbeille').values()
    return JsonResponse(list(trash), safe=False)

def toggle_read_status_api(request, message_id):
    try:
        message = Message.objects.get(id_message=message_id)
        message.est_lu = not message.est_lu
        message.save()
        return JsonResponse({"success": True, "est_lu": message.est_lu})
    except Message.DoesNotExist:
        return JsonResponse({"success": False, "error": "Message introuvable"}, status=404)

# ------------------------------
# 🌐 Pages HTML
# ------------------------------
def base(request):
    return render(request, "base.html")

def accueil(request):
    return render(request, "accueil.html")

def inbox_page(request):
    return render(request, "inbox.html")

def sent_page(request):
    return render(request, "sent.html")

def drafts_page(request):
    return render(request, "drafts.html")

def scheduled_page(request):
    return render(request, "scheduled.html")

def archive_page(request):
    return render(request, "archive.html")

def trash_page(request):
    return render(request, "trash.html")

def email_detail_page(request):
    return render(request, "email_detail.html")
