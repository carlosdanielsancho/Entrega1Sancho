from django import forms


class AlbumForm(forms.Form):
    performer = forms.CharField(
        label="Nombre del album",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-performer",
                "placeholder": "Nombre de album",
                "required": "True",
            }
        ),
    )
    title = forms.CharField(
        label="Título del album",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-title",
                "placeholder": "Título del album",
                "required": "True",
            }
        ),
    )
    release = forms.IntegerField(
        label="Lanzamiento:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-release",
                "placeholder": "Lanzamiento",
                "required": "True",
            }
        ),
    )
    genre = forms.CharField(
        label="Género:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "album-genre",
                "placeholder": "Género",
                "required": "True",
            }
        ),
    )
