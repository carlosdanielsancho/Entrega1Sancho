from django.contrib import messages
from django.shortcuts import render

from album.models import Album
from album.forms import AlbumForm

# Create your views here.

def get_albums(request):
    albums = Album.objects.all()
    return albums


def create_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            data = album_form.cleaned_data
            actual_objects = Album.objects.filter(
                performer=data["performer"],
                title=data["title"],
                release=data["release"],
                genre=data["genre"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El album {data['title']} de {data['performer']} ya está creado",
                )
            else:
                album = Album(
                    performer=data["performer"],
                    title=data["title"],
                    release=data["release"],
                    genre=data["genre"],
                )
                album.save()
                messages.success(
                    request,
                    f"Album {data['title']} de {data['performer']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"albums": get_albums(request)},
                template_name="album/album_list.html",
            )

    album_form = AlbumForm(request.POST)
    context_dict = {"form": album_form}
    return render(
        request=request,
        context=context_dict,
        template_name="album/album_form.html",
    )


def albums(request):
    albums = Album.objects.all()

    context_dict = {"albums": albums}

    return render(
        request=request,
        context=context_dict,
        template_name="album/album_list.html",
    )
