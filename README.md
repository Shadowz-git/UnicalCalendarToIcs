# UnicalCalendarToIcs
Un semplice script python che permette di convertire il NUOVO calendario delle lezioni di un corso Unical, in un calendario in formato .ics.

# PARAMETRI
<code><b>_ID_CORSO_</b>: str</code> = Id del corso di laurea. [Esempio: "0733", corso di Laure in Informatica - Triennale]<br>
<code><b>_MESI_</b>: int[]</code> = La lista dei mesi da controllare per l'orario [Esempio: [9, 10, 11, 12], da Settembre a Dicembre]<br>
<code><b>_ANNO_CORSO_</b>: int</code> = Anno del corso da controllare [Esempio: 3, Terzo anno]<br>
<code><b>_ANNO_ACCADEMICO_</b>: int</code> = Anno accademico da controllare<br>
### Parametro Avanzato
<code><b>_CONTROLLO_GRUPPI_</b>: bool</code> = Un controllo per permettere di differenziare il calendario in due gruppi [Esempio: True, Secondo anno di informatica, erano suddivisi in 2 gruppi A e B]<br>
<code><b>_GRUPPO_CONTROLLO_</b>: "A"|"B"</code> = Il gruppo da filtrare per il calendario.

E' inserito un meccanismo su una lista di colori, per aggiungere un colore randomico ad una determinata materia durante il salvaggio del calendario.
DOVREBBE funzionare perchè è scritto nella documentazione di iCalendar, ma non funziona perchè so cattivi.


Se lo usate, na stellina non dispiace. <3
_Sono accetti consigli e possibili miglioramenti (Discord: cryptidshadw) Ciau_
