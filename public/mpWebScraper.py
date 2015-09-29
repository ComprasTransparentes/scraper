# -*- coding: utf-8-*-
import sys
import httplib2
import re
import requests
from bs4 import BeautifulSoup
import json
import lxml.html

urlToScrape = []
idsToScrape = []
rut = "\A[0-9]{1,2}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0-9Kk]{1}"
rutalter = "[0-9]{8,12}"
orgName = "grdItemOC_ctl[0-9]{2,3}_ucAward_gvLines_ctl[0-9]{2,3}_gvLines_lblOrganization"
supplier = "(\bgrdItemOC_ctl)([0-9]{2,3})(_ucAward_gvLines_ctl)([0-9]{2,3})(_gvLines_lblSupplierComment\b)"
price = "grdItemOC_ctl[0-9]{2,3}_ucAward_gvLines_ctl[0-9]{2,3}_gvLines_lblTotalNetPrice"
quant = "grdItemOC_ctl[0-9]{2,3}_ucAward_gvLines_ctl[0-9]{2,3}_gvLines_txtAwardedQuantity"
netvalue = "grdItemOC_ctl[0-9]{2,3}_ucAward_gvLines_ctl[0-9]{2,3}_gvLines_lblTotalNetAward"
isselected = '>Adjudicada<'
itemname = "grdItemOC_ctl[0-9]{2,3}_ucAward_lblDescription"
quantity = "grdItemOC_ctl[0-9]{2,3}_ucAward__LblRBICuantityNumber"

def getItems(id_tender):
    data = []
    itemid = []
    itemsResponse = requests.get('http://localhost:3000/api/v1/tenders/search_for_participants',data =json.dumps({"id" : id_tender}), headers = {'content-type': 'application/json'})
    for element in json.loads(itemsResponse.text)['items']:
        if element['cantidad'].is_integer():
            number = int(element['cantidad'])
        else:
            number = element['cantidad']
        data.append(element['descripcion'].encode('utf-8').strip()  + str(number).encode('utf-8').strip())
        itemid.append(element['item_id'])
    return (itemid, data)

def getData(url, id_tender):
    h = httplib2.Http(".cache")
    totalItems = []
    resp, content = h.request(url, "GET", headers={'cache-control':'no-cache'})

    soup = BeautifulSoup(content, from_encoding="utf-8")
    soup2 = BeautifulSoup(content, "html5lib",  from_encoding="utf-8")

    #print url
    #url = "http://www.mercadopublico.cl/Procurement/Modules/RFB/StepsProcessAward/PreviewAwardAct.aspx?qs=/0Gb2TNQJQ89Yc+ruBBtOlBzqtsu94AJRg2rRptsnF0="
    #print id_tender
    getItems(id_tender)
    items = getItems(id_tender)
    itemsCode = items[0]
    itemsData = items[1]

    #remove linebreaks from elements
    itemsData2 = []
    for data in itemsData:
        itemsData2.append(data.replace("\r\n",""))

    for element in soup2.findAll(id="rptBids_"):
        parts = []
        tagData = element.encode('utf-8').strip()
        #print tagData
        largoData = len(re.findall(itemname, tagData)[0])
        posVar1 = re.search(itemname, tagData).start()

        descr =  tagData[posVar1 + largoData +2: tagData.find("<", posVar1 +largoData -1)].strip()
        #print descr

        #Quant from item description
        largoData = len(re.findall(quantity, tagData)[0])
        posVar1 = re.search(quantity, tagData).start()
        quant =  tagData[posVar1 + largoData +2: tagData.find("<", posVar1 +largoData -1)].strip()

        #Look the item into the array.
        keyItem = descr+quant.replace(",",".")

        #Replace all weird chars
        keyItem = keyItem.replace("&amp;", "&")
        keyItem = keyItem.replace("&gt;", ">")
        keyItem = keyItem.replace("&lt;", "<")
        keyItem = keyItem.replace("\n","")

        parts= parts + iteratorParser(element, "cssPRCGridViewRow")
        parts= parts + iteratorParser(element, "cssPRCGridViewAltRow")

        item_id = ""
        print "busco:" + keyItem

        iterBool = True
        kk = 0
        while iterBool:
            lectura = itemsData2[kk]
            #print "lectura:"  + lectura
            if keyItem == lectura:
                #print "exito"
                item_id = itemsCode[kk]
                itemsData2.remove(lectura)
                itemsCode.remove(item_id)
                #print "ok"
                break
            #Condicion de salida

            if kk >= len(itemsData2):
                iterBool = False
            else:
                kk = kk +1


        if item_id == "":
            print "No encuentro :" + keyItem
        #    print "Busco en: "
            print items
            sys.exit(0)

        #print iteratorParser(element, "cssPRCGridViewRow")

        itemData =  {
                    "item_id" : int(item_id),
                    "parts" : parts
                    }
        #print itemData
        totalItems.append(itemData)
    finalJson = json.dumps({"tender_id" : id_tender , "items" : totalItems})
    #print finalJson
    #print "todo ok"
    #sys.exit(0)
    if len(json.loads(finalJson)["items"]) < 1:
        print "Raro"
        sys.exit(0)
    itemsResponse = requests.post('http://localhost:3000/api/v1/tenders/create_participants',data =finalJson, headers = {'content-type': 'application/json'})

def iteratorParser(element, className):
    parts = []
    for data in element.parent.parent.findAll(class_=className):
        ladata = data.encode('utf-8').strip()
        #Data from Buyer
        largoData = len(re.findall(orgName, ladata)[0])
        posVar1 = re.search(orgName, ladata).start()
        idBruto =  ladata[posVar1 + largoData +2: ladata.find("<", posVar1 +largoData -1)].strip()
        #print idBruto
        try:
            part_rut = re.findall(rut, idBruto)[0]
            part_name = idBruto[len(part_rut)+1:]
        except:
            try:
                part_rut = re.findall(rutalter, idBruto)[0]
                part_name = idBruto[len(part_rut)+1:]
            except:
                part_rut = ""
                part_name = idBruto
        #print idBruto
        #Data from price
        largoData = len(re.findall(price, ladata)[0])
        posVar1 = re.search(price, ladata).start()
        part_precio =  ladata[posVar1 + largoData +2: ladata.find("<", posVar1 +largoData -1)].strip()
        #print precioBruto
        #Data from cant
        largoData = len(re.findall(quant, ladata)[0])
        posVar1 = re.search(quant, ladata).start()
        cantAdjudicada =  ladata[posVar1 + largoData +2: ladata.find("<", posVar1 +largoData -1)].strip()
        #print cantAdjudicada
        #Data from netValue
        largoData = len(re.findall(netvalue, ladata)[0])
        posVar1 = re.search(netvalue, ladata).start()
        netVal=  ladata[posVar1 + largoData +2: ladata.find("<", posVar1 +largoData -1)].strip()
        #print netVal
        #Data from winner
        if len(re.findall(isselected, ladata)) == 0:
            is_winner = 0
        else:
            is_winner = 1
        compJson = {
                    "part_rut": part_rut,
                    "part_name": part_name,
                    "part_precio": part_precio,
                    "part_cant": cantAdjudicada,
                    "part_valor": netVal,
                    "is_winner": is_winner
                        }
        parts.append(compJson)
    return parts



if __name__ == "__main__":
    #Get codes
    validIter = True
    iterSize = 100
    greatLoop = 0
    while validIter:
        urlToScrape = []
        idsToScrape = []
        getCodesFromAPI = requests.get('http://localhost:3000/api/v1/tenders/all',  data = json.dumps({"page": 1, "per_page" : iterSize}), headers = {'content-type': 'application/json'})
        data = json.loads(getCodesFromAPI.text)
        #print len(data['tenders'])
        for element in data['tenders']:
            urlToScrape.append(element['url_acta'])
            idsToScrape.append(element['tender_id'])

        if len(urlToScrape) == len(idsToScrape):
            i = 0
            while i < len(urlToScrape):
                print urlToScrape[i]
                print idsToScrape[i]
                getData(urlToScrape[i],idsToScrape[i])

                i=i+1
        else:
            print "error en largo de arreglos"
            print urlToScrape
            print idsToScrape
            sys.exit(0)
        greatLoop = greatLoop + 1
        if len(urlToScrape) < iterSize or greatLoop == 6:
            validIter = False
        else:
            print "vuelta"



