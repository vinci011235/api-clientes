from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ser válido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O número de celular deve seguir este modelo: 99 91234-1234'})
        
        return data

    