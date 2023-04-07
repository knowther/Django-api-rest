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


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculados(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model= Matricula
        fields = ['aluno_nome']