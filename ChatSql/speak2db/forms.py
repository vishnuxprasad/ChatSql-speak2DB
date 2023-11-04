from django import forms
from .models import DatabaseConnection

class DatabaseConnectionForm(forms.ModelForm):
    class Meta: 
        model = DatabaseConnection
        fields = ['database_type', 'username', 'password', 'host', 'port', 'name']