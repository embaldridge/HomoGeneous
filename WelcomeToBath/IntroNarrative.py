from __future__ import division
import sys
import time

# time lags
l = 0.8
m = 0.5
s = 0.12

def says(s, t=0.09):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(t)


def Tell_us_a_story():
    
    says("\nIntroduction:\n\n")
    time.sleep(l)
    says("Let's define some variables. ")
    time.sleep(l)
    says("For our story, we will need a he-heroine, so named for reasons yet revealed",)
    says( ', an anti-hero, because heroic heros are boring, and a village. No, not a town; a village. ',)
    time.sleep(l)
    
    says(" The name of the village in which our story takes place is Bath, so named for reasons unknown. ",)
    time.sleep(m)
    says("Like many villages, Bath had its share of polite people, sidewalks and buildings, markets to purchase produce, poultry, and such,",)
    says(" and places to gather in groups for games and gay gatherings. ")
    time.sleep(m)    
    says("And also like many of the cities you may know of, Bath had a growing demographic of Lunatics to avoid.\n\n")
    time.sleep(m)
    
    says("Unlike the lunatics in the villages and town you may be accustomed to avoiding")
    says(", the lunatics of Bath were, more specifically and because the difference is important,")
    says(" proper Lunatics.", s)
    time.sleep(m)
    says(" All the men of Bath looked and acted the same, as did all women.") 
    says(" Nobody recognized anybody and nobody wanted to.")
    time.sleep(m)
    says(" Of course, this makes it quite difficult to recognize anyone, including a Lunatic. ")
    time.sleep(l)
    
    says("But Bath, you see, was a society of anonymous people. Not by choice, no. That would be absurd. ")
    time.sleep(l)
    says("No, the citizenry of Bath were anonymous by biology, that is, by their rapid departure on an ")
    says("evolutionary trajectory unlike that of any homonid yet discovered. In fact, one might say that the ")
    says("people of Bath behaved or were biologically more like spiders or salmon, that is, if spiders and salmon ")
    says("looked very much like people and if all those people looked very much like each other. ")
    time.sleep(m)
    says("But I digress.\n\n")
    time.sleep(l)

    says("Returning to our narrative, this tale of a secret society of anonymous people requires a few caveats.")
    time.sleep(m)
    says(" For example, it would be a bit difficult to maintain anonymity if you have people")
    says(" using names, owning property, raising families, and holding stable jobs.") 
    time.sleep(m)
    says(" So, ")
    time.sleep(m)
    says("we will have none of that nonsense.", s)
    time.sleep(m)
    says(" There were also no elderly and no infirmed, and well, no one that stuck out. ",)
    says("What stood for innocent children were, quite literally, ")
    says("precocious and rapidly growing cannibals.", s)
    time.sleep(m)
    says(" But, we'll get to the reproductive biology of this curious species of human later")
    time.sleep(m)
    says(" As for now, I'll simply refer to them as Homo geneous and simply refer you to the source code. ")
    time.sleep(m)
    says("That's right,")
    time.sleep(m)
    says(" your author has buried the nuts and bolts of this story in the source code.")
    says(" Why? Well honestly, for reasons that will remain unrevealed until he tells me so that I may tell you.\n\n")
    time.sleep(l)

    says(" Having have read the code, you know that we have started out with an incredibly odd and implausible ")
    says("village of anonymous pacifists who go about their days playing lotteries and shucking their responsibilties.")
    time.sleep(m)
    says(" Sure, why not start from a low point?", s)
    time.sleep(l)
    
    says("\n\nActually, things are about to get interesting because our he-heroine and anti-hero are just about to meet. ")
    says("INITIATING RANDOM SAMPLING...\n", s)
    time.sleep(l)
    
    return