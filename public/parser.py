# -*- coding: utf-8-*-
import time
import os
import glob
import re
import sys
import unicodedata
from json import JSONEncoder
import json
import requests
import datetime as dd
import collections
import time
import logging
import logging.handlers


positionToken = 0
tokens = []
my_logger = logging.getLogger('MyLogger')
activeToken = ""
tokenUsage = 0

def readTokens():
    global tokens
    headers = {'content-type': 'application/json'}
    okVal = True
    while okVal:
        try:
            tokenArray= requests.get('http://localhost:3000/api/v1/tokens/get_token.json', headers = headers)
            okVal = False
            print tokenArray.content
        except:
            pass
    for element in json.loads(tokenArray.content)['tokens']:
        tokens.append(element)

def refreshToken():
    global activeToken
    global tokenUsage
    global my_logger
    my_logger.debug("Info - Token " + activeToken + "; uso " + str(tokenUsage))
    headers = {'content-type': 'application/json'}
    if activeToken != "":
        kConst = True
        while kConst:
            try:
                requests.post('http://localhost:3000/api/v1/tokens/update_token.json',data= json.dumps({"token": activeToken, "amount" : tokenUsage }), headers = headers)
                kConst = False
            except:
                pass
    activeToken = tokens.pop(0)
    tokenUsage = 0

def tryAPIRequest(url):
    global tokenUsage
    headers = {'content-type': 'application/json'}
    print url+activeToken
    cumTry = True
    while cumTry:
        try:
            customRequest = requests.get(url+activeToken, headers = headers)
            cumTry = False
        except:
            pass
    #customRequest.raise_for_status()
    return json.loads(customRequest.content)

def tender_scraper(startingDate):
    global tokenUsage
    fesha = startingDate
    delta = dd.timedelta(days=1)
    endDate = dd.date.today()
    while fesha <= endDate:
        if fesha.day<10:
            theDay = "0"+str(fesha.day)
        else:
            theDay = str(fesha.day)
        #print theDay
        if fesha.month<10:
            theMonth = "0"+str(fesha.month)
        else:
            theMonth = str(fesha.month)
        #print theMonth
        theYear= str(fesha.year)
        dateParam = theDay+theMonth+theYear
        print dateParam
        tokenValidator = True
        while tokenValidator:
            #print activeToken
            dailyTenders = tryAPIRequest('http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?fecha='+dateParam+'&ticket=')
            # Condition token working
            if "Cantidad" in dailyTenders:
                tokenUsage = tokenUsage +1
                tokenValidator = False
            else:
                if len(tokens)>0:
                    refreshToken()
                else:
                    my_logger.debug("Warning - No quedan tokens disponibles")
                    sys.exit(0)

        for data in dailyTenders["Listado"]:
            #Get Tender name
            if data.get("Nombre") is None:
                tenderName = None
            else:
                tenderName = data["Nombre"].encode('utf-8')
            #Gey tenderCode
            if data.get("CodigoExterno") is None:
                tenderCode = None
            else:
                tenderCode = data["CodigoExterno"].encode('utf-8')
                print tenderCode
            # tenderCode = "1553-1157-L115"
            #hay tender sin fecha de cierre
            try:
                tenderExpiringDate = data["FechaCierre"].encode('utf-8')
            except:
                tenderExpiringDate = None
            #Get Status
            if data.get("CodigoEstado") is None:
                tenderStatusCode = None
            else:
                tenderStatusCode = data["CodigoEstado"]
            # tenderStatusCode = 12

            #CHECK IF THE EXTERNAL CODE EXISTS
            #print tenderCode
            apiReq = True
            while apiReq:
                try:
                    getDataFromAPIRequest = requests.get('http://localhost:3000/api/v1/tenders/search?code='+ tenderCode, headers = {'content-type': 'application/json'})
                    getDataFromAPI= json.loads(getDataFromAPIRequest.text.encode('utf-8'))
                    apiReq = False
                except:
                    pass
            if getDataFromAPI["isCreated"] is True:
                if getDataFromAPI["state"]==tenderStatusCode:
                    #if statusCode is the same do nothing
                    # print "doNothing"
                    pass
                else:
                    #the tender exists, but the status code is different
                    postPutData =   {
                                        "state": tenderStatusCode,
                                        "date": dateParam,
                                        "code": tenderCode,
                                    }
                    #TODO : update call
                    print json.dumps(postPutData)
                    KConsta = True
                    while KConsta:
                        try:
                            updateData = requests.post('http://localhost:3000/api/v1/tenders/state',data=json.dumps(postPutData), headers = {'content-type': 'application/json'})
                            KConsta = False
                        except:
                            pass
                    #print  updateData.text.encode('utf-8')

            else:
                #if don't exists, get the data from the api request
                areasArray = []
                tokenValidator = True
                while tokenValidator:
                    #print activeToken
                    newTender = tryAPIRequest('http://api.mercadopublico.cl/servicios/v1/publico/licitaciones.json?codigo='+tenderCode+'&ticket=')
                    #print newTender

                    error1000 = False

                    try:
                        messageEr = newTender["Codigo"]
                        if messageEr == 10000:
                            error1000 = True
                            tokenUsage = tokenUsage +1
                            tokenValidator = False
                            #print "entro al try"
                    except:
                        pass

                    if "Cantidad" in newTender:
                        tokenUsage = tokenUsage +1
                        tokenValidator = False
                    else:
                        if len(tokens)>0:
                            refreshToken()
                        else:
                            my_logger.debug("Warning - No quedan tokens disponibles")
                            sys.exit(0)


                if tenderCode == '507428-204-LP12':
                    print "skipping legs"
                    continue
                if error1000 == True:
                    #Codigo 10000
                    my_logger.debug("Check - Licitacion Missing: " + tenderCode)
                    continue
                    #sys.exit(0)
                if newTender["Cantidad"] == 0:
                    #La licitacion desaparece
                    my_logger.debug("Check - Licitacion Missing: " + tenderCode)
                    continue
                else:
                    aux= newTender["Listado"][0]

                    #Get info about buyer

                    #Get buyersCode
                    if aux.get("Comprador").get("CodigoOrganismo") is None:
                        buyersCode = None
                    else:
                        buyersCode = aux["Comprador"]["CodigoOrganismo"].encode('utf-8')

                    #Get buyersName
                    if aux.get("Comprador").get("NombreOrganismo") is None:
                        buyersName = None
                    else:
                        buyersName = aux["Comprador"]["NombreOrganismo"].encode('utf-8')

                    #Get rutUnidad
                    if aux.get("Comprador").get("RutUnidad") is None:
                        rutUnidad = None
                    else:
                        rutUnidad = aux["Comprador"]["RutUnidad"].encode('utf-8')

                    #Get codigoUnidad
                    if aux.get("Comprador").get("CodigoUnidad") is None:
                        codigoUnidad = None
                    else:
                        codigoUnidad = aux["Comprador"]["CodigoUnidad"].encode('utf-8')

                    #Get nombreUnidad
                    if aux.get("Comprador").get("NombreUnidad") is None:
                        nombreUnidad = None
                    else:
                        nombreUnidad = aux["Comprador"]["NombreUnidad"].encode('utf-8')

                    #Get direccionUnidad
                    if aux.get("Comprador").get("DireccionUnidad") is None:
                        direccionUnidad = None
                    else:
                        direccionUnidad = aux["Comprador"]["DireccionUnidad"].encode('utf-8')

                    #Get comunaUnidad
                    if aux.get("Comprador").get("ComunaUnidad") is None:
                        comunaUnidad = None
                    else:
                        comunaUnidad = aux["Comprador"]["ComunaUnidad"].encode('utf-8')

                    #Get buyersRegion
                    if aux.get("Comprador").get("RegionUnidad") is None:
                        buyersRegion = None
                    else:
                        buyersRegion = aux["Comprador"]["RegionUnidad"].encode('utf-8')

                    #Get rutUsuario
                    if aux.get("Comprador").get("RutUsuario") is None:
                        rutUsuario = None
                    else:
                        rutUsuario = aux["Comprador"]["RutUsuario"].encode('utf-8')

                    #Get codigoUsuario
                    if aux.get("Comprador").get("CodigoUsuario") is None:
                        codigoUsuario = None
                    else:
                        codigoUsuario = aux["Comprador"]["CodigoUsuario"].encode('utf-8')

                    #Get nombreUsuario
                    if aux.get("Comprador").get("NombreUsuario") is None:
                        nombreUsuario = None
                    else:
                        nombreUsuario = aux["Comprador"]["NombreUsuario"].encode('utf-8')

                    #Get cargoUsuario
                    if aux.get("Comprador").get("CargoUsuario") is None:
                        cargoUsuario = None
                    else:
                        cargoUsuario = aux["Comprador"]["CargoUsuario"].encode('utf-8')

                    #Get info about Tender

                    #Get tenderDesc
                    if aux.get("Descripcion") is None:
                        tenderDesc = None
                    else:
                        tenderDesc = aux["Descripcion"].encode('utf-8')

                    #Get diasCierreLicitacion
                    if aux.get("DiasCierreLicitacion") is None:
                        diasCierreLicitacion = None
                    else:
                        diasCierreLicitacion = aux["DiasCierreLicitacion"].encode('utf-8')

                    #Get informada
                    if aux.get("Informada") is None:
                        informada = None
                    else:
                        informada = aux["Informada"]

                    #Get codigoTipo
                    if aux.get("CodigoTipo") is None:
                        codigoTipo = None
                    else:
                        codigoTipo = aux["CodigoTipo"]

                    #Get tipo
                    if aux.get("Tipo") is None:
                        tipo = None
                    else:
                        tipo = aux["Tipo"].encode('utf-8')

                    #Get tipoConvocatoria
                    if aux.get("TipoConvocatoria") is None:
                        tipoConvocatoria = None
                    else:
                        tipoConvocatoria = aux["TipoConvocatoria"].encode('utf-8')

                    #Get moneda
                    if aux.get("Moneda") is None:
                        moneda = None
                    else:
                        moneda = aux["Moneda"].encode('utf-8')

                    #Get etapas
                    if aux.get("Etapas") is None:
                        etapas = None
                    else:
                        etapas = aux["Etapas"]

                    #Get estadoEtapas
                    if aux.get("EstadoEtapas") is None:
                        estadoEtapas = None
                    else:
                        estadoEtapas = aux["EstadoEtapas"].encode('utf-8')

                    #Get tomaRazon
                    if aux.get("TomaRazon") is None:
                        tomaRazon = None
                    else:
                        tomaRazon = aux["TomaRazon"].encode('utf-8')

                    #Get estadoPublicidadOfertas
                    if aux.get("EstadoPublicidadOfertas") is None:
                        estadoPublicidadOfertas = None
                    else:
                        estadoPublicidadOfertas = aux["EstadoPublicidadOfertas"]

                    #Get justificacionPublicidad
                    if aux.get("JustificacionPublicidad") is None:
                        justificacionPublicidad = None
                    else:
                        justificacionPublicidad = aux["JustificacionPublicidad"].encode('utf-8')

                    #Get contrato
                    if aux.get("Contrato") is None:
                        contrato = None
                    else:
                        contrato = aux["Contrato"].encode('utf-8')

                    #Get obras
                    if aux.get("Obras") is None:
                        obras = None
                    else:
                        obras = aux["Obras"].encode('utf-8')

                    #Get cantidadReclamos
                    if aux.get("CantidadReclamos") is None:
                        cantidadReclamos = None
                    else:
                        cantidadReclamos = aux["CantidadReclamos"]

                    #Get unidadTiempoEvaluacion
                    if aux.get("UnidadTiempoEvaluacion") is None:
                        unidadTiempoEvaluacion = None
                    else:
                        unidadTiempoEvaluacion = aux["UnidadTiempoEvaluacion"]

                    #Get direccionVisita
                    if aux.get("DireccionVisita") is None:
                        direccionVisita = None
                    else:
                        direccionVisita = aux["DireccionVisita"].encode('utf-8')

                    #Get direccionEntrega
                    if aux.get("DireccionEntrega") is None:
                        direccionEntrega = None
                    else:
                        direccionEntrega = aux["DireccionEntrega"].encode('utf-8')

                    #Get estimacion
                    if aux.get("Estimacion") is None:
                        estimacion = None
                    else:
                        estimacion = aux["Estimacion"]

                    #Get fuenteFinanciamiento
                    if aux.get("FuenteFinanciamiento") is None:
                        fuenteFinanciamiento = None
                    else:
                        fuenteFinanciamiento = aux["FuenteFinanciamiento"].encode('utf-8')

                    #Get visibilidadMonto
                    if aux.get("VisibilidadMonto") is None:
                        visibilidadMonto = None
                    else:
                        visibilidadMonto = aux["VisibilidadMonto"]

                    #Get montoEstimado
                    if aux.get("MontoEstimado") is None:
                        montoEstimado = None
                    else:
                        montoEstimado = str(aux["MontoEstimado"])

                    #Get tiempo
                    if aux.get("Tiempo") is None:
                        tiempo = None
                    else:
                        tiempo = aux["Tiempo"]

                    #Get unidadTiempo
                    if aux.get("UnidadTiempo") is None:
                        unidadTiempo = None
                    else:
                        unidadTiempo = aux["UnidadTiempo"].encode('utf-8')

                    #Get modalidad
                    if aux.get("Modalidad") is None:
                        modalidad = None
                    else:
                        modalidad = aux["Modalidad"]

                    #Get tipoPago
                    if aux.get("TipoPago") is None:
                        tipoPago = None
                    else:
                        tipoPago = aux["TipoPago"].encode('utf-8')

                    #Get nombreResponsablePago
                    if aux.get("NombreResponsablePago") is None:
                        nombreResponsablePago = None
                    else:
                        nombreResponsablePago = aux["NombreResponsablePago"].encode('utf-8')

                    #Get emailResponsablePago
                    if aux.get("EmailResponsablePago") is None:
                        emailResponsablePago = None
                    else:
                        emailResponsablePago = aux["EmailResponsablePago"].encode('utf-8')

                    #Get nombreResponsableContrato
                    if aux.get("NombreResponsableContrato") is None:
                        nombreResponsableContrato = None
                    else:
                        nombreResponsableContrato = aux["NombreResponsableContrato"].encode('utf-8')

                    #Get emailResponsableContrato
                    if aux.get("EmailResponsableContrato") is None:
                        emailResponsableContrato = None
                    else:
                        emailResponsableContrato = aux["EmailResponsableContrato"].encode('utf-8')

                    #Get fonoResponsableContrato
                    if aux.get("FonoResponsableContrato") is None:
                        fonoResponsableContrato = None
                    else:
                        fonoResponsableContrato = aux["FonoResponsableContrato"].encode('utf-8')

                    #Get prohibicionContratacion
                    if aux.get("ProhibicionContratacion") is None:
                        prohibicionContratacion = None
                    else:
                        prohibicionContratacion = aux["ProhibicionContratacion"].encode('utf-8')

                    #Get subContratacion
                    if aux.get("SubContratacion") is None:
                        subContratacion = None
                    else:
                        subContratacion = aux["SubContratacion"].encode('utf-8')

                    #Get unidadTiempoDuracionContrato
                    if aux.get("UnidadTiempoDuracionContrato") is None:
                        unidadTiempoDuracionContrato = None
                    else:
                        unidadTiempoDuracionContrato = aux["UnidadTiempoDuracionContrato"]

                    #Get tiempoDuracionContrato
                    if aux.get("TiempoDuracionContrato") is None:
                        tiempoDuracionContrato = None
                    else:
                        tiempoDuracionContrato = aux["TiempoDuracionContrato"].encode('utf-8')

                    #Get tipoDuracionContrato
                    if aux.get("TipoDuracionContrato") is None:
                        tipoDuracionContrato = None
                    else:
                        tipoDuracionContrato = aux["TipoDuracionContrato"].encode('utf-8')

                    #Get justificacionMontoEstimado
                    if aux.get("JustificacionMontoEstimado") is None:
                        justificacionMontoEstimado = None
                    else:
                        justificacionMontoEstimado = aux["JustificacionMontoEstimado"].encode('utf-8')

                    #Get ObservacionContract
                    if aux.get("ObservacionContract") is None:
                        observacionContract = None
                    else:
                        observacionContract = aux["ObservacionContract"].encode('utf-8')

                    #Get extensionPlazo
                    if aux.get("ExtensionPlazo") is None:
                        extensionPlazo = None
                    else:
                        extensionPlazo = aux["ExtensionPlazo"]

                    #Get esBaseTipo
                    if aux.get("EsBaseTipo") is None:
                        esBaseTipo = None
                    else:
                        esBaseTipo = aux["EsBaseTipo"]

                    #Get unidadTiempoContratoLicitacion
                    if aux.get("UnidadTiempoContratoLicitacion") is None:
                        unidadTiempoContratoLicitacion = None
                    else:
                        unidadTiempoContratoLicitacion = aux["UnidadTiempoContratoLicitacion"].encode('utf-8')

                    #Get valorTiempoRenovacion
                    if aux.get("ValorTiempoRenovacion") is None:
                        valorTiempoRenovacion = None
                    else:
                        valorTiempoRenovacion = aux["ValorTiempoRenovacion"].encode('utf-8')

                    #Get periodoTiempoRenovacion
                    if aux.get("PeriodoTiempoRenovacion") is None:
                        periodoTiempoRenovacion = None
                    else:
                        periodoTiempoRenovacion = aux["PeriodoTiempoRenovacion"].encode('utf-8')

                    #Get esRenovable
                    if aux.get("EsRenovable") is None:
                        esRenovable = None
                    else:
                        esRenovable = aux["EsRenovable"]


                    #Get info about dates

                    #Get fechaCreacion
                    if aux.get("Fechas").get("FechaCreacion") is None:
                        fechaCreacion = None
                    else:
                        fechaCreacion = aux["Fechas"]["FechaCreacion"]

                    #Get fechaCierre
                    if aux.get("Fechas").get("FechaCierre") is None:
                        fechaCierre = None
                    else:
                        fechaCierre = aux["Fechas"]["FechaCierre"]

                    #Get fechaInicio
                    if aux.get("Fechas").get("FechaInicio") is None:
                        fechaInicio = None
                    else:
                        fechaInicio = aux["Fechas"]["FechaInicio"]

                    #Get fechaFinal
                    if aux.get("Fechas").get("FechaFinal") is None:
                        fechaFinal = None
                    else:
                        fechaFinal = aux["Fechas"]["FechaFinal"]

                    #Get fechaPubRespuestas
                    if aux.get("Fechas").get("FechaPubRespuestas") is None:
                        fechaPubRespuestas = None
                    else:
                        fechaPubRespuestas = aux["Fechas"]["FechaPubRespuestas"]

                    #Get fechaActoAperturaTecnica
                    if aux.get("Fechas").get("FechaActoAperturaTecnica") is None:
                        fechaActoAperturaTecnica = None
                    else:
                        fechaActoAperturaTecnica = aux["Fechas"]["FechaActoAperturaTecnica"]

                    #Get fechaActoAperturaEconomica
                    if aux.get("Fechas").get("FechaActoAperturaEconomica") is None:
                        fechaActoAperturaEconomica = None
                    else:
                        fechaActoAperturaEconomica = aux["Fechas"]["FechaActoAperturaEconomica"]

                    #Get fechaPublicacion
                    if aux.get("Fechas").get("FechaPublicacion") is None:
                        fechaPublicacion = None
                    else:
                        fechaPublicacion = aux["Fechas"]["FechaPublicacion"]

                    #Get fechaAdjudicacion
                    if aux.get("Fechas").get("FechaAdjudicacion") is None:
                        fechaAdjudicacion = None
                    else:
                        fechaAdjudicacion = aux["Fechas"]["FechaAdjudicacion"]

                    #Get fechaEstimadaAdjudicacion
                    if aux.get("Fechas").get("FechaEstimadaAdjudicacion") is None:
                        fechaEstimadaAdjudicacion = None
                    else:
                        fechaEstimadaAdjudicacion = aux["Fechas"]["FechaEstimadaAdjudicacion"]

                    #Get fechaSoporteFisico
                    if aux.get("Fechas").get("FechaSoporteFisico") is None:
                        fechaSoporteFisico = None
                    else:
                        fechaSoporteFisico = aux["Fechas"]["FechaSoporteFisico"]

                    #Get fechaTiempoEvaluacion
                    if aux.get("Fechas").get("FechaTiempoEvaluacion") is None:
                        fechaTiempoEvaluacion = None
                    else:
                        fechaTiempoEvaluacion = aux["Fechas"]["FechaTiempoEvaluacion"]

                    #Get fechaEstimadaFirma
                    if aux.get("Fechas").get("FechaEstimadaFirma") is None:
                        fechaEstimadaFirma = None
                    else:
                        fechaEstimadaFirma = aux["Fechas"]["FechaEstimadaFirma"]

                    #Get fechaUsuario
                    if aux.get("Fechas").get("FechaUsuario") is None:
                        fechaUsuario = None
                    else:
                        fechaUsuario = aux["Fechas"]["FechaUsuario"]

                    #Get fechaVisitaTerreno
                    if aux.get("Fechas").get("FechaVisitaTerreno") is None:
                        fechaVisitaTerreno = None
                    else:
                        fechaVisitaTerreno = aux["Fechas"]["FechaVisitaTerreno"]

                    #Get fechaEntregaAntecedentes
                    if aux.get("Fechas").get("FechaEntregaAntecedentes") is None:
                        fechaEntregaAntecedentes = None
                    else:
                        fechaEntregaAntecedentes = aux["Fechas"]["FechaEntregaAntecedentes"]

                    # Parse data from adjudicacion global

                    adjudicacionGlobal = {}
                    #Chek if none
                    if aux.get("Adjudicacion") is None:
                        adjudicacionGlobal = None
                    else:
                        #Get tipo
                        if aux.get("Adjudicacion").get("Tipo") is None:
                            tipo = None
                        else:
                            tipo = aux["Adjudicacion"]["Tipo"]

                        #Get fecha
                        if aux.get("Adjudicacion").get("Fecha") is None:
                            fecha = None
                        else:
                            fecha = aux["Adjudicacion"]["Fecha"].encode('utf-8')

                        #Get numero
                        if aux.get("Adjudicacion").get("Numero") is None:
                            numero = None
                        else:
                            numero = aux["Adjudicacion"]["Numero"].encode('utf-8')

                        #Get numeroOferentes
                        if aux.get("Adjudicacion").get("NumeroOferentes") is None:
                            numeroOferentes = None
                        else:
                            numeroOferentes = aux["Adjudicacion"]["NumeroOferentes"]

                        #Get urlActa
                        if aux.get("Adjudicacion").get("UrlActa") is None:
                            urlActa = None
                        else:
                            urlActa = aux["Adjudicacion"]["UrlActa"]

                        adjudicacionGlobal ={
                            "tipo": tipo,
                            "fecha": fecha,
                            "numero": numero,
                            "numero_oferentes": numeroOferentes,
                            "url_acta": urlActa
                        }
                    #Get info about items

                    newTenderElements =  aux["Items"]["Cantidad"]
                    itemsAmmount = len(aux["Items"]["Listado"])
                    listedElements = []

                    for item in aux["Items"]["Listado"]:
                        #Get correlativo
                        if item.get("Correlativo") is None:
                            correlativo = None
                        else:
                            correlativo = item["Correlativo"]

                        #Get codigoProducto
                        if item.get("CodigoProducto") is None:
                            codigoProducto = None
                        else:
                            codigoProducto = item["CodigoProducto"]

                        #Get codigoCategoria
                        if item.get("CodigoCategoria") is None:
                            codigoCategoria = None
                        else:
                            codigoCategoria = item["CodigoCategoria"].encode('utf-8')

                        #Get categoria
                        if item.get("Categoria") is None:
                            categoria = None
                        else:
                            categoria = item["Categoria"].encode('utf-8')

                        #Get nombreProducto
                        if item.get("NombreProducto") is None:
                            nombreProducto = None
                        else:
                            nombreProducto = item["NombreProducto"].encode('utf-8')

                        #Get descripcion
                        if item.get("Descripcion") is None:
                            descripcion = None
                        else:
                            descripcion = item["Descripcion"].encode('utf-8')

                        #Get unidadMedida
                        if item.get("UnidadMedida") is None:
                            unidadMedida = None
                        else:
                            unidadMedida = item["UnidadMedida"].encode('utf-8')

                        #Get cantidad
                        if item.get("Cantidad") is None:
                            cantidad = None
                        else:
                            cantidad = item["Cantidad"]

                        newItem = {
                            "correlativo": correlativo,
                            "codigo_producto": codigoProducto,
                            "codigo_categoria": codigoCategoria,
                            "categoria": categoria,
                            "nombre_producto": nombreProducto,
                            "descripcion": descripcion,
                            "unidad_medida": unidadMedida,
                            "cantidad": cantidad
                        }

                        #Get adjudicationData
                        adjudicacion = {}
                        if item.get("Adjudicacion") is None:
                            adjudicacion = None
                        else:
                            #Get rutProveedor
                            if item.get("Adjudicacion").get("RutProveedor") is None:
                                rutProveedor = None
                            else:
                                rutProveedor = item["Adjudicacion"]["RutProveedor"].encode('utf-8')

                            #Get nombreProveedor
                            if item.get("Adjudicacion").get("NombreProveedor") is None:
                                nombreProveedor = None
                            else:
                                nombreProveedor = item["Adjudicacion"]["NombreProveedor"].encode('utf-8')

                            #Get cantidad
                            if item.get("Adjudicacion").get("Cantidad") is None:
                                cantidad = None
                            else:
                                cantidad = item["Adjudicacion"]["Cantidad"]

                            #Get montoUnitario
                            if item.get("Adjudicacion").get("MontoUnitario") is None:
                                montoUnitario = None
                            else:
                                montoUnitario = item["Adjudicacion"]["MontoUnitario"]

                            #Create the adjudication array with correct data
                            adjudicacion = {
                                "rut_proveedor": rutProveedor,
                                "nombre_proveedor": nombreProveedor,
                                "cantidad": cantidad,
                                "monto_unitario": montoUnitario}

                        #Add adjudication list to the item
                        newItem["adjudicacion"] = adjudicacion

                        #Add item to the array
                        listedElements.append(newItem)

                    postTenderData = {
                                        "code": tenderCode,
                                        "name": tenderName,
                                        "state": tenderStatusCode,
                                        "date": dateParam,
                                        "descripcion": tenderDesc,
                                        "buyer":{
                                                "code": buyersCode,
                                                "nombre": buyersName,
                                                "rut_unidad" : rutUnidad,
                                                "codigo_unidad": codigoUnidad,
                                                "nombre_unidad": nombreUnidad,
                                                "direccion_unidad":direccionUnidad,
                                                "comuna_unidad": comunaUnidad,
                                                "region_unidad": buyersRegion,
                                                "rut_usuario": rutUsuario,
                                                "codigo_usuario": codigoUsuario,
                                                "nombre_usuario":nombreUsuario,
                                                "cargo_usuario": cargoUsuario
                                                },
                                        "dias_cierre_licitacion":diasCierreLicitacion,
                                        "informada": informada,
                                        "codigo_tipo": codigoTipo,
                                        "tipo": tipo,
                                        "tipo_convocatoria":tipoConvocatoria,
                                        "moneda": moneda,
                                        "etapas": etapas,
                                        "estado_etapas": estadoEtapas,
                                        "toma_razon": tomaRazon,
                                        "estado_publicidad_ofertas": estadoPublicidadOfertas,
                                        "justificacion_publicidad": justificacionPublicidad,
                                        "contrato": contrato,
                                        "obras": obras,
                                        "cantidad_reclamos": cantidadReclamos,
                                        "fechas": {
                                            "fecha_creacion": fechaCreacion,
                                            "fecha_cierre": fechaCierre,
                                            "fecha_inicio": fechaInicio,
                                            "fecha_final": fechaFinal,
                                            "fecha_pub_respuestas": fechaPubRespuestas,
                                            "fecha_acto_apertura_tecnica": fechaActoAperturaTecnica,
                                            "fecha_acto_apertura_economica": fechaActoAperturaEconomica,
                                            "fecha_publicacion": fechaPublicacion,
                                            "fecha_adjudicacion": fechaAdjudicacion,
                                            "fecha_estimada_adjudicacion": fechaEstimadaAdjudicacion,
                                            "fecha_soporte_fisico": fechaSoporteFisico,
                                            "fecha_tiempo_evaluacion": fechaTiempoEvaluacion,
                                            "fecha_estimada_firma": fechaEstimadaFirma,
                                            "fechas_usuario": fechaUsuario,
                                            "fecha_visita_terreno": fechaVisitaTerreno,
                                            "fecha_entrega_antecedentes": fechaEntregaAntecedentes
                                        },
                                        "unidad_tiempo_evaluacion": unidadTiempoEvaluacion,
                                        "direccion_visita": direccionVisita,
                                        "direccion_entrega": direccionEntrega,
                                        "estimacion": estimacion,
                                        "fuente_financiamiento": fuenteFinanciamiento,
                                        "visibilidad_monto": visibilidadMonto,
                                        "monto_estimado": montoEstimado,
                                        "tiempo": tiempo,
                                        "unidad_tiempo": unidadTiempo,
                                        "modalidad": modalidad,
                                        "tipo_pago": tipoPago,
                                        "nombre_responsable_pago": nombreResponsablePago,
                                        "email_responsable_pago": emailResponsablePago,
                                        "nombre_responsable_contrato": nombreResponsableContrato,
                                        "email_responsable_contrato": emailResponsableContrato,
                                        "fono_responsable_contrato": fonoResponsableContrato,
                                        "prohibicion_contratacion": prohibicionContratacion,
                                        "sub_contratacion": subContratacion,
                                        "unidad_tiempo_duracion_contrato": unidadTiempoDuracionContrato,
                                        "tiempo_duracion_contrato": tiempoDuracionContrato,
                                        "tipo_duracion_contrato": tipoDuracionContrato,
                                        "justificacion_monto_estimado": justificacionMontoEstimado,
                                        "observacion_contract": observacionContract,
                                        "extension_plazo": extensionPlazo,
                                        "es_base_tipo": esBaseTipo,
                                        "unidad_tiempo_contrato_licitacion": unidadTiempoContratoLicitacion,
                                        "valor_tiempo_renovacion": valorTiempoRenovacion,
                                        "periodo_tiempo_renovacion": periodoTiempoRenovacion,
                                        "es_renovable": esRenovable,
                                        "adjudicacion":adjudicacionGlobal,
                                        "items" : listedElements
                                    }
                    #Post Data to local database
                    # print json.dumps(postTenderData, indent=4, sort_keys=True)
                    kkConst = True
                    while kkConst:
                        try:
                            postData = requests.post('http://localhost:3000/api/v1/tenders',data=json.dumps(postTenderData), headers = {'content-type': 'application/json'})
                            kkConst = False
                        except:
                            pass
                    # postData.raise_for_status()
                    #print  postData.text.encode('utf-8')
                    # print tokenUsage
                    # requests.post('http://localhost:3000/api/v1/tokens/update_token.json',data= json.dumps({"token": activeToken, "amount" : tokenUsage }), headers = {'content-type': 'application/json'})
                    # my_logger.debug("Info - Token " + activeToken + "; uso " + str(tokenUsage))
                    # sys.exit(0)
            # sys.exit(0)
        fesha = fesha + delta
    kConst = True
    while kConst:
        try:
            requests.post('http://localhost:3000/api/v1/tokens/update_token.json',data= json.dumps({"token": activeToken, "amount" : tokenUsage }), headers = {'content-type': 'application/json'})
            my_logger.debug("Info - Token " + activeToken + "; uso " + str(tokenUsage))
            kConst = False
        except:
            pass



def buildLogs():
    LOG_FILENAME = 'logging_hackslabs.out'
    # Set up a specific logger with our desired output level
    global my_logger

    my_logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1000000, backupCount=5)
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    my_logger.addHandler(ch)

if __name__ == "__main__":
    buildLogs()
    readTokens()
    ##yyyymmdd
    tender_scraper(dd.date(2015,8,26))






