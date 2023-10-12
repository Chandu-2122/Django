from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(LiveFacialImage)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(VotedOrNot)
admin.site.register(Vote)
