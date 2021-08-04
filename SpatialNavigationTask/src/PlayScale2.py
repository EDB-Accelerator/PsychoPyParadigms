# Python3-based package
"""
MIT License

Copyright (c) 2021 NIMH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from DictWrite import SectionStart,SectionEnd
from DrawButton import DrawButton
from SelectScale import SelectScale
from SelectFourOption import SelectFourOption

def PlayScale2(df,dfRaw,params,dict,dictRaw,win):

    if dict["Language"] == "English":
        # labels = ["Does not apply to me at all","Fully applicable to me"]
        labels = ["Not uncomfortable","Very uncomfortable"]
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "1. When I'm in a building I've never been to before, "
                                                           "I can point effortlessly in the direction of the building's "
                                                           "main entrance.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "2. When I see a landmark (building, monument, intersection) "
                                                           "that I have seen several times, I know exactly from which "
                                                           "side I have seen that landmark before.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "3. In an unfamiliar city, I can easily tell where to go from an information board with a map. ",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "4. Without a map, I can estimate the distance of a route that I have traveled for the first time.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "5. I can estimate how long it would take a route in an unknown city if I see the route on a map "
                    "(with legend and scale).  ",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "6. I can always orient myself quickly and correctly in an unfamiliar environment.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "7. I always want to know exactly where I am (that is, I am always orientating myself in an "
                    "unfamiliar environment).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "8. I'm afraid of getting lost somewhere.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "9. I'm afraid of getting lost in a strange city.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "10. In an unfamiliar city I prefer to walk in a group than alone.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "11. When I get lost, I get nervous.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "12. How uncomfortable do you feel in the following situation:\n\n- Decide which direction to go "
                    "when you are just coming from a train, bus or metro station.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "13. How uncomfortable do you feel in the following situation:\n\n- Finding your way in an unknown "
                    "building (eg a hospital).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "14. How uncomfortable do you feel in the following situation:\n\n- Finding your way to an "
                    "appointment "
                    "in an unfamiliar city or part of a city.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "15. I'm scared to go to a destination I've never been to.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "16. I can usually remember a new route after taking it once.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "17. I am good at estimating distances (for example, from myself to a building I can see).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "18. I am good at understanding and following directions.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "19. I am good at giving directions (that is, explaining a known route to someone).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "20. When I walk out of a store, I don't have to re-orient myself to know where to go.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "21. I like to take new roads (for example shortcuts) to well-known destinations.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "22. I can easily think of the shortest route to a known destination.",
                    labels)
    else:
        labels = ["Helemaal niet op mij van toepassing", "Volledig op mij van toepassing"]
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "1. Als ik me in een gebouw bevind waar ik nooit eerder ben "
                                                           "geweest, kan ik moeiteloos wijzen in de richting van de "
                                                           "hoofdingang van het gebouw.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "2. Als ik een herkenningspunt (gebouw, monument, kruispunt) "
                                                           "zie dat ik meerdere keren heb gezien, weet ik precies van "
                                                           "welke kant ik dat herkenningspunt eerder heb gezien.",labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win, "3. In een onbekende stad kan ik gemakkelijk aflezen waar "
                                                           "ik heen moet van een informatiebord met een plattegrond. ",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "4. Ik kan zonder kaart goed de afstand schatten van een afgelegde route, die ik voor de "
                    "eerste keer loop.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "5. Ik kan goed schatten hoe lang ik over een route in een onbekende stad zou doen als ik de route "
                    "op een kaart (met legenda en schaal) zie.  ", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "6. Ik kan mezelf altijd snel en juist oriënteren in een onbekende omgeving.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "7. Ik wil altijd precies weten waar ik ben (dat wil zeggen, ik ben in een onbekende omgeving "
                    "altijd bezig met mezelf te oriënteren).", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "8. Ik ben bang om ergens de weg kwijt te raken.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "9. Ik ben bang te verdwalen in een vreemde stad.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "10. In een onbekende stad loop ik liever in een groep dan alleen.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "11. Als ik verdwaal, word ik nerveus.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "12. In welke mate voelt u zich ongemakkelijk in de volgende situatie:\n\n- Beslissen welke richting"
                    " u op moet als u net van een trein, bus of metro station komt.", labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "13. In welke mate voelt u zich ongemakkelijk in de volgende situatie:\n\n- De weg vinden in een "
                    "onbekend gebouw (bijvoorbeeld een ziekenhuis).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "14. In welke mate voelt u zich ongemakkelijk in de volgende situatie:\n\n- De weg vinden naar een "
                    "afspraak in een onbekende stad of deel van een stad.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "15. Ik vind het eng om naar een bestemming te gaan waar ik nog nooit ben geweest.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "16. Ik kan me meestal een nieuwe route herinneren nadat ik hem één keer heb afgelegd.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "17. Ik ben goed in het schatten van afstanden (bijvoorbeeld, van mezelf naar een gebouw dat ik kan "
                    "zien).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "18. Ik ben goed in het begrijpen en opvolgen van routebeschrijvingen.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "19. Ik ben goed in het geven van routebeschrijvingen (dat wil zeggen, een bekende route uitleggen "
                    "aan iemand).",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "20. Als ik een winkel uit loop, hoef ik me niet opnieuw oriënteren om te weten waar ik heen moet.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "21. Ik neem graag nieuwe wegen (bijvoorbeeld binnendoorweggetjes) naar bekende bestemmingen.",
                    labels)
        SelectScale(df, dfRaw, params, dict, dictRaw, win,
                    "22. Ik kan gemakkelijk de kortste route naar een bekende bestemming bedenken.",
                    labels)

    # Ending message Initialize
    dict["Section"] = "Last screen"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    stims = []
    txts = []
    if dict["Language"] == "English":
        txts.append("This is the end of the investigation.\n\n"
                    "Thank you for your time and contribution to science!\n\n"
                    )
    else:
        txts.append("Dit is het einde van het onderzoek.\n\n"
                    "Hartelijk dank voor je tijd en bijdrage aan de wetenschap!\n\n"
                    )

    DrawButton(df, dfRaw, params, dict, dictRaw, win, stims, txts, [0,150], "Continue")
    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])

