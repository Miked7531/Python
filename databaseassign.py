import sqlite3
conn = sqlite3.connect('dba.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()
#conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_filename)VALUES(?)",(file,))
    conn.commit()
#conn.close()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files")
    files = cur.fetchall()
    print(files)
conn.close()
    
