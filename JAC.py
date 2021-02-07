################################################################################
################################################################################
############################## Projet Bot Discord ##############################
################################################################################
################################################################################

#Copyright © 2021 Nathan. All rights reserved.
#@author Nathan
#name : JAC-BOT

## Imports
import discord
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
import os
import asyncio
import threading


from gif import init_gif

################################# Bot Discord ##################################

## Création de la classe bot héritant de discord.Client

class Bot(discord.Client):
    # Modifiable :
    delay = 5
    delay_short = 4
    NB_QUESTIONS = 5 # le nombre de questions pour le mode multijoueur


    # Non Modifiable - Initialisation des variables
    listen_for_mode=False
    listen_for_level=False
    listen_for_answer=False
    start_ = False
    hauteur = 0
    niveau = 1
    mode = 1
    t_debut = 0
    t_fin = 0
    players = {}
    questions_counter = 1
    channel = None
    chrono = False
    classement_tmp = []



    #constructeur
    def __init__(self):
        super().__init__()


    def create_im_question(self):
        '''
        Méthode créant l'image avec une note
        '''
        # Configuration
        plt.close('all')## Ferme les fenetres deja ouvertes
        plt.figure("Find the note !", figsize=(6,5))# création de la fenetre avec titre
        plt.axis('off')# pas d'axe
        plt.xlim(-2,6)# Limites des axes
        plt.ylim(-12,20)

        # Création des lignes
        List_x=[k for k in range(5)]# liste des x

        for i in range(5): # création des 5 lignes
            List_y=[2*i for k in List_x]
            plt.plot(List_x, List_y, color="black")

        # Affichage d'une note
        x = 2
        if self.niveau==2:
            y = random.randint(-5,12) # note choisie de facon aléatoire niveau 2 (hors de la portée)
        elif self.niveau==3:
            y = random.randint(-9,19) # note choisie de facon aléatoire niveau 3 (hors de la portée - expert)
            self.delay = self.delay_short #temps plus court
        else :
            y = random.randint(-2,9) # note choisie de facon aléatoire niveau 1 (sur la portée Do-Sol)

        plt.scatter(x, y, s=300, c='black')# cercle de la note

        if(y>4):
            # Note haute, queue vers le bas
            plt.plot([x-0.175,x-0.175], [y, y-6], color="black", linewidth=3)
        else :
            # Note basse, queue vers le haut
            plt.plot([x+0.175,x+0.175], [y, y+6], color="black", linewidth=3)

        # si note en dehors de la portée, on ajoute les lignes
        if y>9 or y<-1:
            tmp = y
            while(tmp<0 or tmp>=9):
                if(y%2==0):
                    plt.plot([x-0.4,x+0.4], [tmp, tmp], color="black")
                    if y>9:tmp-=2
                    else :tmp+=2
                elif (y>4):
                    plt.plot([x-0.4,x+0.4], [tmp-1, tmp-1], color="black")
                    tmp-=2
                elif (y<4):
                    plt.plot([x-0.4,x+0.4], [tmp+1, tmp+1], color="black")
                    tmp+=2

        # Affichage
        plt.title("Find the note !")
        #Affichage de la clé de sol
        image = plt.imread("./images/gkey.png")#Récupère la clé de sol
        ax = plt.gca()
        im = OffsetImage(image, zoom=0.15)
        artists = []
        ab = AnnotationBbox(im, (0.6, 4), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
        self.hauteur = y
        # Enregistrement de l'image
        plt.savefig(os.getcwd() +"/jac_img")

    '''
    Méthode vérifiant la réponse fournie
    '''
    def check_answer(self, res, delay):
        # Réponses
        y=self.hauteur
        notes_values=[]
        for i in range(7):
            notes_values.append([i-2+k*7 for k in range(-1,4)])

        notes = ["do", "ré", "mi", "fa", "sol", "la", "si"]
        norma = {}
        norma["do"]=["do", "Do", "DO", "C", "c"]
        norma["ré"]=["ré", "re", "RÉ", "Ré", "RE", "Re", "D", "d"]
        norma["mi"]=["mi", "Mi", "MI", "E", "e"]
        norma["fa"]=["fa", "Fa", "FA", "F", "f"]
        norma["sol"]=["sol", "Sol", "SOL", "G", "g"]
        norma["la"]=["la", "La", "LA", "A", "a"]
        norma["si"]=["si", "Si", "SI", "B", "b"]

        dict = {}
        for j in range(7):
            dict[notes[j]]=notes_values[j]

        try :
            res=[k  for (k, val) in norma.items() if res in val][0]

            if(y in dict[res] and delay<self.delay):
                return("Bonne réponse !\n")
            elif y in dict[res] and delay>self.delay:
                return ("Trop looong ! mais c\'est une bonne réponse !")
            else :
                return("Faux, c\'était un " + str([k  for (k, val) in dict.items() if y in val][0]) + "\n")

        except (KeyError, IndexError):
            return("Ooops... saisie non valide... formats acceptés : si, Si, SI, B, b")




## Partie Bot

    '''
    Création d'embed
    '''
    def create_embed(self, title, description, color, img=""):
        embed = discord.Embed()
        embed.title=title
        embed.description = description
        embed.color = color
        if(img!=""):
            embed.set_image(url=img)
        return embed

    '''
    Méthode appelée au lancement du bot
    '''
    async def on_ready(self):
        print("Ready !")
        print("Logged in as ")
        print(self.user.name)
        print(self.user.id)
        print("------")


    async def createQuestion(self, message):
        # Question suivante
        self.create_im_question()
        self.listen_for_answer = True
        message_img = await message.channel.send(file=discord.File(os.getcwd() +"/jac_img.png"))
        if self.niveau == 1:
            await message_img.add_reaction("💡")
        #Réactivation du chrono
        self.t_debut=time.time()
        self.classement_tmp = []



    async def on_reaction_add(self, reaction, user):
        '''
        Ajoute une image d'aide en cas de réaction (pour le niveau 1)
        '''
        if self.start_:
            if user != self.user and reaction.emoji == "💡":
                await self.channel.send(file=discord.File("./images/help.jpg"))
                self.t_debut=time.time()



    async def displayResult(self, message):
        '''
        Affiche le classement des joueurs
        '''
        print(self.players)
        R = {k: v for k, v in sorted(self.players.items(), key=lambda item: item[1], reverse=True)}
        res = "**Classement :**\n"
        for k in range(min(3, len(self.players))):
            res += (str(k+1) + " - " + list(R.keys())[k] + " (" + str(list(R.values())[k]) + " points)\n")
        await message.channel.send(res)


    async def sendMeme(self, message, txtAnswer):
        score = self.players[message.author.name]
        L = init_gif(score, txtAnswer)
        if len(L)>0:
            await message.channel.send(L[random.randint(0,len(L)-1)])

    '''
    Méthode appelée à chaque message envoyé sur le serveur ou le bot est présent
    '''
    async def on_message(self, message):

        if (message.content.startswith("!start")):
            self.start_ = True
            self.channel = message.channel
            await message.channel.send("Bienvenue ! \nCommandes :\n - !play, \n - !help, \n - !stop")


        if(message.author == self.user):#Ignore les messages provenant du bot
            return

        elif self.start_ :
            #Stop
            if(message.content.startswith("!stop")):
                self.listen_for_level=False
                self.listen_for_answer=False
                self.start_ = False
                await message.add_reaction("👋")
                return

            #Aide
            if(message.content.startswith("!help") and not self.listen_for_answer):
                intr = ""
                cmd = "**Commandes :**\n - !play : commencer le jeu \n - !stop : arreter de jouer \n\n"
                mds = "**Modes :** \n - Entrainement \n - Multijoueurs \n\n"
                fmts = "**Formats des réponses :** si, Si, SI, B, b \n\n"
                cnt = "Copyright © 2021 Nathan.\n"
                await message.channel.send(intr + cmd + mds + fmts + cnt)

            # Mode Entrainement
            if(self.listen_for_answer and self.mode == 1):
                # print("Mode Traning")
                self.t_fin = time.time()
                txt = self.check_answer(str(message.content), self.t_fin - self.t_debut)
                self.listen_for_answer = False
                # await message.channel.send(txt) # reponse sous format texte classique
                if(txt[0]=="B"):
                    if not message.author.name in self.players:
                        self.players[message.author.name] = 1
                    else:
                        self.players[message.author.name] += 1
                    embed = self.create_embed(txt, " ", discord.Colour(int("0x00FF00", 16)))


                else:
                    if(txt[0]=="T"):
                        if not message.author.name in self.players:
                            self.players[message.author.name] = 0
                        embed = self.create_embed(txt, " ", discord.Colour(int("0xFFA500", 16)))
                    else:
                        self.players[message.author.name] = 0
                        embed = self.create_embed(txt, " ", discord.Colour(int("0xFF0000", 16)))
                await message.channel.send(embed=embed)
                await self.sendMeme(message, txt[0])
                await self.createQuestion(message)



            # Mode Multijoueurs
            if(self.listen_for_answer and self.mode == 2):
                #print("Mode Multi")
                tmp = time.time()
                txt = self.check_answer(str(message.content), tmp - self.t_debut)
                if(txt[0]=="B" or txt[0]=="T"):

                    if not message.author.name in self.classement_tmp :
                        self.classement_tmp.append(message.author.name)
                        points = max(0, 4 - len(self.classement_tmp))
                        if not message.author.name in self.players:
                            self.players[message.author.name] = points
                        else:
                            self.players[message.author.name] += points
                        await message.add_reaction("✅")

                else:
                    if not message.author.name in self.players : tmp = 0
                    else: tmp = self.players[message.author.name]
                    self.players[message.author.name] = max(0, tmp-2)
                    await message.add_reaction("❌")

                if not self.chrono:
                    try:
                        self.chrono = True
                        reaction, user = await discord.Client().wait_for('reaction_add', timeout=5.0)
                    except asyncio.TimeoutError:
                        self.questions_counter += 1
                        if self.questions_counter <= self.NB_QUESTIONS:
                            await self.createQuestion(message)
                            self.chrono = False
                        else :
                            self.chrono = False
                            self.listen_for_answer = False
                            await self.displayResult(message)
                    else:
                        await self.channel.send(file=discord.File("./images/help.jpg"))


            if(self.listen_for_level):
                self.niveau = int(message.content)
                self.listen_for_level = False
                await message.add_reaction("👌")
                await self.createQuestion(message)

            if(self.listen_for_mode):
                self.listen_for_mode = False
                self.mode = int(message.content)
                self.questions_counter = 1
                await message.add_reaction("👌")
                players = {} # reinitialise le dico players
                await message.channel.send("**Niveau :** \n 1 - facile \n 2 - dur \n 3 - très dur")
                self.listen_for_level = True


            #Selection mode
            if(message.content.startswith("!play") and not self.listen_for_answer):
                await message.channel.send("**Mode** : \n 1 - Entrainement \n 2 - Multijoueurs")
                self.listen_for_mode = True







