
# 📧 Projet Webmail — Installation & Démarrage

## 1️⃣ Prérequis

* **Python 3.10+** installé

  * Windows : `python --version`
  * Linux : `python3 --version`
* **pip** installé

  * Windows : `pip --version`
  * Linux : `pip3 --version`
* **Git** (optionnel mais recommandé)

---

## 2️⃣ Récupérer le projet

Depuis GitHub :

```bash
git clone <url-du-repo>
cd PROJET-FIN-ANNEE-M1
```

Sinon, créez un dossier :

* **Windows (PowerShell)**

  ```powershell
  cd C:\Users\<username>\Documents\PROJET-FIN-ANNEE-M1
  ```

* **Linux (bash)**

  ```bash
  mkdir -p ~/Documents/PROJET-FIN-ANNEE-M1
  cd ~/Documents/PROJET-FIN-ANNEE-M1
  ```

---

## 3️⃣ Créer un environnement virtuel

* **Windows**

  ```powershell
  python -m venv venv
  venv\Scripts\activate
  ```

* **Linux/macOS**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

👉 Vous devez voir `(venv)` devant votre invite de commande.

---

## 4️⃣ Installer Django et les dépendances

Si `requirements.txt` existe déjà :

```bash
pip install -r requirements.txt
```

Sinon installez manuellement Django + PostgreSQL driver :

```bash
pip install django psycopg2-binary
```

---

## 5️⃣ Créer la structure du projet Django

Si le projet **n’existe pas encore** :

```bash
django-admin startproject WEB_MAIL .
python manage.py startapp Appli_WEB_Mail
```

👉 Après ça, tu obtiendras la structure suivante :

```
PROJET-FIN-ANNEE-M1/
│── venv/                  # environnement virtuel
│── WEB_MAIL/              # projet Django
│   ├── Appli_WEB_Mail/    # ton app principale
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
│── requirements.txt
│── db.sqlite3             # si tu utilises SQLite
```

---

## 6️⃣ Lancer le serveur

```bash
python manage.py runserver   # Windows
python3 manage.py runserver  # Linux/macOS
```

👉 Accéder à [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 7️⃣ Migrer la base de données

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 8️⃣ Créer un superutilisateur

```bash
python manage.py createsuperuser
```

👉 Puis accéder à l’admin :
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 9️⃣ Ajouter une nouvelle dépendance

Exemple :

```bash
pip install djangorestframework
pip freeze > requirements.txt
```



Remarque : à Chaque fois que vous cloner, supprimer le venv et recréer le en ajoutant les dependances dans requirment.txt
Supprimer le venv à chaque clone et reinstalle le avec requirement.txt 
