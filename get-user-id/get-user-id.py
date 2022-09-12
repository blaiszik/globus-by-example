"""
Example showing how to get details about the logged in user including the UUID
"""
from globus_sdk import AuthClient
from fair_research_login import NativeClient

# Inputs
client_id = '7414f0b4-7d05-4bb6-bb00-076fa3f17cf5'
requested_scopes = ['openid', 'profile']

# Register a Native App for a client_id at https://developers.globus.org
client = NativeClient(client_id=client_id)

# Automatically saves tokens in ~/.globus-native-apps.cfg
tokens = client.login(
    # Request any scopes you want to use here.
    requested_scopes = requested_scopes    
)

# TODO: Add some description here of resource server vs scopes
# Authorizers automatically choose a refresh token authorizer if possible,
# and will automatically save new refreshed tokens when they expire.
# ac_authorizer = client.get_authorizers()['auth.globus.org']

# Also supported
ac_authorizer = client.get_authorizers_by_scope()['openid']

# Example client usage:
auth_cli = AuthClient(authorizer=ac_authorizer)
user_info = auth_cli.oauth2_userinfo()
print(f'Hello {user_info["name"]}! How are you today?')

print(f'The primary UUID for this user is {user_info["sub"]}')
print('======== Other oAuth2 Information ========')
print(auth_cli.oauth2_userinfo())