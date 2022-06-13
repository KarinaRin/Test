from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import Articles, CustomUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RegistrUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ArticlesRegistrSerializers
    permission_classes = (IsOwnerOrReadOnly, )

    def post(self, request, *args, **kwargs):
        serializer = ArticlesRegistrSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class ArticlesCreateView(generics.CreateAPIView):
    serializer_class = ArticlesDetailSerializers
    queryset = Articles.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializers
    queryset = Articles.objects.filter(public=True)


class ArticlesPrivateListView(generics.ListAPIView):
    serializer_class = ArticlesPrivateListSerializers
    queryset = Articles.objects.filter(public=False)
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ArticlesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticlesDetailSerializers
    queryset = Articles.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
