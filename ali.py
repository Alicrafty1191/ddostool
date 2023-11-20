import socket, requests
def get(url):
    if(("https://" in str(url) or "http://" in str(url)) and "www." in str(url)):
        full_url = "https://www.google.com"
        domain = "www.google.com"
    else:
        print(f"""Error Connection => [
            The Url '{url}' is Worng,
            Plase Enter The Url like This 'https://www.example.com'.
]""")
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((domain,80))
    host = socket.gethostbyname(domain)
    sock.sendall(f'GET https://www.google.com HTTP/1.1\r\n'\
    + 'User-Agent: agent123\r\n'\
    + 'Host: '+host+'\r\n'\
    + '\r\n')
    print(sock.recv(4096))
    sock.close()
get("https://www.google.com")
def readline(command):
    cmd = str(command)
    if(cmd=="ip"):
        info = """"""
red = '\u001b[38;5;1m'
green = '\u001b[38;5;2m'
yellow = '\u001b[38;5;3m'
reset = '\u001b[38;5;255m'
print(red+"""                                                                            
        ##      ###                /###           /                 ###     
     /####       ###    #         /  ############/                   ###    
    /  ###        ##   ###       /     #########                      ##    
       /##        ##    #        #     /  #                           ##    
      /  ##       ##              ##  /  ##                           ##    
      /  ##       ##  ###            /  ###          /###     /###    ##    
     /    ##      ##   ###          ##   ##         / ###  / / ###  / ##    
     /    ##      ##    ##     """+green+"""     ##   ##        /   ###/ /   ###/  ##    
    /      ##     ##    ##          ##   ##       ##    ## ##    ##   ##    
    /########     ##    ##          ##   ##       ##    ## ##    ##   ##    
   /        ##    ##    ##           ##  ##       ##    ## ##    ##   ##    
   #        ##    ##    ##            ## #      / ##    ## ##    ##   ##    
  /####      ##   ##    ##         """+yellow+"""    ###     /  ##    ## ##    ##   ##    
 /   ####    ## / ### / ### /           ######/    ######   ######    ### / 
/     ##      #/   ##/   ##/              ###       ####     ####      ##/  
#                                                                           
 ##                                                                         
                                                                            
                                                                            
                                                                            
                                                                            """+reset)

run = True
while run:
    cmd = str(input(f"{yellow}~ {green}${reset}"))
    readline(cmd)