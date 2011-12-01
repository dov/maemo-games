#!/usr/bin/env python
######################################################################
#  A Pentomino game in Python with the goocanvas.
#
#  Dov Grobgeld <dov.grobgeld@gmail.com>
#
#  This program is licensed under the GPL.
#
#  Todo:
#    * Make it possible to choose a given puzze.
#    * Hints
#    * Make more decorations.
#    * Time the solution.
#    * Indicate when the user solves the puzzle.
#
#  Version: 0.1.1
# 
######################################################################

import random
import gtk
from gtk import keysyms
import math
import goocanvas

class PentoGames:
    """ This class contain all existing pentomino combinations """
    games={}
    games["5x3"]=[
        "FPU",
        "LNV",
        "LPV",
        "LTY",
        "NPU",
        "PUV",
        "PUY",
        ]
    games["5x4"]=[
#        "FIPU",
        "FLPU",
        "FLTY",
        "FLUV",
        "FLUY",
        "FPUY",
#        "ILNV",
#        "ILPV",
#        "ILTY",
#        "INPU",
#        "IPUV",
#        "IPUY",
        "LNPU",
        "LNVZ",
        "LPTV",
        "LPTY",
        "LPUY",
        "LPVY",
        "LPVZ",
        "LPWY",
        "LPYZ",
        "LUVY",
        "NPUY",
        "NTVY",
        "PTVW",
        "PUVZ",
        ]
    games["5x5"]=[
#        "FILPU",
#        "FILTY",
#        "FILUV",
#        "FILUY",
        "FIPUY",
        "FLPUW",
        "FLPUX",
        "FLPVW",
        "FLPVY",
        "FLUYZ",
        "FNPUV",
        "FNTVY",
        "FPTUY",
#        "ILNPU",
#        "ILNVZ",
#        "ILPTV",
#        "ILPTY",
#        "ILPUY",
#        "ILPVY",
#        "ILPVZ",
#        "ILPWY",
#        "ILPYZ",
#        "ILUVY",
#        "INPUY",
#        "INTVY",
#        "IPTVW",
#        "IPUVZ",
        "LNPTW",
        "LNPUZ",
        "LNPVY",
        "LNPWY",
        "LNUVZ",
        "LNUWY",
        "LPTUX",
        "LPTUZ",
        "LPTWY",
        "LPUVW",
        "LPVYZ",
        "LPWYZ",
        "LTVWY",
        "LUVYZ",
        "NPUVY",
        "NPUYZ",
        "NPVWY",
        "PVWYZ",
        ]
    games["5x6"]=[
#        "FILNPT",
#        "FILNPV",
#        "FILNUY",
#        "FILNVW",
#        "FILPTV",
#        "FILPTY",
#        "FILPUW",
#        "FILPUX",
#        "FILPUY",
#        "FILPVW",
#        "FILPVY",
#        "FILPWY",
#        "FILPYZ",
#        "FILUVX",
#        "FILUVY",
#        "FILUVZ",
#        "FILUYZ",
#        "FINPTY",
#        "FINPUV",
#        "FINPUY",
#        "FINPVY",
#        "FINPVZ",
#        "FINTVY",
#        "FINUVY",
#        "FINVWY",
#        "FIPTUV",
#        "FIPTUY",
#        "FIPTVY",
#        "FIPTVZ",
#        "FIPUVW",
#        "FIPUVY",
#        "FIPUYZ",
#        "FIPVWY",
#        "FITUVY",
#        "FITUVZ",
#        "FITUWY",
        "FLNPTU",
        "FLNPTV",
        "FLNPTW",
        "FLNPTY",
        "FLNPUV",
        "FLNPUY",
        "FLNPVY",
        "FLNPVZ",
        "FLNTUY",
        "FLNTUZ",
        "FLNTVW",
        "FLNTVX",
        "FLNTVZ",
        "FLNUVW",
        "FLNUWY",
        "FLPTUV",
        "FLPTUX",
        "FLPTUY",
        "FLPTUZ",
        "FLPTWY",
        "FLPTYZ",
        "FLPUVY",
        "FLPUWY",
        "FLPUXY",
        "FLPVWY",
        "FLPVYZ",
        "FLPWYZ",
        "FLTUVY",
        "FLTVYZ",
        "FLUVYZ",
        "FNPTUY",
        "FNPUVW",
        "FNPUVX",
        "FNPUVY",
        "FNPUVZ",
        "FNPUYZ",
        "FNPVWY",
        "FNUVYZ",
        "FPTUWY",
        "FPTUXY",
        "FPTVWY",
        "FPUVXY",
        "FPUVYZ",
#        "ILNPTV",
#        "ILNPTW",
#        "ILNPTY",
#        "ILNPTZ",
#        "ILNPUY",
#        "ILNPUZ",
#        "ILNPVW",
#        "ILNPVY",
#        "ILNPVZ",
#        "ILNPWY",
#        "ILNTUY",
#        "ILNTUZ",
#        "ILNUVX",
#        "ILNUVY",
#        "ILNUVZ",
#        "ILNUWY",
#        "ILNUYZ",
#        "ILPTUV",
#        "ILPTUX",
#        "ILPTUZ",
#        "ILPTVW",
#        "ILPTVY",
#        "ILPTVZ",
#        "ILPTWY",
#        "ILPTYZ",
#        "ILPUVW",
#        "ILPUVZ",
#        "ILPUWY",
#        "ILPUYZ",
#        "ILPVWY",
#        "ILPVYZ",
#        "ILPWYZ",
#        "ILTUXY",
#        "ILTVWY",
#        "ILTWYZ",
#        "ILUVYZ",
#        "INPTUY",
#        "INPTUZ",
#        "INPTVW",
#        "INPTVZ",
#        "INPUVY",
#        "INPUVZ",
#        "INPUYZ",
#        "INPVWY",
#        "INTUVW",
#        "INTUWY",
#        "INTVYZ",
#        "INUVYZ",
#        "IPTUVY",
#        "IPTUWY",
#        "IPTVWY",
#        "IPTVWZ",
#        "IPTVYZ",
#        "IPTWYZ",
#        "IPUVYZ",
#        "IPVWYZ",
        "LNPTUV",
        "LNPTUX",
        "LNPTUY",
        "LNPTVY",
        "LNPTVZ",
        "LNPTWY",
        "LNPTWZ",
        "LNPTYZ",
        "LNPUVW",
        "LNPUVX",
        "LNPUVY",
        "LNPUWY",
        "LNPUXY",
        "LNPUXZ",
        "LNPUYZ",
        "LNPVWY",
        "LNPVYZ",
        "LNPWYZ",
        "LNTUVZ",
        "LPTUVY",
        "LPTUYZ",
        "LPTVWX",
        "LPTVYZ",
        "LPTWYZ",
        "LPUVWY",
        "LPUVXZ",
        "LPVWYZ",
        "LTVWYZ",
        "NPTUVX",
        "NPTUVZ",
        "NPTUYZ",
        "NPTVWY",
        "NPUVYZ",
        "NPVWYZ",
        "NTUWYZ",
        "NUVWYZ",
        "PTUVWY",
        ]
    games["5x7"]=[
#        "FILNPTU",
#        "FILNPTV",
#        "FILNPTW",
#        "FILNPTY",
#        "FILNPTZ",
#        "FILNPUV",
#        "FILNPUW",
#        "FILNPUY",
#        "FILNPVW",
#        "FILNPVY",
#        "FILNPVZ",
#        "FILNPWY",
#        "FILNPYZ",
#        "FILNTUY",
#        "FILNTUZ",
#        "FILNTVW",
#        "FILNTVX",
#        "FILNTVZ",
#        "FILNUVW",
#        "FILNUVY",
#        "FILNUWY",
#        "FILNUYZ",
#        "FILNVWY",
#        "FILNVWZ",
#        "FILPTUV",
#        "FILPTUW",
#        "FILPTUX",
#        "FILPTUY",
#        "FILPTUZ",
#        "FILPTVW",
#        "FILPTVY",
#        "FILPTWY",
#        "FILPTYZ",
#        "FILPUVW",
#        "FILPUVY",
#        "FILPUVZ",
#        "FILPUWY",
#        "FILPUWZ",
#        "FILPUXY",
#        "FILPUYZ",
#        "FILPVWY",
#        "FILPVWZ",
#        "FILPVYZ",
#        "FILPWYZ",
#        "FILTUVY",
#        "FILTUWY",
#        "FILTUXY",
#        "FILTVXY",
#        "FILTVYZ",
#        "FILUVWY",
#        "FILUVYZ",
#        "FILVWYZ",
#        "FILVXYZ",
#        "FINPTUV",
#        "FINPTUY",
#        "FINPTVY",
#        "FINPUVW",
#        "FINPUVX",
#        "FINPUVY",
#        "FINPUVZ",
#        "FINPUWY",
#        "FINPUYZ",
#        "FINPVWY",
#        "FINPVYZ",
#        "FINTVWY",
#        "FINTVYZ",
#        "FINUVWY",
#        "FINUVYZ",
#        "FIPTUVY",
#        "FIPTUWY",
#        "FIPTUXY",
#        "FIPTUYZ",
#        "FIPTVWY",
#        "FIPTVYZ",
#        "FIPUVWY",
#        "FIPUVWZ",
#        "FIPUVXY",
#        "FIPUVYZ",
        "FLNPTUV",
        "FLNPTUX",
        "FLNPTUY",
        "FLNPTUZ",
        "FLNPTVW",
        "FLNPTVY",
        "FLNPTVZ",
        "FLNPTWY",
        "FLNPTWZ",
        "FLNPTYZ",
        "FLNPUVW",
        "FLNPUVX",
        "FLNPUVY",
        "FLNPUVZ",
        "FLNPUWY",
        "FLNPUWZ",
        "FLNPUXY",
        "FLNPUXZ",
        "FLNPUYZ",
        "FLNPVWY",
        "FLNPVYZ",
        "FLNPWYZ",
        "FLNTUVY",
        "FLNTUVZ",
        "FLNTUYZ",
        "FLNUVWY",
        "FLNUVXY",
        "FLNUVYZ",
        "FLNUWYZ",
        "FLNVWYZ",
        "FLPTUVW",
        "FLPTUVX",
        "FLPTUVY",
        "FLPTUVZ",
        "FLPTUWY",
        "FLPTUXY",
        "FLPTUYZ",
        "FLPTVWX",
        "FLPTVWY",
        "FLPTVWZ",
        "FLPTVXY",
        "FLPTVYZ",
        "FLPTWXY",
        "FLPTWYZ",
        "FLPUVWY",
        "FLPUVYZ",
        "FLPUWYZ",
        "FLPUXYZ",
        "FLPVWYZ",
        "FLTUVXY",
        "FLTVWYZ",
        "FLTVXYZ",
        "FLUVWYZ",
        "FLUVXYZ",
        "FNPTUVX",
        "FNPTUVY",
        "FNPTUVZ",
        "FNPTUYZ",
        "FNPTVWY",
        "FNPTVYZ",
        "FNPUVWY",
        "FNPUVXY",
        "FNPUVYZ",
        "FNPVWYZ",
        "FNTUVWY",
        "FPTUVWY",
        "FPUVXYZ",
#        "ILNPTUV",
#        "ILNPTUW",
#        "ILNPTUX",
#        "ILNPTUY",
#        "ILNPTVW",
#        "ILNPTVY",
#        "ILNPTVZ",
#        "ILNPTWY",
#        "ILNPTWZ",
#        "ILNPTYZ",
#        "ILNPUVW",
#        "ILNPUVX",
#        "ILNPUVY",
#        "ILNPUWY",
#        "ILNPUWZ",
#        "ILNPUXY",
#        "ILNPUXZ",
#        "ILNPUYZ",
#        "ILNPVWY",
#        "ILNPVYZ",
#        "ILNPWYZ",
#        "ILNTUVY",
#        "ILNTUVZ",
#        "ILNTUXY",
#        "ILNUVXY",
#        "ILNUVYZ",
#        "ILPTUVW",
#        "ILPTUVY",
#        "ILPTUVZ",
#        "ILPTUWY",
#        "ILPTUYZ",
#        "ILPTVWX",
#        "ILPTVWY",
#        "ILPTVWZ",
#        "ILPTVXY",
#        "ILPTVYZ",
#        "ILPTWYZ",
#        "ILPUVWY",
#        "ILPUVWZ",
#        "ILPUVXZ",
#        "ILPUVYZ",
#        "ILPUWXY",
#        "ILPUWYZ",
#        "ILPVWYZ",
#        "ILTVWYZ",
#        "INPTUVX",
#        "INPTUVY",
#        "INPTUVZ",
#        "INPTUWY",
#        "INPTUYZ",
#        "INPTVWY",
#        "INPUVWZ",
#        "INPUVYZ",
#        "INPVWYZ",
#        "INTUVWY",
#        "INTUVXY",
#        "INTUWYZ",
#        "INTVWYZ",
#        "INUVWYZ",
#        "IPTUVWY",
#        "IPTUVYZ",
#        "IPTUWYZ",
#        "IPTVWYZ",
#        "IPUVXYZ",
#        "ITUVWYZ",
        "LNPTUVW",
        "LNPTUVX",
        "LNPTUVY",
        "LNPTUVZ",
        "LNPTUWY",
        "LNPTUXY",
        "LNPTUYZ",
        "LNPTVWY",
        "LNPTVWZ",
        "LNPTVYZ",
        "LNPTWYZ",
        "LNPUVWY",
        "LNPUVWZ",
        "LNPUVXY",
        "LNPUVXZ",
        "LNPUVYZ",
        "LNPUWYZ",
        "LNPUXYZ",
        "LNPVWYZ",
        "LNTUVWX",
        "LNTUVXY",
        "LNTUVYZ",
        "LNUVXYZ",
        "LPTUVWY",
        "LPTUVXY",
        "LPTUVYZ",
        "LPTUXYZ",
        "LPTVWYZ",
        "LPUVWXY",
        "LPUVWYZ",
        "LPUVXYZ",
        "LPVWXYZ",
        "NPTUVYZ",
        "NPTVWYZ",
        "NPUVXYZ",
        ]
    games["5x8"]=[
#        "FILNPTUV",
#        "FILNPTUW",
#        "FILNPTUX",
#        "FILNPTUY",
#        "FILNPTUZ",
#        "FILNPTVW",
#        "FILNPTVX",
#        "FILNPTVY",
#        "FILNPTVZ",
#        "FILNPTWX",
#        "FILNPTWY",
#        "FILNPTWZ",
#        "FILNPTXY",
#        "FILNPTXZ",
#        "FILNPTYZ",
#        "FILNPUVW",
#        "FILNPUVX",
#        "FILNPUVY",
#        "FILNPUVZ",
#        "FILNPUWY",
#        "FILNPUWZ",
#        "FILNPUXY",
#        "FILNPUXZ",
#        "FILNPUYZ",
#        "FILNPVWX",
#        "FILNPVWY",
#        "FILNPVWZ",
#        "FILNPVXY",
#        "FILNPVXZ",
#        "FILNPVYZ",
#        "FILNPWYZ",
#        "FILNTUVY",
#        "FILNTUVZ",
#        "FILNTUWY",
#        "FILNTUXY",
#        "FILNTUYZ",
#        "FILNTVWY",
#        "FILNTVWZ",
#        "FILNTVXZ",
#        "FILNTVYZ",
#        "FILNUVWY",
#        "FILNUVWZ",
#        "FILNUVXY",
#        "FILNUVYZ",
#        "FILNUWYZ",
#        "FILNVWYZ",
#        "FILPTUVW",
#        "FILPTUVX",
#        "FILPTUVY",
#        "FILPTUVZ",
#        "FILPTUWX",
#        "FILPTUWY",
#        "FILPTUWZ",
#        "FILPTUXY",
#        "FILPTUYZ",
#        "FILPTVWX",
#        "FILPTVWY",
#        "FILPTVWZ",
#        "FILPTVXY",
#        "FILPTVXZ",
#        "FILPTVYZ",
#        "FILPTWXY",
#        "FILPTWYZ",
#        "FILPTXYZ",
#        "FILPUVWX",
#        "FILPUVWY",
#        "FILPUVWZ",
#        "FILPUVXY",
#        "FILPUVXZ",
#        "FILPUVYZ",
#        "FILPUWXY",
#        "FILPUWYZ",
#        "FILPUXYZ",
#        "FILPVWXY",
#        "FILPVWYZ",
#        "FILTUVWX",
#        "FILTUVWY",
#        "FILTUVXY",
#        "FILTUVYZ",
#        "FILTUWXY",
#        "FILTUWYZ",
#        "FILTUXYZ",
#        "FILTVWYZ",
#        "FILTVXYZ",
#        "FILUVWYZ",
#        "FILUVXYZ",
#        "FINPTUVW",
#        "FINPTUVX",
#        "FINPTUVY",
#        "FINPTUVZ",
#        "FINPTUWY",
#        "FINPTUYZ",
#        "FINPTVWY",
#        "FINPTVYZ",
#        "FINPUVWX",
#        "FINPUVWY",
#        "FINPUVWZ",
#        "FINPUVXY",
#        "FINPUVXZ",
#        "FINPUVYZ",
#        "FINPUWYZ",
#        "FINPVWXY",
#        "FINPVWYZ",
#        "FINTUVWY",
#        "FINTUVXY",
#        "FINTUVYZ",
#        "FINTVWYZ",
#        "FIPTUVWY",
#        "FIPTUVYZ",
#        "FIPTUWYZ",
#        "FIPTVWYZ",
#        "FIPUVWYZ",
#        "FIPUVXYZ",
        "FLNPTUVW",
        "FLNPTUVY",
        "FLNPTUVZ",
        "FLNPTUWY",
        "FLNPTUWZ",
        "FLNPTUXY",
        "FLNPTUXZ",
        "FLNPTUYZ",
        "FLNPTVWX",
        "FLNPTVWY",
        "FLNPTVWZ",
        "FLNPTVXY",
        "FLNPTVYZ",
        "FLNPTWXY",
        "FLNPTWYZ",
        "FLNPUVWX",
        "FLNPUVWY",
        "FLNPUVWZ",
        "FLNPUVXY",
        "FLNPUVXZ",
        "FLNPUVYZ",
        "FLNPUWXY",
        "FLNPUWYZ",
        "FLNPUXYZ",
        "FLNPVWXY",
        "FLNPVWXZ",
        "FLNPVWYZ",
        "FLNPVXYZ",
        "FLNTUVWY",
        "FLNTUVXY",
        "FLNTUVYZ",
        "FLNTUWXY",
        "FLNUVWXY",
        "FLNUVWYZ",
        "FLPTUVWX",
        "FLPTUVWY",
        "FLPTUVXY",
        "FLPTUVYZ",
        "FLPTUWXY",
        "FLPTUWYZ",
        "FLPTUXYZ",
        "FLPTVWXY",
        "FLPTVWXZ",
        "FLPTVWYZ",
        "FLPTWXYZ",
        "FLPUVWXY",
        "FLPUVWXZ",
        "FLPUVWYZ",
        "FLPUVXYZ",
        "FLTUVWYZ",
        "FLTUVXYZ",
        "FLUVWXYZ",
        "FNPTUVWY",
        "FNPTUVXY",
        "FNPTUVYZ",
        "FNPTUWYZ",
        "FNPTUXYZ",
        "FNPTVWXY",
        "FNPTVWYZ",
        "FNPUVWYZ",
        "FNPUVXYZ",
#        "ILNPTUVW",
#        "ILNPTUVX",
#        "ILNPTUVY",
#        "ILNPTUVZ",
#        "ILNPTUWX",
#        "ILNPTUWY",
#        "ILNPTUWZ",
#        "ILNPTUXY",
#        "ILNPTUYZ",
#        "ILNPTVWX",
#        "ILNPTVWY",
#        "ILNPTVWZ",
#        "ILNPTVXY",
#        "ILNPTVYZ",
#        "ILNPTWYZ",
#        "ILNPUVWX",
#        "ILNPUVWY",
#        "ILNPUVWZ",
#        "ILNPUVXY",
#        "ILNPUVXZ",
#        "ILNPUVYZ",
#        "ILNPUWXY",
#        "ILNPUWYZ",
#        "ILNPUXYZ",
#        "ILNPVWXY",
#        "ILNPVWYZ",
#        "ILNTUVWX",
#        "ILNTUVWY",
#        "ILNTUVXY",
#        "ILNTUVYZ",
#        "ILNTUWXY",
#        "ILNUVWYZ",
#        "ILNUVXYZ",
#        "ILPTUVWY",
#        "ILPTUVWZ",
#        "ILPTUVXY",
#        "ILPTUVXZ",
#        "ILPTUVYZ",
#        "ILPTUWXY",
#        "ILPTUWYZ",
#        "ILPTUXYZ",
#        "ILPTVWXY",
#        "ILPTVWXZ",
#        "ILPTVWYZ",
#        "ILPTVXYZ",
#        "ILPTWXYZ",
#        "ILPUVWXY",
#        "ILPUVWYZ",
#        "ILPUVXYZ",
#        "ILPUWXYZ",
#        "ILPVWXYZ",
#        "ILTUVWYZ",
#        "ILTUVXYZ",
#        "INPTUVWY",
#        "INPTUVXZ",
#        "INPTUVYZ",
#        "INPTUWYZ",
#        "INPTVWYZ",
#        "INPUVWXY",
#        "INPUVWYZ",
#        "INPUVXYZ",
#        "IPTUVWXY",
#        "IPTUVWYZ",
        "LNPTUVWX",
        "LNPTUVWY",
        "LNPTUVXY",
        "LNPTUVXZ",
        "LNPTUVYZ",
        "LNPTUWXY",
        "LNPTUWYZ",
        "LNPTUXYZ",
        "LNPTVWXY",
        "LNPTVWYZ",
        "LNPTVXYZ",
        "LNPUVWXZ",
        "LNPUVWYZ",
        "LNPUVXYZ",
        "LNPVWXYZ",
        "LNTUVWYZ",
        "LNTUWXYZ",
        "LNUVWXYZ",
        "LPTUVWXY",
        "LPTUVWXZ",
        "LPTUVWYZ",
        "LPTVWXYZ",
        "LTUVWXYZ",
        "NPTUVWYZ",
        ]
    games["5x9"]=[
#        "FILNPTUVW",
#        "FILNPTUVX",
#        "FILNPTUVY",
#        "FILNPTUVZ",
#        "FILNPTUWX",
#        "FILNPTUWY",
#        "FILNPTUWZ",
#        "FILNPTUXY",
#        "FILNPTUXZ",
#        "FILNPTUYZ",
#        "FILNPTVWX",
#        "FILNPTVWY",
#        "FILNPTVWZ",
#        "FILNPTVXY",
#        "FILNPTVXZ",
#        "FILNPTVYZ",
#        "FILNPTWXY",
#        "FILNPTWXZ",
#        "FILNPTWYZ",
#        "FILNPTXYZ",
#        "FILNPUVWX",
#        "FILNPUVWY",
#        "FILNPUVWZ",
#        "FILNPUVXY",
#        "FILNPUVXZ",
#        "FILNPUVYZ",
#        "FILNPUWXY",
#        "FILNPUWYZ",
#        "FILNPUXYZ",
#        "FILNPVWXY",
#        "FILNPVWXZ",
#        "FILNPVWYZ",
#        "FILNPVXYZ",
#        "FILNTUVWX",
#        "FILNTUVWY",
#        "FILNTUVWZ",
#        "FILNTUVXY",
#        "FILNTUVXZ",
#        "FILNTUVYZ",
#        "FILNTUWXY",
#        "FILNTUWYZ",
#        "FILNTUXYZ",
#        "FILNTVWXY",
#        "FILNTVWYZ",
#        "FILNUVWXY",
#        "FILNUVWYZ",
#        "FILNUVXYZ",
#        "FILNUWXYZ",
#        "FILPTUVWX",
#        "FILPTUVWY",
#        "FILPTUVWZ",
#        "FILPTUVXY",
#        "FILPTUVXZ",
#        "FILPTUVYZ",
#        "FILPTUWXY",
#        "FILPTUWXZ",
#        "FILPTUWYZ",
#        "FILPTUXYZ",
#        "FILPTVWXY",
#        "FILPTVWXZ",
#        "FILPTVWYZ",
#        "FILPTVXYZ",
#        "FILPTWXYZ",
#        "FILPUVWXY",
#        "FILPUVWXZ",
#        "FILPUVWYZ",
#        "FILPUVXYZ",
#        "FILPUWXYZ",
#        "FILPVWXYZ",
#        "FILTUVWXY",
#        "FILTUVWYZ",
#        "FILTUVXYZ",
#        "FILTUWXYZ",
#        "FILUVWXYZ",
#        "FINPTUVWX",
#        "FINPTUVWY",
#        "FINPTUVWZ",
#        "FINPTUVXY",
#        "FINPTUVXZ",
#        "FINPTUVYZ",
#        "FINPTUWYZ",
#        "FINPTUXYZ",
#        "FINPTVWXY",
#        "FINPTVWYZ",
#        "FINPUVWYZ",
#        "FINPUVXYZ",
#        "FINPVWXYZ",
#        "FINTUVWXY",
#        "FINTUVWYZ",
#        "FINTUVXYZ",
#        "FIPTUVWXY",
#        "FIPTUVWYZ",
#        "FIPTUVXYZ",
        "FLNPTUVWX",
        "FLNPTUVWY",
        "FLNPTUVWZ",
        "FLNPTUVXY",
        "FLNPTUVXZ",
        "FLNPTUVYZ",
        "FLNPTUWXY",
        "FLNPTUWYZ",
        "FLNPTUXYZ",
        "FLNPTVWXY",
        "FLNPTVWXZ",
        "FLNPTVWYZ",
        "FLNPTVXYZ",
        "FLNPTWXYZ",
        "FLNPUVWXY",
        "FLNPUVWYZ",
        "FLNPUVXYZ",
        "FLNPUWXYZ",
        "FLNPVWXYZ",
        "FLNTUVWXY",
        "FLNTUVWYZ",
        "FLNTUVXYZ",
        "FLNTUWXYZ",
        "FLNUVWXYZ",
        "FLPTUVWXY",
        "FLPTUVWXZ",
        "FLPTUVWYZ",
        "FLPTUVXYZ",
        "FLPTVWXYZ",
        "FLPUVWXYZ",
        "FNPTUVWYZ",
        "FNPTUVXYZ",
        "FNPTVWXYZ",
        "FPTUVWXYZ",
#        "ILNPTUVWX",
#        "ILNPTUVWY",
#        "ILNPTUVWZ",
#        "ILNPTUVXY",
#        "ILNPTUVXZ",
#        "ILNPTUVYZ",
#        "ILNPTUWXY",
#        "ILNPTUWXZ",
#        "ILNPTUWYZ",
#        "ILNPTUXYZ",
#        "ILNPTVWXY",
#        "ILNPTVWYZ",
#        "ILNPTVXYZ",
#        "ILNPUVWXY",
#        "ILNPUVWXZ",
#        "ILNPUVWYZ",
#        "ILNPUVXYZ",
#        "ILNPUWXYZ",
#        "ILNPVWXYZ",
#        "ILNTUVWXY",
#        "ILNTUVWXZ",
#        "ILNTUVWYZ",
#        "ILNTUVXYZ",
#        "ILNTUWXYZ",
#        "ILNTVWXYZ",
#        "ILNUVWXYZ",
#        "ILPTUVWXY",
#        "ILPTUVWXZ",
#        "ILPTUVWYZ",
#        "ILPTUVXYZ",
#        "ILPTUWXYZ",
#        "ILPTVWXYZ",
#        "ILPUVWXYZ",
#        "ILTUVWXYZ",
#        "INPTUVWXY",
#        "INPTUVWYZ",
#        "INPTUVXYZ",
#        "INPTVWXYZ",
#        "INPUVWXYZ",
#        "IPTUVWXYZ",
        "LNPTUVWXY",
        "LNPTUVWXZ",
        "LNPTUVWYZ",
        "LNPTUVXYZ",
        "LNPTUWXYZ",
        "LNPTVWXYZ",
        "LNPUVWXYZ",
        "LPTUVWXYZ",
        ]
    games["5x10"]=[
        "FILNPTUVWX",
        "FILNPTUVWY",
        "FILNPTUVWZ",
        "FILNPTUVXY",
        "FILNPTUVXZ",
        "FILNPTUVYZ",
        "FILNPTUWXY",
        "FILNPTUWXZ",
        "FILNPTUWYZ",
        "FILNPTUXYZ",
        "FILNPTVWXY",
        "FILNPTVWXZ",
        "FILNPTVWYZ",
        "FILNPTVXYZ",
        "FILNPTWXYZ",
        "FILNPUVWXY",
        "FILNPUVWXZ",
        "FILNPUVWYZ",
        "FILNPUVXYZ",
        "FILNPUWXYZ",
        "FILNPVWXYZ",
        "FILNTUVWXY",
        "FILNTUVWXZ",
        "FILNTUVWYZ",
        "FILNTUVXYZ",
        "FILNTUWXYZ",
        "FILNTVWXYZ",
        "FILNUVWXYZ",
        "FILPTUVWXY",
        "FILPTUVWXZ",
        "FILPTUVWYZ",
        "FILPTUVXYZ",
        "FILPTUWXYZ",
        "FILPTVWXYZ",
        "FILPUVWXYZ",
        "FILTUVWXYZ",
        "FINPTUVWXY",
        "FINPTUVWXZ",
        "FINPTUVWYZ",
        "FINPTUVXYZ",
        "FINPTUWXYZ",
        "FINPTVWXYZ",
        "FINPUVWXYZ",
        "FINTUVWXYZ",
        "FIPTUVWXYZ",
        "FLNPTUVWXY",
        "FLNPTUVWXZ",
        "FLNPTUVWYZ",
        "FLNPTUVXYZ",
        "FLNPTUWXYZ",
        "FLNPTVWXYZ",
        "FLNPUVWXYZ",
        "FLNTUVWXYZ",
        "FLPTUVWXYZ",
        "FNPTUVWXYZ",
        "ILNPTUVWXY",
        "ILNPTUVWXZ",
        "ILNPTUVWYZ",
        "ILNPTUVXYZ",
        "ILNPTUWXYZ",
        "ILNPTVWXYZ",
        "ILNPUVWXYZ",
        "ILPTUVWXYZ",
        "INPTUVWXYZ",
        "LNPTUVWXYZ",
        ]
    games["5x11"]=[
        "FILNPTUVWXY",
        "FILNPTUVWXZ",
        "FILNPTUVWYZ",
        "FILNPTUVXYZ",
        "FILNPTUWXYZ",
        "FILNPTVWXYZ",
        "FILNPUVWXYZ",
        "FILNTUVWXYZ",
        "FILPTUVWXYZ",
        "FINPTUVWXYZ",
        "FLNPTUVWXYZ",
        "ILNPTUVWXYZ",
        ]
    games["5x12"]=[
        "FILNPTUVWXYZ",
        ]
        


class Pentomino:
    """A class that holds the shape and colors of the 12 pentominos"""

    def __init__(self,
                 tile_size):
        self.pento_dict = {
            "F" : { "color":"gray60",
                    "path":"ulururrdlddl",
                    'center':(0.5,-1.5)},
            "I" : { "color":"midnightblue",
                    "path":"uuuuurdddddl",
                    'center':(0.5,-2.5) },
            "L" : { "color":"sandybrown",
                    "path":"uuuurdddrdll",
                    "center":(0.5,-1.5) },
            "N" : { "color":"orchid",
                    "path":"uuururddlddl",
                    "center":(1,-2) },
            "P" : { "color":"pink",
                    "path":"uururdddll",
                    "center":(1,-1) },
            "T" : { "color":"LightGreen",
                    "path":"uulurrrdlddl",
                    "center":(0.5,-1.5)},
            "U" : { "color":"khaki",
                    "path":"uurdrurddlll",
                    "center":(1.5,-0.5)},
            "V" : { "color":"LightSkyBlue",
                    "path":"uuurddrrdlll",
                    "center":(0.5,-0.5)},
            "W" : { "color":"YellowGreen",
                    "path":"urururddldll",
                    "center":(1.5,-1.5)},
            "X" : { "color":"Tomato",
                    "path":"ururdrdldlul",
                    "center":(1.5,-0.5) },
            "Y" : { "color":"brown",
                    "path":"uuuurdrdlddl",
                    "center":(0.5,-2.5)},
            "Z" : { "color":"turquoise", 
                    "path":"uurrurddlldl",
                    "center":(1.5,-1.5) },
        };
        self.dir_dict = {
            "u" : (0,-1),
            "r" : (1,0),
            "d" : (0, 1),
            "l" : (-1,0)
        };
        self.tile_size=tile_size

    def set_tile_size(self, tile_size):
        self.size = tile_size

    def get_color(self, name):
        return self.pento_dict[name]["color"]

    def get_pento_point_list(self, name, orientation, flip):
        a11=1
        a12=0
        a21=0
        a22=1
        if orientation==1:
            a11=0
            a12=-1
            a21=1
            a22=0
        elif orientation==2:
            a11=-1
            a12=0
            a21=0
            a22=-1
        elif orientation==3:
            a11=0
            a12=1
            a21=-1
            a22=0
        if flip:
            a11=-a11
            a12=-a12

        xc,yc = self.pento_dict[name]["center"]
        pl = []
        x=0
        y=0
        xp=(x-xc)*a11+(y-yc)*a12+xc
        yp=(x-xc)*a21+(y-yc)*a22+yc
        pl.append((xp*self.tile_size, yp*self.tile_size))
        for c in self.pento_dict[name]["path"]:
            dx, dy = self.dir_dict[c]
            x += dx
            y += dy
            xp=(x-xc)*a11+(y-yc)*a12+xc
            yp=(x-xc)*a21+(y-yc)*a22+yc
            pl.append((xp*self.tile_size, yp*self.tile_size))
        return pl

# The cursor is currently simply a square.
class BoardCursor(goocanvas.Group):
    def __init__(self,
                 parent,
                 x0,
                 y0,
                 tile_size) :
        goocanvas.Group.__init__(self,parent=parent)
        s=tile_size #shortcut
        s2=s/2
        shape = [(x0-s2,y0-s2), 
                 (x0+s2,y0-s2), 
                 (x0+s2,y0+s2),
                 (x0-s2,y0+s2)]
        p = goocanvas.Points (shape)
        self.rect = goocanvas.Polyline(parent=self,
                                       points=p,
                                       close_path=True,
                                       fill_pattern=None,
                                       stroke_color="white",
                                       line_width=4)
        self.solid_pattern = self.rect.get_property("stroke_pattern")
    # Set the color of the cursor depending on whether it has
    # picked up a tile or not.
    def set_state(self,state):
        self.rect.set_properties(stroke_pattern=None)

class Gento:
    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def setup_item_signals (self, item):
        item.connect ("motion_notify_event", self.on_motion_notify)
        item.connect ("button_press_event", self.on_button_press)
        item.connect ("button_release_event", self.on_button_release)

    def on_motion_notify (self, item, target, event):
        if (self.dragging == True) and (event.state & gtk.gdk.BUTTON1_MASK):
            new_x = event.x
            new_y = event.y
            item.translate (new_x - self.drag_x, new_y - self.drag_y)
        return True
    
    def on_key_press (self, item, event):
        """ Handle key presses on the canvas
        The following keypresses are supported:
        0-9 : Create a new game with size 10-12,3-9
        Right,Up,Down,Left : Move current piece
        R,F: Rotate and flip current piece.

        The OLPC keys are bound as well.
        """
        k = event.keyval
        dx=0
        dy=0
        if k>=ord('0') and k<=ord('9'):
            new_width=k-ord('0')
            if (new_width<3):
                new_width = new_width + 10
            self.puzzle_width = new_width
            self.new_game()
            return True
        elif k==keysyms.Right or k==keysyms.KP_Right:
            dx=1
        elif k==keysyms.Left or k==keysyms.KP_Left:
            dx=-1
        elif k==keysyms.Up or k==keysyms.KP_Up:
            dy=-1
        elif k==keysyms.Down or k==keysyms.KP_Down:
            dy=1
        elif k==keysyms.r or k==keysyms.KP_Home or k==keysyms.Home:
            if self.pickup_tile:
                it = self.pickup_tile # shortcut
                it.orientation = (it.orientation+1)%4
                pl =self.pento.get_pento_point_list(it.pento_name,
                                                    it.orientation,
                                                    it.flip)
                points = goocanvas.Points (pl)
                it.props.points=points
        elif k==keysyms.f or k==keysyms.KP_End or k==keysyms.End:
            if self.pickup_tile:
                it = self.pickup_tile # shortcut
                it.flip = not it.flip
                pl =self.pento.get_pento_point_list(it.pento_name,
                                                    it.orientation,
                                                    it.flip)
                points = goocanvas.Points (pl)
                it.props.points=points
                
        elif k==keysyms.KP_Next or k==keysyms.Next:
            self.new_game()
        elif k==keysyms.N or k==keysyms.n:
            """ Next game """
            self.new_game(self.puzzle_num+1)
            return True
        elif k==keysyms.P or k==keysyms.p:
            """ Previous game """
            self.new_game(self.puzzle_num-1)
            return True
        elif k==keysyms.U or k==keysyms.u:
            """ Higher level """
            if self.puzzle_width < 12:
                self.puzzle_width = self.puzzle_width + 1
                self.new_game(self.puzzle_num)
            return True
        elif k==keysyms.D or k==keysyms.d:
            """ Lower level """
            if self.puzzle_width > 3:
                self.puzzle_width = self.puzzle_width - 1
                self.new_game(self.puzzle_num)
            return True
        elif k==keysyms.Z or k==keysyms.z:
            """ Lower level """
            self.new_game(0)
            return True
        
        if self.pickup_tile != None:
            self.pickup_tile.translate(dx*self.tile_size, dy*self.tile_size)
        #print "Key press keyval=", event.keyval
        return True

    # return the com of the bounding box
    def get_com(self, points):
        min_x=1000
        min_y=1000
        max_x=-1000
        max_y=-1000
        for p in points :
            x,y = p
            if x<min_x:
                x = min_x
            if x>max_x:
                x=max_x
            if y<min_y:
                y = min_y
            if y>max_y:
                y = max_y
        return (min_x+max_x)/2, (min_y+max_y)/2

    def on_button_press (self, item, target, event):
#        self.cursor.set_state("hide")
        if event.button == 1:
            item.raise_(None)
            self.drag_x = event.x
            self.drag_y = event.y

            fleur = gtk.gdk.Cursor (gtk.gdk.FLEUR)
            canvas = item.get_canvas ()
            canvas.pointer_grab (item,
                                 gtk.gdk.POINTER_MOTION_MASK |
                                 gtk.gdk.BUTTON_PRESS_MASK | 
                                 gtk.gdk.BUTTON_RELEASE_MASK,
                                 fleur,
                                 event.time)
            self.dragging = True
            self.pickup_tile = item
        elif event.button == 3:
            pento_name = item.pento_name

            if self.dragging:
                # Both buttons flips the piece
                item.flip = not item.flip
            else:
                item.orientation = (item.orientation+1)%4
            pl =self.pento.get_pento_point_list(pento_name,
                                                item.orientation,
                                                item.flip)
            points = goocanvas.Points (pl)
            item.props.points=points
        return True

    def on_rotate_button_press (self, item, target, event):
        if self.pickup_tile:
            it = self.pickup_tile # shortcut
            it.orientation = (it.orientation+1)%4
            pl =self.pento.get_pento_point_list(it.pento_name,
                                                it.orientation,
                                                it.flip)
            points = goocanvas.Points (pl)
            it.props.points=points
        return True

    def on_flip_button_press (self, item, target, event):
        if self.pickup_tile:
            it = self.pickup_tile # shortcut
            it.flip = (1-it.flip)%4
            pl =self.pento.get_pento_point_list(it.pento_name,
                                                it.orientation,
                                                it.flip)
            points = goocanvas.Points (pl)
            it.props.points=points

        return True

    def on_new_button_press (self, item, target, event):
        self.new_game()
        return True

    def on_button_release (self, item, target, event):
        if event.button==1:
            canvas = item.get_canvas ()
            canvas.pointer_ungrab (item, event.time)
            # tbd - gridify position.
            self.dragging = False
            # Quantize pos of group
            trans = item.get_transform()
            xq = math.floor(trans[4]/self.tile_size+0.5)*self.tile_size
            yq = math.floor(trans[5]/self.tile_size+0.5)*self.tile_size
            trans.translate(xq-trans[4],yq-trans[5])
            item.set_transform(trans)
    
    def draw_grid(self, width, height):
        """ Draw a grid. This should be generalized to any shape."""
        root = self.canvas.get_root_item()
        self.grid = goocanvas.Group(parent=root)
        x0 = self.tile_size*2
        y0 = self.tile_size*1
        # vertical lines
        for i in range(0,width+1):
            lw = 1
            if i==0 or i==width:
                lw=3
            line = [(x0+self.tile_size*i, y0),
                    (x0+self.tile_size*i, y0+self.tile_size*height)]
            goocanvas.Polyline(parent = self.grid,
                               points = goocanvas.Points(line),
                               close_path=True,
                               fill_pattern=None,
                               stroke_color="gray50",
                               line_width=lw)
        # horizontal lines
        for i in range(0,height+1):
            lw = 1
            if i==0 or i==height:
                lw=3
            line = [(x0, y0+self.tile_size*i),
                    (x0+self.tile_size*width, y0+self.tile_size*i)]
            goocanvas.Polyline(parent = self.grid,
                               points = goocanvas.Points(line),
                               close_path=True,
                               fill_pattern=None,
                               stroke_color="gray50",
                               line_width=lw)
        
    def new_game(self, new_puzzle_id=-1):
        """ Create a new gameboard at the size determined by
        puzzle_width and puzzle_height.
        """
        game_key = str(self.puzzle_height) + "x" + str(self.puzzle_width)
        games = PentoGames.games[game_key]
                 
        root = self.canvas.get_root_item()
        for item in self.tiles:
            child_num = root.find_child (item)
            root.remove_child (child_num)
        self.tiles = []
        if self.grid:
            child_num = root.find_child(self.grid)
            root.remove_child(child_num)

        self.draw_grid(self.puzzle_width,self.puzzle_height)
        # Randomly create a new puzzle from the puzzle DB
        if new_puzzle_id==-1:
            self.puzzle_num = int(random.random()*len(games))
        else:
            self.puzzle_num = (len(games)+new_puzzle_id) % len(games)
        game = games[self.puzzle_num]

        pos=0
        for pento in game:
            pl =self.pento.get_pento_point_list(pento,0,0)
            color=self.pento.get_color(pento)
            points = goocanvas.Points (pl)
            tile =  goocanvas.Polyline(parent=root,
                                       points=points,
                                       close_path=True,
                                       fill_color=color)
            # Initial position of the tile
            xpos=1.4*(pos%3)
            ypos=2*(pos/3)
            tile.translate(self.tile_size*(self.puzzle_width+3.5+xpos),
                           self.tile_size*(3+ypos))
            self.setup_item_signals(tile)
            tile.pento_name = pento
            tile.orientation = 0
            tile.flip = False
            self.tiles.append(tile)
            pos=pos+1

        # Show name of current puzzle
        if self.item_name :
            child_num = root.find_child(self.item_name)
            root.remove_child(child_num)
        self.item_name = goocanvas.Text (parent=root,
                                         text="PuzzleID: " + game_key + ":" + str(self.puzzle_num), 
                                         x=10, 
                                         y=20, 
                                         anchor=gtk.ANCHOR_W,
                                         font = "Sans Bold 15",
                                         fill_color="white"
                                         )
            
    def LetterButton(self,
                     parent=None,
                     color="pink",
                     text_color="black",
                     x=0,
                     y=0,
                     size=80,
                     text="",
                     cb=None):
        """A generic letter button"""
        bg = goocanvas.Group(parent = parent,
                             x=x,
                             y=y)
        goocanvas.Rect(parent = bg,
                       x=0,
                       y=0,
                       width=size,
                       height=size,
                       fill_color=color)
        goocanvas.Text(parent = bg,
                       anchor=gtk.ANCHOR_CENTER,
                       x=size/2,
                       y=size/2,
                       font="Sans Bold %.0f"%(1.0*size*3/4),
                       text=text,
                       fill_color=text_color)
        bg.connect ("button_press_event",cb)

    def __init__(self, width=4):
        self.dragging = False
        self.current_item = None
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        vbox = gtk.VBox()
        self.window.add(vbox)
        self.canvas = goocanvas.Canvas()
        self.canvas.set_size_request(800,600)
        self.canvas.set_bounds(0,0,1200,1000)
        vbox.pack_start(self.canvas, True, True, 0)
        root = self.canvas.get_root_item()
        self.tile_size = 50
        self.puzzle_width=width
        self.puzzle_height=5
        self.pento = Pentomino(self.tile_size)
        self.tiles=[]
        self.grid=None
        self.item_name=None
        self.new_game()
#        for pento in "FILNPTUVWXYZ":
#        self.cursor = BoardCursor(root, 525,225,self.tile_size)
#        self.cursor.set_state("hide")
#        self.setup_item_signals(self.cursor)
        self.canvas.connect ("key_press_event", self.on_key_press)
        self.pickup_tile = None
        gtk.Widget.grab_focus(self.canvas)

        self.LetterButton(parent=root,
                          color="pink",
                          text="R",
                          x=0,y=50,size=80,
                          cb=self.on_rotate_button_press)
        self.LetterButton(parent=root,
                          color="lightgreen",
                          text="F",
                          x=0,y=140,size=80,
                          cb=self.on_flip_button_press)
        self.LetterButton(parent=root,
                          color="cyan",
                          text="N",
                          x=0,y=140+90,size=80,
                          cb=self.on_new_button_press)

        self.window.show_all()

import sys
width=3
if len(sys.argv)>1:
    width = int(sys.argv[1])
gento = Gento(width=width)
gtk.main()
