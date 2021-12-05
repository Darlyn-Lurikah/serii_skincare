from django.http import HttpResponse


class StripeWH_Handler:
    """Custom class to Handle Stripe webhooks"""

    def __init__(self, request):
        """ Assigning as class attr, lets us access
        request attr from Stripe
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
