# Use CouchDB to create a CouchDB client
# from cloudant.client import CouchDB
# client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984')


from cloudant.result import Result, ResultByKey
from cloudant.document import Document
import json


# Use Cloudant to create a Cloudant client using account
from cloudant.client import Cloudant
#client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME)
# or using url
USERNAME="a31ca7df-0342-4707-8e48-c048c0551391-bluemix"
PASSWORD="35404a79b9515597a3f9caf449eab51f4ffbce672737811411abed3166805011"
urlAddress='https://a31ca7df-0342-4707-8e48-c048c0551391-bluemix:35404a79b9515597a3f9caf449eab51f4ffbce672737811411abed3166805011@a31ca7df-0342-4707-8e48-c048c0551391-bluemix.cloudant.com'
client = Cloudant(USERNAME, PASSWORD, url=urlAddress)

# Connect to the server
client.connect()

# Perform client tasks...
session = client.session()
print 'Username: {0}'.format(session['userCtx']['name'])
print 'Databases: {0}'.format(client.all_dbs())




# Create a database using an initialized client
# The result is a new CloudantDatabase or CouchDatabase based on the client
#my_database = client.create_database('my_database')

# You can check that the database exists
#if my_database.exists():
#    print 'SUCCESS!!'


# Open an existing database
my_database = client['iotp_2ohgjp_default_2016-10-24']
result_collection = Result(my_database.all_docs, include_docs=True)

my_doc=my_database['0000c920-99e9-11e6-ba87-379de776ae12']
#print my_doc

result = result_collection[0]                   # result is the 1st in the collection
result = result_collection[9]
result = result_collection[100: 200]  

# Get all of the documents from my_database
#print result

# Retrieve documents where the name field is 'foo'
selector = {'deviceId': {'$eq': 'AndroidDevice001'}}
docs = my_database.get_query_result(selector)[:100]
for doc in docs:
    print doc


# Disconnect from the server
client.disconnect()
