from django import forms


class PessoaFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaFormAdmin, self).__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
        self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'



