from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Override ready method to call
    # custom update_total method, updating
    # order totals automatically
    def ready(self):
        import checkout.signals
