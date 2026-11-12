# Mon premier projet Streamlit

Cette app est hébergée sur **Streamlit Community Cloud**.
Elle permet de vérifier que seuls les comptes présents dans le fichier `accounts.csv` peuvent y avoir accès.

Une fois la connexion autorisée, l'app contient 2 pages visibles dans un menu rétractable à gauche de l'écran :
 - une page d'accueil qui indique que ce contenu n'est accessible qu'aux utilisateurs authentifiés
 - une page de galerie photos qui affiche 3 photos de hiboux

Démo en ligne : [https://app-securisee-test.streamlit.app](https://app-securisee-test.streamlit.app/)

## Installation en local

1. Créer l'environnement virtuel :

    ```bash
    python -m venv venv
    ```

2. Activer l'environnement virtuel (sous Windows avec Git Bash) :

    ```bash
    source venv/Scripts/activate
    ```

3. Installer les dépendances :

    ```bash
    python -m pip install -r requirements.txt
    ```

4. Lancer l'application Streamlit :

    ```bash
    streamlit run app_securisee.py
    ```

## Compte de test et connexion

Pour se connecter, vous pouvez utiliser les ID suivants :
- Nom d'utilisateur : utilisateur
- Mot de passe : mdp123