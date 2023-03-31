import mysql.connector

cnx = mysql.connector.connect(user='root', password='hui123',

host='127.0.0.1',database="userinfo")

mycursor = cnx.cursor()
sql = 'insert into userinformation(name,sex,weight,height,likecolor) values (%s,%s,%s,%s,%s)'
val = ('张佳辉','男','130','190','bluesky')
for c in range(10):
    mycursor.execute(sql,val)

cnx.commit()



