from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        })
    )
    email = forms.CharField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={   # Cambiado temporalmente a TextInput para que el navegador no se ponga técnico
            'class': 'form-control',
            'placeholder': 'Escribe tu email'
        })
    )
    content = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Escribe tu mensaje'
        })
    )