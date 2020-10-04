from flask import Flask, url_for, render_template, request, redirect
import classes as c




app = Flask(__name__)

global i
i = 1 #have a [next day] button in the top tab as well as the current day

lst = ["","Sunday", "Saturday", "Friday", "Thurday", "Wednesday", "Tuesday", "Monday"]

@app.route('/', methods=['GET', 'POST'])
def base():
    global p
    if request.method == 'POST':
        username = request.form['username']
        t = c.in_class(username.lower())
        if t[0]:
            p = t[1]
        else:
            p = c.create_person(username.lower())
        return redirect(url_for('budget_menu'))
    return render_template('home.html')

@app.route('/budget_menu', methods=['GET', 'POST'])
def budget_menu():
    return render_template('budget_menu.html') #make pretty


@app.route('/add_finance',  methods=['GET', 'POST'])
def add_finance():
    return render_template('add_finance.html') #make drop down menu with the text box next to it

@app.route('/ask',  methods=['GET', 'POST'])    
def ask():
    if request.method == 'POST':
        price = request.form['price']
        try:
            m = float(price)
            f = float(float(i)/7)
            if (m/float(p.budget)) < f:
                return redirect(url_for('success')) # Show text "go for it"
            else:
                return redirect(url_for('error')) #Show text "nah"
        except:
            return redirect(url_for('error'))
    return render_template('ask.html')

@app.route('/new_budget', methods=['GET', 'POST'])
def new_budget():
    if request.method == 'POST':
        new_budget = request.form['new_budget']
        try:
            new_budget = int(new_budget)
            p.new_budget(new_budget)
            return redirect(url_for('success'))
        except:
            return redirect(url_for('error'))

    return render_template('new_budget.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')








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


        # elif t.lower() == "budget":
        #     c.new_bud(c.p[0])


        # elif t.lower() == "ask":
        #     m = c.inpt("Price: ")               #need help with algorithm
        #     try:
        #         m = float(m)
        #         p = float(i/7)
        #         if (m/float(c.p[0].budget)) < p:
        #             print("Go For It")
        #         else:
        #             print("Nah")
        #     except:
        #         print("Invalid")


        elif t.lower() == "next day":
            i += 1
            if i == 7:
                i = 1
            print(lst[i])
    


        elif t.lower() == "quit":
            break


        else:
            pass

        
