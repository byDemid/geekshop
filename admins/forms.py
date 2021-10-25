from django import forms
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

from products.models import ProductsCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class CategoryUpdateFormAdmin(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    # description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}), required=False)
    # is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-control py-4"}))
    discount = forms.IntegerField(widget=forms.NumberInput(), label='скидка', required=False, min_value=0, max_value=90,
                                  initial=0)

    class Meta:
        model = ProductsCategory
        # exclude =()
        fields = ("name", "description", 'discount')

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateFormAdmin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'placeholder': 'Введите имя категории'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'placeholder': 'Введите описание'}))

    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'placeholder': 'Введите имя продукта'}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'placeholder': 'Введите описание'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите цену'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите количество'}))

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
