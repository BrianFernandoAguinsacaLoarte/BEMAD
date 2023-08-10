
from django.shortcuts import render, redirect

from dawnbem.forms import RegistroForm, JugadorForm, InscripcionForm, EquipoForm, PartidoForm, MarcadorForm, TemporadaForm, ReglamentoForm, ReglaForm
from dawnbem.models import Registro, Jugador, Inscripcion, Equipo, Partido, Marcador, Temporada, Reglamento, Regla


# Create your views here.
def mi_vista(request):
    contexto = {
        'titulo': 'Ejemplo de página HTML en Django',
        'contenido': '¡Hola! Esta es una página HTML generada con Django.',
        'contenido2': 'Enlazado exitosamente Html y DJango'
    }
    return render(request, 'index.html', contexto)

def registro(request):
    context = {
        'titulo': 'Registro',
        'contenido1': 'Registro de Usuario',
    }
    return render(request, 'Registro.html', context)

def inscripcion(request):
    contexto = {
        'titulo': 'Inscripcion',
        'contenido1': 'Inscripcion de Usuario',
    }
    return render(request, 'Inscripcion.html', contexto)

def jugador(request):
    contexto = {
        'titulo': 'Jugador',
        'contenido1': 'Inscripcion de Jugador',
    }
    return render(request, 'Jugador.html', contexto)

def Deporte(request):
    contexto = {
        'titulo': 'Deporte',
        'contenido1': 'Inscripcion de Deporte',
    }
    return render(request, 'Deporte.html', contexto)

def equipo(request):
    contexto = {
        'titulo': 'Equipo',
        'contenido1': 'Inscripcion de Equipo',
    }
    return render(request, 'Equipo.html', contexto)

def Grupo(request):
    contexto = {
        'titulo': 'Grupo',
        'contenido1': 'Inscripcion de Grupo',
    }
    return render(request, 'Grupo.html', contexto)

def Sorteo(request):
    contexto = {
        'titulo': 'Sorteo',
        'contenido1': 'Inscripcion de Sorteo',
    }
    return render(request, 'Sorteo.html', contexto)

def partido(request):
    contexto = {
        'titulo': 'Partido',
        'contenido1': 'Inscripcion de Partido',
    }
    return render(request, 'Partido.html', contexto)

def marcador(request):
    contexto = {
        'titulo': 'Marcador',
        'contenido1': 'Inscripcion de Marcador',
    }
    return render(request, 'Marcador.html', contexto)

def reglamento(request):
    contexto = {
        'titulo': 'Reglamento',
        'contenido1': 'Inscripcion de Reglamento',
    }
    return render(request, 'Reglamento.html', contexto)

def regla(request):
    contexto = {
        'titulo': 'Regla',
        'contenido1': 'Inscripcion de Regla',
    }
    return render(request, 'Regla.html', contexto)

def temporada(request):
    contexto = {
        'titulo': 'Temporada',
        'contenido1': 'Inscripcion de Temporada',
    }
    return render(request, 'Temporada.html', contexto)

def home(request):
    registro_list = Registro.objects.all()
    jugador_list = Jugador.objects.all()
    inscripcion_list = Inscripcion.objects.all()
    equipo_list = Equipo.objects.all()
    partido_list = Partido.objects.all()
    marcador_list = Marcador.objects.all()
    temporada_list = Temporada.objects.all()
    reglamento_list = Reglamento.objects.all()
    regla_list = Regla.objects.all()
    context = {'registro_list': registro_list, 'jugador_list': jugador_list,
               'inscripcion_list': inscripcion_list, 'equipo_list': equipo_list
               , 'partido_list': partido_list, 'marcador_list': marcador_list
               , 'temporada_list': temporada_list, 'reglamento_list': reglamento_list,
               'regla_list': regla_list}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def registro_detail(request,id):
    registro = Registro.objects.get(id=id)
    context = {'registro': registro}
    return render(request, 'registroDetail.html', context)

def nuevo_Registro(request):
    registro = Registro.objects.all()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroNuevo')

    form = RegistroForm()
    registro_list = Registro.objects.all()
    context = {'form': form,
               'registro_list': registro_list,
               'registro': registro
               }
    return render(request, 'registroNuevo.html', context)

def editar_Registro(request, id):
    registro = Registro.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('registroNuevo')

    form = RegistroForm(instance=registro)
    registro_list = Registro.objects.all()
    context = {'form': form,
               'registro_list': registro_list,
               'registro': registro
               }
    return render(request, 'registroEditar.html', context)
def eliminar_Registro(request, id):
    registro_list = Registro.objects.all()
    context = {
               'registro_list': registro_list
               }
    registro = Registro.objects.get(id=id)
    registro.delete()
    return redirect('registroNuevo')


def jugador_detail(request,id):
    jugador = Jugador.objects.get(id=id)
    context = {'jugador': jugador}
    return render(request, 'jugadorDetail.html', context)

def nuevo_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadorNuevo')

    form = JugadorForm()
    jugador_list = Jugador.objects.all()
    context = {'form': form,
               'jugador_list': jugador_list
               }
    return render(request, 'jugadorNuevo.html', context)
def editar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugadorNuevo')

    form = JugadorForm(instance=jugador)
    jugador_list = Jugador.objects.all()
    context = {'form': form,
               'jugador_list': jugador_list,
               'jugador': jugador
               }
    return render(request, 'jugadorEditar.html', context)

def eliminar_jugador(request, id):
    jugador_list = Jugador.objects.all()
    context = {
               'registro_list': jugador_list
               }
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    return redirect('jugadorNuevo')

def inscripcion_detail(request,id):
    inscripcion = Inscripcion.objects.get(id=id)
    context = {'inscripcion': inscripcion}
    return render(request, 'inscripcionDetail.html', context)

def nueva_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcionNueva')

    form = InscripcionForm()
    inscripcion_list = Inscripcion.objects.all()
    context = {'form': form,
               'inscripcion_list': inscripcion_list
               }
    return render(request, 'inscripcionNueva.html', context)
def editar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('inscripcionNueva')

    form = InscripcionForm(instance=inscripcion)
    inscripcion_list = Inscripcion.objects.all()
    context = {'form': form,
               'inscripcion_list': inscripcion_list,
               'inscripcion': inscripcion
               }
    return render(request, 'inscripcionEditar.html', context)

def eliminar_inscripcion(request, id):
    inscripcion_list = Inscripcion.objects.all()
    context = {
               'inscripcion_list': inscripcion_list
               }
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()
    return redirect('inscripcionNueva')

def equipo_detail(request,id):
    equipo = Equipo.objects.get(id=id)
    context = {'equipo': equipo}
    return render(request, 'equipoDetail.html', context)

def nuevo_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipoNuevo')

    form = EquipoForm()
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'equipo_list': equipo_list
               }
    return render(request, 'equipoNuevo.html', context)

def editar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipoNuevo')

    form = EquipoForm(instance=equipo)
    equipo_list = Equipo.objects.all()
    context = {'form': form,
               'equipo_list': equipo_list,
               'equipo': equipo
               }
    return render(request, 'equipoEditar.html', context)

def eliminar_equipo(request, id):
    equipo_list = Equipo.objects.all()
    context = {
               'equipo_list': equipo_list
               }
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('equipoNuevo')

def partido_detail(request,id):
    partido = Partido.objects.get(id=id)
    context = {'partido': partido}
    return render(request, 'partidoDetail.html', context)

def nuevo_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidoNuevo')
    else:
        form = PartidoForm()

    partido_list = Partido.objects.all()
    context = {'form': form,
               'partido_list': partido_list
               }
    return render(request, 'partidoNuevo.html', context)

def editar_partido(request, id):
    partido = Partido.objects.get(id=id)
    if request.method == 'POST':
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('partidoNuevo')

    form = PartidoForm(instance=partido)
    partido_list = Partido.objects.all()
    context = {'form': form,
               'partido_list': partido_list,
               'partido': partido
               }
    return render(request, 'partidoEditar.html', context)

def eliminar_partido(request, id):
    partido_list = Partido.objects.all()
    context = {
               'partido_list': partido_list
               }
    partido = Partido.objects.get(id=id)
    partido.delete()
    return redirect('partidoNuevo')

def marcador_detail(request,id):
    marcador = Marcador.objects.get(id=id)
    context = {'marcador': marcador}
    return render(request, 'marcadorDetail.html', context)

def nuevo_marcador(request):
    if request.method == 'POST':
        form = MarcadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcadorNuevo')

    form = MarcadorForm()
    marcador_list = Marcador.objects.all()
    context = {'form': form,
               'marcador_list': marcador_list
               }
    return render(request, 'marcadorNuevo.html', context)

def editar_marcador(request, id):
    marcador = Marcador.objects.get(id=id)
    if request.method == 'POST':
        form = MarcadorForm(request.POST, instance=marcador)
        if form.is_valid():
            form.save()
            return redirect('marcadorNuevo')

    form = MarcadorForm(instance=marcador)
    marcador_list = Marcador.objects.all()
    context = {'form': form,
               'marcador_list': marcador_list,
               'marcador': marcador
               }
    return render(request, 'marcadorEditar.html', context)

def eliminar_marcador(request, id):
    marcador_list = Marcador.objects.all()
    context = {
               'marcador_list': marcador_list
               }
    marcador = Marcador.objects.get(id=id)
    marcador.delete()
    return redirect('marcadorNuevo')

def temporada_detail(request,id):
    temporada = Temporada.objects.get(id=id)
    context = {'temporada': temporada}
    return render(request, 'temporadaDetail.html', context)

def nueva_temporada(request):
    if request.method == 'POST':
        form = TemporadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('temporadaNueva')

    form = TemporadaForm()
    temporada_list = Temporada.objects.all()
    context = {'form': form,
               'temporada_list': temporada_list
               }
    return render(request, 'temporadaNueva.html', context)

def editar_temporada(request, id):
    temporada = Temporada.objects.get(id=id)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect('temporadaNueva')

    form = TemporadaForm(instance=temporada)
    temporada_list = Temporada.objects.all()
    context = {'form': form,
               'temporada_list': temporada_list,
               'temporada': temporada
               }
    return render(request, 'temporadaEditar.html', context)

def eliminar_temporada(request, id):
    temporada_list = Temporada.objects.all()
    context = {
               'temporada_list': temporada_list
               }
    temporada = Temporada.objects.get(id=id)
    temporada.delete()
    return redirect('temporadaNueva')

def reglamento_detail(request,id):
    reglamento = Reglamento.objects.get(id=id)
    context = {'reglamento': reglamento}
    return render(request, 'reglamentoDetail.html', context)

def nuevo_reglamento(request):
    if request.method == 'POST':
        form = ReglamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reglamentoNuevo')

    form = ReglamentoForm()
    reglamento_list = Reglamento.objects.all()
    context = {'form': form,
               'reglamento_list': reglamento_list
               }
    return render(request, 'reglamentoNuevo.html', context)

def editar_reglamento(request, id):
    reglamento = Reglamento.objects.get(id=id)
    if request.method == 'POST':
        form = ReglamentoForm(request.POST, instance=reglamento)
        if form.is_valid():
            form.save()
            return redirect('reglamentoNuevo')

    form = ReglamentoForm(instance=reglamento)
    reglamento_list = Reglamento.objects.all()
    context = {'form': form,
               'reglamento_list': reglamento_list,
               'reglamento': reglamento
               }
    return render(request, 'reglamentoEditar.html', context)
def eliminar_reglamento(request, id):
    reglamento_list = Reglamento.objects.all()
    context = {
               'reglamento_list': reglamento_list
               }
    reglamento = Reglamento.objects.get(id=id)
    reglamento.delete()
    return redirect('reglamentoNuevo')

def regla_detail(request,id):
    regla = Regla.objects.get(id=id)
    context = {'regla': regla}
    return render(request, 'reglaDetail.html', context)

def nueva_regla(request):
    if request.method == 'POST':
        form = ReglaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reglaNueva')

    form = ReglaForm()
    regla_list = Regla.objects.all()
    context = {'form': form,
               'regla_list': regla_list
               }
    return render(request, 'reglaNueva.html', context)

def editar_regla(request, id):
    regla = Regla.objects.get(id=id)
    if request.method == 'POST':
        form = ReglaForm(request.POST, instance=regla)
        if form.is_valid():
            form.save()
            return redirect('reglaNueva')

    form = ReglaForm(instance=regla)
    regla_list = Regla.objects.all()
    context = {'form': form,
               'regla_list': regla_list,
               'regla': regla
               }
    return render(request, 'reglaEditar.html', context)

def eliminar_regla(request, id):
    regla_list = Regla.objects.all()
    context = {
               'regla_list': regla_list
               }
    regla = Regla.objects.get(id=id)
    regla.delete()
    return redirect('reglaNueva')

def inicio(request):
    return render(request, 'inicio.html')
