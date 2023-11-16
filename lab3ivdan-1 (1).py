#Laboration 4 2023-11-14 Ivan Witte och Danya Jamel

elev_namn = {}
ANTAL_ELEVER = 3
for namn in range(ANTAL_ELEVER):
    namnen = input("Vad heter elev"+ str(namn+1)+"? ")
    elev_hopp = []
    ANTAL_HOPP = 3
    for hopp in range(ANTAL_HOPP):
        längd = (input("Hur långt var hoppet"+ str(hopp+1)+ "? "))
        elev_hopp.append(längd)
    elev_namn[namnen] = elev_hopp

val = int(input("Elevernas längdhoppstabell! \n Välj en av följande resultat: \n 1. Alla tre hoppen. \n 2. Längsta hoppet. \n 3. Det tredje och sista hoppet. \n 4. Avsluta. \n Vad väljer du?: "))
if val == 1:
    print(elev_namn)
# INTE KLAR ÄNNU under detta 
elif val ==2:
    max = elev_hopp[0]
    for längd in range(1, len(elev_hopp)):
        if max < elev_hopp[längd]:
            max= elev_hopp[längd]
