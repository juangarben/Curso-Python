import json

def save_state(home,filename="state.json"):
    with open(filename,"w") as f:
        json.dump(home.get_status(),f,indent=4)