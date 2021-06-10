import pymongo


def insert_data(name,phone,password,latitude,longitude):
    myClient = pymongo.MongoClient()
    db = myClient["rest"]
    col= db["Customer"]
    rec1 = {
        "name":name,
        "phone":phone,
        "pass":password,
        "location_customer":{'type':"Point", "coordinates": [latitude,longitude]},
        "location_rest": {'type': "Point", "coordinates": ['13.0615','80.2615']}
    }
    rec_id = col.insert_one(rec1)
    print("Data inserted with record id ",rec_id)
    cursor = col.find()
    for x in cursor:
        print(x)



def select_data(phone,password):
    myClient = pymongo.MongoClient()
    db = myClient["rest"]
    col = db["Customer"]
    rec1 = {
        "phone": phone,
        "pass": password
    }
    ph=None
    pa=None
    for doc in col.find(rec1):
        print(doc)
        ph=doc["phone"]
        pa=doc["pass"]
    if((phone==ph) and (password==pa)):
        return 1
