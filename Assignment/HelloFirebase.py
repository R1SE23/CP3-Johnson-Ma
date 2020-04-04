import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Fetch the service account key JSON file contents
cred = credentials.Certificate('hellofirebase-f8e70-firebase-adminsdk-vdhwr-c3d0045a9a.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hellofirebase-f8e70.firebaseio.com/'})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')
posts_ref = ref.child('Users')

new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together


users_ref = ref.child('user/-M3u1v9piMnwJePS8Wxp')
users_ref.delete()

print(ref.get())