from myshop.celery import app  # Use your Celery app instance
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = (
        f"Dear {order.first_name},\n\n"
        f"You have successfully placed an order."
        f"Your order ID is {order.id}."
    )
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
