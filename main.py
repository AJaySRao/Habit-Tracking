import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hmgv54asf45sdaf4532fsfdd3"
USERNAME = "jakelong"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# new_user = requests.post(url=pixela_endpoint, json=user_param)
# print(new_user.text)
# {"message":"Success. Let's visit https://pixe.la/@jakelong , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "Id" : "graph3ode",
    "name": "Programming",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=graph_header)
print(graph_response.text)
