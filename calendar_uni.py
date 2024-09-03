import requests
import random
from icalendar import Calendar, Event, vText
from pathlib import Path
from datetime import datetime, date
import pytz
import os


ID_CORSO = "0733"
MESI = [9, 10, 11, 12]
ANNO_CORSO = 3
ANNO_ACCADEMICO = 2024
ANNO_ATTUALE = datetime.now().year
CONTROLLO_GRUPPI = False
# A = Lunedì/Mercoledì/Venerdì Mattina e Martedì/Giovedì Pomeriggio
# B = Martedì/Giovedì Mattina e Lunedì/Mercoledì/Venerdì Pomeriggio
GRUPPO_CONTROLLO = "A" # o B




def aggiungi_evento(cal: Calendar, data: dict) -> None:
    event = Event()
    event.add('name', data['name'])
    event.add('summary', data['name'])
    event.add('description', data['description'])
    event.add('dtstart', data['dtstart'])
    event.add('dtend', data['dtend'])
    event['location'] = data['location']
    event.add('COLOR', data['color'])
    cal.add_component(event)

def salva_calendario(calendario: Calendar, nome_calendario = "Calendario") -> None:
    directory = Path.cwd() / 'Calendari'
    try:
        directory.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists")
    else:
        print("Folder was created")

    with open(os.path.join(directory, f'{nome_calendario}.ics'), 'wb') as file:
        file.write(calendario.to_ical())

    print("Calendario creato con successo.")


def get_gruppo(data_start: datetime, data_end: datetime) -> str:
    # %H ora 00-24, %w weekday da 0-6, 0 è domenica
    ora_start = int(data_start.strftime("%H"))
    ora_end = int(data_end.strftime("%H"))
    giorno = int(data_start.strftime("%w"))
    if ora_start >= 8 and ora_end <= 14:
        if giorno == 1 or giorno == 3 or giorno == 5:
            return "A"
        else:
            return "B"
    elif ora_start >= 13 and ora_end <= 19:
        if giorno == 2 or giorno == 4:
            return "A"
        else:
            return "B"


def main() -> None:
    calendari = []

    cal = Calendar()
    cal.add('prodid', 'https://github.com/Shadowz-git')
    cal.add('version', '2.0')
    for mese in MESI:
        calendario_get = requests.get(f'https://storage.portale.unical.it/api/ricerca/cds-websites/{ID_CORSO}/timetable/?lang=it&academic_year={ANNO_ACCADEMICO}&year={ANNO_CORSO}&date_year={ANNO_ATTUALE}&date_month={mese}&search_teacher=&search_location=&af_cod=')
        calendario = calendario_get.json()
        calendari.append(calendario)

    lista_colori = ['Aqua', 'BlueViolet', 'DarkBlue', 'DarkGreen', 'DarkOrange', 'DodgerBlue', 'HotPink', 'Lavender', 'LightCoral', 'Moccasin', 'RoyalBlue', 'Gold']
    colori = {}

    for calendario in calendari:
        for i in range(len(calendario)):
            data_calendario = calendario[i]

            info_giorno_start = date.fromisoformat(data_calendario['dataInizio'])
            info_giorno_end = date.fromisoformat(data_calendario['dataFine'])
            info_ora_start = str(data_calendario['orarioInizio']).split(':')
            info_ora_end = str(data_calendario['orarioFine']).split(':')

            data_inizio = datetime(info_giorno_start.year, info_giorno_start.month, info_giorno_start.day, int(info_ora_start[0]), int(info_ora_start[1]), 0, tzinfo=pytz.timezone("Europe/Rome"))
            data_fine = datetime(info_giorno_end.year, info_giorno_end.month, info_giorno_end.day, int(info_ora_end[0]), int(info_ora_end[1]), 0, tzinfo=pytz.timezone("Europe/Rome"))

            if CONTROLLO_GRUPPI and get_gruppo(data_inizio, data_fine) != GRUPPO_CONTROLLO:
                continue

            docente = "Non segnato" if len(data_calendario['docente']) == 0 else data_calendario['docente']

            if not colori.get(str(data_calendario['insegnamento'])):
                colori[str(data_calendario['insegnamento'])] = random.choice(lista_colori)
                lista_colori.remove(colori[str(data_calendario['insegnamento'])])

            colore = colori.get(str(data_calendario['insegnamento']))

            data = {'name': str(data_calendario['insegnamento']),
                    'description': f"Docenti: {docente}",
                    'dtstart': data_inizio,
                    'dtend': data_fine,
                    'location': vText(f"Edificio: {data_calendario['edificio']} - Aula: {data_calendario['aula']}"),
                    'color' : colore
                    }
            aggiungi_evento(cal, data)

    nome_calendario = f"Calendario-{ID_CORSO}-{ANNO_CORSO}-{ANNO_ATTUALE}"

    if CONTROLLO_GRUPPI:
        nome_calendario = f"Calendario-{ID_CORSO}-{ANNO_CORSO}-{ANNO_ATTUALE}-Gruppo_{GRUPPO_CONTROLLO}"

    salva_calendario(cal, nome_calendario=nome_calendario)

if __name__ == '__main__':
    main()