
################################################################################
################################################################################
############################## Projet Bot Discord ##############################
################################################################################
################################################################################

#Copyright © 2021 Nathan. All rights reserved.
#@author Nathan
#name : JAC-BOT


from JAC import Bot
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
print(s3)

if __name__== "__main__":
    bot = Bot()
    bot.run("ODA2MjMyNjYyNjcwMDQ5MzQw.YBmcrQ.3ElavlJH0aD0vVNt6lmwvjR7Hu0")#/!\Token a ne pas communiquer