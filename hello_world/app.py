import json
import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    result ={}
    my_dict={'api.cloudtrim.in':{'api':'P@ssw0rd'},'shop1.cloudtrim.in':{'shop1':'P@ssw0rd'} ,'shop2.cloudtrim.in':{'shop2':'P@ssw0rd'} ,'shop3.cloudtrim.in':{'shop3':'P@ssw0rd'}}
    for key,val in my_dict.items():
        #print(key ,"====>",val)
        for k,v in val.items():
            str=k+":"+v
            #call the apu
            r=requests.get('http://'+key+'/index.php/api/v1/admins', auth=(k, v))
            tempresult=json.loads(r.text)
            tempresult[0]['auth'] = str
            result[key]=tempresult[0]
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "admins":  result
            # "location": ip.text.replace("\n", "")
        }),
    }
