SEP = ","

giorni_sett={
        "lunedì" : 0,
        "martedì": 1,
        "mercoledì": 2,
        "giovedì": 3,
        "venerdì": 4,
        }

file = open("OrarioTabellaGlobale.csv", "r")
def docenti_classe(classe):
    '''
    
    Genera il file docenti_classe.txt che contiene l'elenco dei docenti di una classe
   
        Parametri:
            classe (string): 3 caratteri - classe di cui si vuole l'elenco dei docenti
                         es: 2LE
   
   
    '''
    file_ot = open("docenti_classe.txt","w")
    riga = file.readline()
    while riga != "":
        riga = riga.strip().split(SEP)
        for i in riga:
            if i == classe:
                docente = riga[0] + '\n'
                file_ot.write(docente)
                break
        
        
        riga = file.readline()
    
    file.close()
    file_ot.close()
               



def orario_docente(docente):
    '''
    Genera il file orario_docente.txt che contiene l'orario di un docente
   
        Parametri:
            docente (string): il nome del docente del quale si vuole l'orario
                         es: ADAMOLI PAOLO
   
   
    '''
    file_ot = open("orario_docente.txt","w")
    
    riga = file.readline()
    file_ot.write(riga)
    riga = file.readline()
    file_ot.write(riga)
    
    count = 0
    
    riga=file.readline()
    
    while riga != "":
        riga_letta = riga.strip().split(SEP)
        docente_letto = riga_letta[0].strip()
        
        if docente_letto == docente:
            file_ot.write(riga)
            
            for elemento in riga_letta:
                ore = elemento.strip()
                
                if ore != "" and ore != docente_letto:
                    count += 1
        
        riga = file.readline()
    count = str(count)
    file_ot.write(count)
    file_ot.close()

    
    
    
def ore_disponibili_docente(nome):
    '''
    Genera il file ore_libere_docente.txt che contiene il numero di ore che il docente ha a disposizione (D)
   
        Parametri:
            docente (string): il nome del docente del quale si vuole conoscere le ore disponibili
                         es: ADAMOLI PAOLO
   
   
    '''
    
    
    file_ot = open("ore_libere_docente.txt","w")
    
    count = 0
    
    riga = file.readline()
    
    while riga != "":
        riga_letta = riga.strip().split(SEP)
        docente_letto = riga_letta[0].strip()
        
        if docente_letto == nome:
            
            for elemento in riga_letta:
                ore = elemento.strip()
                
                if ore == "D" :
                    count += 1
        
        riga = file.readline()
    count = str(count)
    file_ot.write(count)
    
    
    

    
    


def lezioni_docente_ora_giorno(giorno,ora):
    '''
    Genera il file lezione_in_ora.txt che contiene i docenti che hanno lezione in una determinata ora di un determinato giorno
   
        Parametri:
            giorno (string): giorno di cui si vuole sapere l'orario di una certa ora
                         es: lunedì
            
            ora (int): l'ora di cui si vuole sapere quali docenti hanno lezione
                         es: 2
   
   
    '''
    
    file_ot = open("lezione_in_ora.txt","w")
    count = 0
    pos=(8 * giorni_sett[giorno]) + ora 
    file.readline()
    file.readline()
    riga = file.readline().strip()
    
    while riga != "":
        riga=riga.split(SEP)
        if riga[pos] !=  "   ":
            file_ot.write(riga[0] + "\n")
            count += 1
        riga = file.readline().strip()
    count = str(count)
    file_ot.write(count)
    
       
       