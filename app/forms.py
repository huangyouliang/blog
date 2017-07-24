from django import forms
from django.forms.models import fields_for_model
from app.models import Publisher,User,itemsb,Cliente



from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

#使用form
class PublisherForm1(forms.Form):

    name = forms.CharField(label='名称', error_messages={"required": "这个必填"})
    address = forms.CharField()
    city = forms.CharField()
    email = forms.CharField()

#使用django.form
class PublisherForm2(forms.Form):
    name = forms.CharField(label='名称', error_messages={"required": "这个必填"})
    address = forms.CharField()
    city = forms.CharField()
    email = forms.CharField()


#使用ModelForm    z在页面上自动生成表单
class PublisherForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(PublisherForm.self).clean()
        value = cleaned_data.get('name')
        #print("打印："%value)
        try:
            Publisher.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except Publisher.DoesNotExist:
            pass
        return cleaned_data




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ("username","password","xueke","truename", "typefs","labnumber","zhiwu","zhicheng","tel","tel_office","eamil",)
    #     # exclude=("id",)

        fields = ("username","password","id")
       # exclude =("email",)



class ItemsbForm(forms.ModelForm):
    class Meta:

      model = itemsb
      exclude = ("email1",)



class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['']




