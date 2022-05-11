#Enterpise Class
#import
import requests
import json

class ent: #Enterprise object
    '''enterprise class'''
    def __init__(self, ID, type):
        '''init variables '''
        super().__init__()

        self.ID = ID
        self.type = type

    def increaseCallCapacity(self, channels, a, bursting=0,):
        currentCapacity = self.getCallCapacity(a) 
        currentmaxcall = currentCapacity['maxActiveCalls']
        currentbursting = currentCapacity['burstingMaxActiveCalls']

        if currentbursting == -1: # if no bursting capacity set to 0 
            currentbursting = 0
        
        endpoint = "/service-providers/trunk-groups/call-capacity"
        headers = {
            "Authorization": "Bearer "+a.token,
            "Content-Type": "application/json"
        }
        data = {
            "maxActiveCalls": currentmaxcall + channels,
            "serviceProviderId": self.ID
        }
        
        if bursting != 0: # if bursting capacity is set (passed into method increaseCallCapacity)
            data["burstingMaxActiveCalls"] = currentbursting + bursting

        # API call
        response = requests.put(a.api_host+endpoint,data=json.dumps(data),headers=headers) # PUT request so it uses payload to identify which group to adjust
        return response.json()

    # returns current call capacity used for above method
    def getCallCapacity(self, a):
        endpoint = "/service-providers/trunk-groups/call-capacity?serviceProviderId="+self.ID
        headers = {
            "Authorization": "Bearer "+a.token
        }
        data = {
        }
        response = requests.get(a.api_host+endpoint,data=data,headers=headers)
        return response.json()

    def __repr__(self) -> str:
        return f"ID: {self.ID}, Type: {self.type}"
    