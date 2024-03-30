import sqlite3
import contextlib

def add_to_table(conn, table, **data):
    columns = []
    values = tuple()
    for k, v in data.items():
        columns.append(k)
        values += (v,)
    columns_str = ', '.join(columns)
    values_str = ', '.join(["?" for _ in values])

    sql = f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    return cur.lastrowid

def select_where(conn, table, **query):
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f'{k}=?')
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f'SELECT * FROM {table} WHERE {q}', values)
    rows = cur.fetchall()
    print(rows)


def update(conn, table, id, **kwargs):
    param = [f'{k}=?' for k in kwargs]
    param = ', '.join(param)
    values = tuple(v for v in kwargs.values())
    values += (id,) 

    sql = f"""
        UPDATE {table}
        SET {param}
        WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def delete_where(conn, table, **kwargs):
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f'{k}=?')
        values += (v,)
    q = " AND ".join(qs)

    sql = f"DELETE FROM {table} WHERE {q}"
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

if __name__ == "__main__":

    db_file = 'test_database.db'

    create_marka_table = """
                    CREATE TABLE Marka(
                    id integer PRIMARY KEY,
                    nazwa varchar(255) NOT NULL,
                    kraj_poch varchar(255)
                    );
                    """
    create_car_table = """
                    CREATE TABLE Auto(
                    id integer PRIMARY KEY,
                    marka_id integer,
                    model varchar(255) NOT NULL,
                    color varchar(255),
                    FOREIGN KEY (marka_id) REFERENCES Marka(id)
                    );
"""


    with contextlib.closing(sqlite3.connect(db_file)) as conn:
        cur = conn.cursor()
    # Tworzenie Relacji

        #cur.execute(create_marka_table)
        #cur.execute(create_car_table)

    # Dodawanie Atrybutów
        
        #mark_id = add_to_table(conn, "Marka", nazwa="Audi", kraj_poch="Niemcy")

        #car = add_to_table(conn, "Auto", marka_id=mark_id, model="A5", color="Black")
        #car2 = add_to_table(conn, "Auto", marka_id=mark_id, model="A5", color="Yellow")

    # Odczytywanie Atrybutów
        
        #select_where(conn,"Auto", color="Black")
        #conn.commit()

    # Updatowanie wartości w relacji
        
        #update(conn, "Auto", 2, color="Green")

    # Usuwanie 
        
        #delete_where(conn, "Auto", id=1)