import boto3

client = boto3.client('sns')

#create an s3 topic
response = client.create_topic(
    Name='x23196505-project-final',
    Attributes={
        'DisplayName': 'x23196505-project-final',
        
    },
)

if response:
    print("Topc is created")

#create a subscription    
response2 = client.subscribe(
    TopicArn=response['TopicArn'],
    Protocol='email',
    Endpoint='x23196505@student.ncirl.ie',
    ReturnSubscriptionArn=True
)

print("Subscription has been added to the user")