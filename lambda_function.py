import json
import logging
from sqlalchemy.orm import Session
from src.utils.db_session import db_session
from src.db.database import get_db
from src.services.login_user import login
from src.services.create_access_token import create_access_token

def lambda_handler(event, context):
    try:
        db: Session = db_session(get_db)
        if not db:
            return {
                'statusCode': 500,
                'body': json.dumps('Failed to create database session')
            }
            
        body = event.get('body')
        if not body:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON in request body')
            }
            
        try:
            body_data = json.loads(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON in request body')
            }
        
        email = body_data.get('email')
        password = body_data.get('password')
        
        if not email or not password:
            return {
                'statusCode': 400,
                'body': json.dumps('Email and password are required')
            }
            
        user_info = login(db, email, password)
        if not user_info:
            return {
                'statusCode': 404,
                'body': json.dumps('User not found')
            }
            
        access_token = create_access_token(user_info)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'user': user_info,
                'access_token': access_token,
                'token_type': 'Bearer'
            })
        }
    except Exception as e:
        logging.error(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }