from django.urls import path
from participant.views import Participants  , Add_participants,update_Participants,delete_participant

urlpatterns = [
    path('', Participants, name='participant_list'), 
    path('add-participants/' , Add_participants , name="add_participant"),
    path('update/<int:id>/',update_Participants,name='update_Participants'),
    path('delete/<int:id>/',delete_participant,name='delete_participant'),
]
