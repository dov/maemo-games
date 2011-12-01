#!/usr/bin/python
""" Generate games from the pentomino solutions file. It is not used for
playing the gento game"""

import sys
import re

print "games={}"
for sol in ['5x3','5x4','5x5','5x6','5x7','5x8','5x9','5x10','5x11','5x12']:
    f= open("solutions-"+sol+".txt")
    games={}
    for line in f:
        line =re.sub('\s','',
                     re.sub(r'^.*?,\s*','',line))
        pieces={}
        for c in line:
            pieces[c]=1
        game=pieces.keys()
        game.sort()
        games["".join(game)]=1

    games_arr = games.keys()
    games_arr.sort()
    print "games[\""+sol+"\"]=["
    for k in games_arr:
        print "    \""+k+"\","
    print "    ]"

