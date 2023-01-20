# Collage_maker
Photo gallery generator (Python)

## Prerequisites
1. Unsplah API Access Key
- Sign in on https://unsplash.com/developers
- Click on 'Your apps' button and create an application
- Once application will be created API access key will be generated
- Add generated Access Key to .env file in your repository as a envrionment variable
- Add '.env' to .gitignore file to protect sensitive information (key number)
- In order to use env variable install dotenv library
```
  pip install load_dotenv
```
and import load_dotenv into your module

```
  from dotenv import load_dotenv
```
