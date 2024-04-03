
from django import  forms
from products.models import Product
class ProductForm(forms.Form):
    name = forms.CharField(max_length=100,
                           label='Product Name', required=True)
    price = forms.IntegerField(label='Price', required=True)
    image = forms.ImageField(required=False, label='Image')
    code = forms.CharField(max_length=100)

    ## unique validation
    ## check code --> not exists before in the database

    def clean_code(self):
        code = self.cleaned_data['code']
        ## code --> check if exits before in the database
        code_found = Product.objects.filter(code=code).exists()
        if code_found :
            raise forms.ValidationError('Code used before , please choose another one')

        return code

#model form
class ProductModelForm(forms.ModelForm):
    # build form based on model
    class Meta:
        model = Product
        fields = '__all__'

    # def clean_code(self):
    #     code = self.cleaned_data['code']
    #     code_found = Product.objects.filter(code=code).exists()
    #     if code_found:
    #         raise forms.ValidationError('Code used before , please choose another one')
    #
    #     return code

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name)<2:
            raise forms.ValidationError('Name length must be greater than 2 chars')
        return name


