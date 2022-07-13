from django.urls import path
from .views import ClientCreateView, ClientUpdateView, ClientDeleteView, ClientWalletUpdateView, ClientAPIView, Homepage

app_name = 'crm'

urlpatterns = [
    path("", Homepage.as_view(), name='homepage'),
    path("client-create/", ClientCreateView.as_view(), name="createclient"),
    path("client-update/<int:pk>/", ClientUpdateView.as_view(template_name="crm/updateclient.html"), name="updateclient"),
    path("client-delete/<int:pk>/", ClientDeleteView.as_view(), name='deleteclient'),
    path("edit-balance/<int:pk>/", ClientWalletUpdateView.as_view(), name='updateclientbalance'),
    path('api/getbalance/', ClientAPIView.as_view(), name='api-view'),
]