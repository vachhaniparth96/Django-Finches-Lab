from django.shortcuts import render

finches = [
    {
        "name": "European Goldfinch",
        "description": "A small passerine bird in the finch family that is native to Europe, North Africa and western Asia.",
        "size": "Small",
    },
    {
        "name": "Eurasian Chaffinch",
        "description": "A common and widespread small passerine bird in the finch family.",
        "size": "Small",
    },
    {
        "name": "Purple Finch",
        "description": "A small finch that breeds in coniferous and mixed forests of Canada and the northeastern United States.",
        "size": "Small",
    },
    {
        "name": "House Finch",
        "description": "A bird in the finch family native to western North America.",
        "size": "Small",
    },
    {
        "name": "Common Rosefinch",
        "description": "A medium-sized passerine bird in the finch family.",
        "size": "Medium",
    },
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    return render(request, "finches/index.html", {
        "finches": finches
    })
