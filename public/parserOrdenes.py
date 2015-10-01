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


def order_scraper(startingDate):
    fesha = startingDate
    delta = dd.timedelta(days=1)
    endDate = dd.date.today()
    while fesha <= endDate:
        if fesha.day<10:
            theDay = "0"+str(fesha.day)
        else:
            theDay = str(fesha.day)
        if fesha.month<10:
            theMonth = "0"+str(fesha.month)
        else:
            theMonth = str(fesha.month)
        theYear="2014"
        dateParam = theDay+theMonth+theYear
        headers = {'content-type': 'application/json'}
        dailyOrdersRequest = requests.get('http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?fecha='+dateParam+'&ticket=0942223B-FAE2-4060-950E-36D16916F7E2', headers = headers)
        #Error exception
        dailyOrdersRequest.raise_for_status()

        dailyOrders = json.loads(dailyOrdersRequest.text.encode('utf-8'))

        for data in dailyOrders["Listado"]:
            orderName = data["Nombre"].encode('utf-8')
            orderCode = data["Codigo"].encode('utf-8')
            orderStatusCode = data["CodigoEstado"]
            #CHECK IF THE ORDER CODE EXISTS
            headers = {'content-type': 'application/json'}

            getOrderDataFromMongoRequest = requests.get('http://localhost:3000/api/v1/orders/search?code='+orderCode+'&type=1', headers = headers)

            getOrderDataFromMongo= json.loads(getOrderDataFromMongoRequest.text.encode('utf-8'))
            if getOrderDataFromMongo["isCreated"] == "true":
                if getOrderDataFromMongo["state"]==orderStatusCode:
                    #doNothing
                    pass
                    print "doNothing"
                else:
                    #if orderStatusCode is different create a new entry
                    #{"state": 8, "date": "27022014", "type": 1, "code": "213-L12-20"}
                    postPutData =   {
                                        "state": orderStatusCode,
                                        "date": dateParam,
                                        "type": "1",
                                        "code": orderCode,
                                    }
                    updateData = requests.post('http://localhost:3000/api/v1/orders/state',data=json.dumps(postPutData), headers = headers)
                    #print  updateData.text.encode('utf-8')
                    #print "doSomethingDifferent"
                    pass
            else:
                areasArray = []
                headers = {'content-type': 'application/json'}
                newOrderRequest = requests.get('http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo='+orderCode+'&ticket=0942223B-FAE2-4060-950E-36D16916F7E2', headers = headers)
                newOrderRequest.raise_for_status()
                newOrder = json.loads(newOrderRequest.text.encode('utf-8'))
                aux = newOrder["Listado"][0]
                #Get Data from Order
                orderCreationDate = aux["Fechas"]["FechaCreacion"].encode('utf-8')
                orderCurrency = aux["TipoMoneda"].encode('utf-8')
                orderTotalAmount = aux["Total"]
                orderTenderCorde = aux["CodigoLicitacion"]
                orderSupplierCode = aux["Proveedor"]["Codigo"].encode('utf-8')
                orderSupplierName = aux["Proveedor"]["Nombre"].encode('utf-8')
                orderBuyerCode = aux["Comprador"]["CodigoOrganismo"].encode('utf-8')
                orderBuyerName = aux["Comprador"]["NombreOrganismo"].encode('utf-8')
                areasAux  = []
                valueAux = []
                nameAux = []
                areasFinal = []
                itemsData = []
                itemsNums = len(aux["Items"]["Listado"])
                for itemm in aux["Items"]["Listado"]:
                    areasAux.append({itemm["Categoria"].encode('utf-8'):itemm["Total"]})
                    itemsData.append({"cantidad": itemm["Cantidad"],
                        "producto": itemm["Producto"].encode('utf-8'),
                        "monto": itemm["Total"]})

                counter = collections.Counter()
                for d in areasAux:
                    counter.update(d)
                for keys in counter.keys():
                    nameAux.append(keys)
                for values in counter.values():
                    valueAux.append(values)
                for nam,val in zip(nameAux, valueAux):
                    areasFinal.append({"name":nam, "amount" : val})
                postOrderData = {
                                    "code": orderCode,
                                    "name": orderName,
                                    "tender_code": orderTenderCorde,
                                    "areas": areasFinal,
                                    "supplier":{
                                                    "code": orderSupplierCode,
                                                    "name": orderSupplierName
                                                },
                                    "buyer":
                                                {
                                                    "code": orderBuyerCode,
                                                    "name": orderBuyerName
                                                },
                                    "total": orderTotalAmount,
                                    "currency": orderCurrency,
                                    "created_at": orderCreationDate,
                                    "state": orderStatusCode,
                                    "states": [
                                                {
                                                    "state": orderStatusCode,
                                                    "date": dateParam
                                                }
                                               ],
                                    "items_num": itemsNums,
                                    "items_desc": itemsData
                                }


                #Post Data to local database
                headers = {'content-type': 'application/json'}
                postData = requests.post('http://localhost:3000/api/v1/orders',data=json.dumps(postOrderData), headers = headers)
        fesha = fesha + delta

if __name__ == "__main__":
    order_scraper(dd.date(2014,12,06))
