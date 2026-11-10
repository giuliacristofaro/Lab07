from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # da fare
    def get_all_generi(self) -> list[str]:
        """
        Recupera tutti i generi distinti presenti nel database per popolare il Dropdown.
        """
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
            return result

        try:
            cursor = cnx.cursor(dictionary=True)
            # Selezioniamo solo i generi, evitando i duplicati (DISTINCT)
            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
            cursor.execute(query)

            for row in cursor:
                result.append(row["genere"])

            cursor.close()
            cnx.close()
        except Exception as e:
            print(f"Errore DAO nella lettura dei generi: {e}")

        return result

    def get_libri_filtrati(self, id_biblioteca: int = None, genere: str = None) -> list[Libro]:
        """
        Recupera i libri dal database. Se id_biblioteca o genere sono None,
        la funzione SQL COALESCE() ignorerà quel filtro.
        """
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
            return result

        try:
            cursor = cnx.cursor(dictionary=True)

            # Utilizziamo COALESCE per gestire i filtri opzionali.
            # %s verrà sostituito da id_biblioteca o genere. Se passiamo None (che in SQL è NULL),
            # COALESCE(NULL, colonna) restituisce 'colonna', quindi colonna = colonna (sempre VERO).
            query = """
                SELECT * FROM libro 
                WHERE genere = COALESCE(%s, genere) 
                  AND id_biblioteca = COALESCE(%s, id_biblioteca)
            """

            # Passiamo i parametri alla query come tupla
            cursor.execute(query, (genere, id_biblioteca))

            for row in cursor:
                # Creiamo l'oggetto Libro con lo spacchettamento del dizionario
                libro = Libro(**row)
                result.append(libro)

            cursor.close()
            cnx.close()
        except Exception as e:
            print(f"Errore DAO nella lettura dei libri filtrati: {e}")

        return result
