from flask import Flask, escape, request, render_template
app = Flask(__name__)

purchases = [
    {
        'from': 'USD',
        'quantity_from': 100,
        'to': 'CUC',
        'quantity_to': 90,
        'date': 'April 20, 2020 - 12:00',
        'PU': 25
    },
    {
        'from': 'EUR',
        'quantity_from': 12,
        'to': 'USD',
        'quantity_to': 20,
        'date': 'April 2, 2020 - 14:00',
        'PU': 35
    },
    {
        'from': 'MN',
        'quantity_from': 1000,
        'to': 'CUC',
        'quantity_to': 40,
        'date': 'April 5, 2020 - 16:00',
        'PU': 45
    },
    {
        'from': 'EUR',
        'quantity_from': 1,
        'to': 'MN',
        'quantity_to': 24,
        'date': 'April 10, 2020 - 18:00',
        'PU': 60
    },
    {
        'from': 'MN',
        'quantity_from': 111,
        'to': 'MN',
        'quantity_to': 124,
        'date': 'April 1, 2020 - 11:00',
        'PU': 100
    },
    {
        'from': 'USD',
        'quantity_from': 900,
        'to': 'EUR',
        'quantity_to': 1000,
        'date': 'April 30, 2020 - 8:00',
        'PU': 50
    },
]

#*********************************************#
#*******************Router********************#
#*********************************************#
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        './home_view/home.html',
        title = 'Home',
        purchases = purchases
    )

@app.route('/purchase')
def purchase():
    return render_template('./purchase_view/purchase.html', title = 'Purchase')

@app.route('/status')
def about():
    return render_template('./status_view/status.html', title = 'Status')
#*********************************************#
#*********************************************#
#*********************************************#

if __name__ == '__main__':
    app.run(debug=True)