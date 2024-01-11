from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

# finches = [
#     {
#         "name": "European Goldfinch",
#         "description": "A small passerine bird in the finch family that is native to Europe, North Africa and western Asia.",
#         "size": "Small",
#     },
#     {
#         "name": "Eurasian Chaffinch",
#         "description": "A common and widespread small passerine bird in the finch family.",
#         "size": "Small",
#     },
#     {
#         "name": "Purple Finch",
#         "description": "A small finch that breeds in coniferous and mixed forests of Canada and the northeastern United States.",
#         "size": "Small",
#     },
#     {
#         "name": "House Finch",
#         "description": "A bird in the finch family native to western North America.",
#         "size": "Small",
#     },
#     {
#         "name": "Common Rosefinch",
#         "description": "A medium-sized passerine bird in the finch family.",
#         "size": "Medium",
#     },
#     {
        #         "name": "Carduellis",
        #         "description": "A medium-sized passerine bird in the finch family.",
        #         "size": "Medium",
# ]


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {
        "finches": finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "finches/detail.html", {
        "finch": finch
    })
    
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'
    
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['description', 'size']
    
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'