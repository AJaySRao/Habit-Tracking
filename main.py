import requests

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "hmgv54asf45sdaf4532fsfdd3"
USERNAME = "jakelong"
GRAPH_ID = "graph3ode"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# new_user = requests.post(url=pixel_endpoint, json=user_param)
# print(new_user.text)
# {"message":"Success. Let's visit https://pixe.la/@jakelong , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_param = {
    "Id": GRAPH_ID,
    "name": "Programming",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=graph_header)
# print(graph_response.text)

edit_graph_ep = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20220326",
    "quantity": "10"
}

response = requests.post(url=edit_graph_ep, json=pixel_data, headers=graph_header)
print(response.text)
