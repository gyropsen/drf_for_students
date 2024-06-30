import requests
import stripe

from config.settings import APILAYER_API_KEY, STRIPE_API_KEY

# This is your test secret API key.
stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(amount):
    """Конвертировать рубли в доллары"""
    url = "https://api.apilayer.com/exchangerates_data/latest?base=USD"
    response = requests.get(url, headers={"apikey": APILAYER_API_KEY})
    if response.status_code == 200:
        rate = response.json()["rates"]["RUB"]
        return int(amount / rate)


def create_stripe_price(amount):
    """Создать цену в страйп"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "payment_name"},
    )


def create_stripe_session(price):
    """Создание сессии на отплату в страйп"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def check_payment(session_id):
    stripe.checkout.Session.retrieve(session_id)
