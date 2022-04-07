"""    USER SCHEMA     """

schema1 = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'mobileno':{'type': 'string'},
        'dob':{'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password','name','mobileno','dob']
}

schema2 = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}

schema3 = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'mobileno':{'type': 'string'},
        'dob':{'type': 'string'},
        'password': {'type': 'string'}
    }}

"""    COMPANY SCHEMA   """

schema4 = {
    'type': 'object',
    'properties': {
         "name":{'type': 'string'},
            "category":{'type': 'string'},
            "website":{'type': 'string'},
            "days":{'type': 'string'},
            "time":{'type': 'string'},
            "address":{'type': 'string'}
    },
    'required': ['category','name','website','days','time','address']
}

schema5= {
    'type': 'object',
    'properties': {
         "name":{'type': 'string'},
            "category":{'type': 'string'},
            "website":{'type': 'string'},
            "days":{'type': 'string'},
            "time":{'type': 'string'},
            "address":{'type': 'string'}
    }
}

"""    PRODUCT  SCHEMA   """
schema6 = {
    'type': 'object',
    'properties': {
    "products":{'type':'array'}
    },
    'required': ['products']
}

schema7 = {
    'type':'object',
    'properties':{
            "name":{'type': 'string'},
            "stock":{'type': 'string'},
            "price":{'type': 'string'},
            "description":{'type': 'string'}
    }
}