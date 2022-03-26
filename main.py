import requests

pixel_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": "hmgv54asf45sdaf4532fsfdd3",
    "username": "jakelong",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# new_user = requests.post(url=pixel_endpoint, json=user_param)
# print(new_user.text)
# {"message":"Success. Let's visit https://pixe.la/@jakelong , it is your profile page!","isSuccess":true}
