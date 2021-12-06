from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        exclude = ('user',)

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
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State',
        }

        # Makes cursor start in full_name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Iterate through & add * if required form fields
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # Set form fields to dict placeholders (above)
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add our css class
            self.fields[field].widget.attrs['class'] = 'rounded-0 profile-form-input'
            # Remove field label as We're using placeholders
            self.fields[field].label = False
