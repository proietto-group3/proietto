from django.urls import path
from inbox.views import inbox, incoming, send_message, user_search, NewConversation

app_name = "inbox"

urlpatterns = [
    path('', inbox, name="inbox"),
    path("incoming/<username>", incoming, name="incoming"),
    path("send/", send_message, name="send_message"),
    path("new/", user_search, name="usersearch"),
    path("new/<username>", NewConversation, name="newconversation"),
   ]