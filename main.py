import classes as c

if __name__ == "__main__":
    c.create_person()
    i = 7
    lst = ["","Sunday", "Saturday", "Friday", "Thurday", "Wednesday", "Tuesday", "Monday"]
    print(lst[i])
    while True:
        t = c.inpt("Enter Finance Category, 'ask', 'budget','next day',  or 'quit': ")


        if (t.lower() in ["housing","transportation","food","utilities","clothing","healthcare","insurance","supplies","personal","debt","retirement","education","savings","donations","entertainment"]):
            m = c.inpt("Enter Price: ")
            try:
                m = int(m)
                c.p[0].add_finance(t,m)
                if c.p[0].budget < 0:
                    print("You spent way too much !")
            except:
                print("Invalid")


        elif t.lower() == "budget":
            c.new_bud(c.p[0])


        elif t.lower() == "ask":
            m = c.inpt("Price: ")               #need help with algorithm
            try:
                m = float(m)
                p = float(1/float(i))
                if (m/float(c.p[0].budget)) < p:
                    print("Go For It")
                else:
                    print("Nah")
            except:
                print("Invalid")


        elif t.lower() == "next day":
            i-=1
            if i == 0:
                i = 7
            print(lst[i])
    


        elif t.lower() == "quit":
            break


        else:
            pass

        
