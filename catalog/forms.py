from django import forms

from catalog.models import Product, Version


class MixinFormStile:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(MixinFormStile, forms.ModelForm):

    def clean(self):
        clean_data = super().clean()
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(
                    'Недопустимое значение имени товара или описания (включены запрещённые слова)')
        return clean_data

    class Meta:
        model = Product
        exclude = ('last_change',)


class VersionForm(MixinFormStile, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

