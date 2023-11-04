from django.shortcuts import render, redirect
from .models import DatabaseConnection
from .forms import DatabaseConnectionForm
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import re

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

def home(request):
    return render(request, 'home.html')

def dbconnect(request):
    global db_uri
    if request.method == 'POST':
        form = DatabaseConnectionForm(request.POST)
        if form.is_valid():
            # Check which database type the user selected
            #database_type = request.POST.get('inlineRadioOptions')
            database_type = form.cleaned_data['database_type'].lower()
            db_username = form.cleaned_data['username'].lower()
            db_password = form.cleaned_data['password'].lower()
            db_host = form.cleaned_data['host'].lower()
            db_port = form.cleaned_data['port']
            db_name = form.cleaned_data['name'].lower()

            if 'postgresql' in database_type:
                db_uri = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

            elif 'mysql' in database_type:
                db_uri = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


            # Saving the database connection details
            db_connection = DatabaseConnection(
                database_type=database_type,
                username=db_username,
                password=db_password,
                host=db_host,
                port=db_port,
                name=db_name,
            )
            db_connection.save()

            return redirect('chat')
        else:
            print(form.errors)

    else:
        form = DatabaseConnectionForm()

    return render(request, 'dbconnect.html', {'form': form})


@csrf_exempt
def chat(request):
            if request.method == 'GET':
                  # Render the initial chatbot interface
                  return render(request, 'chat.html')
            if request.method == 'POST':
                 return JsonResponse({'response': 'hello'})
            if db_uri is None:
                 return JsonResponse({'response': 'Database connection not established'})
            response = ""
            '''
            if request.method == 'POST':


                query = request.POST.get('message', '')

                
                db = SQLDatabase.from_uri(db_uri)
                llm = OpenAI(temperature=0)

                db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, top_k=3)

            
                response = db_chain.run(query)
            
            return JsonResponse({'response': response})
            '''


