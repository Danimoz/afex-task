from django.shortcuts import render
from .models import Client, ClientWallet
from rest_framework.views import APIView
from .serializers import ClientSerializer
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.response import Response
from django.views import View

# Create your views here.
class Homepage(View):
    def get(self, request, *args, **kwargs):
        qs = Client.objects.all()
        return render(request, 'home.html', {'qs': qs})

class ClientCreateView(CreateView):
    model = Client
    fields = ['cid', 'first_name', 'last_name', 'country_code', 'email', 'address', 'phone']
    success_url = '/'

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['cid', 'first_name', 'last_name', 'country_code', 'email', 'address', 'phone']
    success_url = '/'

class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/'

class ClientWalletUpdateView(UpdateView):
    model = ClientWallet
    fields = ['clients', 'available_balance']
    success_url = '/'

class ClientAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = ClientSerializer(data = data)

        if serializer.is_valid():
            cid = serializer.data['cid']            
            try:
                acct = Client.objects.get(cid = cid)
                acct_bal = acct.clientwallet.available_balance
                acct_name = acct.first_name
                details = {'Name': acct_name, 'Balance': acct_bal}
                return Response({'details': details}, status=status.HTTP_200_OK)
            except: 
                return Response({'message': 'This CID does not have an account'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)