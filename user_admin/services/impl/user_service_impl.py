from ..interfaces.user_service import UserService
from ...models.user import User
import logging

class UserImpl(UserService):

    def get_by_id(id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            logging.error('User does not exist')
            return  {'error': 'User does not exist'} 

        user = {'id': user.id, 'name': user.name, 'email': user.email, 'active': user.active}  

        logging.info('User retrieved: ' + user.get('name'))
        return user


    def get_all():
        users = User.objects.all()
        users = [{'id': user.id, 'name': user.name, 'email': user.email, 'active': user.active} for user in users]
        return users
        

    def create(user):
        new_user = User( 
            name = user.get('name'),
            email = user.get('email'),
            active = user.get('active')
            )
        
        try:
            new_user.save()
        except:
            logging.error('An error occurred while generating the user')
            return {'error': 'An error occurred while generating the user'}     
        
        logging.info('User created generated correctly')
        return {'success': 'The user was generated correctly'}


    def update(user, id):

        try:
            current_user = User.objects.get(pk=id)
        except User.DoesNotExist:
            logging.error('User does not exist')
            return  {'error': 'User does not exist'} 

        current_user.name = user.get('name')
        current_user.email = user.get('email')
        current_user.active = user.get('active')

        try:
            current_user.save()
        except:
            logging.error('An error occurred while updating the user')
            return {'error': 'An error occurred while updating the user'}
        
        logging.info('The user was updated correctly')
        return {'success': 'The user was updated correctly'}      



    def delete(id):

        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            logging.error('User does not exist')
            return  {'error': 'User does not exist'} 
        
        try:
            user.delete()
            logging.info('The user was deleted correctly')
            return {'success': 'The user was deleted correctly'}      
        except User.DoesNotExist:
            logging.error('An error occurred while deleting the user')
            return  {'error': 'An error occurred while deleting the user'}      



    def get_all_active():
        users = list(filter(lambda user: user.active == True, User.objects.all())) 
        users = [{'id': user.id, 'name': user.name, 'email': user.email, 'active': user.active} for user in users]
        return users                            
