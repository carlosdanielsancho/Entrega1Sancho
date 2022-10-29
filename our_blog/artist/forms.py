from ckeditor.widgets import CKEditorWidget
from django import forms

from artist.models import Artist


class ArtistForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del artista",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "artist-name",
                "placeholder": "Nombre del artista",
                "required": "True",
            }
        ),
    )

    genre = forms.CharField(
        label="Género:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "artist-genre",
                "placeholder": "Género musical",
                "required": "True",
            }
        ),
    )

    active = forms.CharField(
            label="Actividad",
            required=False,
            widget=forms.TextInput(
                attrs={
                    "class": "artist-active",
                    "placeholder": "Actividad",
                    "required": "True",
                }
            ),
        )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "artist-description",
                "placeholder": "Descripcion del artista",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Artist
        fields = ["name", "genre", "active", "description"]