from django.contrib import admin
from .models import Matricula,Cidade,Curso
# Register your models here.

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display= ('nome_aluno', 'endereço', 'cidade')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display= ('nome','sigla_estado',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display= ('nome',)
    
    