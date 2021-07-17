from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from todos.models import Todo


@api_view(['GET'])
def EndPoints(request):
    routes = [
        {
            'Endpoint' : '/todos/',
            'Http Method' : 'GET',
            'body' : None,
            'description' : 'get an array of todos',
        },
        {
            'Endpoint' : '/todos/:id',
            'Http Method' : 'GET',
            'body' : None,
            'description' : 'get a single todo using id',
        },
        {
            'Endpoint' : '/todos/',
            'Http Method' : 'POST',
            'body' : {'title' : '', 'description' : '', },
            'description' : 'create a new todo',
        },
        {
            'Endpoint' : '/todos/:id',
            'Http Method' : 'PUT',
            'body' : {'title' : '', 'description' : '', },
            'description' : 'update a new todo',
        },
        {
            'Endpoint' : '/todos/:id',
            'Http Method' : 'DELETE',
            'body' : None,
            'description' : 'delete a todo',
        },
    ]
    return Response(routes)


@api_view(['GET','POST'])
def Todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        todo = Todo.objects.create(
            title = data['title'],
            description = data['description'],
            complete = data['complete']
        )
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data)

# Get a single todo, update and delete
@api_view(['PUT','DELETE','GET'])
def SingleTodo(request, pk):
    if request.method == 'PUT':
       
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        todo = Todo.objects.get(id=pk)
        todo.delete()
        
        return Response('Todo Deleted')

    if request.method == 'GET':
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data)
