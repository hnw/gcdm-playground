def hello_pubsub(data, context):
    """
    :type data: dict
    :type context: google.cloud.functions.Context
    """
    import base64
    data.g
    if 'data' in data:
        name = base64.b64decode(data['data']).decode('utf-8')
    else:
        name = 'World'
    context
    print('Hello {}!'.format(name))
