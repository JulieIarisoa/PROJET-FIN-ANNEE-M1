# 📧 Projet Webmail — Installation & Démarrage

## 1️⃣ Prérequis

* **Python 3.10+** installé (vérifier avec `python --version`)
* **pip** installé (vérifier avec `pip --version`)
* Git (facultatif mais recommandé)

---

## 2️⃣ Cloner ou créer le projet

Si vous travaillez depuis GitHub :

```powershell
git clone <url-du-repo>
cd projet-webmail
```

Sinon, placez-vous dans le dossier de travail :

```powershell
cd C:\Users\<username>\Documents\projet-webmail
```

---

## 3️⃣ Créer un environnement virtuel

```powershell
python -m venv venv
```

Activer l’environnement :

```powershell
venv\Scripts\activate
```

👉 Vous devez voir `(venv)` devant votre invite de commande.

---

## 4️⃣ Installer les dépendances

Si le fichier `requirements.txt` existe :

```powershell
pip install -r requirements.txt
```

Sinon, installez Django :

```powershell
pip install django
```

---

## 5️⃣ Créer le projet Django (si pas encore fait)

```powershell
python -m django startproject webmail_project
```

---

## 6️⃣ Lancer le serveur

Se placer dans le dossier du projet :

```powershell
cd webmail_project
python manage.py runserver
```

👉 Ouvrir [http://127.0.0.1:8000](http://127.0.0.1:8000) dans un navigateur.
Vous devriez voir la page de bienvenue Django 🎉

---

## 7️⃣ Créer les apps (si pas encore faites)

```powershell
python manage.py startapp accounts
python manage.py startapp mail
```

---

## 8️⃣ Migrer la base de données

Avant la première exécution :

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

## 9️⃣ Créer un superutilisateur (admin)

```powershell
python manage.py createsuperuser
```

👉 Suivre les instructions (nom, email, mot de passe).

Ensuite, accéder à l’admin :
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 10️⃣ Ajouter une dépendance

Si vous ajoutez une nouvelle librairie (ex: `pip install djangorestframework`), n’oubliez pas de mettre à jour `requirements.txt` :

```powershell
pip freeze > requirements.txt
```



Supprimer le venv à chaque clone et reinstalle le avec requirement.txt 
