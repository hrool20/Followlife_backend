swagger_login_dict = {
    'tags': [
        'resources'
    ],
    'summary': 'User Login',
    'description': 'Endpoint to log in the database.',
    'operationId': 'loginPost',
    'consumes': [
        'application/json'
    ],
    'produces': [
        'application/json'
    ],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'description': 'Login object necessary to log in. You can use either "email" or "phoneNumber"',
            'required': False,
            'schema': {
                '$ref': '#definitions/login'
            }
        }
    ],
    'definitions': {
        'login': {
            'type': 'object',
            'required': [
                'password',
                'lastIPConnection'
            ],
            'properties': {
                'email': {
                    'type': 'string',
                    'example': 'example@example.com'
                },
                'phoneNumber': {
                    'type': 'string',
                    'description': 'Required if email is not given.',
                    'example': '123456789'
                },
                'password': {
                    'type': 'string'
                },
                'lastIPConnection': {
                    'type': 'string',
                    'example': '10.96.00.123'
                }
            }
        }
    },
    'responses': {
        '200': {
            'description': 'Login successfully.',
            'schema': {
                '$ref': '#/definitions/login'
            },
            'examples': {
                'result': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwYjI5ODk1Yy02MzdkLTQ3YTktYmJjNC05N'
                                   'zA2NTA4ZTE3YjYiLCJleHAiOjE1MzI2NjQ3NTcsImZyZXNoIjp0cnVlLCJ...',
                    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhZWI0MzI5NC1hODBmLTQzYTEtODViMS1i'
                                    'NWFkMjFiZTg5MmUiLCJleHAiOjE1MzUxNzAzNTcsImlhdCI6MTUzMjU3O...',
                    'user': {
                        'fullName': 'Hugo Andres',
                        'id': 1,
                        'lastName': 'Rosado Oliden'
                    }
                }
            }
        }
    }
}
