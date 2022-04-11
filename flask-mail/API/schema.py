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
        'email': {'type': 'string'},
    }
    ,'required': ['email']
    }

schema4 = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'otp': {'type': 'number'}
    }
    ,'required': ['email','otp']
    }

schema5 = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'otp': {'type': 'number'},
        'newpassword':{'type':"string"}
    }
    ,'required': ['email','otp','newpassword']
    }