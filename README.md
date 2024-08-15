# Atlan Backend Challenge

## Description

This repository contains the code for the task of the Atlan Backend Challenge which was building the backend system for the Collect Service with the following use cases - 

- A market research agency wanted to validate responses coming in against a set of 
  business rules (eg. monthly savings cannot be more than monthly income) and send 
  the response back to the data collector to fix it when the rules generate a flag

- A very common need for organizations is wanting all their data onto Google Sheets,
  wherein they could connect their CRM, and also generate graphs and charts offered
  by Sheets out of the box. In such cases, each response to the form becomes a row in
  the sheet, and questions in the form become columns.

## Design Architecture

![Collect Architecture](./Atlan%20Backend%20Challenge%20Design%20Architecture.drawio)


## Local Setup

### Required

- VS Code

- AWS Toolkit (VS Code Extension)

- AWS CLI

- AWS SAM CLI

- Docker

### Steps

1. Configure a virtual environment for the project using [pyenv](https://pypi.org/project/pyenv/) with Python version 3.9.7. The steps can be found [here](https://realpython.com/intro-to-pyenv/).(Optional)

2. Get ```access key ID``` and ```secret access key``` from AWS

3. Configure AWS CLI to include the ```access key ID``` and ```secret access key```

    Command to configure AWS CLI - 
    ```bash 
    aws configure
    ```

>Quickstart to the command can be found [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Steps for deploying the Application

### Prerequisites

- A MySQL RDS with the access rules setup so that the Db Proxy lambda can access it

- S3 Buckets for the following - 
    1. Configuration templates for the Atlan Backend except the Db Proxy Lambda
    2. Configuration templates for the Db Proxy Lambda
    3. Bucket to store the CSVs
    4. Bucket to store the Google Credentials Json files

- ECR Repositories for the following - 
    1. Docker image for Atlan Backend except Db Proxy Lambda
    2. Docker image for Db Proxy Lambda

- Json file with the Google Access Credentials imported into the respective S3 Bucket

### Steps

1. Create the IAM role for the db proxy lambda layer using the [template](./aws_templates/db_proxy_role.yaml) using Cloudformation.

2. Configure the respective values in the config file of [db_proxy_config](./db_proxy_lambda/db_proxy_config.toml)

3. Run the following to deploy the db proxy lambda - 
```bash
sam build && sam deploy --config-file ./db_proxy_config.toml
```

4. Add the Arn for the db proxy lambda to the [template](./aws_templates/permissions_and_roles.yaml)

5. Create the IAM roles for the remaining lambdas using the [template](./aws_templates/permissions_and_roles.yaml) using Cloudformation.

6. Configure the respective values in the config file of [atlan_collect_backend.toml](./atlan_validation_and_data_collection_lambdas/atlan_collect_backend.toml)

7. Run the following to deploy the atlan collect backend - 
```bash
sam build && sam deploy --config-file ./atlan_collect_backend.toml
```

## Request Payloads

### collect

    {
        "response_id": Response ID,
        "response_family_id": Response Family ID,
        "user_id": User ID,
        "username": Username,
        "location": Location,
        "submitted_time": Submitted Time,
        "synced_time": Synced Time,
        "last_modified_time": Last Modified Time,
        "name": Name,
        "email": Email,
        "mobile_number": MOBILE Number,
        "gender": Gender,
        "age": Age,
        "what is the monthly income?": Monthly Income,
        "what is the monthly savings?": Monthly Savings,
        "what is the monthly expenditure?": Monthly Total Expenditure,
        "How much money do you spend monthly on food?": Monthly Food Expenditure,
        "How much money do you spend monthly on your cable service?": Monthly Cable Expenditure,
        "How much money do you spend monthly on healthcare?": Monthly Healthcare Expenditure,
        "How much money do you spend monthly on fuel for your car?": Monthly Fuel Expenditure
    }

### google-sheet

    {
        "table_name": The name of the table whose data is to be imported 
    }

## Flagging Conditions

- Monthly Total Expenditure >= (Food + Cable + Healthcare + Fuel) Expenditure (Rule1)

- Monthly (Income - Expenditure) >= Monthly Savings >= 0 (Rule2)

# Some points to remember

- Avoid any kind of cloud formation configuration drift at all costs

> What is cloud formation drift? Click [here](https://www.google.com/search?q=cloudformation+%2B+drift&oq=cloud&aqs=chrome.1.69i57j69i59l3j69i60l3.3673j0j7&sourceid=chrome&ie=UTF-8) to know more

