#!/usr/bin/python2
#c0d3d by n0t3rm
import os
import requests
import sys
##################
os.system("clear")
##################
url = sys.argv[1]
arquivo = open(sys.argv[2])

print """\t\t\n\033[34m\033[1m
 ___                  _   __  __
/ __| ___ __ _ _ _ __| |_ \ \/ /
\__ \/ -_) _` | '_/ _| ' \ >  <
|___/\___\__,_|_| \__|_||_/_/\_\

\033[0;0m"""

print "#"*80
######################
########

for linhas in arquivo:
    linhas = linhas.rstrip('\n')
    link = url+ linhas+'/'
    request = requests.get(link)
    status = request.status_code
    if status == 200:
        print "[\033[32m\033[1m+\033[0;0m] %s ==> encontrado!"%(link)
    elif status == 403:
        print "[\033[33m\033[1m!\033[0;0m] %s ==> acesso negado!"%(link)
####
