import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # da fare
        self.dd_biblioteca = ft.Dropdown(
            label="Seleziona Biblioteca",
            width=300,
            options=[],
            on_select=self.controller.leggi_biblioteca
        )

        self.dd_genere = ft.Dropdown(
            label="Seleziona Genere",
            width=300,
            options=[],
            on_select=self.controller.leggi_genere
        )

        # Riga per disporre i filtri orizzontalmente
        row_filtri = ft.Row(
            controls=[self.dd_biblioteca, self.dd_genere],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        # Sezione 3: Libri
        # da fare
        self.btn_mostra = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri
        )

        self.lst_libri = ft.ListView(
            expand=True,
            spacing=10,
            height=400  # Altezza per gestire lo scroll dei libri
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # da fare
            row_filtri,
            ft.Container(height=10),  # Spazio vuoto

            # Sezione 3: Libri
            # da fare
            self.btn_mostra,
            self.lst_libri
        )

        # Popoliamo i menu a tendina chiedendolo al controller prima di fare l'update finale della pagina
        if self.controller:
            self.controller.popola_dropdowns()

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
