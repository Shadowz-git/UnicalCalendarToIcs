# UnicalCalendarToIcs
Un semplice script python che permette di convertire il NUOVO calendario delle lezioni di un corso Unical, in un calendario in formato .ics.

# PARAMETRI
_ID_CORSO_ = Id del corso di laurea. [Esempio: "0733", corso di Laure in Informatica - Triennale]
_MESI_ = La lista dei mesi da controllare per l'orario [Esempio: [9, 10, 11, 12], da Settembre a Dicembre]
_ANNO_CORSO_ = Anno del corso da controllare [Esempio: 3, Terzo anno]
_ANNO_ACCADEMICO_ = Anno accademico da controllare
### Parametro Avanzato
_CONTROLLO_GRUPPI_ = Un controllo per permettere di differenziare il calendario in due gruppi [Esempio: True, Secondo anno di informatica, erano suddivisi in 2 gruppi A e B]
_GRUPPO_CONTROLLO_ = Il gruppo da filtrare per il calendario.

E' inserito un meccanismo su una lista di colori, per aggiungere un colore randomico ad una determinata materia durante il salvaggio del calendario.
DOVREBBE funzionare perchè è scritto nella documentazione di iCalendar, ma non funziona perchè so cattivi.


Se lo usate, na stellina non dispiace. <3
_Sono accetti consigli e possibili miglioramenti (Discord: cryptidshadw) Ciau_
