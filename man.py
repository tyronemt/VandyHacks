from flask import Flask, url_for, render_template, request, redirect
import classes as c


app = Flask(__name__)

i = 7 #have a next day button in the top tab as well as the current day

lst = ["","Sunday", "Saturday", "Friday", "Thurday", "Wednesday", "Tuesday", "Monday"]

@app.route('/', methods=['GET', 'POST'])
def base():
    global p
    if request.method == 'POST':
        username = request.form['username']
        t = c.in_class(username)
        if t[0]:
            p = t[1]
        else:
            p = c.create_person(username)
        return redirect(url_for('budget_menu'))
    return render_template('home.html')

@app.route('/budget_menu', methods=['GET', 'POST'])
def budget_menu():
    return render_template('budget_menu.html')


@app.route('/add_finance',  methods=['GET', 'POST'])
def add_finance():
    return render_template('add_finance.html')

@app.route('/ask',  methods=['GET', 'POST'])
def ask():
    return render_template('ask.html')

@app.route('/new_budget', methods=['GET', 'POST'])
def new_budget():
    return render_template('new_budget.html')










if __name__ == "__main__":
    app.run(debug=True)

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

        
