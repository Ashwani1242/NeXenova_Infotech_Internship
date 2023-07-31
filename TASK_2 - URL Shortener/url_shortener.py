import requests

def shorten_link(full_link, link_name):
    
    api_key = "91d55f867a130ce4c1d4c936a2302162298bc"
    base_url = "https://cutt.ly/api/api.php"
    
    payload = {'key': api_key, 'short': full_link, 'name': link_name}
    request = requests.get(base_url, params=payload)
    data = request.json()
    
    print('')
    
    try:
        
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print("Title:", title)
        print("Link:", short_link)
        
    except:
        
        status = data['url']['status']
        print("Error Status:", status)


link = input("Enter a Link: ")
name = input("Name of your Link: ")

shorten_link(link, name)