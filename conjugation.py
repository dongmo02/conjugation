# Willkommen zum Konjugationsprogramm!
# Dieses Programm bietet die Konjugation von deutschen Verben in verschiedenen Tempora an: Präsens, Futur I und Präteritum.
# Input und Konjugation sind teilweise an die verbale Struktur und Ausnahmen gebunden. Verbesserungen und Strukturierung sind enthalten.

def willkommen():
    print("WILLKOMMEN IN MEINEM PROGRAMM, WO SIE DIE KONJUGATION VON VERBEN ERHALTEN KÖNNEN!")
    print("NB: Stellen Sie einen Punkt zwischen die Partikel und das Verb (z.B. 'auf.machen')")
    print("\n")

def konjugation_praesens():
    verb = input("Schreiben Sie das Verb, das Sie konjugieren möchten: ")
    pare = ""
    partikel_verben = ["ab","an","auf","aus","ein","empor","vorbei","zurück","fest","frei","hoch","vor","hervor","weg","herum","herein","hinauf","zu","durch","zusammen","kennen","um","heraus","hervor"]
    modal_verben = ["können","dürfen","mögen","sollen","wissen","müssen","wollen"]
    hilfs_verben = ["sein","haben","werden"]
    starke_verben = ["fahren","laden","lassen","waschen","schlafen","tragen","fallen","halten","schlagen","wachsen","braten","backen","blasen"]
    ablaut_e_verben = ["geben","treffen","werfen","nehmen","helfen","treten","essen","sprechen","sterben","gelten","vergessen"]
    ablaut_ie_verben = ["lesen","sehen","stehlen"]    
    weitere_verben = ["regnen","öffnen","begegnen","zeichnen","atmen"]

    # Partikel erkennen
    if '.' in verb:
        # Trennung von Partikel und Verb am Punkt
        pare, verb = verb.split('.')
    elif " " in verb:
        pare, verb = verb.split(" ")
    
    a = len(verb)
    t = a - 2
    z = 0

    # Special cases für Konjugation
    # (Erweiterung, bessere Lesbarkeit sollte mit Funktionen erfolgen, s. Beispiele unten!)
    if verb in hilfs_verben:
        if verb == "sein":
            return ["ich bin", "du bist", "er/sie/es ist", "wir sind", "ihr seid", "sie/Sie sind"]
        elif verb == "haben":
            return ["ich habe", "du hast", "er/sie/es hat", "wir haben", "ihr habt", "sie/Sie haben"]
        elif verb == "werden":
            return ["ich werde", "du wirst", "sie wird", "wir werden", "ihr werdet", "sie/Sie werden"]

    # Modalverben
    if verb in modal_verben:
        # z.B. wollen: ich will, du willst...
        stamm = verb[0:a-2]
        modalformen = {
            "wollen": ["ich will", "du willst", "er/sie/es will", "wir wollen", "ihr wollt", "sie/Sie wollen"],
            "müssen": ["ich muss", "du musst", "er/sie/es muss", "wir müssen", "ihr müsst", "sie/Sie müssen"],
            "sollen": ["ich soll", "du sollst", "er/sie/es soll", "wir sollen", "ihr sollt", "sie/Sie sollen"],
            "wissen": ["ich weiß", "du weißt", "er/sie/es weiß", "wir wissen", "ihr wisst", "sie/Sie wissen"],
            "dürfen": ["ich darf", "du darfst", "er/sie/es darf", "wir dürfen", "ihr dürft", "sie/Sie dürfen"],
            "können": ["ich kann", "du kannst", "er/sie/es kann", "wir können", "ihr könnt", "sie/Sie können"],
            "mögen": ["ich mag", "du magst", "er/sie/es mag", "wir mögen", "ihr mögt", "sie/Sie mögen"]
        }
        return modalformen.get(verb, [])
    
    # Reguläres Verb (Vereinfachung!)
    konj_list = []
    stamm = verb[:-2]
    # Beispielhafte Konjugation für Schwache Verben
    konj_list.append("ich {}e{}".format(stamm, f" {pare}" if pare else ""))
    konj_list.append("du {}st{}".format(stamm, f" {pare}" if pare else ""))
    konj_list.append("er/sie/es {}t{}".format(stamm, f" {pare}" if pare else ""))
    konj_list.append("wir {}en{}".format(stamm, f" {pare}" if pare else ""))
    konj_list.append("ihr {}t{}".format(stamm, f" {pare}" if pare else ""))
    konj_list.append("sie/Sie {}en{}".format(stamm, f" {pare}" if pare else ""))
    return konj_list

def konjugation_futur():
    verb = input("Schreiben Sie das Verb, das Sie konjugieren möchten: ")
    # Hilfsverb "werden" wird mit Infinitiv verwendet
    return [
        f"ich werde {verb}",
        f"du wirst {verb}",
        f"sie wird {verb}",
        f"wir werden {verb}",
        f"ihr werdet {verb}",
        f"sie/Sie werden {verb}"
    ]

def konjugation_präteritum():
    verb = input("Schreiben Sie das Verb, das Sie konjugieren möchten: ")
    # Vereinfachte Konjugation, Präteritumformen aus Dateien können optional ergänzt werden!
    stamm = verb[:-2]
    praet_list = []
    praet_list.append(f"ich {stamm}te")
    praet_list.append(f"du {stamm}test")
    praet_list.append(f"er/sie/es {stamm}te")
    praet_list.append(f"wir {stamm}ten")
    praet_list.append(f"ihr {stamm}tet")
    praet_list.append(f"sie/Sie {stamm}ten")
    return praet_list

def hauptmenue():
    willkommen()
    print("Wählen Sie das Tempus zur Konjugation aus:")
    print("1: Präsens")
    print("2: Futur I")
    print("3: Präteritum")
    auswahl = input("Geben Sie Ihre Auswahl ein: ")
    try:
        zeit = int(auswahl)
    except ValueError:
        print("Ungültige Eingabe!")
        return

    if zeit == 1:
        formen = konjugation_praesens()
    elif zeit == 2:
        formen = konjugation_futur()
    elif zeit == 3:
        formen = konjugation_präteritum()
    else:
        print("Ungültige Auswahl!")
        return

    print("\nKonjugation:")
    for f in formen:
        print(f)
    print("\n\nDanke für Ihr Vertrauen!")
    print("NB: Ich kann Fehler machen, Teddy arbeitet noch an mir!")

if __name__ == "__main__":
    hauptmenue()
