from transit import Transit as Tr
from generator import Generator as Gen
from multiplier import Multiplier as Mlt
from music21 import *
import os
from enum import Enum
import random

class Constructs(Enum):
    ascendant = 4, 0
    morning = 1, 2
    recognition = 3, 8
    valsz = 2, 2
    wreck = 5, 3
        

def main():
    tr = Tr()
    #uploadFiles(tr)            # Use this for processing external music files
    s = stream.Stream()
    p0 = stream.Part()
    gen = Gen(tr)
    gen.generate(p0)

    mlt = Mlt()
    chosenConstruct = random.choice(
        [construct.name for construct in Constructs]
        )
    print(chosenConstruct)
    beat = random.randint(
        Constructs[chosenConstruct].value[1],
        Constructs[chosenConstruct].value[1] + 2
        )*10 + 100
    print(beat)
    eval("mlt."+chosenConstruct)(s, p0, beat)
    mlt.streamCompleting(s)
    #s.write('midi', fp='..\M.midi')      #Use this for resaving generated music
    fileSearching(1, s)


def fileSearching(index,s):
    try:
        file = open(f"..\GeneratedMusic{index}.midi", 'r')
    except FileNotFoundError:
        s.write('midi', fp=f"..\GeneratedMusic{index}.midi")
        print(f"file GeneratedMusic{index}.midi has been created")
    else:
        fileSearching(index+1, s)


def uploadFiles(tr):
    dat_dir = '..\\ForLearn'
    files = [os.path.join(dat_dir,x) for x in os.listdir(dat_dir)]
    for f in files:
        tr.updateTable(f)


if __name__ == '__main__':
    main()
