from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_routes(request):
    return Response([
        '/api/books/',
        '/api/books/id',
        '/api/books/add',
        '/api/books/edit/id',
        '/api/books/delete/id',

        '/api/users/',
        '/api/users/register',
        '/api/users/login',
        '/api/users/profile',
        '/api/users/profile/edit',
        '/api/users/profile/delete',

        '/api/authenmticat',
        '/api/signup',
        '/api/users/',
        'GET /api/user/',
        'PUT /api/user/',
        'DELETE /api/user/',
    ])




