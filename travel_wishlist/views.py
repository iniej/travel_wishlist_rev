from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

# Create a view
# This view will handle requests to the home page
def place_list(request):

    if request.method == 'post': # User clicking add button
        form = NewPlaceForm(request.POST)
        place = form.save() # Call the save function.
        if form.is_valid(): # If new place is valid, then add to list
            place.save()
            return redirect('place_list')

        # If the request is not a post the form is not valid,
        # display the form with the list on the wishlist page.
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited' : visited})



def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')#search primary key
        place = get_object_or_404(Place, pk = pk) #search places by primary key
        place.visited = True #set the boolean flag to True
        place.save() # save the place in the database
    return redirect('place_list')


def place_info(request):
    pk = request.POST.get('pk')
    place = get_object_or_404(Place, pk = pk)
    if not place.visited:
        form = PlaceInfoForm()
        if request.method == 'POST':
            form = PlaceInfoForm(request.POST)
            if form.is_valid():
                place = form.save()
                place.visited = True
                place.save()
        return render(request, 'travel_wishlist/info.html', {'place': place,'form': form})
    return render(request, 'travel_wishlist/info.html', {'place' : place})
