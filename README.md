
# Restaurant Management Application

Application has been created as a part of Cloud Platfrom Programming Module and is deployed to AWS Elastic Beastalk



## Authors

- [Ashwin Sabu (x23196505)](https://github.com/ashwinsabu2000)


## Dependencies Required
Inorder to run the application the following dependencies need to installed: 
- asgiref==3.7.2
- beautifulsoup4==4.12.3
- best-employee-finder-ashwinsabu20000==0.0.1
- boto3==1.34.83
- botocore==1.34.83
- coverage==7.4.4
- Django==4.1
- django-bootstrap-v5==1.0.11
- django-storages==1.14.2
- jmespath==1.0.1
- pillow==10.3.0
- python-dateutil==2.9.0.post0
- s3transfer==0.10.1
- six==1.16.0
- soupsieve==2.5
- sqlparse==0.4.4
- typing_extensions==4.10.0
- tzdata==2024.1
- urllib3==1.26.18

All the list of packages installed are in requirement.txt, it can be installed using pip install requirement.txt
## Deployment steps for Elastic Beanstalk
- Create a configuration file as in .ebextensions/django.config.
- Create an application in elastic beanstalk using eb init command.
- Create an environment inside the application.
- Add the environement domain in settings.py file located in cpp_proj/settings.pu
- Update the changes in the staging directry and perform eb deploy to deploy the changes