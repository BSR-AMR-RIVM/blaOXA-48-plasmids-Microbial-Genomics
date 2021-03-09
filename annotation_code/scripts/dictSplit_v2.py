# dictSplit_v1
# druk bezig geweest met dit proberen, maar nu probleem met het vergelijken.
# een idee die ik had was dit script toch aan te passen
# eerst een lijst maken bij de dictionaries die alle genen pakt
# daar awk op los laten zodat alleen de unieke genen er uit worden gefilterd
# vervolgens kijken bij de twee files die zijn vergeleken, met dit script > wanneer splitLine overeenkomt met de unieke list, pak dan de sequentie mee
# - 
# bedenk me alleen tijdens het typen dat alle "products" niet worden meegenomen op deze manier, daarom heb ik hem in het begin van het bedenkprocess ook achterwege gelaten.
# - 
# wat nog wel kan is genen van sequentie splitten in de huidige files? en zo enkel de sequenties met elkaar vergelijken
# genen printen als de seq overeen komt en alle multiline sequenties singleline maken (UPDATE: gebeurd al in dit script)

# dictSplit_v2
# bedacht alles in een mooie filtered lijst te zetten (">" + gen) en producten met hun sequentie) en vervolgens hier op verder te gaam
# filenaam doen we er bij, en in het volgende script moeten we dan splitten op _ en dan de eerste twee met elkaar vergelijken bv. splitLine[0]
# moeten we dan ook de sequentie met elkaar vergelijken? if splitLineA[0] == splitLineB[0] and seqLineA == seqLineB?
# twee files aanmaken met resultaten? de een met alle overeenkomsten, de ander met alle verschillen. 
# ! niet vergeten de hele line van de splitline te printen zodat we kunnen onderscheide welke unieke waarden van welk bestand komt.
# vervolgens visualiseren in een spreidingsdiagram?
# UPDATE: vergelijken door middel van > awk 'FNR==NR{f[$0]+=1; next} !($0 in f) { print FNR, $0}' < dus geen identifiers meer nodig in header

import sys
import re

FILE = sys.argv[1]

count = 0

filename = FILE.strip(".txt")

with open(FILE, "r+") as f:
    for line in f:
        stripLine = line.strip("OrderedDict")
        subLine = re.sub(r'[\(\)\[\]\']', '', stripLine)
        splitLine = subLine.split(",")
        
        # als splitLine[0] gelijk staat aan "gene" dan betekend het dat er een gen is geïdentificeerd en geannoteerd
        # wanneer dit niet het geval is staat er alleen een beschrijving bij het product (bijvoorbeeld hypotetical protein)

        if splitLine[0] != "gene" and splitLine[8] == " product":
            pro = splitLine[9].strip(" ")
            seq = splitLine[11].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[11] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[12].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[13] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[14].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')
        
        elif splitLine[0] != "gene" and splitLine[9] == " product" and splitLine[11] == " translation":
            pro = splitLine[10].strip(" ")
            seq = splitLine[12].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] != "gene" and splitLine[9] == " product" and splitLine[13] == " translation":
            pro = splitLine[10].strip(" ")
            seq = splitLine[14].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] != "gene" and splitLine[11] == " product" and splitLine[13] == " translation":
            pro = splitLine[12].strip(" ")
            seq = splitLine[14].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')
        
        elif splitLine[0] != "gene" and splitLine[11] == " product" and splitLine[12] == " 1" and splitLine[14] == " translation":
            pro = splitLine[12].strip(" ") + "," + splitLine[13].strip(" ")
            seq = splitLine[15].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] != "gene" and splitLine[11] == " product" and splitLine[15] == " translation":
            pro = splitLine[12].strip(" ")
            seq = splitLine[16].strip(" ")
            print(">" + pro) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[14] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[15].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[15] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[16].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')
        
        elif splitLine[0] == "gene" and splitLine[16] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[17].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[17] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[18].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[18] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[19].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[19] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[20].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        elif splitLine[0] == "gene" and splitLine[20] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[21].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')
        
        elif splitLine[0] == "gene" and splitLine[21] == " translation":
            gen = splitLine[1].strip(" ")
            seq = splitLine[22].strip(" ")
            print(">" + gen) # + "_" + filename)
            print(seq, end='')

        else:
            next

    # de counter werd gebruikt tijdens het testen van het script om te kijken of alle regels afgehandeld werden
    # wanneer een regel niet door de code wordt afgevangen, dan komt hij in de else terecht en werd de counter opgeteld
    # zo kon ik altijd kijken of de code klaar was, of nog extra condities nodig had        
    #         count += 1
    #         print(line)

    # print(count)
      