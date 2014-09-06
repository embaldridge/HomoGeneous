from __future__ import division
import sys
import time

# time lags
l = 0.8
m = 0.5
s = 0.12

def says(s, t=0.08):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(t)


def Tell_us_a_story():
    
    says("\nIntroduction:\n\n")
    time.sleep(l)
    says("Let's define some variables: ")
    time.sleep(l)
    says("For our story, we'll need a ",)
    says( 'he-heroine, an anti-hero, and a village.\n',)
    time.sleep(l)
    
    says("The name of the village in which our story takes place, is Bath. ",)
    time.sleep(m)
    says("Like many villages, Bath had its share of people, buildings,",)
    says(" places to gather, and ")
    time.sleep(m)    
    says("lunatics to avoid. ", s)
    time.sleep(m)
    
    says("Unlike the lunatics in the villages you might be accustomed to ")
    says("avoiding, the lunatics of Bath were, more specifically and because the")
    says(" difference is important, ")
    says("proper Lunatics.", s)
    time.sleep(m)
    says(" All the men of Bath look and act the same, as do all women.") 
    says(" Nobody recognizes anybody and nobody wants to.")
    time.sleep(m)
    says(" Of course, this makes it quite difficult to recognize a Lunatics. ")
    time.sleep(l)
    
    says("Likeweise, this tail of an anonymous society requires a few caveats.")
    time.sleep(m)
    says(" For example, it's a bit difficult to maintain anonymity if you've got people")
    says(" using names, owning property, raising families, and holding down stable jobs.") 
    time.sleep(m)
    says(" So, ")
    time.sleep(m)
    says("we will have none of that.", s)
    time.sleep(m)
    says("\n\nThere are no elderly, no infirmed, and what stands in for ",)
    says("children are, quite literally, ")
    says("precocious cannibals.", s)
    time.sleep(m)
    says(" But, we'll get to the reproductive biology of this curious species of")
    says(" human later.")
    time.sleep(m)
    says(" As for now, I'll simply refer to them as Homo neutralis ")
    says("(Neutral man) and simply refer you to the source code. ")
    time.sleep(m)
    says("That's right,")
    time.sleep(m)
    says(" your narrator has buried the nuts and bolts of this story")
    says(" in the source code.\n\n")
    time.sleep(l)
    
    says("Oh good. You have already read the source code.")
    time.sleep(m)
    says(" You are really on top of things ;)\n\n")
    time.sleep(l)
    
    says("Now that you have read the code, you can see that I have started us out with")
    says(" an incredibly odd and implausible village of anonymous passivists who go")
    says(" about their days playing lotteries, and shucking financial responsibilties")
    says(" and family values.")
    time.sleep(m)
    says(" Sure, why not start from a low point?", s)
    time.sleep(l)
    
    says("\n\nActually, things are about to get interesting because")
    says(" our he-heroine and anti-hero are just about to meet. ")
    says("INITIATING RANDOM SAMPLING...\n", s)
    time.sleep(l)
    
    return