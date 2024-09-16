from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Set your Stripe secret key
stripe.api_key = 'sk_test_51PzkEoCORWJITDO5g6kcYyZNjOTXOGGNpMiE0mAfTAhZSpkOYUA7LtGLqE3jee6CKcjOuJ5BtKetQwHpcBooiUn800J4YaB9yU'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    YOUR_DOMAIN = "http://localhost:8080"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Flashcard Set',
                    },
                    'unit_amount': 5000,  # $50.00
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return jsonify({'id': checkout_session.id})

@app.route('/success')
def success():
    return "Payment successful!"

@app.route('/cancel')
def cancel():
    return "Payment canceled."

if __name__ == '__main__':
    app.run(port=8080)
