import boto3

client = boto3.client('sns')

response = client.create_topic(
    Name='x23196505-project-final',
    Attributes={
        'DisplayName': 'x23196505-project-final',
        
    },
)

if response:
    print("Topc is crreated")
    
response2 = client.subscribe(
    TopicArn=response['TopicArn'],
    Protocol='email',
    Endpoint='x23196505@student.ncirl.ie',
    ReturnSubscriptionArn=True
)

print("Subscription has been added to the user")