AWS Serverless Application – CloudFront, S3, API Gateway, Lambda, DynamoDB
 This project is a fully serverless web application built using AWS services.
 Static content is hosted in S3, delivered via CloudFront, and backend APIs run through API Gateway,
 Lambda, and DynamoDB.
 Architecture Overview
 User → CloudFront → S3 (Frontend) → API Gateway
 ↓ ↓
 Lambda (GET) Lambda (POST)
 \ /
 → DynamoDB
 Services Used- Amazon S3 – Hosts the static website files (HTML, CSS, JS)- Amazon CloudFront – CDN for caching & low-latency delivery- Amazon API Gateway – Handles frontend → backend API requests- AWS Lambda – Executes GET and POST logic- Amazon DynamoDB – NoSQL database for storing data
 Project Structure
 frontend/
 index.html
 script.js
 style.css
 lambda/
 getData.js / getData.py
 putData.js / putData.py
 template/
architecture.png
 README.md
 LICENSE
 Setup Instructions
 1. Upload Frontend to S3- Create an S3 bucket- Enable Static Website Hosting- Upload files- Make public or use OAC with CloudFront
 2. Configure CloudFront- Create distribution- Set S3 as origin
 3. Create API Gateway- Add GET and POST methods- Connect to Lambda
 4. Create Lambda Functions- GET reads from DynamoDB- POST writes to DynamoDB
 5. DynamoDB Setup- Create table- Set primary key- Allow Lambda IAM permissions
 API Endpoints
GET /getData – Fetch data
 POST /putData – Insert data