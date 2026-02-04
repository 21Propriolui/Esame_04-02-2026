from database.DB_connect import DBConnect
from model.artist import Artist
from model.connessioni import Connessioni


class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT * 
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_roles():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ 
                SELECT DISTINCT role
                FROM authorship
                ORDER BY role
                """
        cursor.execute(query)

        for row in cursor:
            result.append(row['role'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artists_by_role(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT DISTINCT ar.artist_id as id, ar.name as name, COUNT(DISTINCT o.object_id) as indice
                FROM artists ar, authorship au, objects o
                WHERE ar.artist_id = au.artist_id and o.object_id = au.object_id
                AND au.role = %s
                AND o.curator_approved = 1
                GROUP BY ar.artist_id, ar.name
                """
        cursor.execute(query, (ruolo,))

        for row in cursor:
            artist = Artist(**row)
            result.append(artist)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connected_artists(ruolo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT ar1.artist_id id1,ar2.artist_id id2, COUNT(DISTINCT o1.object_id) indice
                FROM artists ar1, artists ar2, authorship au1, authorship au2, objects o1, objects o2
                where ar1.artist_id = au1.artist_id and au1.object_id = o1.object_id 
                and ar2.artist_id = au2.artist_id and au2.object_id = o2.object_id
                and ar1.artist_id < ar2.artist_id 
                and o1.curator_approved = o2.curator_approved
                and o1.curator_approved = 1
                and au1.role = au2.role
                and au1.role = %s
                group by ar1.artist_id, ar2.artist_id
                """
        cursor.execute(query, (ruolo,))

        for row in cursor:
            artist = Connessioni(**row)
            result.append(artist)

        cursor.close()
        conn.close()
        return result