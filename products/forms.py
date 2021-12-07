from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    # Defines model and desired fields
    class Meta:
        model = Product
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        # Override init to make field changes
        super().__init__(*args, **kwargs)
        # Get all categories
        categories = Category.objects.all()
        # Create list of tuples of friendly category names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use firendly names not catergory ids
        self.fields['category'].choices = friendly_names
        # Iterate through category fields to match theme
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'