from django.shortcuts import render,redirect
import folium
from  .models import  Search
from  .forms import  SearchForm
import geocoder
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=SearchForm()
    address = Search.objects.all().last()
    # address = request.POST.get('address')
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country=location.country

    #map obyektini yaratamiz
    m = folium.Map(location=[19,12],zoom_start=2)
    # folium.Marker([41.2358300,69.3111100],tooltip="Manzilni yaqinroqdan ko'rish",popup="Toshkent shahri").add_to(m)

    folium.Marker([lat,lng],tooltip="Manzilni yaqinroqdan ko'rish",popup=country).add_to(m)

    m = m._repr_html_()
    context = {'m' : m,'form':form}
    return render(request,'index.html',context)
    