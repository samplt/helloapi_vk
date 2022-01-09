import vk
import requests

app_token = 'f33b9ddff33b9ddff33b9ddff0f3412286ff33bf33b9ddf92ec862762a1723835973c57'
group_token = '088b4ca44feb225a63bdbb0299b4c24c9b07399ac3eebcc2d88b03092e6ce00ce88a93c31ffc749c51eac'
response = requests.get('https://api.vk.com/method/wall.get', params = {
																		'access_token': app_token,
																		'owner_id': '-4816492',
																		#'scope': group_token,
																		'v': 5.81,
																		'domain': 'zelenograd_1' ,
																		#'filter': 'suggests',
																		'count': 100
																		})
data=response.json()
print(data)


#group_session = vk.Session(access_token=group_token)
#apivk = vk.API(group_session)
#wallposts = apivk.wall.get(group_id=-4816492, v=5.81)
#print(wallposts)