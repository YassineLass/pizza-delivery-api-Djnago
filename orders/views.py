import imp
from django.shortcuts import render,get_object_or_404

from rest_framework import generics,status
from rest_framework.response import Response
from orders import serializers
from orders.models import Order, User
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class OrderCreateView(generics.GenericAPIView):

    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Get all orders details")
    def get(self,request):
        orders = Order.objects.all()

        serialized = self.serializer_class(instance=orders,many=True)
        return Response(data=serialized.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Add new order")    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if(serializer.is_valid()):

            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetail_Serializer
    queryset = Order.objects.all()
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary="Get Order Details by ID")
    def get(self,request,id):
        order = get_object_or_404(Order,pk=id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Update an Order")
    def put(self,request,id):
        data = request.data
        order = get_object_or_404(Order,pk=id)
        serializer = self.serializer_class(data=data ,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete an Order by ID")
    def delete(self,request,id):
        order = get_object_or_404(Order,pk=id)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class Update_status(generics.GenericAPIView):
    serializer_class = serializers.UpdateStatusSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary="Update the status of an order ")
    def put(self,request,id):
        order = get_object_or_404(Order,pk=id)
        data = request.data
        serializer = self.serializer_class(data=data ,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

class UserOrder_all(generics.GenericAPIView):
    serializer_class = serializers.OrderDetail_Serializer
    queryset = Order.objects.all()
    IsAuthenticatedOrReadOnly

    @swagger_auto_schema(operation_summary="Get all orders for a User ")
    def get(self,request,id):
        user=User.objects.get(pk=id)
        orders=Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrder_one(generics.GenericAPIView):
    serializer_class = serializers.OrderDetail_Serializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Get a specific Order details for a user ")
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)

        order=get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK) 

              

