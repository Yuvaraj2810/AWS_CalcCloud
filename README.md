# AWS_ CloudCalc 
# Description:
 CloudCalc is an innovative web-based calculator application designed to leverage the power of AWS cloud services. This project integrates AWS Amplify, Lambda, IAM, DynamoDB, and API Gateway to deliver a robust and scalable solution for performing mathematical operations.
 
 ## Key Features:

✔User-Friendly Interface: A sleek and intuitive UI that allows users to perform various mathematical operations including addition, subtraction, multiplication, division, and exponentiation.

✔Serverless Architecture:Utilizes AWS Lambda for executing backend logic, ensuring high availability and scalability without the need for server management.

✔Secure Data Storage:Employs DynamoDB for storing calculation results, ensuring data is securely managed and easily retrievable.

✔API Integration: API Gateway facilitates seamless communication between the frontend and backend, enabling efficient data exchange.

✔Continuous Deployment:AWS Amplify provides a streamlined CI/CD pipeline, ensuring that updates and new features are deployed effortlessly.

## Technologies Used:

✔AWS Amplify: For hosting and continuous deployment of the web application.

✔AWS Lambda: For executing backend logic in a serverless environment.

✔AWS IAM: For managing access and permissions securely.

✔Amazon DynamoDB: For storing and retrieving calculation results.

✔Amazon API Gateway: For creating and managing APIs that connect the frontend with the backend.

## Architecture
The architecture of CloudCalc includes:

1. **Frontend**:
    - **AWS Amplify**: Hosts the static website and provides CI/CD.

2. **Backend**:
    - **AWS Lambda**: Executes backend logic for mathematical operations.
    - **Amazon API Gateway**: Routes API requests to Lambda functions.
    - **Amazon DynamoDB**: Stores calculation results and timestamps.

3. **Security**:
    - **AWS IAM**: Manages access control and permissions.

### Architecture Diagram
```
+-------------------+        +-------------------+        +-------------------+
|                   |        |                   |        |                   |
|    User Browser   | <----> |    API Gateway    | <----> |    Lambda         |
|                   |        |                   |        |    Functions      |
+-------------------+        +-------------------+        +-------------------+
        |                           |                           |
        |                           |                           |
        v                           v                           v
+-------------------+        +-------------------+        +-------------------+
|                   |        |                   |        |                   |
|    AWS Amplify    |        |    AWS IAM        |        |    DynamoDB       |
|                   |        |                   |        |                   |
+-------------------+        +-------------------+        +-------------------+
```

## Acknowledgements
- Thanks to all contributors and the AWS community for their support and resources.

---
