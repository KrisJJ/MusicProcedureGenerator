from music21 import *

class Multiplier:
    
    def __init__(self):
        self.buf = []
        self.position = 0
        
        self.part1 = stream.Part()
        self.part1.id = "Piano part"
        self.part1.append(instrument.Piano())
        
        self.part2 = stream.Part()
        self.part2.id = "Koto part"
        self.part2.append(instrument.Koto())
        
        self.part3 = stream.Part()
        self.part3.id = "Piano harmony part"
        self.part3.append(instrument.Piano())
        
        self.part4 = stream.Part()
        self.part4.id = "Choir part"
        self.part4.append(instrument.Soprano())
        
        self.part5 = stream.Part()
        self.part5.id = "Choir harmony part"
        self.part5.append(instrument.Bass())
        
        self.part6 = stream.Part()
        self.part6.id = "Violin part"
        self.part6.append(instrument.Violin())
        

    def streamCompleting(self, stream0):
        stream0.insert(0, self.part1)
        stream0.insert(0, self.part2)
        stream0.insert(0, self.part3)
        stream0.insert(0, self.part4)
        stream0.insert(0, self.part5)
        stream0.insert(0, self.part6)


    def morning(self, stream0, part0, temp):
        
        stream0.insert(
            self.position,
            tempo.MetronomeMark(number=temp)
            )
        
        for el in part0.getElementsByClass('RomanNumeral'):
            self.buf.append(el.pitches[0])
            
        for i in range(8):
            if i < 6:
                for el in self.buf:
                    self.part1.append(note.Note(el))
                    self.part3.append(note.Rest())
            else:
                tup = duration.Tuplet(2, 4)
                tup.setDurationType('quarter')
                dur = duration.Duration('quarter')
                dur.appendTuplet(tup)
                for el in self.buf:
                    rom = roman.RomanNumeral('I', el.name)
                    rom.duration = dur
                    self.part1.append(rom)
                    nott = note.Note(el.name)
                    nott.octave = el.octave - 2
                    nott.duration = dur
                    self.part3.append(nott)
                

            if i < 8:
                if i >= 4:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    step = 1
                elif i >= 2:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('eighth')
                    dur = duration.Duration('eighth')
                    dur.appendTuplet(tup)
                    step = 2
                    
                if i < 2:
                    for j in range(len(self.buf)):
                        self.part6.append(note.Rest())
                else:
                    for j in range(len(self.buf)):
                        if j % step == 0:
                            nott = note.Note(self.buf[j])
                            nott.duration = dur
                            self.part6.append(nott)

            self.position += 9
            
        self.part1.insert(
            self.position,
            note.Rest()
            )
        self.part2.insert(
            self.position,
            note.Rest()
            )
        self.part3.insert(
            self.position,
            note.Rest()
            )
        self.part4.insert(
            self.position,
            note.Rest()
            )
        self.part5.insert(
            self.position,
            note.Rest()
            )
        self.part6.insert(
            self.position,
            note.Rest()
            )


    def valsz(self, stream0, part0, temp):
        stream0.insert(
            self.position,
            tempo.MetronomeMark(number=temp)
            )

        for el in part0.getElementsByClass('RomanNumeral'):
            self.buf.append(el.pitches[0])

        for i in range(11):
            for el in self.buf[:4]:
                tup = duration.Tuplet(3, 3)
                tup.setDurationType('quarter')
                dur = duration.Duration('quarter')
                dur.appendTuplet(tup)
                    
                nott = note.Note(el.ps)
                nott.duration = dur
                nott.octave -= 2
                self.part3.append(nott)

                nott = note.Note(el.ps + 16)
                nott.duration = dur
                nott.octave -= 2
                nott1 = note.Note(el.ps + 12)
                nott1.duration = dur
                nott1.octave -= 2
                self.part3.append(
                    chord.Chord([nott, nott1])
                    )
                
                nott = note.Note(el.ps + 16)
                nott.duration = dur
                nott.octave -= 2
                nott1 = note.Note(el.ps + 12)
                nott1.duration = dur
                nott1.octave -= 2
                self.part3.append(
                    chord.Chord([nott, nott1])
                    )

                tup = duration.Tuplet(1, 3)
                tup.setDurationType('quarter')
                dur = duration.Duration('quarter')
                dur.appendTuplet(tup)
                nott = note.Note(el.ps)
                nott.duration = dur
                self.part1.append(nott)

            
            if i == 0:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part6.append(rest)
                
            elif i >= 1 and i < 6:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.name)
                    nott.octave = el.octave
                    nott.duration = dur
                    self.part6.append(nott)

            else:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part6.append(rest)


            if i == 0:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)

            elif i >= 3 and i < 6:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    rom = roman.RomanNumeral('I', el.name)
                    rom.duration = dur
                    self.part4.append(rom)
            else:
                for el in self.buf:
                    tup = duration.Tuplet(2, 3)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)


            self.position += 12
            stream0.insert(
                self.position,
                tempo.MetronomeMark(number = temp + i*4)
                )

        tup = duration.Tuplet(1, 3)
        tup.setDurationType('quarter')
        dur = duration.Duration('quarter')
        dur.appendTuplet(tup)
        nott = note.Note(el.ps)
        nott.duration = dur
        nott.octave -= 2
        self.part3.append(nott)
        self.position += 3

        self.part1.insert(
            self.position,
            note.Rest()
            )
        self.part2.insert(
            self.position,
            note.Rest()
            )
        self.part3.insert(
            self.position,
            note.Rest()
            )
        self.part4.insert(
            self.position,
            note.Rest()
            )
        self.part5.insert(
            self.position,
            note.Rest()
            )
        self.part6.insert(
            self.position,
            note.Rest()
            )


    def recognition(self, stream0, part0, temp):
        stream0.insert(
            self.position,
            tempo.MetronomeMark(number=temp)
            )

        for el in part0.getElementsByClass('RomanNumeral'):
            self.buf.append(el.pitches[0])

        for i in range(6):
            if i >= 3:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)

                    tup = duration.Tuplet(4, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)
                    
            elif i >= 2:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)
                    
            elif i >= 1:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    nott = note.Note(el)
                    nott.duration = dur
                    self.part2.append(nott)
                    
            else:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part2.append(rest)

            if i >= 4:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.octave -= 2
                    self.part5.append(nott)
                    
            else:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part5.append(rest)

            if i >= 5:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rom = roman.RomanNumeral('I', el.name)
                    rom.duration = dur
                    self.part4.append(rom)
                    
            else:
                for el in self.buf:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)

            for el in self.buf:
                tup = duration.Tuplet(1, 4)
                tup.setDurationType('quarter')
                dur = duration.Duration('quarter')
                dur.appendTuplet(tup)
                    
                nott = note.Note(el)
                nott.duration = dur
                self.part6.append(nott)

            self.position += 32

        tup = duration.Tuplet(4, 4)
        tup.setDurationType('quarter')
        dur = duration.Duration('quarter')
        nott = note.Note(el)
        nott.duration = dur
        self.part2.append(nott)
        self.position += 1

        self.part1.insert(
            self.position,
            note.Rest()
            )
        self.part2.insert(
            self.position,
            note.Rest()
            )
        self.part3.insert(
            self.position,
            note.Rest()
            )
        self.part4.insert(
            self.position,
            note.Rest()
            )
        self.part5.insert(
            self.position,
            note.Rest()
            )
        self.part6.insert(
            self.position,
            note.Rest()
            )


    def ascendant(self, stream0, part0, temp):
        stream0.insert(
            self.position,
            tempo.MetronomeMark(number=temp)
            )

        for el in part0.getElementsByClass('RomanNumeral'):
            self.buf.append(el.pitches[0])

        for i in range(10):
            if i >= 6:
                for j in range(len(self.buf)):
                    tup = duration.Tuplet(4, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(self.buf[j].ps + 16)
                    nott.duration = dur
                    nott.octave -= 3
                    self.part6.append(nott)
                    nott = note.Note(self.buf[j].ps)
                    nott.duration = dur
                    nott.octave -= 2
                    self.part6.append(nott)
                    
                    if i < 8:
                        if j % 2 == 1:
                            tup = duration.Tuplet(6, 8)
                            tup.setDurationType('half')
                            dur = duration.Duration('half')
                            dur.appendTuplet(tup)
                            nott = note.Note(el.ps + 12)
                            nott.duration = dur
                            nott.octave -= 2
                            nott.volume = 60
                            self.part3.append(nott)
                            
                            tup = duration.Tuplet(3, 8)
                            tup.setDurationType('half')
                            dur = duration.Duration('half')
                            dur.appendTuplet(tup)
                            nott = note.Note(el.ps + 16)
                            nott.duration = dur
                            nott.octave -= 2
                            nott.volume = 60
                            self.part3.append(nott)
                            
                        else:
                            tup = duration.Tuplet(1, 4)
                            tup.setDurationType('half')
                            dur = duration.Duration('half')
                            dur.appendTuplet(tup)
                            nott = note.Note(el.ps + 12)
                            nott.duration = dur
                            nott.octave -= 2
                            nott.volume = 60
                            self.part3.append(nott)
                        
            elif i>=4:
                for el in self.buf:
                    tup = duration.Tuplet(4, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps + 4)
                    nott.duration = dur
                    nott.octave = 3
                    nott1 = note.Note(el.ps)
                    nott1.duration = dur
                    nott1.octave = 3
                    self.part3.append(
                        chord.Chord([nott, nott1])
                        )
                    
                    for j in range(3):
                        nott = note.Note(el.ps)
                        nott.duration = dur
                        nott.octave = 3
                        self.part3.append(nott)

                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    self.part1.append(nott)

                for j in range(len(self.buf)):
                    if j % 4 == 1 or j == 4:
                        tup = duration.Tuplet(2, 4)
                        tup.setDurationType('quarter')
                        dur = duration.Duration('quarter')
                        dur.appendTuplet(tup)
                        nott = note.Note(self.buf[j].ps + 12)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
                        nott = note.Note(self.buf[j].ps + 16)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
                        
                    else:
                        tup = duration.Tuplet(2, 4)
                        tup.setDurationType('half')
                        dur = duration.Duration('half')
                        dur.appendTuplet(tup)
                        nott = note.Note(self.buf[j].ps + 16)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
            
            elif i >= 2:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps + 4)
                    nott.duration = dur
                    nott.octave = 3
                    nott1 = note.Note(el.ps)
                    nott1.duration = dur
                    nott1.octave = 3
                    self.part3.append(
                        chord.Chord([nott, nott1])
                        )

                    nott = note.Note(el)
                    nott.duration = dur
                    self.part1.append(nott)

                for j in range(len(self.buf)):
                    if j % 4 == 1:
                        tup = duration.Tuplet(2, 4)
                        tup.setDurationType('quarter')
                        dur = duration.Duration('quarter')
                        dur.appendTuplet(tup)
                        nott = note.Note(self.buf[j].ps + 12)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
                        nott = note.Note(self.buf[j].ps + 16)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
                        
                    else:
                        tup = duration.Tuplet(2, 4)
                        tup.setDurationType('half')
                        dur = duration.Duration('half')
                        dur.appendTuplet(tup)
                        nott = note.Note(self.buf[j].ps + 16)
                        nott.duration = dur
                        nott.octave -= 2
                        self.part6.append(nott)
                    
            else:
                for el in self.buf[:4]:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps + 4)
                    nott.duration = dur
                    nott.octave = 3
                    nott1 = note.Note(el.ps)
                    nott1.duration = dur
                    nott1.octave = 3
                    self.part3.append(
                        chord.Chord([nott, nott1])
                        )

                    nott = note.Note(el)
                    nott.duration = dur
                    self.part1.append(nott)

                for el in self.buf[:4]:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.octave -= 1
                    self.part6.append(nott)

            if i >= 6:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.octave = 4
                    self.part4.append(nott)

                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.octave = 3
                    self.part5.append(nott)

            elif i >= 4:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.octave = 3
                    self.part5.append(nott)

                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)
                    
            elif i >= 2:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part5.append(rest)

                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)
                    
            else:
                for el in self.buf:
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    dur.appendTuplet(tup)
                    rest = note.Rest()
                    rest.duration = dur
                    self.part5.append(rest)

                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)


            if i < 2:
                self.position += 16
            else:
                self.position += 32

            if i >= 5:
                stream0.insert(
                    self.position,
                    tempo.MetronomeMark(number = temp + 360)
                    )
            else:
                stream0.insert(
                    self.position,
                    tempo.MetronomeMark(number = temp + (i+1) * 10)
                    )

        tup = duration.Tuplet(3, 4)
        tup.setDurationType('half')
        dur = duration.Duration('half')
        nott = note.Note(el.ps + 12)
        nott.duration = dur
        nott.octave = 2
        self.part6.append(nott)
        self.position += 1

        stream0.insert(
            self.position - 1,
            tempo.MetronomeMark(number=temp)
            )        

        self.part1.insert(
            self.position,
            note.Rest()
            )
        self.part2.insert(
            self.position,
            note.Rest()
            )
        self.part3.insert(
            self.position,
            note.Rest()
            )
        self.part4.insert(
            self.position,
            note.Rest()
            )
        self.part5.insert(
            self.position,
            note.Rest()
            )
        self.part6.insert(
            self.position,
            note.Rest()
            )


    def wreck(self, stream0, part0, temp):
        stream0.insert(
            self.position,
            tempo.MetronomeMark(number=temp)
            )

        for el in part0.getElementsByClass('RomanNumeral'):
            self.buf.append(el.pitches[0])

        for i in range(4):
            for el in self.buf[:4]:
                for j in range(8):
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('eighth')
                    dur = duration.Duration('eighth')
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    nott.volume = 70
                    self.part2.append(nott)
                    
                if i >= 3:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('whole')
                    dur = duration.Duration('whole')
                    rom = roman.RomanNumeral('I', el.name)
                    rom.duration = dur
                    self.part4.append(rom)
                    
                elif i >= 1:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('whole')
                    dur = duration.Duration('whole')
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    self.part4.append(nott)
                    
                else:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('whole')
                    dur = duration.Duration('whole')
                    rest = note.Rest()
                    rest.duration = dur
                    self.part4.append(rest)

                if i >= 2:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('half')
                    dur = duration.Duration('half')
                    rest = note.Rest()
                    rest.duration = dur
                    self.part1.append(rest)
                    
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('quarter')
                    dur = duration.Duration('quarter')
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    self.part1.append(nott)
                    
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('eighth')
                    dur = duration.Duration('eighth')
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    self.part1.append(nott)
                    
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('eighth')
                    dur = duration.Duration('eighth')
                    nott = note.Note(el.ps)
                    nott.duration = dur
                    self.part1.append(nott)
                    
                else:
                    tup = duration.Tuplet(1, 4)
                    tup.setDurationType('whole')
                    dur = duration.Duration('whole')
                    rest = note.Rest()
                    rest.duration = dur
                    self.part1.append(rest)

                tup = duration.Tuplet(1, 4)
                tup.setDurationType('whole')
                dur = duration.Duration('whole')
                rest = note.Rest()
                rest.duration = dur
                self.part6.append(rest)

        tup = duration.Tuplet(2, 4)
        tup.setDurationType('half')
        dur = duration.Duration('half')
        dur.appendTuplet(tup)
        nott = note.Note(self.buf[4].ps + 12)
        nott.duration = dur
        nott.octave = 3
        nott1 = note.Note(el.ps)
        nott1.duration = dur
        nott1.octave = 3
        self.part1.append(
            chord.Chord([nott, nott1])
            )
        
        rest = note.Rest()
        rest.duration = dur
        self.part2.append(rest)
        rest = note.Rest()
        rest.duration = dur
        self.part4.append(rest)
        rest = note.Rest()
        rest.duration = dur
        self.part6.append(rest)

        for el in self.buf:
            for j in range(8):
                    tup = duration.Tuplet(2, 4)
                    tup.setDurationType('16th')
                    dur = duration.Duration('16th')
                    nott = note.Note(el.ps - j*2)
                    nott.duration = dur
                    self.part6.append(nott)
                    
        for j in range(4):
            tup = duration.Tuplet(1, 4)
            tup.setDurationType('whole')
            dur = duration.Duration('whole')
            rest = note.Rest()
            rest.duration = dur
            self.part1.append(rest)
            rest = note.Rest()
            rest.duration = dur
            self.part2.append(rest)
            rest = note.Rest()
            rest.duration = dur
            self.part4.append(rest)

        for j in range(6):
            tup = duration.Tuplet(1, 4)
            tup.setDurationType('whole')
            dur = duration.Duration('whole')
            rom = roman.RomanNumeral('I', self.buf[j].name)
            rom.duration = dur
            self.part4.append(rom)
            if j % 3 == 2:
                rest = note.Rest()
                rest.duration = dur
                self.part4.append(rest)

        self.position = 112
            
        self.part1.insert(
            self.position,
            note.Rest()
            )
        self.part2.insert(
            self.position,
            note.Rest()
            )
        self.part3.insert(
            self.position,
            note.Rest()
            )
        self.part4.insert(
            self.position,
            note.Rest()
            )
        self.part5.insert(
            self.position,
            note.Rest()
            )
        self.part6.insert(
            self.position,
            note.Rest()
            )
