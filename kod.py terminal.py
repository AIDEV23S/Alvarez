def text_till_rovarsp(text): #här defineras en funktion
    konsonanter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"#alla consonanter små och stora 
    text_resultat = ""#tomt yta

    for bokstaven in text:
        if bokstaven in konsonanter:
            text_resultat += bokstaven + "o" + bokstaven # går igenom varje tecken om det är consonanst läggs det ett "o"
        else:
            text_resultat += bokstaven
    return text_resultat

input_text = input(" lägg in text att översättas till rövarspråket :  ")
text_resultat = text_till_rovarsp(input_text) #här kallar jag på funktionen
print(" i rövarspråket blir : ", text_resultat)
