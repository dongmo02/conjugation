print(" WILlKOMMEN IN MEINEM PROGRAMM, WO SIE DIE KONJUGATION von MANCHEN VERBEN HABEN KÖNNEN")
print("NB:stell einen punkt zwischen die Partikel und das verb ")
print("\n")
zeit=0
zeit=input("geben sie das Tempus ein,in dem sie ihr verb konjugieren möchten \n 1:präsent \n 2:futur1 \n 3:präteritum \n geben sie ihre Auswahl ein:")
zeit=int(zeit)
if zeit==1:
 verb=input("schrei das verb ,das sie die konjugation wollen:")
 pare=1
 ü=1
 q1=1
 ref=1
 if " " in verb:
    ref, verb = verb.split(" ")
    q1 = 5
 a = len(verb)
 t = a - 2

 if '.'in verb:
  ü=2
  pare,verb=verb.split(".")
  a=len(verb)
  z=0
  t=a-2
 par=["ab","an","auf","aus","ein","empor","vorbei","zurück","fest","frei","hoch","vor","hervor","weg","herum","herein","hinauf","zu","durch","zusammen","kennen","um","heraus","hervor"]
 verb8=["regnen","öffnen","begegnen","zeichnen","atmen"]
 verb20=["sein","haben","werden"]
 verb0=["können","dürfen","mögen","sollen","wissen","müssen","wollen"]
 verb7=["fahren","laden","lassen","waschen","schlafen","tragen","fallen","halten","fallen","schlagen","wachsen","braten","backen","blasen"]
 verb10=["geben","treffen","werfen","nehmen","helfen","treten","essen","sprechen","sterben","gelten","vergessen"]
 verb11=["lesen","sehen","stehlen"]
 if verb in verb8:
     h = 5
 else:
    h=6
 if verb in verb20:
    v=5
 else:
    v=6
 if verb in verb0:
   h1 = 5
 else:
    h1=6
 if pare in par:
     ß=5
 else:
     ß=6
 if verb in verb11:
    r =5
 else:
    r=6
 if verb in verb10:
    j= 5
 else:
     j=6


 if verb in verb7:
   p=4
 else:
  p=3
 if ß==6 and ü==2 :
    verb=pare+verb
    a=len(verb)
    t = a - 2
 if q1==5:
  if ß==5:
     if p == 4 or j == 5 or r == 5 :
        if j == 5:
            verb15 = verb.replace('e', 'i', 1)
            verb = verb[0:a - 2]
            verb15 = verb15[0:a - 2]
            print("ich {0}e mich  {1}".format(verb,pare))
            if verb == "nehm":
                print("du nimmst dich {1}".format(pare))
                print("sie nimmt sich {1}".format(pare))
            else:
                if verb[z - 1] == "ß" or verb[z - 1] == "s":
                    print("du {0}t  dich {1}".format(verb15,pare))
                else:
                    print("du {0}st  dich {1}".format(verb15,pare))
                print("es/sie/er {0}t  sich {1}".format(verb15,pare))
            print("wir {0}en  uns {1}".format(verb,pare))
            if verb[z - 1] == ("d" or "t") or h == 5:
                print("ihr {0}et  euch {1}".format(verb,pare))
            else:
                print("ihr {0}t  euch {1}".format(verb,pare))
            print("sie/Sie {0}en sich {1}".format(verb,pare))
        elif p == 4:
            verb9 = verb.replace('a', 'ä')
            verb = verb[0:a - 2]
            z = len(verb)
            verb9 = verb9[0:a - 2]
            print("ich {0}e mich  {1}".format(verb,pare))
            if verb[z - 1] == "ß" or verb[z - 1] == "s":
                print("du {0}t dich {1}".format(verb9,pare))
            else:
                print("du {0}st dich {1}".format(verb9,pare))
            if verb[z - 1] == "t":
                print("es/sie/er {0}  sich {1}".format(verb9,pare))
            else:
                print("es/sie/er {0}t sich {1}".format(verb9,pare))
            print("wir {0}en uns  {1}".format(verb,pare))
            if verb[z - 1] == ("d" or "t") or h == 5:
                print("ihr {0}et euch {1}".format(verb,pare))
            else:
                print("ihr {0}t  euch {1}".format(verb,pare))
            print("sie/Sie {0}en sich {1}".format(verb,pare))
        elif r == 5:
            verb14 = verb.replace('e', 'ie', 1)
            verb = verb[0:a - 2]
            z = len(verb)
            verb14 = verb14[0:a + 1 - 2]
            print("ich {0}e mich {1}".format(verb,pare))
            if verb[z - 1] == "ß" or verb[z - 1] == "s":
                print("du {0}t dich {1}".format(verb14,pare))
            else:
                print("du {0}st dich {1}".format(verb14,pare))
            print("es/sie/er {0}t sich {1}".format(verb14,pare))
            print("wir {0}en  {1} uns ".format(verb,pare))
            if verb[z - 1] == ("d" or "t") or h == 5:
                print("ihr {0}et  euch {1} ".format(verb,pare))
            else:
                print("ihr {0}t euch {1}".format(verb,pare))
            print("sie/Sie {0} sich  {1}en".format(verb,pare))


     else:
        if verb[t] == 'e':
            verb = verb[0:a - 2]
            z = len(verb)
            print("ich {0}e mich {1}".format(verb,pare))
            if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                print("du {0}est dich {1}".format(verb,pare))
            elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
                print("du {0}t dich  {1}".format(verb,pare))
            else:
                print("du {0}st dich {1}".format(verb,pare))
            if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                print("es/sie/er {0}et sich  {1}".format(verb,pare))
            else:
                print("es/sie/er {0}t sich {1}".format(verb,pare))
            print("wir {0}en uns  {1}".format(verb,pare))
            if verb[z - 1] == "d" or verb[z - 1] == "t":
                print("ihr {0}et euch  {1}".format(verb,pare))
            else:
                print("ihr {0}t  euch {1}".format(verb,pare))
            print("sie/Sie {0}en sich {1}".format(verb,pare))
        else:
            verb = verb[0:a - 1]
            z = len(verb)
            if verb[z - 1] == "l":
                verb1 = verb[0:z - 2]
                print("ich {0}le mich {1}".format(verb,pare))
            else:
                print("ich {0}e  mich {1}".format(verb,pare))
            if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                print("du {0}est dich {1}".format(verb,pare))
            elif verb[z - 1] == ("ß" or "s" or "z"):
                print("du {0}t  dich {1}".format(verb,pare))
            else:
                print("du {0}st dich {1}".format(verb,pare))
            if verb[z - 1] == ("d" or "t") or h == 5:
                print("es/sie/er {0}et sich  {1}".format(verb,pare))
            else:
                print("es/sie/er {0}t sich {1}".format(verb,pare))
            print("wir {0}n uns {1}".format(verb,pare))
            if verb[z - 1] == ("d" or "t"):
                print("ihr {0}et euch  {1}".format(verb,pare))
            else:
                print("ihr {0}t euch {1}".format(verb,pare))
            print("sie/Sie {0}n sich  {1}".format(verb,pare))
  else:

   if p==4 or j==5 or r==5 or h1==5:
    if j==5:
     pare=" "
     if "e" in pare:
           verb15 = verb.replace('e', 'i', 1)
           verb = pare + verb
     else:
           verb15 = verb.replace('e', 'i')
     verb = verb[0:a - 2]
     verb15 = verb15[0:a - 2]
     print("ich {0}e mich".format(verb))
     if verb=="nehm":
         print("du nimmst dich ")
         print("sie nimmt sich  ")
     else:
      if verb[z - 1] == "ß" or verb[z - 1] == "s":
         print("du {0}t dich ".format(verb15))
      else:
         print("du {0}st dich".format(verb15))
      print("es/sie/er {0}t sich".format(verb15))
     print("wir {0}en uns".format(verb))
     if verb[z - 1] == ("d" or "t") or h == 5:
         print("ihr {0}et euch".format(verb))
     else:
         print("ihr  {0}t euch".format(verb))
     print("sie/Sie {0}en sich".format(verb))
   elif p==4:
    verb9=verb.replace('a','ä')
    verb = verb[0:a - 2]
    z = len(verb)
    verb9 = verb9[0:a - 2]
    print("ich {0}e mich".format(verb))
    if verb[z - 1] == "ß" or verb[z - 1] == "s":
      print("du {0}t dich".format(verb9))
    else:
      print("du {0}st dich".format(verb9))
    if verb[z - 1] == "t":
       print("es/sie/er {0} sich".format(verb9))
    else:
       print("es/sie/er {0}t sich".format(verb9))
    print("wir {0}en uns".format(verb))
    if verb[z - 1] == ("d" or "t") or h == 5:
       print("ihr {0}et euch".format(verb))
    else:
       print("ihr {0}t euch".format(verb))
    print("sie/Sie {0}en sich".format(verb))
   elif r==5:
     if "e" in pare:
           verb14= verb.replace('e', 'ie', 2)
     else:
           verb14 = verb.replace('e', 'ie', 1)
     verb = verb[0:a - 2]
     z = len(verb)
     verb14 = verb14[0:a+1 - 2]
     print("ich {0}e mich".format(verb))
     if verb[z - 1] == "ß" or verb[z - 1] == "s":
      print("du {0}t dich".format(verb14))
     else:
      print("du {0}st dich".format(verb14))
     print("es/sie/er {0}t sich".format(verb14))
     print("wir {0}en uns".format(verb))
     if verb[z - 1] == ("d" or "t") or h == 5:
         print("ihr {0}et euch".format(verb))
     else:
         print("ihr  {0}t euch".format(verb))
     print("sie/Sie {0}en sich".format(verb))
   elif h1==5:
      if  verb=="wollen":
         verbs= verb.replace(verb[1], 'i')
      elif verb=="müssen":
          verbs = verb.replace(verb[1], 'u')
      elif  verb=="wissen":
          verbs = verb.replace("ss", 'ß')
          verbs = verbs.replace('i', 'ei')
      elif verb=="sollen":
           verbs=verb
      else:
          verbs = verb.replace(verb[1], 'a')
      verb = verb[0:a - 2]
      z = len(verb)
      verbs = verbs[0:a  - 2]
      print("ich {0}".format(verbs))
      if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
          print("du {0}est".format(verbs))
      elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
          print("du {0}t".format(verbs))
      else:
          print("du {0}st".format(verbs))
      print("es/sie/er {0}".format(verbs))
      print("wir {0}en".format(verb))
      if verb[z - 1] == ("d" or "t") or h == 5:
          print("es/sie/er {0}et".format(verb))
      else:
          print("es/sie/er {0}t".format(verb))
      print("sie/Sie {0}en".format(verb))

   else:
    if  verb[t]=='e':
      verb=verb[0:a-2]
      z = len(verb)
    print("ich {0}e mich".format(verb))
    if verb[z - 1] == "d" or verb[z - 1] == "t" or h==5:
     print("du {0}est dich".format(verb))
    elif verb[z - 1] == "ß" or verb[z - 1] == "s" or  verb[z - 1] == "z":
     print("du {0}t dich".format(verb))
    else:
     print("du {0}st dich".format(verb))
    if verb[z - 1] == "d" or verb[z - 1] =="t" or h==5:
     print("es/sie/er {0}et sich".format(verb))
    else:
     print("es/sie/er {0}t sich".format(verb))
    print("wir {0}en uns".format(verb))
    if verb[z - 1] == "d" or verb[z - 1] =="t":
     print("ihr {0}et euch".format(verb))
    else:
        print("ihr {0}t euch".format(verb))
        print("sie/Sie {0}en sich".format(verb))

 else:
  if ß == 5:
        if p == 4 or j == 5 or r == 5:
            if j == 5:
                verb15 = verb.replace('e', 'i', 1)
                verb = verb[0:a - 2]
                verb15 = verb15[0:a - 2]
                print("ich {0}e   {1}".format(verb, pare))
                if verb == "nehm":
                    print("du nimmst  {1}".format(pare))
                    print("du nimmt  {1}".format(pare))
                else:
                    if verb[z - 1] == "ß" or verb[z - 1] == "s":
                        print("du {0}t  {1}".format(verb15, pare))
                    else:
                        print("du {0}st   {1}".format(verb15, pare))
                print("es/sie/er {0}t  {1}".format(verb15, pare))
                print("wir {0}en  {1}".format(verb, pare))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et  {1}".format(verb, pare))
                else:
                    print("ihr {0}t  {1}".format(verb, pare))
                print("sie/Sie {0}en  {1}".format(verb, pare))
            elif p == 4:
                verb9 = verb.replace('a', 'ä')
                verb = verb[0:a - 2]
                z = len(verb)
                verb9 = verb9[0:a - 2]
                print("ich {0}e  {1}".format(verb, pare))
                if verb[z - 1] == "ß" or verb[z - 1] == "s":
                    print("du {0}t  {1}".format(verb9, pare))
                else:
                    print("du {0}st  {1}".format(verb9, pare))
                if verb[z - 1] == "t":
                    print("es/sie/er {0}  {1}".format(verb, pare))
                else:
                    print("es/sie/er {0}t  {1}".format(verb9, pare))
                print("wir {0}en  {1}".format(verb, pare))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et  {1}".format(verb, pare))
                else:
                    print("ihr {0}t  {1}".format(verb, pare))
                print("sie/Sie {0}en  {1}".format(verb, pare))
            elif r == 5:
                verb14 = verb.replace('e', 'ie', 1)
                verb = verb[0:a - 2]
                z = len(verb)
                verb14 = verb14[0:a + 1 - 2]
                print("ich {0}e  {1}".format(verb, pare))
                if verb[z - 1] == "ß" or verb[z - 1] == "s":
                    print("du {0}t  {1}".format(verb14, pare))
                else:
                    print("du {0}st  {1}".format(verb14, pare))
                print("es/sie/er {0}t  {1}".format(verb14, pare))
                print("wir {0}en  {1}".format(verb, par))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et  {1}".format(verb, pare))
                else:
                    print("ihr {0}t  {1}".format(verb, pare))
                print("sie/Sie {0}  {1}en".format(verb, pare))


        else:
            if verb[t] == 'e':
                verb = verb[0:a - 2]
                z = len(verb)
                print("ich {0}e  {1}".format(verb, pare))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("du {0}est  {1}".format(verb, pare))
                elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
                    print("du {0}t  {1}".format(verb, pare))
                else:
                    print("du {0}st  {1}".format(verb, pare))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("es/sie/er {0}et  {1}".format(verb, pare))
                else:
                    print("es/sie/er {0}t  {1}".format(verb, pare))
                print("wir {0}en  {1}".format(verb, pare))
                if verb[z - 1] == "d" or verb[z - 1] == "t":
                    print("ihr {0}et  {1}".format(verb, pare))
                else:
                    print("ihr {0}t  {1}".format(verb, pare))
                print("sie/Sie {0}en  {1}".format(verb, pare))
            else:
                verb = verb[0:a - 1]
                z = len(verb)
                if verb[z - 1] == "l":
                    verb1 = verb[0:z - 2]
                    print("ich {0}le  {1}".format(verb, pare))
                else:
                    print("ich {0}e  {1}".format(verb, pare))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("du {0}est  {1}".format(verb, pare))
                elif verb[z - 1] == ("ß" or "s" or "z"):
                    print("du {0}t  {1}".format(verb, pare))
                else:
                    print("du {0}st  {1}".format(verb, pare))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("es/sie/er {0}et  {1}".format(verb, pare))
                else:
                    print("es/sie/er {0}t  {1}".format(verb, pare))
                print("wir {0}n  {1}".format(verb, pare))
                if verb[z - 1] == ("d" or "t"):
                    print("ihr {0}et  {1}".format(verb, pare))
                else:
                    print("ihr {0}t  {1}".format(verb, pare))
                print("sie/Sie {0}n  {1}".format(verb, pare))


  else:

        if p == 4 or j == 5 or r == 5 or h1 == 5 or v==5:
            if j == 5:
                print(pare)
                pare=" h"
                if "e" in pare:
                    verb15 = verb.replace('e', 'i', 1)
                    verb15= pare + verb15
                    verb=pare+verb
                    a=len(verb)
                else:
                    verb15 = verb.replace('e', 'i')
                verb = verb[0:a - 2]
                verb15 = verb15[0:a - 2]
                print("ich {0}e".format(verb))
                if verb == "nehm":
                    print("du nimmst")
                    print("du nimmt")
                else:
                    z=len(verb)
                    if verb[z - 1] == "ß" or verb[z - 1] == "s":
                        print("du {0}t".format(verb15))
                    else:
                        print("du {0}st".format(verb15))
                if verb[z - 1] == "t":
                    print("es,sie,er{0}".format(verb15))
                else:
                    print("es,sie,er{0}t".format(verb15))
                print("wir {0}en".format(verb))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et".format(verb))
                else:
                    print("ihr {0}t".format(verb))
                print("sie/Sie {0}en".format(verb))
            elif p == 4:
                verb9 = verb.replace('a', 'ä')
                verb = verb[0:a - 2]
                z = len(verb)
                verb9 = verb9[0:a - 2]
                print("ich {0}e".format(verb))
                if verb[z - 1] == "ß" or verb[z - 1] == "s":
                    print("du {0}t".format(verb9))
                else:
                    print("du {0}st".format(verb9))
                if verb[z - 1] == "t":
                    print("ihr {0}".format(verb9))
                else:
                    print("ihr {0}t".format(verb9))
                print("wir {0}en".format(verb))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("es/sie/er {0}et".format(verb))
                else:
                    print("es/sie/er {0}t".format(verb))
                print("sie/Sie {0}en".format(verb))
            elif r == 5:
                verb14 = verb.replace('e', 'ie', 1)
                verb = verb[0:a - 2]
                z = len(verb)
                verb14 = verb14[0:a + 1 - 2]
                print("ich {0}e".format(verb))
                if verb[z - 1] == "ß" or verb[z - 1] == "s":
                    print("du {0}t".format(verb14))
                else:
                    print("du {0}st".format(verb14))
                print("es/sie/er {0}t".format(verb14))
                print("wir {0}en".format(verb))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et".format(verb))
                else:
                    print("ihr {0}t".format(verb))
                print("sie/Sie {0}en".format(verb))
            elif h1 == 5:
                if verb == "wollen":
                    verbs = verb.replace(verb[1], 'i')
                elif verb == "müssen":
                    verbs = verb.replace(verb[1], 'u')
                elif verb == "wissen":
                    verbs = verb.replace("ss", 'ß')
                    verbs = verbs.replace('i', 'ei')
                elif verb == "sollen":
                    verbs = verb
                else:
                    verbs = verb.replace(verb[1], 'a')
                verb = verb[0:a - 2]
                z = len(verb)
                verbs = verbs[0:a - 2]
                print("ich {0}".format(verbs))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("du {0}est".format(verbs))
                elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
                    print("du {0}t".format(verbs))
                else:
                    print("du {0}st".format(verbs))
                print("es/sie/er {0}".format(verbs))
                print("wir {0}en".format(verb))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("ihr {0}et".format(verb))
                else:
                    print("ihr {0}t".format(verb))
                print("sie/Sie {0}en".format(verb))
            elif v==5:
                 if verb=="sein":
                        print("ich bin")
                        print("du bist")
                        print("er/es/er ist")
                        print("wir sind")
                        print("ihr seid")
                        print("sie/Sie sind")
                 if verb=="haben":
                     print("ich habe")
                     print("du hast")
                     print("er/sie/es hat")
                     print("wir haben")
                     print("ihr habt")
                     print("sie/Sie haben")
                 if verb=="werden":
                     print("ich werde")
                     print("du wirst")
                     print("sie wird")
                     print("wir werden")
                     print("ihr werdet")
                     print("sie/Sie werden")

        else:
            if verb[t] == 'e':
                verb = verb[0:a - 2]
                z = len(verb)
                print("ich {0}e".format(verb))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("du {0}est".format(verb))
                elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
                    print("du {0}t".format(verb))
                else:
                    print("du {0}st".format(verb))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("es/sie/er {0}et".format(verb))
                else:
                    print("es/sie/er {0}t".format(verb))
                print("wir {0}en".format(verb))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h==5:
                    print("ihr {0}et".format(verb))
                else:
                    print("ihr {0}t".format(verb))
                print("sie/Sie {0}en".format(verb))
            else:
                verb = verb[0:a - 1]
                z = len(verb)
                if verb[z - 1] == "l":
                    verb1 = verb[0:z - 2]
                    print("ich {0}le".format(verb1))
                else:
                    print("ich {0}e".format(verb))
                if verb[z - 1] == "d" or verb[z - 1] == "t" or h == 5:
                    print("du {tu0}est".format(verb))
                elif verb[z - 1] == ("ß" or "s" or "z"):
                    print("du {0}t".format(verb))
                else:
                    print("du {0}st".format(verb))
                if verb[z - 1] == ("d" or "t") or h == 5:
                    print("es/sie/er {0}et".format(verb))
                else:
                    print("es/sie/er {0}t".format(verb))
                print("wir {0}n".format(verb))
                if verb[z - 1] == ("d" or "t"):
                    print("ihr {0}et".format(verb))
                else:
                    print("ihr {0}t".format(verb))
                print("sie/Sie {0}n".format(verb))
elif zeit==2:
    verb = input("schrei das verb ,das sie  die konjugation wollen:")
    print("ich werde {0}".format(verb))
    print("du wirst {0}".format(verb))
    print("sie wird {0}".format(verb))
    print("wir werden {0}".format(verb))
    print("ihr werdet {0}".format(verb))
    print("sie/Sie werden {0}".format(verb))
elif zeit ==3:
    verb = input("schrei das verb ,das sie die konjugation wollen:")
    ted = open('verbe.txt', 'r', encoding="utf-8")
    tede = open('prateritum.txt', 'r', encoding="utf-8")
    k=0
    i=0
    ü=0
    while ted and k==0 and ü!=106:
      mon = ted.readline()
      a=len(mon)
      mon = mon[0:a - 1]
      if verb==mon:
         k=1
      i = i + 1
      ü=ü+1
    if k==1:
        ü=0
        u=1
        while tede and ü!=106:
            ton = tede.readline()
            ton = ton[0:a - 1]
            if u==i:
                verb=ton
            u=u+1
            ü=ü+1

    else:
        a=len(verb)
        if verb[a - 3] == "d" or verb[a - 3] == "t":
            verb=verb[0:a-2]
            verb=verb +"eten"
        else:
            verb = verb[0:a - 2]
            verb = verb + "ten"

    if k==0:
        a=len(verb)
        verb=verb[0:a - 2]
        z = len(verb)
        print("ich {0}e".format(verb))
        if verb[z - 1] == "d" or verb[z - 1] == "t" :
            print("du {0}est".format(verb))
        elif verb[z - 1] == "ß" or verb[z - 1] == "s" or verb[z - 1] == "z":
            print("du {0}t".format(verb))
        else:
            print("du {0}st".format(verb))

        print("es/sie/er {0}e".format(verb))
        print("wir {0}en".format(verb))
        if verb[z - 1] == "d" or verb[z - 1] == "t":
            print("ihr {0}et".format(verb))
        else:
            print("ihr {0}t".format(verb))
        print("sie/Sie {0}en".format(verb))
    else:
        z = len(verb)
        if verb!="hatte":
          verb = verb[0:z- 1]
        z = len(verb)
        print("ich {0}".format(verb))
        if verb[z - 1] == "d" or verb[z - 1] == "t" :
            print("du {0}est".format(verb))
        elif verb[z - 1] == ("ß" or "s" or "z"):
            print("du {0}t".format(verb))
        else:
            print("du {0}st".format(verb))
        print("es/sie/er {0}".format(verb))
        if verb[z - 1] == "e":
            print("wir {0}n".format(verb))
        else:
            print("wir {0}en".format(verb))
        if verb[z - 1] == ("d" or "t"):
            print("ihr {0}et".format(verb))
        else:
            print("ihr {0}t".format(verb))
        print("sie/Sie {0}en".format(verb))







print("\n\n\ndanke für ihr Vetrauen")
print("NB:ich kann die Fehler begehen,denn teddy ist noch nicht mit mir fertig")






