from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        # Get values from the form
        linda_ironing = float(request.form.get('linda_ironing', 0))
        linda_washing = float(request.form.get('linda_washing', 0))
        linda_cashier = float(request.form.get('linda_cashier', 0))
        linda_packing = float(request.form.get('linda_packing', 0))

        # Given values
        full_bonus = 15000  # IDR
        ironing_full = 50  # kg
        washing_full = 70  # kg
        cashier_full = 80  # kg
        packing_full = 70  # kg

        # Calculate bonuses
        ironing_bonus = (linda_ironing / ironing_full) * full_bonus
        washing_bonus = (linda_washing / washing_full) * full_bonus
        cashier_bonus = (linda_cashier / cashier_full) * full_bonus
        packing_bonus = (linda_packing / packing_full) * full_bonus

        # Total bonus
        total_bonus = ironing_bonus + washing_bonus + cashier_bonus + packing_bonus
        output = "maxed out (15k)" if total_bonus > 15000 else total_bonus

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
