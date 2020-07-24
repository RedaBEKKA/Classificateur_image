from django.contrib import admin
from images.models import Image

# Register your models here
class PypySite(admin.AdminSite):
    site_header = 'Reda Images Administration'

adminSite = PypySite(name='admin')
adminSite.register(Image)
#@admin.register(Image,site=adminSite)
