from parser import load_matrices
import requests
import json

def getGDP():
    matrix, reversed_matrix, code_to_name = load_matrices()
    f = open("GDP.json","w")
    res ={}
    for code in code_to_name:
        r = requests.get("http://api.worldbank.org/countries/%s/indicators/NY.GDP.PCAP.CD?per_page=10&date=2007:2007&format=json" % code)
        print r.content
        try :
            print code
            content=json.loads(r.content)
            res[code]= content[1][0]["value"]
            print res[code]
        except Exception, e:
            print e
        #print res[code]

    f.write(json.dumps(res))
    f.close()

#getGDP()

def getPop():
    matrix, reversed_matrix, code_to_name = load_matrices()
    f = open("POP.json","w")
    res ={}
    for code in code_to_name:
        r = requests.get("http://api.worldbank.org/countries/%s/indicators/SP.POP.TOTL?per_page=10&date=2007:2007&format=json" % code)
        print r.content
        try :
            print code
            content=json.loads(r.content)
            res[code]= content[1][0]["value"]
            print res[code]
        except Exception, e:
            print e
        #print res[code]

    f.write(json.dumps(res))
    f.close()





def getIndicator(indicator_code, file_name):
    matrix, reversed_matrix, code_to_name = load_matrices()
    f = open(file_name+".json","w")
    res ={}
    for country_code in code_to_name:
        print "http://api.worldbank.org/countries/%s/indicators/%s?per_page=10&date=2007:2007&format=json" % (country_code,indicator_code)
        r = requests.get("http://api.worldbank.org/countries/%s/indicators/%s?per_page=10&date=2007:2007&format=json" % (country_code,indicator_code))
        print r.content
        try :
            print country_code
            content=json.loads(r.content)
            res[country_code]= content[1][0]["value"]
            print res[country_code]
        except Exception, e:
            print e
        #print res[code]

    f.write(json.dumps(res))
    f.close()

#getIndicator("SH.TBS.INCD","TUBERCULOSIS")

#getIndicator("SH.DYN.AIDS.ZS","HIV")
getIndicator("SH.DYN.MORT","UNDER-FIVE-MORTALITY")