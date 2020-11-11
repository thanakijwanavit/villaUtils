import json
from awsSchema.apigateway import Response, Event
from datetime import datetime


def dtconvert(event, context):
    body = Event.parseBody(event)
    if not all(key in body for key in ['date', 'formatter']):
        return Response.returnError(message='missing date or formatter keys')

    timeStamp = datetime.strptime(body['date'], body['formatter']).timestamp()
    return Response.returnSuccess(body = str(timeStamp))
