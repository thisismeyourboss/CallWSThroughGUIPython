import requests

endpoint = 'http://localhost:8080/sum'

def callWS(result,x,y,z):
    try:
        session = requests.Session()
        req = session.get(endpoint,params={'x': x,'y': y,'z': z})  
        #if you want more information you can print status code
        #print(req.status_code)
        #print(req.text)
        result.set(req.text)
    except:
        print("Error calling Ws")
      
