from django import forms

from catalog.models import Product, Version


class MixinFormStile:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(MixinFormStile, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        if name is not None and description is not None:
            for word in self.forbidden_words:
                if word in name.lower():
                    self.add_error('name', forms.ValidationError(
                        'Недопустимое значение имени товара (включены запрещённые слова)', code='name_error'))
                if word in description.lower():
                    self.add_error('description', forms.ValidationError(
                        'Недопустимое значение описания товара (включены запрещённые слова)', code='description_error'))
        return cleaned_data

    class Meta:
        model = Product
        exclude = ('last_change', 'owner',)


class VersionForm(MixinFormStile, forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        product = self.cleaned_data.get('product')
        status = cleaned_data.get('status')
        if status == "активна":
            if len(Version.objects.filter(status='активна', product=product).exclude(id=self.instance.id)) == 1:
                self.add_error('status', forms.ValidationError(
                    'Возможна лишь одна активная версия. Пожалуйста, активируйте только 1 версию.',
                    code='status_error'))
        return cleaned_data

    class Meta:
        model = Version
        fields = '__all__'
