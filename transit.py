from music21 import *
import json
import os

class Transit:
    
    def __init__(self):
        self.tableName = 'stt.txt'


    def calcPosib(self):
        posibTab = {}
        tab = self.loadTable()
        for i in tab.keys():
            jTab = {}
            for j in tab[i].keys():
                note = []
                freq = []
                sumF = 0
                kTab = {}
                for k in tab[i][j].keys():
                    note.append(k)
                    freq.append(tab[i][j][k])
                    sumF += tab[i][j][k]
                freqRel = [fr/sumF * 100 for fr in freq]
                for m in range(len(note)):
                    kTab.update({note[m]: freqRel[m]})
                jTab.update({j: kTab})
            posibTab.update({i: jTab})

        return posibTab


    def loadTable(self):
        if os.stat(self.tableName).st_size < 40:
            tab = {}
        else:
            with open(self.tableName, 'r') as f:
                tab = json.load(f)  
        return tab


    def updateTable(self, track):
        c = converter.parse(track)
        tab = self.loadTable()
        fst = ''
        scd = ''
        for el in c.recurse():
            rom = ''
            if el.classes[0] == 'Chord':
                pitch = el.pitches
                elem = []
                for p in pitch:
                    if p.octave >= 4:
                        elem.append(
                            note.Note(p.nameWithOctave)
                            )
                if len(elem) > 0:
                    rom = roman.romanNumeralFromChord(el).figureAndKey
                    
            elif el.classes[0] == 'Note':
                ch = chord.Chord([el])
                rom = roman.romanNumeralFromChord(ch).figureAndKey
                
            if rom != '':
                if fst == '':
                    fst = str(rom)
                elif scd == '':
                    scd = str(rom)
                else:
                    if fst in tab.keys():
                        if scd in tab[fst].keys():
                            if str(rom) in tab[fst][scd].keys():
                                tab[fst][scd][str(rom)] += 1
                            else:
                                tab[fst][scd][str(rom)] = 1
                        else:
                            tab[fst][scd] = {str(rom): 1}
                    else:
                        tab[fst] = {scd: {str(rom): 1}}
                    fst, scd = scd, str(rom)

        with open(self.tableName, 'w') as f:
            json.dump(tab, f)

