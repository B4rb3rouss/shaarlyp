# Shaarlyp - Shaarli en ligne de commande

Un petit outil en ligne de commande pour ajouter des liens à son [shaarli](http://sebsauvage.net/wiki/doku.php?id=php:shaarli). Pour l'utiliser, vous aurez besoin de python-requests. Sous debian, ça s'installe tout seul avec la commande `apt-get install python3-requests`. (oui, python**3**).

Ce qu'il fait? Il vous permet de poster un lien. Voici comment il
s'utilise : 

    python3 shaarlyp.py <identifiant> <mot de passe> <adresse de votre shaarli> <url> <titre> <privé (0 ou 1) <description> <tags>

seuls les 4 premiers paramètres sont obligatoires.

Vous pouvez préciser un titre, une description et des tags. De plus,
vous pouvez poster des liens privés : `0` (ou rien) pour public et `1` pour
privé.


Je vous conseille vivement de mettre des `"` entre chaque champ pour
éviter des erreurs inattendues.

[Page initiale](http://yeuxdelibad.net/Programmation/Shaarlyp.html)
