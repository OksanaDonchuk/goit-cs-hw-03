from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
import argparse


config = dotenv_values('.env')

uri = f"mongodb+srv://{config['USER_MDB']}:{config['PASSWORD_MDB']}@cluster1.d4fmwa1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(uri, server_api=ServerApi('1'))

parser = argparse.ArgumentParser(description='Actions with cats db')
parser.add_argument('--action', choices=['read_all', 'read_by_name', 'update_age', 'update_features', 'delete_by_name', 'delete_all'], help='Available actions: read_all, read_by_name, update_age, update_features, delete_by_name, delete_all')
parser.add_argument('--id', help='ID of the cat')
parser.add_argument('--name', help='Name of the cat')
parser.add_argument('--age', help='New age of the cat')
parser.add_argument('--feature', help='New feature to add to the cat', nargs='+')

args = vars(parser.parse_args())

action = args['action']
cat_id = args['id']
name = args['name']
age = args['age']
features = args['feature']

db = client['my_cats']
data = db['cats']

def read_all():
    cats = data.find()
    for cat in cats:
        print(cat)

def read_by_name():
    name = input('Please enter name: ')
    cat = data.find_one({'name': name})
    if cat:
        print(cat)
    else:
        print(f"Cat {name} not found")
        
def update_by_age():
    name = input('Please enter name: ')
    updated_age = input('Please enter new age: ')
    data.update_one({'name': name}, {'$set': {'age': updated_age}})
    print(f"Now the cat {name} is {updated_age} years old")
    
def update_by_features():
    name = input('Please enter name: ')
    new_feature = input('Please enter feature: ')
    data.update_one({'name': name}, {'$push': {'features': new_feature}})
    print(f"Now the cat {name} has new feature {new_feature}")
    
def delete_by_name():
    name = input('Please enter name: ')
    data.delete_one({'name': name})
    print(f"The cat {name} has been removed")
    
def delete_all():
    data.delete_many({})
    print('All data from the "cats" database has been deleted')
    
def main():
    try:
        match action:
            case 'read_all':
                read_all()
            case 'read_by_name':
                read_by_name()
            case 'update_age':
                update_by_age()
            case 'update_features':
                update_by_features()
            case 'delete_by_name':
                delete_by_name()
            case 'delete_all':
                delete_all()
                
    except Exception as e:
        print(e)     
        
if __name__ == "__main__":
    main()     
        
    




