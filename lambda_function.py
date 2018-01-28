import boto3
import json

def lambda_handler(event, context):

    client=boto3.client('ec2',region_name='us-east-1')
    prices=client.describe_spot_price_history(InstanceTypes=['m3.medium'],MaxResults=1,ProductDescriptions=['Linux/UNIX (Amazon VPC)'],AvailabilityZone='us-east-1a')
    print (prices)
    print (prices['SpotPriceHistory'][0]['SpotPrice'])
    spotPrice = str((prices['SpotPriceHistory'][0]['SpotPrice']))
    instanceType = str((prices['SpotPriceHistory'][0]['InstanceType']))
    az = str((prices['SpotPriceHistory'][0]['AvailabilityZone']))
   
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Instance Type: " + instanceType + "</br>" + "Lowest Spot Price: $" + spotPrice + "</br>" 
        + "AZ with lowest price:" + az
           
    }
    
