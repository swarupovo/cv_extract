from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from api.backend.pdf_read import read_pdf
from api.models import CvUp
from .serializers import ProfileSerializer, CvUpSerializer
from drf_yasg.utils import swagger_auto_schema


class Upload(APIView):
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(request_body=CvUpSerializer,
                         operation_description="Authenticates User and returns User Profile.",
                         responses={200: ProfileSerializer})
    def post(self, request):
        if ".pdf" in str(request.FILES['file']):
            cv_obj = CvUp.objects.create(file=request.FILES['file'])
            cv_obj.save()
            a = read_pdf(request.FILES['file'])
            # print(a)
            profile_serializer = ProfileSerializer(data=a)
            print(profile_serializer)
            if profile_serializer.is_valid():

                profile_serializer.save()

                print("serializer save")
            else:
                print(profile_serializer.errors)

            return JsonResponse({"success": True, "data": a}, status=200)
        else:
            return JsonResponse({"success": "No able to upload this type of document"}, status=415)
        # print(request.FILES['file'])


