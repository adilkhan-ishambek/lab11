import psycopg2


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


while True:
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="29032003"
    )
    sql = 'select * from MyContacts '
    cursor = conn.cursor()
    cursor.execute(sql)
    MyContacts = cursor.fetchall()
    n = input()
    if n == 'sorted data':
        a = MyContacts
        a.sort(key=lambda tup: tup[0], reverse=False)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if n == 'reversed sorted data':
        a = MyContacts
        a.sort(key=lambda tup: tup[0], reverse=True)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if str(n) == 'data':

        for i in MyContacts:
            for j in i:
                print(j, end=' ')
            print()

    elif str(n) == 'insert':
        nn = input().split(" ")
        a = len(nn)
        i = 0
        while i < a:

            sql = f'select * from MyContacts where name = \'{nn[i]}\''
            cursor = conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            # print(res)
            # cursor.execute(f"DELETE FROM MyContacts WHERE name='{nn[i]}'")
            # print(nn[i])
            if is_int(nn[i + 1]):

                if not res:

                    cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (nn[i], nn[i + 1]))
                    # print(nn)
                    print("New user is added")
                    conn.commit()
                else:
                    cursor.execute(f"DELETE FROM MyContacts WHERE name='{nn[i]}'")
                    cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (nn[i], nn[i + 1]))
                    conn.commit()
                    print("User is updated")
                #print(MyContacts)
                i += 2

            else:
                print("Phone Error")
                i += 2
    elif str(n) == 'delete':
        nn = input().split(" ")
    
        for i in nn:
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{i}'")

        conn.commit()
    elif str(n) == "update":
        nn = input()
        if is_int(nn):
            m = input()
            #print(nn)
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{m}'")
            cursor.execute(f"DELETE FROM MyContacts WHERE phonenumber='{nn}'")
            cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (m, nn))
            conn.commit()
        else:
            m = input()
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{nn}'")
            cursor.execute(f"DELETE FROM MyContacts WHERE phonenumber='{m}'")
            cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (nn, m))
            conn.commit()
    elif str(n) == 'find person':
        mm = str(input())
        b = []

        for i in MyContacts:
            if mm.lower() in i[0].lower():
                b.append(i)
        print(b)
       