from flask import Flask, url_for, render_template, request, redirect
import classes as c

app = Flask(__name__)
p = c.create_person()
global i
i = 1 #have a [next day] button in the top tab as well as the current day

lst = ["","Sunday", "Saturday", "Friday", "Thurday", "Wednesday", "Tuesday", "Monday"]

@app.route('/', methods=['GET','POST'])
def base():
    return render_template('budget_menu.html')

@app.route('/add_finance',  methods=['GET', 'POST'])
def add_finance():
    category = request.form['finance_category']
    finance_price = request.form['finance_price']

    if (category.lower() in ["housing","transportation","food","utilities","clothing","healthcare","insurance","supplies","personal","debt","retirement","education","savings","donations","entertainment"]):
        try:
            finance_price = float(finance_price)
            p.add_finance(category,finance_price)
            if p.budget < 0:
                return render_template('finance_success.html') 
        except:
            return render_template('finance_failure.html') 


@app.route('/ask',  methods=['GET', 'POST'])    
def ask():
    if request.method == 'POST':
        ask_price = request.form['ask_price']
        try:
            m = float(ask_price)
            f = float(float(i)/7)
            if (m/float(p.budget)) < f:
                return render_template('ask_success.html') # Show text "go for it"
            else:
                return render_template('ask_fail.html') #Show text "nah"
        except:
            return render_template('error.html')

@app.route('/new_budget', methods=['GET', 'POST'])
def new_budget():
    if request.method == 'POST':
        new_budget = request.form['new_budget']
        try:
            new_budget = float(new_budget)
            p.new_budget(new_budget)
            return render_template('budget_success.html')
        except:
            return render_template('budget_failure.html')








if __name__ == "__main__":
    app.run(debug=True)
