################################################################################
################################################################################
############################## Projet Bot Discord ##############################
################################################################################
################################################################################

#Copyright © 2021 Nathan. All rights reserved.
#@author Nathan
#name : JAC-BOT

import random

def init_gif(score, txtAnswer):
    L=[]
    if txtAnswer == "B" :
        if score == 3:
            L=["https://tenor.com/view/lepers-julien-trois-champion-gif-19396078", "https://tenor.com/view/bruce-lee-bow-master-smile-gif-12365468", "https://tenor.com/view/bmo-dancing-adventure-time-feeling-it-cute-gif-14387827"]


        elif score == 5:
            L=["https://tenor.com/view/simon-cowell-two-thumbs-up-bravo-nice-happy-gif-8782543","https://tenor.com/view/djt-res-true-gif-8281757", "https://tenor.com/view/wow-omg-surprised-scared-kid-gif-10714204", "https://tenor.com/view/elmer-sheep-thumbs-up-like-approved-gif-7569635"]


        elif score == 10:
            L=["https://tenor.com/view/well-done-despicable-me-minions-cheering-gif-4733480", "https://tenor.com/view/clapping-leonardo-dicaprio-leo-dicaprio-well-done-applause-gif-16463566", "https://tenor.com/view/awesome-reaction-you-who-whos-awesome-gif-4860921", "https://tenor.com/view/wow-ted2-ted2gifs-amaze-gif-4869672"]


        elif score == 20:
            L=["https://tenor.com/view/mando-way-mandalorian-star-wars-this-is-the-way-gif-18467372", "https://tenor.com/view/great-job-yes-yeah-scream-baby-gif-15102794", "https://tenor.com/view/hourra-jean-rochefort-gif-12775428", "https://tenor.com/view/clap-clapping-applause-applaud-cheerleader-gif-12591824", "https://tenor.com/view/thor-ragnarok-thor-marvel-yes-excited-gif-8224887"]


        elif score== 27:
            L=["https://tenor.com/view/lady-gaga-amazing-positive-monsters-brilliant-gif-10015226", "https://discord.com/channels/781999243895504896/806235160319098951/807278047329386546", "https://tenor.com/view/rage-frog-puppet-perform-hyper-gif-16477557", "https://tenor.com/view/mr-bean-bike-bikers-gif-14805551"]

        elif score >30:
            L=["https://tenor.com/view/house-md-dr-house-hugh-laurie-you-are-good-point-gif-4272740", "https://tenor.com/view/like-a-boss-boss-suits-gabriel-macht-harvey-specter-gif-3540818", "https://tenor.com/view/like-a-boss-boss-suits-gabriel-macht-harvey-specter-gif-3540818", "https://tenor.com/view/spongebob-like-a-boss-gif-8957722", "https://tenor.com/view/agt-americas-got-talent-heidi-klum-amazing-amazed-gif-4487134", "https://tenor.com/view/confetti-throwing-glitter-fab-feeling-good-fabulous-gif-10927722", "https://tenor.com/view/perfect-kermit-the-frog-kermit-gif-8765461"]
            if random.random() < 0.80 :L=[]


    elif txtAnswer=="T":
        L=["https://tenor.com/view/mr-bean-checking-time-waiting-gif-11570520", "https://tenor.com/view/judge-judy-double-time-faster-hurry-gif-7566976", "https://tenor.com/view/kid-bored-boring-wait-waiting-gif-5434959", "https://tenor.com/view/grandma-84years-waiting-titanic-rose-dewitt-bukater-gif-5132563", "https://tenor.com/view/waiting-cookie-monster-wait-bored-gif-5885685"]

    else :
        L=["https://tenor.com/view/norman-faux-norman-thavaud-gif-12397622", "https://tenor.com/view/wrong-donald-trump-not-right-gif-8471142", "https://tenor.com/view/philippe-poutou-faux-pas-vrai-gif-8451629", "https://tenor.com/view/you-tried-its-alright-its-ok-dont-worry-relax-gif-12421009", "https://tenor.com/view/i-believe-in-second-chances-one-more-chance-try-again-forgive-chance-the-rapper-gif-15442266", "https://tenor.com/view/peter-draws-lets-try-again-try-again-lets-try-gif-11754833", "https://tenor.com/view/game-over-insert-coins-gif-12235828", "https://tenor.com/view/the-game-you-lost-simon-pegg-shaun-of-the-dead-gif-15513407", "https://tenor.com/view/fran%C3%A7ois-hollande-non-nan-gif-13177557","https://tenor.com/view/master-much-to-learn-you-still-have-gif-10612124","https://tenor.com/view/despicable-me-minions-ehh-no-nope-gif-4741703", "https://tenor.com/view/mr-bean-rowan-atkinson-mad-angry-upset-gif-4308696","https://tenor.com/view/hein-melenchon-gif-18357063", "https://tenor.com/view/mr-bean-pivot-scare-shocked-rowan-atkinson-gif-16388374"]
        if random.randint(0,1)==1:L=[]



    return L


