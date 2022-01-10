import vk
import requests

app_token = 'f33b9ddff33b9ddff33b9ddff0f3412286ff33bf33b9ddf92ec862762a1723835973c57'
permissions = 'c51e34e7b4604e0ad0352065f3b331bdde467dc207209155b568291fd023ae129e82a3257ace3d7c5cbdc'
group_token = '088b4ca44feb225a63bdbb0299b4c24c9b07399ac3eebcc2d88b03092e6ce00ce88a93c31ffc749c51eac'

response = requests.get('https://api.vk.com/method/wall.get', params = {
																		'access_token': permissions,
																		'owner_id': '-4816492',
																		#'scope': group_token,
																		'v': 5.81,
																		'domain': 'zelenograd_1' ,
																		'filter': 'suggests',
																		'count': 3
																		})
data=response.json()
print(data)
print(response.request.url) #https://api.vk.com/method/wall.get?access_token=c51e34e7b4604e0ad0352065f3b331bdde467dc207209155b568291fd023ae129e82a3257ace3d7c5cbdc&owner_id=-4816492&v=5.81&domain=zelenograd_1&filter=suggests&count=1
print('rrrrrrrrrrrrrrrrrrrrrrrrrr')
print(response.request.body)
print('eeeeeeeeeeeeeeeeeeeeeeeeee')
print(response.request.headers)



#group_session = vk.Session(access_token=group_token)
#apivk = vk.API(group_session)
#wallposts = apivk.wall.get(group_id=-4816492, v=5.81)
#print(wallposts)

#https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,notify,photos,wall,email,mail,groups,stats,offline&response_type=token&v=5.74
#https://vk.com/dev/permissions
#https://vk.com/dev/implicit_flow_user

#https://vk.com/dev/wall.get?params[owner_id]=-86529522&params[count]=1&params[filter]=suggests&params[extended]=0&params[v]=5.131

#https://www.youtube.com/watch?v=UjMZ7lTYvyI 