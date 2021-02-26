from djongo import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

class BD_Integrada_Aves_Chinalco_Seca_2018(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_proyecto=models.CharField(max_length=255,blank=True,null=True)
    fecha_registro = models.DateField(auto_now=False, blank=True,null=True)

    temporada_status=[
        (1,'Seco'),
        (2,'Humedo'),
        (3,'Nevado')
    ]
    temporada_evaluacion = models.IntegerField(
        null=True, blank=True,
        choices=temporada_status,
        default=1)
    unidad_vegetacion = models.CharField(max_length=255,null=True, blank=True)
    estacion_muestreo = models.CharField(max_length=255,null=True, blank=True)
    unidad_muestreo = models.CharField(max_length=255,null=True, blank=True)
    metodo_muestreo = models.CharField(max_length=255,null=True, blank=True)

    periodo_status=[
        (1,'Diurno'),
        (2,'Tarde'),
        (3,'Nocturno')
    ]
    periodo_dia = models.IntegerField(
        null=True, blank=True,
        choices=periodo_status,
        default=1)
    hora_registro = models.CharField(max_length=255,null=True, blank=True)
    orden = models.CharField(max_length=255,null=True, blank=True)
    familia = models.CharField(max_length=255,null=True, blank=True)
    especie = models.CharField(max_length=255,null=True, blank=True)
    nombre_comun = models.CharField(max_length=255,null=True, blank=True)
    fuente_clasificacion_taxonomica = models.CharField(max_length=255,null=True, blank=True)
    x = models.IntegerField( null=True,blank=True)
    y = models.IntegerField( blank=True,null=True)
    altitud_msnm = models.IntegerField( blank=True,null=True)
    datum = models.CharField(max_length=255, blank=True,null=True)
    temperie = models.CharField(max_length=255, blank=True,null=True)

    tipo_status=[
        (1,'Cuantitativo'),
        (2,'Cualitativo')
    ]
    tipo_evaluacion = models.IntegerField(
        null=True, blank=True,
        choices=tipo_status,
        default=1)
    registro_visual = models.IntegerField( blank=True,null=True)
    registro_auditivo = models.IntegerField( blank=True,null=True)
    registro_captura = models.IntegerField( blank=True,null=True)
    registro_casual = models.IntegerField( blank=True,null=True)
    numero_total_individuos = models.IntegerField( blank=True,null=True)
    distancia_punto_conteo = models.IntegerField( blank=True,null=True)
    observaciones_etologia = models.CharField(max_length=255, blank=True,null=True)
    peso = models.DecimalField( max_digits=10, decimal_places=3 , blank=True,null=True)
    sexo = models.CharField(max_length=255, blank=True,null=True)
    longitud = models.IntegerField( blank=True,null=True)
    especie_ambiente = models.CharField(max_length=255, blank=True,null=True)
    edad_reproductiva = models.IntegerField( blank=True,null=True)
    conducta_reproductiva = models.CharField(max_length=255, blank=True,null=True)
    tipo_locomocion = models.CharField(max_length=255, blank=True,null=True)
    tipo_habitat = models.CharField(max_length=255, blank=True,null=True)
    grupo_triofico = models.CharField(max_length=255, blank=True,null=True)
    especie_endemica = models.CharField(max_length=255, blank=True,null=True)
    zona_endemismo = models.CharField(max_length=255, blank=True,null=True)
    restringida_eba = models.IntegerField( blank=True,null=True)
    restringida_bioma = models.CharField(max_length=255, blank=True,null=True)
    categoria_abundancia = models.CharField(max_length=255, blank=True,null=True)
    DS_O04_2014_MINAGRI = models.CharField(max_length=255, blank=True,null=True)
    iucn = models.CharField(max_length=255, blank=True,null=True)
    cites = models.CharField(max_length=255, blank=True,null=True)
    migratoria = models.CharField(max_length=255, blank=True,null=True)
    congregatoria = models.CharField(max_length=255, blank=True,null=True)
    observaciones_muestra = models.CharField(max_length=255, blank=True,null=True)
    actividad_humana = models.CharField(max_length=255, blank=True,null=True)

    estado_status=[
        (1,'Impactado'),
        (2,'Regular'),
        (3,'Bueno')
    ]
    estado_conservacion_habitat = models.IntegerField(
        null=True, blank=True,
        choices=estado_status,
        default=1)

    colector_registro = models.CharField(max_length=255, blank=True,null=True)
    tipo_muestra = models.CharField(max_length=255, blank=True,null=True)
    estado_muestra = models.CharField(max_length=255, blank=True,null=True)
    preparacion_muestra = models.CharField(max_length=255, blank=True,null=True)
    codigo_colecta = models.CharField(max_length=255, blank=True,null=True)
    institucion_deposito = models.CharField(max_length=255, blank=True,null=True)
    codigo_fotos = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.estacion_muestreo



class CoordenadasIntegradasAves2018(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unidad_vegetacion = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.CharField(max_length=255, blank=True, null=True)
    punto_conteo = models.CharField(max_length=255, blank=True, null=True)
    zona = models.CharField(max_length=255, blank=True, null=True)
    este1 = models.IntegerField( blank=True, null=True)
    norte1 = models.IntegerField( blank=True, null=True)
    altitud = models.IntegerField( blank=True, null=True)
    fecha_registro = models.DateField(auto_now=False, blank=True, null=True)
    temperie = models.CharField(max_length=255, blank=True, null=True)
    conservacion_estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)
    impacto_actividad_humana_cercana = models.CharField(max_length=255, blank=True, null=True)
    descripcion_punto_conteo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.estacion

class Fotos_Integrado_Aves_Chinalco_Seca_2018(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)
    componente_proyecto = models.CharField(max_length=255, blank=True, null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True, null=True)
    codigo_foto = models.CharField(max_length=255, blank=True, null=True)
    fecha_toma = models.DateField(auto_now=False, blank=True, null=True)
    especie = models.CharField(max_length=255, blank=True, null=True)
    paisaje = models.CharField(max_length=255, blank=True, null=True)
    nombre_cientifica= models.CharField(max_length=255, blank=True, null=True)
    nombre_comun = models.CharField(max_length=255, blank=True, null=True)
    nombre_local = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.estacion_muestreo



class georreferenciacion(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    inicial_final_puntual = models.CharField(max_length=255, blank=True,null=True)
    este1 = models.IntegerField( blank=True, null=True)
    norte1 = models.IntegerField( blank=True, null=True)
    altitud1 = models.IntegerField( blank=True, null=True)
    este2 = models.IntegerField( blank=True, null=True)
    norte2 = models.IntegerField( blank=True, null=True)
    altitud2 = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f'{self.inicial_final_puntual}'

    class Meta:
        abstract = True


class Coordenadas_BD(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unidad_vegetacion_quebrada = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    codigo_estacion = models.CharField(max_length=255, blank=True, null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True, null=True)
    tipo_unidad_muestral = models.CharField(max_length=255, blank=True, null=True)
    tamaño_unidad_muestreal = models.CharField(max_length=255, blank=True, null=True)
    subunidad_muestreo = models.CharField(max_length=255, blank=True, null=True)
    disciplina = models.CharField(max_length=255, blank=True, null=True)
    georreferenciacion_WGS8418L = models.EmbeddedField(
        model_container=georreferenciacion
    )
    objects = models.DjongoManager()
    hora_inicio_final = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha = models.DateField(auto_now=False, blank=True,null=True)
    descripcion_estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.sector

class lugar_toma_foto_BD(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    n = models.IntegerField( blank=True, null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True, null=True)
    sector_alto_bajo_medio = models.CharField(max_length=255, blank=True, null=True)
    codigo_quebrada = models.CharField(max_length=255, blank=True, null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)
    unidad_muestreo_um = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.unidad_vegetacion}'

    class Meta:
        abstract = True

class codificacion(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    codigo_foto = models.CharField(max_length=255, blank=True, null=True)
    fecha_toma =  models.DateField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return f'{self.codigo_foto}'

    class Meta:
        abstract = True

class tipo_foto(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    especie = models.CharField(max_length=255, blank=True, null=True)
    paisaje = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.especie}'

    class Meta:
        abstract = True

class especie(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    nombre_cientifico = models.CharField(max_length=255, blank=True, null=True)
    nombre_comun = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_cientifico}'

    class Meta:
        abstract = True

class ubicacion(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    localidad = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.localidad}'

    class Meta:
        abstract = True

class BD_fotos_BD(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lugar_toma_foto = models.EmbeddedField(
        model_container=lugar_toma_foto_BD
    )
    codificacion = models.EmbeddedField(
        model_container=codificacion
    )
    tipo_foto = models.EmbeddedField(
        model_container=tipo_foto
    )
    especie = models.EmbeddedField(
        model_container=especie
    )
    ubicacion = models.EmbeddedField(
        model_container=ubicacion
    )
    objects = models.DjongoManager()
    breve_descripcion_foto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.breve_descripcion_foto


class BD_anfibios_reptiles_BD(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_proyecto = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateField(auto_now=False, blank=True,null=True)
    temporada_evaluacion = models.CharField(max_length=255, blank=True, null=True)
    unidad_vegetacion_quebrada = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    codigo_quebrada = models.CharField(max_length=255, blank=True, null=True)
    disciplina_biologica = models.CharField(max_length=255, blank=True, null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True, null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True, null=True)
    metodo_muestreo = models.CharField(max_length=255, blank=True, null=True)
    tamaño_unidad_muestreo = models.CharField(max_length=255, blank=True, null=True)
    chip_marca_dedos = models.CharField(max_length=255, blank=True, null=True)
    periodo_dia = models.CharField(max_length=255, blank=True, null=True)
    hora_inicio_evaluacion = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hora_finalizacion_evaluacion = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hora_registro = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    familia = models.CharField(max_length=255, blank=True, null=True)
    especie = models.CharField(max_length=255, blank=True, null=True)
    nombre_comun = models.CharField(max_length=255, blank=True, null=True)
    nombre_local = models.CharField(max_length=255, blank=True, null=True)
    fuente_clasificacion_taxonomica = models.CharField(max_length=255, blank=True, null=True)
    x = models.IntegerField( blank=True,null=True)
    y = models.IntegerField( blank=True,null=True)
    proyeccion = models.CharField(max_length=255, blank=True, null=True)
    altitud_msnm = models.IntegerField( blank=True,null=True)
    datum = models.CharField(max_length=255, blank=True,null=True)
    temperatura_ambiente = models.CharField(max_length=255, blank=True, null=True)
    temperatura_suelo = models.CharField(max_length=255, blank=True, null=True)
    profundidad_hojarrasca_cm = models.IntegerField( blank=True,null=True)
    temperie = models.CharField(max_length=255, blank=True,null=True)
    distancia_perpendicular_unidad_muestreo = models.IntegerField( blank=True,null=True)
    altura_registro_distancia_vertical_suelo = models.IntegerField( blank=True,null=True)
    tipo_evaluacion = models.CharField(max_length=255, blank=True,null=True)
    tipo_registro = models.CharField(max_length=255, blank=True,null=True)
    numero_registro_directo = models.CharField(max_length=255, blank=True,null=True)
    numero_registro_indirecto = models.CharField(max_length=255, blank=True,null=True)
    numero_registro_captura = models.CharField(max_length=255, blank=True,null=True)
    estado_hallazgo = models.CharField(max_length=255, blank=True,null=True)
    etologia_comportamiento_individuo_registrado = models.CharField(max_length=255, blank=True,null=True)
    numero_total_individuos = models.IntegerField( blank=True,null=True)
    peso = models.DecimalField( max_digits=10, decimal_places=3 , blank=True,null=True)
    sexo = models.CharField(max_length=255, blank=True,null=True)
    longitud = models.IntegerField( blank=True,null=True)
    longitud_ano_hocico = models.IntegerField( blank=True,null=True)
    longitud_cola_lagartijas_serpientes = models.IntegerField( blank=True,null=True)
    tipo_reproduccion_anfibios = models.CharField(max_length=255, blank=True,null=True)
    estado_reproductivo_in_situ = models.CharField(max_length=255, blank=True,null=True)
    conducta_reproductva_in_situ = models.CharField(max_length=255, blank=True,null=True)
    conducta_social = models.CharField(max_length=255, blank=True,null=True)
    territorialidad = models.CharField(max_length=255, blank=True,null=True)
    habito = models.CharField(max_length=255, blank=True,null=True)
    tipo_habitat_in_situ = models.CharField(max_length=255, blank=True,null=True)
    micro_habitat_in_situ = models.CharField(max_length=255, blank=True,null=True)
    planta_dominante_microhabitat_in_situ = models.CharField(max_length=255, blank=True,null=True)
    grupo_trofico = models.CharField(max_length=255, blank=True,null=True)
    registro_dieta_in_situ = models.CharField(max_length=255, blank=True,null=True)
    especie_endemica = models.CharField(max_length=255, blank=True,null=True)
    nivel_endemismo = models.CharField(max_length=255, blank=True,null=True)
    distribucion_especie_endemica = models.CharField(max_length=255, blank=True,null=True)
    DSO342004AG = models.CharField(max_length=255, blank=True,null=True)
    IUCN = models.CharField(max_length=255, blank=True,null=True)
    CITES = models.CharField(max_length=255, blank=True,null=True)
    uso_potencial = models.CharField(max_length=255, blank=True,null=True)
    observaciones_registro = models.CharField(max_length=255, blank=True,null=True)
    actividad_humana = models.CharField(max_length=255, blank=True,null=True)
    estado_conservacion_habitat = models.CharField(max_length=255, blank=True,null=True)
    distancia_componente_minero = models.CharField(max_length=255, blank=True,null=True)
    medida_control_impedir_ingreso = models.CharField(max_length=255, blank=True,null=True)
    micro_habitat = models.CharField(max_length=255, blank=True,null=True)
    animal_instalaciones = models.CharField(max_length=255, blank=True,null=True)
    riesgo_contacto_animal_instalaciones = models.CharField(max_length=255, blank=True,null=True)
    observaciones_animales_muertos = models.CharField(max_length=255, blank=True,null=True)


    def __str__(self):
            return f'{self.codigo_proyecto}'


class inicio_coordenadas(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    este = models.IntegerField( blank=True, null=True)
    norte = models.IntegerField( blank=True, null=True)
    def __str__(self):
        return f'{self.este}'

    class Meta:
        abstract = True

class final_coordenadas(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    este = models.IntegerField( blank=True, null=True)
    norte = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f'{self.este}'

    class Meta:
        abstract = True

class hoja1_BD(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    estacion_monitoreo = models.CharField(max_length=255, blank=True,null=True)
    coordenadas_inicio = models.EmbeddedField(
        model_container=inicio_coordenadas
    )
    coordenadas_final = models.EmbeddedField(
        model_container=final_coordenadas
    )
    objects = models.DjongoManager()


    def __str__(self):
        return f'{self.unidad_vegetacion}'

class bitacora_BD_Mamiferos(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    dia = models.IntegerField( blank=True)
    fecha = models.DateTimeField(auto_now=False, blank=True,null=True)
    actividades = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return f'{self.actividades}'

class BD_mamiferos_BD_Mamiferos(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True,null=True)
    fecha_registro = models.DateTimeField(auto_now=False, blank=True,null=True)
    temporada = models.CharField(max_length=255, blank=True,null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    disciplina_biologica = models.CharField(max_length=255, blank=True,null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    subunidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    metodo_muestreo = models.CharField(max_length=255, blank=True,null=True)
    tamaño_unidad_muestreo = models.IntegerField( blank=True,null=True)
    numero_estaciones_muestreo = models.CharField(max_length=255, blank=True,null=True)
    periodo_dia = models.CharField(max_length=255, blank=True,null=True)
    hora_inicio_evaluacion = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hora_finalizacion_evaluacion = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hora_registro = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    orden = models.CharField(max_length=255, blank=True,null=True)
    familia = models.CharField(max_length=255, blank=True,null=True)
    especie = models.CharField(max_length=255, blank=True,null=True)
    nombre_comun = models.CharField(max_length=255, blank=True,null=True)
    nombre_local = models.CharField(max_length=255, blank=True,null=True)
    fuente_clasificacion_taxonomica = models.CharField(max_length=255, blank=True,null=True)
    x = models.IntegerField( blank=True,null=True)
    y = models.IntegerField( blank=True,null=True)
    proyeccion = models.CharField(max_length=255, blank=True,null=True)
    altitud_msnm = models.IntegerField( blank=True,null=True)
    datum = models.CharField(max_length=255, blank=True,null=True)
    distancia_unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    distancia_perpendicular_unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    tipo_evaluacion = models.CharField(max_length=255, blank=True,null=True)
    tipo_registro = models.CharField(max_length=255, blank=True,null=True)
    numero_registro_directo = models.CharField(max_length=255, blank=True,null=True)
    numero_registro_indirecto = models.IntegerField( blank=True,null=True)
    registro_captura = models.CharField(max_length=255, blank=True,null=True)
    estado_hallazgo = models.CharField(max_length=255, blank=True,null=True)
    observaciones_etologia = models.CharField(max_length=255, blank=True,null=True)
    numero_total_individuos = models.IntegerField( blank=True,null=True)
    crias = models.IntegerField( blank=True,null=True)
    infantes = models.IntegerField( blank=True,null=True)
    juvenil = models.IntegerField( blank=True,null=True)
    adulto = models.IntegerField( blank=True,null=True)
    peso = models.DecimalField( max_digits=10, decimal_places=3 , blank=True,null=True)
    sexo = models.CharField(max_length=255, blank=True,null=True)
    longitud_total = models.IntegerField( blank=True,null=True)
    longitud_antebrazo = models.IntegerField( blank=True,null=True)
    longitud_tibia = models.IntegerField( blank=True,null=True)
    longitud_pata = models.IntegerField( blank=True,null=True)
    longitud_oreja = models.IntegerField( blank=True,null=True)
    longitud_tragus= models.IntegerField( blank=True,null=True)
    longitud_cola = models.IntegerField( blank=True,null=True)
    estado_reproductivo = models.CharField(max_length=255, blank=True,null=True)
    conducta_reproductiva = models.CharField(max_length=255, blank=True,null=True)
    conducta_social = models.CharField(max_length=255, blank=True,null=True)
    especie_segun_ambiente = models.CharField(max_length=255, blank=True,null=True)
    tipo_locomocion = models.CharField(max_length=255, blank=True,null=True)
    tipo_habitat = models.CharField(max_length=255, blank=True,null=True)
    micro_habitat = models.CharField(max_length=255, blank=True,null=True)
    grupo_trofico = models.CharField(max_length=255, blank=True,null=True)
    registro_dieta = models.CharField(max_length=255, blank=True,null=True)
    especie_endemica = models.CharField(max_length=255, blank=True,null=True)
    nivel_endemismo = models.CharField(max_length=255, blank=True,null=True)
    zona_endemismo = models.CharField(max_length=255, blank=True,null=True)
    DSO042014AG = models.CharField(max_length=255, blank=True,null=True)
    IUCN = models.CharField(max_length=255, blank=True,null=True)
    CITES = models.CharField(max_length=255, blank=True,null=True)
    uso_potencial = models.CharField(max_length=255, blank=True,null=True)
    observaciones_sobre_muestra = models.CharField(max_length=255, blank=True,null=True)
    temperie = models.CharField(max_length=255, blank=True,null=True)
    actividad_humana = models.CharField(max_length=255, blank=True,null=True)
    estado_conservacion_habitat = models.CharField(max_length=255, blank=True,null=True)
    colector_registro = models.CharField(max_length=255, blank=True,null=True)
    codigo_colecta = models.CharField(max_length=255, blank=True,null=True)
    tipo_muestra = models.CharField(max_length=255, blank=True,null=True)
    estado_muestra = models.CharField(max_length=255, blank=True,null=True)
    tipo_preparacion_muestra = models.CharField(max_length=255, blank=True,null=True)
    institucion_deposito = models.CharField(max_length=255, blank=True,null=True)
    codigo_fotos = models.CharField(max_length=255, blank=True,null=True)
    observaciones = models.CharField(max_length=255, blank=True,null=True)



    def __str__(self):
            return f'{self.codigo_proyecto}'


class Esfuerzo_Muestreo_BD_Mamiferos(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, blank=True, null=True)
    grupo1 = models.CharField(max_length=255, blank=True)
    temporada = models.CharField(max_length=255, blank=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True)
    estacion_muestreo1 = models.CharField(max_length=255, blank=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True)
    trampas_noche = models.IntegerField( blank=True, null=True)
    numero_total_individuos = models.IntegerField( blank=True, null=True)
    especie1 = models.IntegerField( blank=True, null=True)
    especie2 = models.IntegerField( blank=True, null=True)
    especie3 = models.IntegerField( blank=True, null=True)
    especie4 = models.IntegerField( blank=True, null=True)
    clima = models.CharField(max_length=255, blank=True)
    grupo = models.CharField(max_length=255, blank=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True)
    unidad_muestreo_transecto = models.CharField(max_length=255, blank=True)
    coordenadas_utm = models.IntegerField( blank=True, null=True)
    coordenadas2_utm = models.IntegerField( blank=True, null=True)
    elevacion_metros = models.IntegerField( blank=True, null=True)
    coordenadas3_utm = models.IntegerField( blank=True, null=True)
    coordenadas4_utm = models.IntegerField( blank=True, null=True)
    elevacion2_metros = models.IntegerField( blank=True, null=True)
    metros_recorridos = models.IntegerField( blank=True, null=True)
    coordenadas5_utm = models.IntegerField( blank=True, null=True)
    coordenadas6_utm = models.IntegerField( blank=True, null=True)
    elevacion3_metros = models.IntegerField( blank=True, null=True)
    coordenadas7_utm = models.IntegerField( blank=True, null=True)
    coordenadas8_utm = models.IntegerField( blank=True, null=True)
    elevacion4_metros = models.IntegerField( blank=True, null=True)
    coordenadas9_utm = models.IntegerField( blank=True, null=True)
    coordenadas10_utm = models.IntegerField( blank=True, null=True)
    elevacion5_metros = models.IntegerField( blank=True, null=True)
    coordenadas11_utm = models.IntegerField( blank=True, null=True)
    coordenadas12_utm = models.IntegerField( blank=True, null=True)
    elevacion6_metros = models.IntegerField( blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    mamiferos_mayores = models.CharField(max_length=255, blank=True, null=True)
    mamiferos_menores = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
            return f'{self.unidad_muestreo}'


class coordenadas_bd_mamiferos(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    este = models.IntegerField( blank=True, null=True)
    norte = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f'{self.este}'

    class Meta:
        abstract = True





class Coordenadas_reporte_BD_Mamiferos(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sector = models.CharField(max_length=255, blank=True,null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    grupo = models.CharField(max_length=255, blank=True,null=True) #campo no existente
    coordenadas_utm_wgs84 = models.EmbeddedField(
        model_container=coordenadas_bd_mamiferos
    )
    altitud = models.IntegerField( blank=True, null=True)
    objects = models.DjongoManager()


    def __str__(self):
                return f'{self.sector}'

class Hoja3_BD_Vegetacion_2018(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    especies = models.CharField(max_length=255, blank=True,null=True)
    DS0432006AG = models.CharField(max_length=255, blank=True,null=True)
    endemico = models.CharField(max_length=255, blank=True,null=True)
    IUCN = models.CharField(max_length=255, blank=True,null=True)
    CITES = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return f'{self.especies}'

class Base_Datos_Vegetacion_2018(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.IntegerField( blank=True, null=True)
    disciplina = models.CharField(max_length=255, blank=True,null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True,null=True)
    fecha_registro = models.DateField(auto_now=False, blank=True,null=True)
    temporada = models.CharField(max_length=255, blank=True,null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    subunidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    metodo_muestreo = models.CharField(max_length=255, blank=True,null=True)
    tamaño_unidad_muestreo = models.IntegerField( blank=True, null=True)
    division = models.CharField(max_length=255, blank=True,null=True)
    orden = models.CharField(max_length=255, blank=True,null=True)
    familia = models.CharField(max_length=255, blank=True,null=True)
    especie = models.CharField(max_length=255, blank=True,null=True)
    nombre_comun = models.CharField(max_length=255, blank=True,null=True)
    nombre_local = models.CharField(max_length=255, blank=True,null=True)
    fuente_clasificacion_taxonomica = models.CharField(max_length=255, blank=True,null=True)
    cobertura_vegetal = models.CharField(max_length=255,blank=True,null=True)
    x_norte = models.IntegerField( blank=True,null=True)
    y_norte = models.IntegerField( blank=True,null=True)
    proyeccion = models.CharField(max_length=255, blank=True,null=True)
    altitud_msnm = models.IntegerField( blank=True,null=True)
    datum = models.CharField(max_length=255, blank=True,null=True)
    numero_individuos = models.CharField(max_length=255, blank=True,null=True)
    DAP_cm = models.IntegerField( blank=True,null=True)
    altura_total = models.IntegerField( blank=True,null=True)
    estado_conservacion_habitat = models.CharField(max_length=255, blank=True,null=True)
    fenologia = models.CharField(max_length=255, blank=True,null=True)
    habito = models.CharField(max_length=255, blank=True,null=True)
    colector_registro = models.CharField(max_length=255, blank=True,null=True)
    tipo_evaluacion = models.CharField(max_length=255, blank=True,null=True)
    uso = models.CharField(max_length=255, blank=True,null=True)
    tipo_uso = models.CharField(max_length=255, blank=True,null=True)
    DS0432006AG = models.CharField(max_length=255, blank=True,null=True)
    endemico = models.CharField(max_length=255, blank=True,null=True)
    IUCN = models.CharField(max_length=255, blank=True,null=True)
    CITES = models.CharField(max_length=255, blank=True,null=True)
    FOTO = models.CharField(max_length=255, blank=True,null=True)
    tipo_ganado_observado = models.CharField(max_length=255, blank=True,null=True)
    observacion = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
            return f'{self.disciplina}'


class Esfuerzo_Muestreo_BD_Vegetacion_2018(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_proyecto = models.CharField(max_length=255, blank=True,null=True)
    fecha = models.DateField(auto_now=False, blank=True,null=True)
    temporada = models.CharField(max_length=255, blank=True,null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    sector = models.CharField(max_length=255, blank=True,null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    esfuerzo_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_esfuerzo_muestreo = models.CharField(max_length=255, blank=True,null=True)
    tamaño_unidad_metros = models.IntegerField( blank=True,null=True)

    def __str__(self):
            return f'{self.codigo_proyecto}'


class Compensacion_Ambiental_Vegetacion_2018(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=255, blank=True,null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True,null=True)
    fecha_registro = models.DateField(auto_now=False, blank=True,null=True)
    temporada = models.CharField(max_length=255, blank=True,null=True)
    unidad_vegetacion = models.CharField(max_length=255, blank=True,null=True)
    estacion_muestreo = models.CharField(max_length=255, blank=True,null=True)
    unidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    subunidad_muestreo = models.CharField(max_length=255, blank=True,null=True)
    metodo_muestreo = models.CharField(max_length=255, blank=True,null=True)
    tamaño_unidad_muestreo = models.IntegerField( blank=True,null=True)
    especie_dominante = models.CharField(max_length=255, blank=True,null=True)
    x_norte = models.IntegerField( blank=True,null=True)
    y_este = models.IntegerField( blank=True,null=True)
    proyeccion = models.CharField(max_length=255, blank=True,null=True)
    altitud_msnm = models.IntegerField( blank=True,null=True)
    datum = models.CharField(max_length=255, blank=True,null=True)
    altura_total_muestra = models.IntegerField( blank=True,null=True)
    area_muestra = models.IntegerField( blank=True,null=True)
    profundidad_total_calicata = models.IntegerField( blank=True,null=True)
    altura_vegetacion = models.IntegerField( blank=True,null=True)
    altura_materia_organica = models.IntegerField( blank=True,null=True)
    estado_conservacion_habitat = models.IntegerField( blank=True,null=True)
    colector_registro = models.IntegerField( blank=True,null=True)
    FOTO = models.IntegerField( blank=True,null=True)
    observacion_impacto = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
            return f'{self.codigo_proyecto}'

