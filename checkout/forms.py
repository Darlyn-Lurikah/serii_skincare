from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    # Which models OrderForm associates with
    # Which fields to render
    class Meta:
        model = Order
        # No autocalc form fields
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Overriding form init method to 
    # customise form
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # Call default init method. Shows 
        # form in default state
        super().__init__(*args, **kwargs)

        # Dict of placeholders to show in form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Makes cursor start in full_name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Iterate through & add * if required form fields 
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Set form fields to dict placeholders (above)
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add css class 
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove field label as We're using placeholders 
            self.fields[field].label = False