import json
from pprint import pprint
from azure.identity import InteractiveBrowserCredential
from msgraphcore import GraphSession


scopes = ['user.read']
browser_credential = InteractiveBrowserCredential(client_id='64ce2270-e01e-45c3-b5af-232bc8de3298git ')
graph_session = GraphSession(browser_credential, scopes)


def get_sample():
    result = graph_session.get('/me/messages', scopes=['mail.read'])
    pprint(result.json())


if __name__ == '__main__':
    get_sample()