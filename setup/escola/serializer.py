from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        #aqui selecionamos retornos específicos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        #aqui onde definimos os campos que vai aparecer no retorno da api, aqui digo que quero todos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Matricula
        #aqui por exemplo excluiria algum campo da resposta
        exclude = []