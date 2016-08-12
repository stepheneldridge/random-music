import random
def init():
    tempo=80
    measures=20
    title='Music'
    file = open('C:\\Users\\Public\\Desktop\\'+title+str(random.random())+'.aria','w')
    file.write('<seqview xscroll="0.000000" yscroll="0" zoom="100">\n')
    file.write('<sequence maintempo="'+str(tempo)+'" measureAmount="'+str(measures)+'" currentTrack="1" beatResolution="1000" internalName="'+title+'" fileFormatVersion="4" channelManagement="auto" metronome="false">\n')
    file.write('<measure  firstMeasure="0" denom="4" num="4"/>\n')
    file.write('<tempo></tempo><text></text><copyright></copyright>\n')
    file.write('<defaultkeysig keytype="2" keysymbolamount="0" />\n')
    track(0,file,0,measures)
    finish(file)
def track(num,file,inst,m):
    instrument = inst
    file.write('<track name="'+str(num)+'" id="'+str(num)+'" channel="0" volume="100" default_volume="80">\n')
    file.write('<key type="C" />\n')
    file.write('<editors height="200">\n')
    file.write('<score enabled="false" musical_notation="true" linear_notation="true" g_clef="true" f_clef="true" scroll="0.547945"/>\n')
    file.write('<keyboard enabled="true" scroll="0.500000" proportion="1.000000"/>\n')
    file.write('<guitar enabled="false"/>\n')
    file.write('<drum enabled="false" scroll="0.000000"/>\n')
    file.write('<controller enabled="false" controller="7"/>\n')
    file.write('</editors>\n')
    file.write('<magneticgrid divider="6" triplet="true" dotted="false"/>\n')
    file.write('<instrument id="'+str(instrument)+'"/>\n')
    file.write('<drumkit id="0" collapseView="false"/>\n')
    file.write('<guitartuning  string0="67" string1="72" string2="76" string3="81" string4="86" string5="91"/>\n')
    notesB(file,m,120)
    file.write('</track>\n')
def notesA(file,measures):
    length=measures*4*1000
    index=0
    while length>0:
        nLen = random.randint(250,1750)
        if length-nLen<0:
            nLen=length
        file.write('<note pitch="'+str(random.randint(50,100))+'" start="'+str(index)+'" end="'+str(index+nLen)+'" volume="80"/>\n')
        length-=nLen
        index+=nLen
    file.write('</track>\n')
def notesB(file,measures,notes):
    length=measures*4*1000
    count = 0
    position = []
    while count<notes:
        count=count+1
        position.append(random.randint(0,length))
    position.sort()
    while count>0:
        nLen = random.randint(1000,4000)
        if position[notes-count]+nLen>length:
            nLen=length-position[notes-count]
        file.write('<note pitch="'+str(random.randint(25,100))+'" start="'+str(position[notes-count])+'" end="'+str(position[notes-count]+nLen)+'" volume="80"/>\n')
        count=count-1
def finish(f):
    f.write('</sequence></seqview>')
    f.close()
init()

