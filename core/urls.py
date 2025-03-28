
from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),

    path('mualliflar/', mualliflar_view,name='mualliflar_list'),
    path('muallif/<int:muallif_id>/',muallif_view),
    path('muallif_qoshish/',muallif_post_view),
    path('mualliflar_yoshi/',katta_mualliflar),
    path('muallif/delete/<int:muallif_id>/',muallif_delete),
    path('tiriklar/',tirikmi),
    path('tirik_kitob/',tirikmlarni_kitobi),
    path('kitob_soni_max/', kitob_soni),
    path('adminlar/', adminlar_view,name='adminlar'),
    path('talabalar/', talabalar_view,name='talabalar_list'),
    path('talaba/<int:talaba_id>/',talaba_view),
    path('talaba/delete/<int:talaba_id>/',talaba_delete),
    path('talaba/delete/<int:talaba_id>/',talaba_delete),
    path('kitoblar/',kitoblar_view),
    path('kitob/<int:kitob_id>/',kitob_view),
    path('kitob_sahifa/',sahifa_max),
    path('tirik_kitob/',tirikmlarni_kitobi),
    path('badiy_kitoblar/',kitoblar_badiy),
    path('s_kitoblar/',kitoblar),
    path('record/<int:pk/',record_view),
    path('record/delete/<int:record_id>/',record_delete),
    path('recordlar/',records_view,name='recordlar_list'),
    path('last_records/',last_records),
    path('bitiruvchilar/',bitiruvchilar),
]
