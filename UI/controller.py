import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # da fare
    def popola_dropdowns(self):
        """Popola i menu a tendina chiedendo i dati al Model all'avvio dell'app."""

        # Popoliamo le biblioteche
        biblioteche = self._model.get_biblioteche()
        # Aggiungiamo l'opzione "Nessun filtro" come prima scelta
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="None", text="Nessun filtro"))

        for b in biblioteche:
            # Usiamo id_biblioteca come 'key' nascosta (serve per la query)
            # e il nome della biblioteca come 'text' visibile all'utente.
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        # Popoliamo i generi
        generi = self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="None", text="Nessun filtro"))

        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()

    # CALLBACKS DROPDOWN
    # da fare
    def leggi_biblioteca(self, e):
        """Callback chiamata quando l'utente seleziona una biblioteca dal Dropdown."""
        scelta = self._view.dd_biblioteca.value
        if scelta == "None" or scelta is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(scelta)  # Convertiamo la key in int per il DB

    def leggi_genere(self, e):
        """Callback chiamata quando l'utente seleziona un genere dal Dropdown."""
        scelta = self._view.dd_genere.value
        if scelta == "None" or scelta is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta

    # AZIONE: MOSTRA LIBRI
    # da fare
    def mostra_libri(self, e):
        """Callback chiamata quando l'utente preme il bottone 'Mostra Libri'."""

        # Chiediamo i libri filtrati al model usando i filtri salvati
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # Svuotiamo la ListView prima di popolarla con i nuovi risultati
        self._view.lst_libri.controls.clear()

        # Controlliamo se ci sono risultati
        if not libri:
            # Se la lista è vuota, usiamo l'alert custom
            self._view.show_alert("Nessun libro soddisfa i criteri di ricerca indicati.")
        else:
            # Se ci sono risultati, li aggiungiamo alla ListView
            for libro in libri:
                testo_libro = f"{libro.titolo} - {libro.autore} (Genere: {libro.genere})"
                self._view.lst_libri.controls.append(ft.Text(testo_libro))

        # Aggiorniamo l'interfaccia grafica per mostrare i cambiamenti
        self._view.update()
