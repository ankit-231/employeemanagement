from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser


def login_view(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        form = AuthenticationForm(request, data=request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f"<h1> {user} is logged in</h1>")
        else:
            return HttpResponse("<h1>invalid username or password</h1>")

    form = AuthenticationForm
    return render(request, "loginform.html", {"form": form})

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_user(request):
    user = CustomUser.objects.filter(is_deleted=False)
    serializer = UserSerializer(user, many=True)
    print(request.user)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def post_user(request):
    data = JSONParser().parse(request)
    
    serializer = UserSerializerPost(data=data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=data['username'])
        if "role" in data:
            try:
                role = Role.objects.get(id=data["role"])
            except Role.DoesNotExist:
                return JsonResponse({'error': "Role does not exist"}, safe=False, status=400)
            user.role_set.add(role)
            user.save()
            for i in user.role_set.all():
                print(i.name)
        if "designation" in data:
            try:
                designation = Designation.objects.get(id=data["designation"])
            except Designation.DoesNotExist:
                return JsonResponse({'error': "Designation does not exist"}, safe=False, status=400)
            user.designation = designation
            user.save()
            print(user.designation)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def edit_user(request):
    print(request.user)
    print(request)
    data = JSONParser().parse(request)
    if "username" not in data:
        return JsonResponse( {"error": "provide username"},status=404)
    
    try:
        user = CustomUser.objects.get(username=data["username"])
    except CustomUser.DoesNotExist:
        return JsonResponse( {"error": "user does not exist"},status=404)
    
    serializer = UserSerializerPost(user, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if "role" in data:
            if data['role'] == 0:
                user.role_set.clear()
            else:
                try:
                    role = Role.objects.get(id=data["role"])
                except Role.DoesNotExist:
                    return JsonResponse({'error': "Role does not exist"}, safe=False, status=400)
                user.role_set.add(role)
                user.save()
                for i in user.role_set.all():
                    print(i.name)
        if "designation" in data:
            try:
                designation = Designation.objects.get(id=data["designation"])
            except Designation.DoesNotExist:
                return JsonResponse({'error': "Designation does not exist"}, safe=False, status=400)
            user.designation = designation
            user.save()
            print(user.designation)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_role(request):
    role = Role.objects.filter(is_deleted=False)
    serializer = RoleSerializer(role, many=True)
    # print(request.user)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def post_role(request):
    data = JSONParser().parse(request)
    serializer = RoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def edit_role(request, pk):
    print(request.user)
    print(request)
    data = JSONParser().parse(request)
    
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return JsonResponse( {"error": "role does not exist"},status=404)
    
    serializer = RoleSerializer(role, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_designation(request):
    designation = Designation.objects.filter(is_deleted=False)
    serializer = DesignationSerializer(designation, many=True)
    # print(request.user)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def post_designation(request):
    data = JSONParser().parse(request)
    serializer = DesignationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def edit_designation(request, pk):
    print(request.user)
    print(request)
    data = JSONParser().parse(request)
    
    try:
        designation = Designation.objects.get(pk=pk)
    except Designation.DoesNotExist:
        return JsonResponse( {"error": "designation does not exist"},status=404)
    
    serializer = DesignationSerializer(designation, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_designation_head(request):
    designation_head = DesignationHead.objects.filter(is_deleted=False)
    serializer = DesignationHeadSerializer(designation_head, many=True)
    # print(request.user)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def post_designation_head(request):
    data = JSONParser().parse(request)
    serializer = DesignationHeadSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def edit_designation_head(request, pk):
    print(request.user)
    print(request)
    data = JSONParser().parse(request)
    
    try:
        designation_head = DesignationHead.objects.get(pk=pk)
    except DesignationHead.DoesNotExist:
        return JsonResponse( {"error": "designation does not exist"},status=404)
    
    serializer = DesignationHeadSerializer(designation_head, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(serializer.errors, safe=False, status=400)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def check(request):
    print(request.user)
    return Response(status=200)


def logout_view(request):
    logout(request)
    return redirect('/mainuser/login/')





