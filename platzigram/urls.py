"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from biologia import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

    #Avez Links
    path('biologia/form_coordenadas_aves/',views.form_coordenadas_aves, name='form_coordenadas_aves'),
    path('biologia/form_base_datos_avez/',views.form_BD_Avez_Chinalco, name='form_BD_Avez_Chinalco'),
    path('biologia/form_fotos_integrado_avez/',views.form_fotos_integrado_Avez_Chinalco, name='form_fotos_integrado_Avez_Chinalco'),

    #Anfivioz_Reptiles (BD) Links
    path('biologia/form_base_anfibios_reptiles/',views.form_anfibios_reptiles_base_datos, name='form_anfibios_reptiles_base_datos'),
    path('biologia/form_coord_anf_rep/',views.form_coordenadas_anfibios_repites_bd, name='form_coordenadas_anfibios_repites_bd'),
    path('biologia/form_hoja_1/',views.form_db_hoja1, name='form_db_hoja1'),
    path('biologia/form_fotos_bd/',views.form_fotos_db, name='form_fotos_db'),

    #Mamiferos Links
    path('biologia/form_bitacora_mamiferos/',views.form_bitacora_mamiferos, name='form_bitacora_mamiferos'),
    path('biologia/form_esfuerzo_muestreo_mamiferos/',views.form_esfuerzo_muestreo_mamiferos, name='form_esfuerzo_muestreo_mamiferos'),
    path('biologia/form_coordenadas_reporte_mamiferos/',views.form_coordenadas_reporte_mamiferos, name='form_coordenadas_reporte_mamiferos'),
    path('biologia/form_BD_mamiferos/',views.form_BD_mamiferos, name='form_BD_mamiferos'),

    #Vegetacion Links
    path('biologia/form_hoja3_vegetacion/',views.form_hoja3_vegetacion, name='form_hoja3_vegetacion'),
    path('biologia/form_Vegetacion_Compensacion_Ambiental/',views.form_Vegetacion_Compensacion_Ambiental, name='form_Vegetacion_Compensacion_Ambiental'),
    path('biologia/form_Vegetacion_Base_datos/',views.form_Vegetacion_Base_datos, name='form_Vegetacion_Base_datos'),
    path('biologia/form_Vegetacion_esfuerzo_muestreo/',views.form_Vegetacion_esfuerzo_muestreo, name='form_Vegetacion_esfuerzo_muestreo'),

    #Lista_Formularios Links
    path('biologia/list_forms_aves/',views.list_forms_Aves, name='lista_formularios_aves'),
    path('biologia/list_forms_anfibios_reptiles/',views.list_forms_Reptiles_Amfibios, name='lista_formularios_anfibios_reptiles'),
    path('biologia/list_forms_mamiferos/',views.list_forms_Mamiferos, name='lista_formularios_mamiferos'),
    path('biologia/list_forms_vegetacion/',views.list_forms_Vegetacion, name='lista_formularios_vegetacion'),

    #FORMULARIOS UNICOS - VISTA
    #Avez
    path('biologia/Avez_chinalco_BD/<id>',views.formulario_unic_Aves_chinalco, name='formulario_unic_Aves_chinalco'),
    path('biologia/Avez_chinalco_BD_coordenadas/<id>',views.formulario_unic_aves_coordenadas_int, name='formulario_unic_aves_coordenadas_int'),
    path('biologia/Avez_chinalco_BD_fotos/<id>',views.formulario_unic_Aves_chinalco_fotos, name='formulario_unic_Aves_chinalco_fotos'),

    #Anfivios

    path('biologia/Reptiles_anfibios_BD/<id>',views.formulario_unic_Reptiles_anfibios_BD, name='formulario_unic_Reptiles_anfibios_BD'),
    path('biologia/Reptiles_anfibios_BD_fotos/<id>',views.formulario_unic_Reptiles_anfibios_BD_fotos, name='formulario_unic_Reptiles_anfibios_BD_fotos'),
    path('biologia/Reptiles_anfibios_coordenadas/<id>',views.formulario_unic_Reptiles_anfibios_coordenadas, name='formulario_unic_Reptiles_anfibios_coordenadas'),
    path('biologia/Reptiles_anfibios_hoja1/<id>',views.formulario_unic_Reptiles_anfibios_BD_hoja1, name='formulario_unic_Reptiles_anfibios_BD_hoja1'),

    #Mamiferos

    path('biologia/Mamiferos_BD/<id>',views.formulario_unic_Mamiferos_BD, name='formulario_unic_Mamiferos_BD'),
    path('biologia/Mamiferos_BD_bitacora/<id>',views.formulario_unic_Mamiferos_bitacora, name='formulario_unic_Mamiferos_bitacora'),
    path('biologia/Mamiferos_BD_coordenadas/<id>',views.formulario_unic_Mamiferos_coordenadas, name='formulario_unic_Mamiferos_coordenadas'),
    path('biologia/Mamiferos_BD_esfuerzo_muestreo/<id>',views.formulario_unic_Mamiferos_ezfuerzo_muestreo, name='formulario_unic_Mamiferos_ezfuerzo_muestreo'),

    #Vegetacion

    path('biologia/Vegetacion_BD/<id>',views.formulario_unic_Vegeta_BD, name='formulario_unic_Vegeta_BD'),
    path('biologia/Vegetacion_BD_compensacion/<id>',views.formulario_unic_Vegeta_compensacion, name='formulario_unic_Vegeta_compensacion'),
    path('biologia/Vegetacion_BD_esfuerzo_muestreo/<id>',views.formulario_unic_Vegeta_esfuerzo_muestreo, name='formulario_unic_Vegeta_esfuerzo_muestreo'),
    path('biologia/Vegetacion_BD_hoja3/<id>',views.formulario_unic_Vegeta_hoja3, name='formulario_unic_Vegeta_hoja3'),



    # ========== EXPORTAR EXCEL (COMPLETO/POR UNIDAD) ============

    #===================================================#
    # Rama de Aves
    path('export/excel', views.export_aves_xls, name='export_excel'),
    path('export/excelAves', views.export_fotos_aves_xls, name='export_excel_aves'),
    path('export/excelAvesCoordenadas', views.export_coordenadas_aves_xls, name='export_excel_coordenadas_aves'),

    #Rama Unico Aves
    path('export/excelUnic/<id>', views.export_aves_unica_xls, name='export_excel_unico'),
    path('export/excelAvesUnic/<id>', views.export_fotos_aves_unica_xls, name='export_excel_aves_unico'),
    path('export/excelAvesCoordenadasUnic/<id>', views.export_coordenadas_aves_unica_xls, name='export_excel_coordenadas_aves_unic'),
    #===================================================#

    #===================================================#
    # Rama de Reptiles
    path('export/excelBDReptilesAnfibios', views.export_Anfibios_reptiles_BD_xls, name='export_excel_bd_anfibios_reptiles'),
    path('export/excelCoordenadasBDAnfiRep', views.Reporte_prueba_coordenadas, name='export_excel_coordenadas_anfi_rep'),
    path('export/excelBDFotosAnfiRep', views.export_BD_Fotos_Reptiles_Anfibios_xls, name='export_excel_fotos_bd_anfi_rep'),
    path('export/excelBDHoja1AnfiRep', views.export_BD_Hoja1_Reptiles_Anfibios_xls, name='export_excel_hoja1_bd_anfi_rep'),

    #Rama Unico Reptiles
    path('export/excelBDHoja1AnfiRep/<id>', views.export_BD_Hoja1_Reptiles_Anfibios_xls_unic, name='export_excel_hoja1_bd_anfi_rep_unic'),
    path('export/excelBDFotosAnfiRep/<id>', views.export_fotos_Reptiles_Anfibios_unico, name='exportar_fotos_Reptiles_Anfibios_unico'),
    path('export/excelCoordenadasBDAnfiRep/<id>', views.Reporte_prueba_coordenadas_unico, name='Reportar_prueba_coordenadas_unico'),
    path('export/excelBDReptilesAnfibios/<id>', views.export_Anfibios_reptiles_BD_unico, name='exportar_Anfibios_reptiles_BD_unico'),

    #===================================================#

    #===================================================#
    # Rama de Mamiferos

    path('export/excelBDMamiferos', views.export_base_datos_mamiferos, name='export_excel_bd_mamiferos'),
    path('export/excelBitacoraMamiferos', views.export_bitacora_mamiferos, name='export_excel_bitacora_mamiferos'),
    path('export/excelReporteCoordenadasMamiferos', views.export_coordenadas_reporte_mamiferos, name='export_excel_coordenadas_reporte_mamiferos'),
    path('export/excelReporteEsfuerzoMuestreoMamiferos', views.export_esfuerzo_muestreo_mamifero, name='export_excel_esfuerzo_muestreo_mamiferos'),

    #Rama Unico Mamiferos
    path('export/excelBDMamiferos/<id>', views.export_base_datos_mamiferos_unic, name='export_excel_bd_mamiferos_unic'),
    path('export/excelReporteCoordenadasMamiferos/<id>', views.export_coordenadas_reporte_mamiferos_unic, name='export_excel_coordenadas_reporte_mamiferos_unic'),
    path('export/excelEsfuerzoMuestreoMamiferos/<id>', views.export_esfuerzo_muestreo_mamiferos_unico, name='export_esfuerzo_muestreo_mamiferos_unico'),
    path('export/excelBitacoraMamiferos/<id>', views.export_bitacora_mamiferos_unico, name='export_bitacora_mamiferos_unico'),


    #===================================================#

    # Descargar Excel Rama de Vegetales
    path('export/excelHoja3', views.export_vegetacion_hoja3, name='export_excel_hoja3'),
    path('export/excelBDVegetacion', views.export_vegetacion_bd, name='export_excel_bd_vegetacion'),
    path('export/excelEsfuerzoVegetacion', views.export_vegetacion_esfuerzo, name='export_excel_esfuerzo_vegetacion'),
    path('export/excelCompensacionVegetacion', views.export_vegetacion_compensacion, name='export_excel_compensacion_vegetacion'),

    # Descargar Excel para un registro de Vegetacion
    path('export/excelHoja3Vegetacion/<id>', views.export_vegetacion_hoja3_unic, name='export_excel_vege_hoja3_unic'),
    path('export/excelEsfuerzoVegetacion/<id>', views.export_vegetacion_esfuerzo_unic, name='export_excel_vege_esfuerzo_unic'),
    path('export/excelCompensacionVegetacion/<id>', views.export_vegetacion_compensacion_unic, name='export_excel_vege_compensacion_unic'),
    path('export/excelBaseDatosVegetacion/<id>', views.export_basedatos_vegetacion_unico, name='export_basedatos_vegetacion_unico'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

