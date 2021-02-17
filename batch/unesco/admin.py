from django.contrib import admin

from unesco.models import Site, Category, Region, State, Iso

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(State)
admin.site.register(Iso)