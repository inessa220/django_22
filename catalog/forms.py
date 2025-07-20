from django.forms import ModelForm, BooleanField
from catalog.models import Product
from django.core.validators import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def clean_name(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data["name"].strip().lower()
        for word in forbidden_words:
            if word in name:
                raise ValidationError(
                    f"{word} нельзя использовать в названии продукта."
                )
        return self.cleaned_data["name"]

    def clean_description(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description = self.cleaned_data["description"].strip().lower()
        for word in forbidden_words:
            if word in description:
                raise ValidationError(
                    f"{word} нельзя использовать в описании продукта."
                )
        return self.cleaned_data["description"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price
