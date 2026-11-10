from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # da fare
    def get_all_biblioteche(self) -> list[Biblioteca]:
        """
        Recupera tutte le biblioteche dal database.
        Ritorna una lista di oggetti Biblioteca.
        """
        # Richiediamo la connessione al database
        cnx = DBConnect.get_connection()
        result = []

        # Se la connessione fallisce, ritorniamo una lista vuota
        if cnx is None:
            print("Connessione fallita")
            return result

        try:
            # dictionary=True ci permette di ricevere i risultati come un dizionario
            # in cui le chiavi sono i nomi delle colonne della tabella
            cursor = cnx.cursor(dictionary=True)

            # Scriviamo ed eseguiamo la query SQL
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)

            # Iteriamo sui risultati
            for row in cursor:
                # Creiamo un oggetto Biblioteca spacchettando il dizionario (**row)
                biblioteca = Biblioteca(**row)
                result.append(biblioteca)

            # Chiudiamo cursore e connessione alla fine
            cursor.close()
            cnx.close()

        except Exception as e:
            print(f"Errore DAO nella lettura delle biblioteche: {e}")

        return result
