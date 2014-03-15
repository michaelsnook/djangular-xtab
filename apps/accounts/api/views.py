from django.contrib.auth.models import User
from rest_framework viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser
from . import authentication, serializers  # see previous post[1] for user serializer.
from rest_framework import serializers 
# 3/15 http://richardtier.com/2014/03/15/authenticate-using-django-rest-framework-endpoint-and-angularjs/
from django.contrib.auth import login, logout
 
# 2/25 http://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
 
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

# 2/25 http://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/
 
class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff
 
    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user

# 2/25 http://richardtier.com/2014/02/25/django-rest-framework-user-endpoint/ 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)
 
    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

# 3/06 http://richardtier.com/2014/03/06/110/
 
#class AuthView(APIView):
#    authentication_classes = (authentication.QuietBasicAuthentication,)
#    serializer_class = serializers.UserSerializer
# 
#    def post(self, request, *args, **kwargs):
#        return Response(self.serializer_class(request.user).data)

# 3/15 http://richardtier.com/2014/03/15/authenticate-using-django-rest-framework-endpoint-and-angularjs/
# updates AuthView from preview post

class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)
 
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)
 
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})