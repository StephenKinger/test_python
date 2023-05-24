#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import simpleservice


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(

    # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
    name='simpleservice',

    # la version du code
    version=simpleservice.__version__,

    # Liste les packages à inserer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),

    # votre pti nom
    author="Stephen KINGER",

    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ça implique.
    author_email="",

    # Une description courte
    description="Tool to monitor apache logs and notify on connexions",

    # Une description longue, sera affichee pour presenter la lib
    # Generalement on dump le README ici
    long_description=open('README.md').read(),

    # Vous pouvez rajouter une liste de dependances pour votre lib
    # et même preciser une version. A l'installation, Python essayera de
    # les telecharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ça existe car c'est très utile.
    # install_requires= ,

    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,

    # Une url qui pointe vers la page officielle de votre lib
    url='http://github.com/StephenKinger/privaan',

    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisees est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: WIP",
        "Natural Language :: English",
        "Operating System :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Recruit",
    ],

    install_requires=['mock>=2.0.0','pygtail>=0.7.0','docopt>=0.6.2','requests>=2.12.4', 'tornado'],

    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour creer des commandes, comme "django-admin".
    # Par exemple, si on veut creer la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # cree automatiquement.
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'simpleservice = simpleservice:simpleservice_run',
        ],
    },

    # A fournir uniquement si votre licence n'est pas listee dans "classifiers"
    # ce qui est notre cas
    license="Mappy S.A.",

    # Il y a encore une chiee de paramètres possibles, mais avec ça vous
    # couvrez 90% des besoins
    cmdclass={
        'develop': PostDevelopCommand,
    },

)