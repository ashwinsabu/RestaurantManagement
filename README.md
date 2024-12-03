
# Restaurant Management Application

## Overview

This project is an academic application developed using the Django framework to streamline restaurant operations by integrating cloud-based services provided by AWS (Amazon Web Services). The platform supports functionalities for restaurant customers, staff, and administrators, with a focus on enhancing the user experience, automating processes, and ensuring scalability and reliability. 

The application implements features like food ordering, order tracking, employee performance evaluation, and customer feedback. It also utilizes AWS services such as S3, SNS, and Elastic Beanstalk to deliver a robust solution.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies and Dependencies](#technologies-and-dependencies)
6. [Deployment](#deployment)
7. [Contributors](#contributors)
8. [License](#license)

## Introduction

The Restaurant Management Application is designed to simplify operations, improve customer satisfaction, and provide tools for staff management. It showcases the integration of cloud computing with modern web development practices, leveraging AWS for CI/CD deployment and enhanced performance.

Key Objectives:
- Automate customer food ordering and tracking.
- Provide staff tools to manage orders and respond to customer queries.
- Implement an employee recognition system based on performance metrics.
- Ensure secure and reliable data handling with AWS cloud services.

## Features

### Customer Features
- **Sign In/Sign Out**: Secure login system for customers.
- **Food Ordering**: Browse the menu and place orders seamlessly.
- **Order Tracking**: Real-time updates on order preparation and delivery.
- **Contact Us**: Raise queries directly through the app, with staff response notifications via email.

### Staff Features
- **Menu Management**: CRUD operations for managing food items.
- **Customer Queries**: Respond to customer queries with automated email notifications.

### Administrator Features
- **Employee Management**: Add and assign roles to employees.
- **Best Employee Program**: Identify top-performing employees based on predefined metrics.

### Cloud Integrations
- **AWS S3**: Store and manage menu images.
- **AWS SNS**: Send email notifications.
- **AWS Elastic Beanstalk**: Deploy and manage the application.
- **AWS CodePipeline and CodeBuild**: Continuous Integration and Deployment for seamless updates.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashwinsabu/RestaurantManagement.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RestaurantManagement
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000) after running the server. 

For cloud-hosted access, visit: [Deployed Application](http://x23196505cppproj.eba-fuaeduwk.eu-west-1.elasticbeanstalk.com/).

## Technologies and Dependencies

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (Default Django Database)
- **Cloud Services**: AWS (S3, SNS, Elastic Beanstalk, CodePipeline, CodeBuild)
- **Python Library**: Published to PyPI for employee performance evaluation

## Deployment

The application is deployed using AWS Elastic Beanstalk, with CI/CD managed by AWS CodePipeline. The code repository is hosted on GitHub: [GitHub Repository](https://github.com/ashwinsabu/RestaurantManagement).

## Contributors

- **Ashwin Sabu**
  - **Email**: [x23196505@student.ncirl.ie](mailto:x23196505@student.ncirl.ie)
  - **Institution**: National College of Ireland

## License

This project is for academic purposes and does not currently include a specific license.
