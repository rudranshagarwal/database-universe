import pymysql
import subprocess as sp
import getpass
import questionary


Entity = ["Planet", "Moon", "Star", "Galaxy",
          "Commet", "Black-Hole", "Nebula"]


def insert_Planet():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new planet's details: ")

        row["Name"] = input("Name: ")
        row["Radius"] = input("Radius: ")
        row["N_moons"] = input("N_moons: ")
        row["Mass"] = input("Mass: ")

        query = "INSERT INTO Planet(Planet_Name, Planet_Radius, Nmoons, Planet_Mass) VALUES('%s', '%s', '%s', '%s')" % (
            row["Name"], row["Radius"], row["N_moons"], row["Mass"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Moon():
    try:
        # Takes emplyee details as input
        a = input("Enter Moon Name: ")
        b = (input("Enter Moon_radius: "))
        c = (input("Enter Moon Mass: "))
        d = input("Insert Planet Name: ")

        if(d == 'NULL'):
            print("Moon wont be added, planet does not exist")
        else:
            query2 = "Select * from Planet where Planet_Name = '%s'" % (d)
            x = cur.execute(query2)
            if x == 0:
                print("Moon wont be added, planet does not exist")
            else:
                query = "Insert into Moons values('%s', '%s', '%s', '%s')" % (
                    a, b, c, d)
                print(query)
                cur.execute(query)
                con.commit()
                print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    #


def star_supernova_to_black_hole():
    #
    try:
        # Takes emplyee details as input
        a = input("Enter Star name: ")
        query = "Delete from Star where Star_Name = '%s'" % (a)

        query3 = "Select Star_Radius from Star where Star_Name = '%s'" % (a)
        for row in con.execute(query3):
            print(row)

        query2 = "Insert into Black_Hole values('%s', '%s')" % (a, None)

        # print(query)

        # con.execute(query)
        # con.commit()

        # print("Star supernovaed to black hole")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Gravity():
    try:
        #Planet, Star, Moon, comet
        a = input("Enter Planet Name: ")
        b = input("Enter Star Name: ")
        c = input("Enter Moon name: ")
        d = input("Enter Comet_name: ")

        query = "Insert into Gravity values('%s', '%s', '%s', '%s')" % (
            a, b, c, d)

        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    #


def insert_Star():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new star's details: ")

        row["Name"] = input("Name: ")
        row["Radius"] = float(input("Radius: "))
        row["Brightness"] = float(input("Brightness: "))
        row["Type"] = input("Type: ")

        row["Revolving"] = input("Revolving Star: ")
        row["Max wavelength"] = float(input("Max wavelength: "))
        row["Avg wavelength"] = float(input("Avg wavelength: "))
        row["Min wavelength"] = float(input("Min wavelength: "))

        querycheck = "Select * FROM Brightness_type where Brightness = '%f'" % (
            row["Brightness"])

        y = cur.execute(querycheck)
        if(y == 0):
            brightnessquery = "INSERT INTO Brightness_type(Brightness, Type) VALUES ('%f', '%s')" % (
                row["Brightness"], row["Type"])
            cur.execute(brightnessquery)
            con.commit()
        flag = 0
        if(len(row["Revolving"]) == 0):

            query = "INSERT INTO Star(Star_Name, Star_Radius, Brightness, Maxlambda, Avglambda, Minlambda) VALUES('%s', '%lf', '%lf', '%f', '%f', '%f')" % (
                row["Name"], row["Radius"], row["Brightness"], row["Max wavelength"], row["Avg wavelength"], row["Min wavelength"])

        else:

            query3 = "Select * from Star where Star_Name = '%s'" % (
                row["Revolving"])
            x = cur.execute(query3)
            if x == 0:
                print("No corresponding revolving star found")
                query = "INSERT INTO Star(Star_Name, Star_Radius, Brightness, Maxlambda, Avglambda, Minlambda) VALUES('%s', '%lf', '%lf', '%f', '%f', '%f')" % (
                    row["Name"], row["Radius"], row["Brightness"], row["Max wavelength"], row["Avg wavelength"], row["Min wavelength"])

            else:
                query = "INSERT INTO Star (Star_Name, Star_Radius, Brightness, Maxlambda, Avglambda, Minlambda, Revolving_Star_Name) VALUES('%s', '%lf', '%lf', '%f', '%f', '%f', '%s')" % (
                    row["Name"], row["Radius"], row["Brightness"], row["Max wavelength"], row["Avg wavelength"], row["Min wavelength"], row["Revolving"])
                flag = 1

        print(query)
        cur.execute(query)
        con.commit()
        if(flag):
            queryreverse = "UPDATE Star SET Revolving_Star_Name = '%s' WHERE Star_Name = '%s' " % (
                row["Name"], row["Revolving"])
            cur.execute(queryreverse)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def insert_Galaxy():
    try:
        # Takes emplyee details as input
        a = input("Enter Galaxy Name: ")

        # Number of stars should be an update query

        c = int(input("Enter Galaxy Radius: "))
        query = "Insert into Galaxy values('%s', '%d', '%d')" % (a, 0, c)

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

    # wh]]


def insert_star_into_galaxy():
    try:
        a = input("Enter Star Name: ")
        b = input("Enter Galaxy Name: ")
        query = "Insert into Star_belongs_to_Galaxy values('%s', '%s')" % (
            a, b)
        query2 = "Select * from Star where Star_Name = '%s'" % (a)
        x = cur.execute(query2)
        query3 = "Select * from Galaxy where Galaxy_Name = '%s'" % (b)
        y = cur.execute(query3)
        if x == 0 or y == 0:
            print("Cannot add to database: Either star or galaxy does not exist")

        else:
            print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Comet():

    #
    try:
        a = input("Enter comet name: ")
        b = (input("Enter comet mass: "))
        c = input("Enter comet cycle: ")
        d = input("Enter star name: ")
        query2 = "Select * from Star where Star_Name = '%s'" % (d)
        x = cur.execute(query2)
        if x == 0:
            print("Cannot add to database: Star doesnt exist")
        else:
            query = "Insert into Comet values('%s', '%s', '%s', '%s')" % (
                a, b, c, d)
            print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Blackhole():

    #
    try:
        # Takes emplyee details as input
        a = input("Enter black hole name: ")
        b = input("Enter black hole event horizon: ")

        query = "Insert into Black_Hole values('%s', '%s')" % (a, b)

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Constellation():
    #
    try:
        # Takes emplyee details as input
        a = input("Enter Constellation name: ")
        b = input("Enter Star_Name1: ")
        c = input("Enter Star_Name2: ")
        query2 = "Select * from Star where Star_Name = '%s'" % (b)
        x = cur.execute(query2)
        query3 = "Select * from Star where Star_Name = '%s'" % (c)
        y = cur.execute(query3)
        if x == 0 or y == 0:
            print("Cannot add to database: At least one Star does not exist")
        else:
            query = "Insert into Constellation values('%s', '%s', '%s')" % (
                a, b, c)
            print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Planet_Revolves_Around_Star():
    try:
        # Takes emplyee details as input
        a = input("Enter Planet name: ")
        b = input("Enter Star name: ")

        query = "Insert into Planet_Revolves_Star values('%s', '%s')" % (a, b)
        query2 = "Select * from Planet where Planet_Name = '%s'" % (a)
        x = cur.execute(query2)
        query3 = "Select * from Star where Star_Name = '%s'" % (b)
        y = cur.execute(query3)
        if x == 0 or y == 0:

            print("Cannot add to database: Either Planet or Star does not exist")
        else:
            print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    #


def insert_Blackhole_centers_Galaxy():

    #
    try:
        # Takes emplyee details as input
        a = input("Enter black hole name: ")
        b = input("Enter galaxy name: ")
        query2 = "Select * from Black_Hole where Black_Hole_name = '%s'" % (a)
        x = cur.execute(query2)
        query3 = "Select * from Galaxy where Galaxy_Name = '%s'" % (b)
        y = cur.execute(query3)
        if x == 0 or y == 0:
            print("Cannot add to database: Either black hole or galaxy does not exist")
        else:
            query = "Insert into Black_hole_centers_galaxy values('%s', '%s')" % (
                a, b)
            print(query)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def insert_Nebula():
    try:
        # Takes emplyee details as input
        a = input("Enter Nebula name: ")
        b = input("Enter Nebula type: ")
        c = float(input("Enter Nebula apparent magnitude: "))
        d = input("Enter Nebula colors").split(",")

        query = "Insert into Nebula values('%s', '%s', '%f')" % (a, b, c)
        print(query)
        cur.execute(query)
        con.commit()
        e = len(d)
        i = 0
        while i < e:
            f = d[i]
            query = "Insert into Nebula_color values('%s', '%s')" % (a, f)
            i = i + 1
            print(query)
            cur.execute(query)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    #


def update_Planet():
    print("Update Planet")

    #


def update_Moon():
    print("Update Moon")
    #


def update_Star():
    print("Update Star")

    #


def update_Galaxy():
    print("Update Galaxy")

    #


def update_Comet():
    print("Update Comet")

    #


def update_Blackhole():
    print("Update Blackhole")

    #


def update_Nebula():
    print("Update Nebula")

    #


def delete_Planet():
    try:
        row = {}
        print("Name of the planet you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Planet WHERE Planet_Name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()

        print("deleted planet")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    #


def Update_Star_Radius():
    try:
        row = {}
        row["Name"] = input("Enter Star Name: ")
        row["Radius"] = input("Enter new radius: ")
        querycheck = "SELECT * FROM Star where Star_Name = '%s' " % (
            row["Name"])
        x = cur.execute(querycheck)
        if(x == 0):
            print("No star with name")
        else:
            query = "UPDATE Star SET Star_Radius = '%s' WHERE Star_Name = '%s' " % (
                row["Radius"], row["Name"])
            print("Radius changed")
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to access database")
        print(">>>>>>>>>>>>>", e)


def delete_Moon():
    try:
        row = {}
        print("Name of the Moon you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Moons WHERE Moon_name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()

        print("deleted Moon")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    #


def update_Galaxy_Radius():
    try:
        row = {}
        row["Name"] = input("Enter Galaxy Name: ")
        row["Radius"] = input("Enter new radius: ")
        querycheck = "SELECT * FROM Galaxy where Galaxy_Name = '%s' " % (
            row["Name"])
        x = cur.execute(querycheck)
        if(x == 0):
            print("No galaxy with name")
        else:
            query = "UPDATE Galaxy SET Galaxy_Radius = '%s' WHERE Galaxy_Name = '%s' " % (
                row["Radius"], row["Name"])
            print("Radius changed")
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to access database")
        print(">>>>>>>>>>>>>", e)


def delete_Star():
    try:
        row = {}
        print("Name of the Star you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Star WHERE Star_Name = '%s'" % (
            row["Name"])
        cur.execute(query)
        con.commit()

        print("deleted Star")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    #


def delete_Galaxy():
    try:
        row = {}
        print("Name of the Galaxy you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Galaxy WHERE Galaxy_Name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()

        print("deleted Galaxy")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    #


def N_Galaxy():
    try:
        query = "SELECT * FROM Galaxy"
        x = cur.execute(query)
        con.commit()
        print("Number of galaxies: ", end='')
        print(x)
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def N_Star():
    try:
        query = "SELECT * FROM Star"
        x = cur.execute(query)
        con.commit()
        print("Number of stars: ", end='')
        print(x)
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def N_Planet():
    try:
        query = "SELECT * FROM Planet"
        x = cur.execute(query)
        con.commit()
        print("Number of planets: ", end='')
        print(x)
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def N_Black_Hole():
    try:
        query = "SELECT * FROM Black_Hole"
        x = cur.execute(query)
        con.commit()
        print("Number of black holes: ", end='')
        print(x)
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def Get_Moon_R():
    try:
        row = {}
        row["Moon"] = input("Enter Moon: ")
        query = "SELECT * FROM Moons where Moon_name = '%s'" % (row["Moon"])
        x = cur.execute(query)
        if(x == 0):
            print("Invalid Moon")
        else:
            row = cur.fetchall()
            print(row[0]["Planet_Name"])

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def Get_Comet_R():
    try:
        row = {}
        row["Comet"] = input("Enter Comet: ")
        query = "SELECT * FROM Comet where Comet_name = '%s'" % (row["Comet"])
        x = cur.execute(query)
        if(x == 0):
            print("Invalid Comet")
        else:
            row = cur.fetchall()
            print(row[0]["Star_Name"])

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def Get_Star_Radius():
    try:
        row = {}
        row["Star"] = input("Enter Star: ")
        query = "SELECT * FROM Star where Star_name = '%s'" % (row["Star"])
        x = cur.execute(query)
        if(x == 0):
            print("Invalid Star")
        else:
            row = cur.fetchall()
            print(row[0]["Star_Radius"])

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def delete_Comet():
    try:
        row = {}
        print("Name of the Comet you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Comet WHERE Comet_name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()
        print("deleted Comet")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    #


def G_Max_Stars():
    try:
        query = "SELECT * Star_Name from Star Order BY Star_Radius ASC LIMIT 1"

        cur.execute(query)
        row = cur.fetchall()
        con.commit()
        print("deleted Comet")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def delete_Blackhole():
    try:
        row = {}
        print("Name of the Blackhole you want to delete")

        row["Name"] = input("Name: ")

        query = "DELETE FROM Black_Hole WHERE Black_Hole_Name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()

        print("deleted Blackhole")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    #


def delete_Nebula():
    try:
        row = {}
        print("Name of the Nebula you want to delete")

        row["Name"] = input("Name: ")
        query = "DELETE FROM Nebula(Nebula_Name) VALUES('%s')" % (row["Name"])
        query = "DELETE FROM Nebula WHERE Nebula_Name = '%s'" % (
            row["Name"])

        cur.execute(query)
        con.commit()

        print("deleted Nebula")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def Insert():
    print("Here we have the following options")
    print("Planet Moon Star Galaxy Comet Black_Hole Nebula")
    print("1 Blackhole_centers_Galaxy")
    print("2 Constellation")
    print("3 Gravity")
    print("4 Planet revoles star")
    print("5 Star belongs to galaxy")

    y = input()
    if y == "Planet":
        insert_Planet()
    elif y == "Moon":
        insert_Moon()
    elif y == "Star":
        insert_Star()
    elif y == "Galaxy":
        insert_Galaxy()
    elif y == "Comet":
        insert_Comet()
    elif y == "Black_Hole":
        insert_Blackhole()
    elif y == "Nebula":
        insert_Nebula()
    elif y == "1":
        insert_Blackhole_centers_Galaxy()
    elif y == "2":
        insert_Constellation()
    elif y == "3":
        insert_Gravity()
        # this
    elif y == "4":
        insert_Planet_Revolves_Around_Star()
        # this
    elif y == "5":
        insert_star_into_galaxy()
        # this


def update():
    print("Here we have the following options")
    print("Planet Moon Star Galaxy Comet Black_Hole Nebula")
    y = input()
    if y == "Planet":
        update_Planet()
    elif y == "Moon":
        update_Moon()
    elif y == "Star":
        update_Star()
    elif y == "Galaxy":
        update_Galaxy()
    elif y == "Comet":
        update_Comet()
    elif y == "Black-Hole":
        update_Blackhole()
    elif y == "Nebula":
        update_Nebula()


def Delete():
    print("Here we have the following options")
    print("Planet Moon Star Galaxy Comet Black_Hole Nebula")
    y = input()
    if y == "Planet":
        delete_Planet()
    elif y == "Moon":
        delete_Moon()
    elif y == "Star":
        delete_Star()
    elif y == "Galaxy":
        delete_Galaxy()
    elif y == "Comet":
        delete_Comet()
    elif y == "Black-Hole":
        delete_Blackhole()
    elif y == "Nebula":
        delete_Nebula()


def Selection():
    print("You have come to Selection Commands")
    print("Options available")
    print("1 Get_planets_around_star: Get all the planets orbiting a star")
    print("2 Get_center_black_hole: Get all black holes which center a galaxy.")
    x = input("1 or 2")

    if x == 1:
        Get_planets_around_star()
    elif x == 2:
        Get_center_black_hole()


def Projection():
    print("You have come to Projection Commands")
    print("Options available")
    print("1 Get_stars_above_radius: get the stars whose radius is above the given value.")
    print("2 Get_overlapping_star_spectrum")
    x = input("1 or 2")

    if x == 1:
        Get_planets_around_star()
    # elif x == 2:
    #     Get_overlapping_star_spectrum()


def S_Max_Radius():
    query = "Select Star_Name , Star_Radius FROM Star ORDER BY Star_Radius  DESC LIMIT 1 "

    x = cur.execute(query)
    row = cur.fetchall()
    print(row[0])

    con.commit()


def P_Max_Radius():
    print("Buffer")


def M_Max_Radius():
    print("Buffer")


def Avg_Star_Radius():
    print("Buffer")


def Aggregate():
    print("You have come to Aggregate Commands")
    print("Options available")
    print("1 Galaxy with max stars")
    print("2 Get_star_with_longest_radius")
    print("3 Get_Planet_with_longest_radius")
    print("4 Get_Moon_with_longest_radius")
    print("5 Get_Average_of_stars")
    x = input("1 or 2 or 3 or 4 or 5")

    if x == 1:
        G_Max_Stars()
    elif x == 2:
        S_Max_Radius()
    elif x == 3:
        P_Max_Radius()
    elif x == 4:
        M_Max_Radius()
    elif x == 5:
        Avg_Star_Radius()


def Complete_star_name():
    print("Buffer")


def Search():
    print("In this command we have : returns all stars whose name contains the given string")
    Complete_star_name()


def Analysis():
    print("You have entered Analysis Command")


def Others():
    print("You have entered Other Command")
    print("We have the following options")
    print("1. Get total number of galaxies")
    print("2. Get total number of stars,")
    print("3. Get total number of Planets,")
    print("4. Get total number of Black Holes")
    print("5. Gets the name of the planet the moon is revolving around")
    print("6. Gets the name of the star the comet is revolving around")
    print("7 Star Radius")

    x = input("1 .. 7: ")

    if x == "1":
        N_Galaxy()
    elif x == "2":
        N_Star()
    elif x == "3":
        N_Planet()
    elif x == "4":
        N_Black_Hole()
    elif x == "5":
        Get_Moon_R()
    elif x == "6":
        Get_Comet_R()
    elif x == "7":
        Get_Star_Radius()


def Command(x):
    if x == "1":
        Selection()
    elif x == "2":
        Projection()
    elif x == "3":
        Aggregate()
    elif x == "4":
        Search()
    elif x == "5":
        Insert()
    elif x == "6":
        update()
    elif x == "7":
        Delete()
    elif x == "8":
        Analysis()
    elif x == "9":
        Others()
    else:
        print("The given command does not exist")

# making other functions


def Get_planets_around_star():
    S_name = input("Star_Name_Please")

    query = "Select Planet_Name FROM Planet_Revolves_Star WHERE Star_Name = '%s" % (
        S_name)
    cur.execute(query)
    con.commit()

    # this will return all stars around a planet
    print("Buffer")


def Get_center_black_hole():
    B_name = input("Black_Hole_Name_Please")

    query = "Select Black_Name FROM Black_hole_centers_galaxy WHERE Galaxy_Name = '%s" % (
        B_name)
    cur.execute(query)
    con.commit()

    print("Buffer")


def Get_stars_above_radius():
    R_radius = input("Enter the radius")

    query = "Select Star_Name FROM Star WHERE Star_Radius > '%s" % (R_radius)

    print("stars whose radius is more than this")
    cur.execute(query)
    con.commit()


def Get_overlappig_star_spectrum():
    # doubt here
    print("overlapping")


if __name__ == "__main__":
    
    

    looper = True
    while(1):
        # tmp = sp.call('clear', shell=True)

        # Can be skipped if you want to hardcode username and password
        username = input("Username: ")
        password = getpass.getpass(prompt="Password: ")

        try:
            # Set db name accordingly which have been create by you
            # Set host to the server's address if you don't want to use local SQL server
            con = pymysql.connect(host='localhost',
                                  port=3306,
                                  user=username,
                                  password=password,
                                  db='UNIVERSE2',
                                  cursorclass=pymysql.cursors.DictCursor)
            # tmp = sp.call('clear', shell=True)
        except Exception as e:
            # tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")
        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                # print("What do you want to do ?")
                # print("We have the following options :")
                # print("1 Selection")
                # print("2 Projection")
                # print("3 Aggregate")
                # print("4 Search")
                # print("5 Insertion")
                # print("6 Update")
                # print("7 Delete")
                # print("8 Analysis")
                # print("9 Other")
                options = {
                    "Selection": Selection,
                    "Projection": Projection,
                    "Aggregate": Aggregate,
                    "Search": Search,
                    "Insertion": Insert,
                    "Update":update,
                    "Delete": Delete,
                    "Analysis": Analysis,
                    "Other": Others,
                }
                to_do = questionary.select("What do you want to do?", options).ask()
                try:
                    options[to_do]()
                except KeyError:
                    break

        x = input()
        Command(x)
        #     Command()
        tmp = input("Enter any key to CONTINUE>")


    print("Welcome to our universe")

    looper = True

    while(looper):
        print("What do you want to do ?")
        print("We have the following options :")
        print("1 Selection")
        print("2 Projection")
        print("3 Aggregate")
        print("4 Search")
        print("5 Insertion")
        print("6 Update")
        print("7 Delete")
        print("8 Analysis")
        print("9 Other")

        x = input()
        Command(x)
