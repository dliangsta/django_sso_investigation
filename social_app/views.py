from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class SSOAuthToken(generics.RetrieveAPIView):

  def get(self, request, *args, **kwargs):
    print("HI! GET!!")
    print(request.user)
    print(request.data)
    return Response(data={
      "your token!": Token.objects.get_or_create(user=request.user)[0].key,
    })
