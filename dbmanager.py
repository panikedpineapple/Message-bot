import sqlite3

import discord


class DBManager():

    def __init__(self, dbfile: str):
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()
        self.create_table()


    def create_table(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Messages(id INT ,
                                author INT,
                                channel INT,
                                content TEXT,
                                created_at TEXT,
                                replyid INT,
                                guild INT);
                                """)
        self.connection.commit()

    def add_message(self, message: discord.Message):


        try:
            rid = message.reference.message_id
        except:
            rid = 0
        message_data = (message.id, message.author.id, message.channel.id, message.content,
                        message.created_at.strftime('%d-%m-%Y %T.%f'),
                        rid, message.guild.id)

        try:
            self.cursor.execute("INSERT INTO Messages VALUES(?,?,?,?,?,?,?);", message_data)
            self.connection.commit()
        except Exception as e:
            print(e)
            print("ERROR inserting message into table.")

    def get_message_by_count(self, count: int):

        command = f'SELECT * FROM Messages ORDER BY id DESC LIMIT {count}'
        data = self.cursor.execute(command).fetchall()
        final = []
        for a in data:
            v = {'id' : a[0],
                 'author' : a[1],
                 'channel' : a[2],
                 'content' : a[3],
                 'created_at' : a[4],
                 'replyid' : a[5],
                 'guild_id' : a[6]}
            final.append(v)

        self.connection.close()
        return final

    def get_message_by_id(self,id):
        a = self.cursor.execute(f"SELECT * FROM Messages WHERE id={id}").fetchone()
        data = {'id' : a[0],
                 'author' : a[1],
                 'channel' : a[2],
                 'content' : a[3],
                 'created_at' : a[4],
                 'replyid' : a[5],
                 'guild_id' : a[6]}

        self.connection.close()
        return data
