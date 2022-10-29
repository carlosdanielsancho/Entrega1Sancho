from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from artist.forms import ArtistForm
from artist.models import Artist

# Create your views here.


def get_artists(request):
    artists = Artist.objects.all()
    paginator = Paginator(artists, 4)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def artists(request):
    return render(
        request=request,
        context={"artist_list": get_artists(request)},
        template_name="artist/artist_list.html",
    )


def artist_create(request):
    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            data = artist_form.cleaned_data
            actual_objects = Artist.objects.filter(
                name=data["name"], genre=data["genre"], active=data["active"] 
            ).count()
            print("actual_objects", actual_objects)
            if not actual_objects:
                artist = Artist(
                    name=data["name"],
                    genre=data["genre"],
                    active=data["active"],
                    description=data["description"],
                )
                artist.save()
                messages.success(
                    request,
                    f"Artista {data['name']} - {data['genre']} - {data['active']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"artist_list": get_artists(request)},
                    template_name="artist/artist_list.html",
                )
            else:
                messages.error(
                    request,
                    f"El artista {data['name']} - {data['genre']} - {data['active']} ya está creado",
                )

    artist_form = ArtistForm(request.POST)
    context_dict = {"form": artist_form}
    return render(
        request=request,
        context=context_dict,
        template_name="artist/artist_form.html",
    )


def artist_detail(request, pk: int):
    return render(
        request=request,
        context={"artist": Artist.objects.get(pk=pk)},
        template_name="artist/artist_detail.html",
    )


def artist_update(request, pk: int):
    artist = Artist.objects.get(pk=pk)

    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        if artist_form.is_valid():
            data = artist_form.cleaned_data
            artist.name = data["name"]
            artist.genre = data["genre"]
            artist.active = data["active"]
            artist.description = data["description"]
            artist.save()

            return render(
                request=request,
                context={"artist": artist},
                template_name="artist/artist_detail.html",
            )

    artist_form = ArtistForm(model_to_dict(artist))
    context_dict = {
        "artist": artist,
        "form": artist_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="artist/artist_form.html",
    )


def artist_delete(request, pk: int):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        artist.delete()

        artists = Artist.objects.all()
        context_dict = {"artist_list": artists}
        return render(
            request=request,
            context=context_dict,
            template_name="artist/artist_list.html",
        )

    context_dict = {
        "artist": artist,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="artist/artist_confirm_delete.html",
    )


class ArtistListView(ListView):
    model = Artist
    paginate_by = 4


class ArtistDetailView(DetailView):
    model = Artist
    fields = ["name", "genre", "active", "description"]


class ArtistCreateView(CreateView):
    model = Artist
    success_url = reverse_lazy("artist:artist-list")

    form_class = ArtistForm
    # fields = ["name", "genre", "active", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate artists"""
        data = form.cleaned_data
        actual_objects = Artist.objects.filter(
            name=data["name"], genre=data["genre"], active=data["active"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El artista {data['name']} - {data['genre']} - {data['active']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Artista {data['name']} - {data['genre']} - {data['active']} creado exitosamente!",
            )
            return super().form_valid(form)


class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ["name", "genre", "active" "description"]

    def get_success_url(self):
        artist_id = self.kwargs["pk"]
        return reverse_lazy("artist:artist-detail", kwargs={"pk": artist_id})


class ArtistDeleteView(DeleteView):
    model = Artist
    success_url = reverse_lazy("artist:artist-list")