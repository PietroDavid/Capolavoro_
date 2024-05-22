import orario_docenti
print("""\
Benvenuto nel menù di selezione, scegli quale opzione vuoi utilizzare:
1)Genera un file che contiene l'elenco dei docenti di una classe
2)Genera un file che contiene l'orario di un docente
3)Genera un file che contiene il numero di ore che il docente ha a disposizione (D)
4)Genera un file che contiene i docenti che hanno lezione in una determinata ora di un determinato giorno
""")
selezione = int(input("scegliere quale opzione utilizzare: "))
if selezione == 1:
    classe = str(input("inserire una classe: "))
    orario_docenti.docenti_classe(classe)

elif selezione == 2:
    docente = str(input("inseire il nome completo di un docente: "))
    orario_docenti.orario_docente(docente)

elif selezione == 3:
    nome = str(input("inseire il nome completo di un docente: "))
    orario_docenti.ore_disponibili_docente(nome)

elif selezione == 4:
    giorno = str(input("inserire il giorno di cui si vuole sapere l'orario di una certa ora: "))
    ora = int(input("inserire l'ora di cui si vuole sapere quali docenti hanno lezione: "))
    orario_docenti.lezioni_docente_ora_giorno(giorno,ora)