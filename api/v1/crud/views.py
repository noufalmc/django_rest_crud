from datetime import datetime

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers import BloodDataSerializer
from crud.models import BloodData


class BloodDataView(APIView):

    def get(self, request):
        blood_data = BloodData.objects.filter(is_deleted=False)
        serialised = BloodDataSerializer(blood_data, many=True)
        response_data = {
            'status': 200,
            'message': 'Data Retrieve',
            'error': '',
            'data': serialised.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BloodDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 200,
                'message': 'Blood Data Successfully Created',
                'error': '',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'status': 422,
                'message': '!Oops',
                'error': serializer.errors,
                'data': ''
            }
            return Response(response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BloodDataDetailView(APIView):
    def get_object(self, pk):
        try:
            return BloodData.objects.get(is_deleted=False, id=pk)
        except BloodData.DoesNotExist:
            response_data = {
                "status": 422,
                "message": "No Content",
                "data": "",
                "errors": ""
            }
            raise NotFound(response_data)

    def get(self, request, pk):
        data = self.get_object(pk)
        serialised = BloodDataSerializer(data)
        if data:
            response_data = {
                "status": 200,
                "message": "Data",
                "data": serialised.data,
                "errors": ""
            }
            return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = self.get_object(pk)
        serialiser = BloodDataSerializer(data, request.data)
        if serialiser.is_valid():
            updated_at = datetime.now()
            serialiser.save(updated_at=updated_at)
            response_data = {
                "status": 200,
                "message": "Data",
                "data": serialiser.data,
                "errors": ""
            }
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            response_data = {
                "status": 422,
                "message": "No Content",
                "data": "",
                "errors": ""
            }
            return Response(response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def patch(self, request, pk):
        data = self.get_object(pk)
        if data:
            serialiser = BloodDataSerializer(data, request.data, partial=True)
            if serialiser.is_valid():
                updated_at = datetime.now()
                serialiser.save(updated_at=updated_at)
                response_data = {
                    "status": 200,
                    "message": "Data",
                    "data": serialiser.data,
                    "errors": ""
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    "status": 422,
                    "message": "Error",
                    "data": '',
                    "errors": serialiser.errors
                }
                return Response(response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        data = self.get_object(pk)
        # HARD DELETE FROM THE DATABASE
        # data.delete()         # NOT RECOMMEND
        if data:
            BloodData.objects.filter(pk=pk).update(is_deleted=True,
                                                   updated_at=datetime.now())
        response_data = {
            'statuscode': 200,
            'title': 'Deleted',
            'data': 'Entire record and associated datas are deleted successfully',
            'errors': '',
            'message': 'Deleted successfully',
        }
        return Response(response_data, status=status.HTTP_200_OK)
