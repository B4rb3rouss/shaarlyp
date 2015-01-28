#!/usr/bin/env python
# -*- coding:Utf-8 -*- 
# Fichier: shaarlyp.py
# Cree le 09 mai 2014 14:06:25
# -*- coding:Utf-8 -*- 


"""

Auteur :      thuban (thuban@yeuxdelibad.net)  
licence :     GNU General Public Licence

Description :
    Command line tool to deal with shaarli
    http://sebsauvage.net/wiki/doku.php?id=php:shaarli

    Requiert python3-requests

    usage : shaarlyp <login> <password> <shaarli adress> <url>

"""
try:
    import re
    import requests
    import sys
    import datetime
except ImportError as err:
        print ("Ne peut pas charger {0}".format(err)) 
        print("Ce programme nécessite le module requests.\
            Sous debian, installez le paquet python3-requests")
        sys.exit(2)

def help():
    print("utilisation: ")
    print('{0} <identifiant> <mot de passe> "<adresse de votre shaarli>"\
 "<url>" "<titre>" <privé (0 ou 1) "<tags>" "<description>"'.format(sys.argv[0]))
    print("seuls les 4 premiers paramètres sont obligatoires")
    print('astuce : utiliser des "" autour de l\'url et des paramètres en cas\
 d \'espaces')
    sys.exit(1)

def main():
    if len(sys.argv) < 5:
        help()
    else:
        login = sys.argv[1]
        password = sys.argv[2]
        shaarli = sys.argv[3]
        url=sys.argv[4]
        title,description,tags,private= "","","",0
        if len(sys.argv) >= 6:
            title=sys.argv[5]
        if len(sys.argv) >= 7:
            if (sys.argv[6] == "0") or (sys.argv[6] == "1"):
                private=int(sys.argv[6])
        if len(sys.argv) >= 8:
            tags=sys.argv[7]
        if len(sys.argv) == 9:
            description=sys.argv[8]
        print(login,password,shaarli,url,title,description,tags,private)
        print("On partage {}".format(url))

    s = requests.session()

    # retrieve token
    r = s.get('{0}/?do=login'.format(shaarli), verify=False)
    a = re.search(r'(?<=token" value=")(.*)(?=">)',r.text)
    token = a.group()

    # login
    print("On s'authentifie")
    pl = {'login': login,'password': password,'token': token }
    r = s.post('{0}/?do=login'.format(shaarli), data=pl, verify=False)
    if r.status_code == 200:
        print("authentification réussie \o/")
    else:
        print("authentification échouée :( ")
        return 1

    print("On poste le lien")
    r = s.get('{0}/?post={1}'.format(shaarli,url), verify=False)
    a = re.search(r'(?<=token" value=")(.*)(?=">)',r.text)
    token = a.group()

    now = datetime.datetime.now()
    date = now.strftime("%Y%m%d_%H%M%S")

    d = { 'lf_url': url,
            'lf_title': title,
            'lf_description': description,
            'lf_tags': tags ,
            'lf_linkdate': date,
            'save_edit': "Save",
            'token': token
            }
    if private == 1:
        print("C'est un lien privé")
        d['lf_private'] = private

    r = s.post('{0}/?post={1}'.format(shaarli,url), data=d, verify=False)

    if r.status_code == 200:
        print("Lien ajouté \o/")
    else:
        print("Problème lors de l'ajout du lien :( ")
        return 1


    return 0

if __name__ == '__main__':
	main()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

