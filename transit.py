from music21 import *
import json
import os

class Transit:
    
    def __init__(self):
        self.table_name = 'stt.txt'


    def load_table(self):
        if os.stat(self.table_name).st_size < 40:
            tab = {}
        else:
            with open(self.table_name, 'r') as f:
                tab = json.load(f)  
        return tab


    def update_table(self, track):
        c = converter.parse(track)
        tab = self.load_table()
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

        with open(self.table_name, 'w') as f:
            json.dump(tab, f)


    def calc_posib(self):
        posib_tab = {}
        tab = self.load_table()
        for i in tab.keys():
            j_tab = {}
            for j in tab[i].keys():
                note = []
                freq = []
                sum_f = 0
                k_tab = {}
                for k in tab[i][j].keys():
                    note.append(k)
                    freq.append(tab[i][j][k])
                    sum_f += tab[i][j][k]
                freq_rel = [fr/sum_f * 100 for fr in freq]
                for m in range(len(note)):
                    k_tab.update({note[m]: freq_rel[m]})
                j_tab.update({j: k_tab})
            posib_tab.update({i: j_tab})

        return posib_tab
