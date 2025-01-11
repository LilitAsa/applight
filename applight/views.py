from django.shortcuts import render, get_object_or_404
from .models import (
    Banner,
    About,
    WatchNow,
    FeaturesCentral,
    Team,
    Testimonials,
    FAQ,
    Block,
    Contact
)

def index(request):
    banner = get_object_or_404(Banner)
    about = About.objects.all()
    watchNow = get_object_or_404(WatchNow)
    features = get_object_or_404(FeaturesCentral)
    features_items = features.items.all()
    team = Team.objects.all()
    testimonials = Testimonials.objects.all()
    faq = FAQ.objects.all()
    block = Block.objects.all()
    contact = Contact.objects.all()

    data = {
        "banner": banner,
        "about": about,
        "watchNow": watchNow,
        "features": features,
        "features_items": features_items,
        "team": team,
        "testimonials": testimonials,
        "faq": faq,
        "block": block,
        "contact": contact
    }

    print(1)
    print(block)
    return render(request, "base.html", data)
