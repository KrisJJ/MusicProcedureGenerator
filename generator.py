from music21 import *
import random

class Generator:
    def __init__(self,tr):
        self.tab = tr.calc_posib()
        self.fst = ''
        self.scd = ''
        self.k = ''

    def generate(self,part):
        for i in range(8):
            if self.fst=='':
                self.fst = random.choice(list(self.tab.keys()))
                parsed_line = self.fst.split(' ')
                part.append(roman.RomanNumeral(parsed_line[0],parsed_line[2]))

            elif self.scd=='':
                self.scd = random.choice(list(self.tab[self.fst].keys()))
                parsed_line = self.scd.split(' ')
                part.append(roman.RomanNumeral(parsed_line[0],parsed_line[2]))

            else:
                d = self.tab[self.fst][self.scd]
                total = 0
                for i in d.keys():
                    total, d[i] = total+d[i], total

                r = random.randint(1,100)
                for i in d.keys():
                    if d[i]<=r:
                        self.fst, self.scd = self.scd, i
                        break
                parsed_line = self.scd.split(' ')
                part.append(roman.RomanNumeral(parsed_line[0],parsed_line[2]))

