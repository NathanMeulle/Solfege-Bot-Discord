
################################################################################
################################################################################
############################## Projet Bot Discord ##############################
################################################################################
################################################################################

#Copyright © 2021 Nathan. All rights reserved.
#@author Nathan
#name : JAC-BOT


from JAC import Bot
from dotenv import load_dotenv
import os


if __name__== "__main__":
    bot = Bot()


    ##TOKEN a indiquer

    # #Directement ci-dessous
    # bot.run("token à indiquer ici")#/!\Token a ne pas communiquer

    # # ou bien dans un fichier config (même répertoire, pas d'extension)
    # # écrire juste
    # # TOKEN=...
    # load_dotenv(dotenv_path="config") # charge le fichier config
    # bot.run(os.getenv("TOKEN"))#/!\Token a ne pas communiquer

    # sur serveur
    bot.run(os.environ("TOKEN"))#/!\Token a ne pas communiquer



