from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    create_table_query = """
            create table Book (
                id integer primary key autoincrement,
                title varchar,
                pages int,
                author varchar,
                price float,
                release_year int
            );
        """
    query = text(create_table_query)

    # # Выполнение SQL-запроса с помощью метода `execute` на соединении
    connection.execute(query)