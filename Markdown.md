# MArkdown
Je me suis déplacée vers le répertoir où le dossier existe : Documents - 
cd documents

J'ai créé un référentiel git vide
git init


#J'ai ajouté l'ensemble des fichiers scripts dans le dossier dédié (Fonction), j'ai donc ajouté le dossier Fonction
#Etant donné que j'ai zipé l'ensemble des scripts dans un dossier Fonctions et j'ai regroupé les scripts dans un dossier Fonctions normal
#La commande ci-dessous a ajouter les deux dossiers Fonctions (le normal et le zip)
git add Fonctions

#Pour vérifier l'ensemble des fichiers en instance d'etre commit, j'ai utilisé:
git status

#Pour ajouter cette tache réalisée et la nommée
git commit -m "Ajout des quatre scripts implémentés"

#Ensuite, j'ai rajouté au répertoire MArdistant la tache réalisée
git remote add github https://github.com/LoubnaKHENNOU/MArkdown.git

#Pour lister l'ensemble des repository distant, j'ai utilisé
git remote -v

#Enfin, j'ai uploadé les fichiers sur le répertoire distant choisi, dans ce cas MArkdown
git push -u github master

