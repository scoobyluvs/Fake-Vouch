import requests
import os
import random
import time

userlist = ['wimp', 'apron', 'lure', 'holystone', 'wealthy', 'alert', 'terrible', 'kindly', 'colt', 'heritage', 'deliver', 'income', 'plunk', 'awed', 'total', 'anybody', 'temporary', 'raven', 'stick', 'enjoin', 'frighten', 'excuse', 'hunt', 'kettle', 'tea', 'converting', 'kneel', 'ericsson', 'bracelet', 'bazaar', 'pitch', 'promotion', 'pplover', 'weekend', 'browtf', 'sugary', 'hazmat', 'honeycomb', 'waffle', 'magistrate', 'strip', 'winning', 'ribbon', 'cete', 's!r?outs', 'upon', 'growth', 'mute', 'cheerful', 'employer', 'normally', 'rinse', 'fe.e', 'cyclist', 'thorns75', 'fez', 'coati', 'hyena', 'trite', 'mercurial', 'wildebeest', 'garment', 'aberrant', 'enormous', 'celebrity', 'grass', 'peaceful', 'threat', 'ship', 'shooting', 'flowerpot', 'emotion', 'below33', 'attract', 'horseradish', 'undershirt']
reasons =  ['160k robux','10k robux','middleman','middleman a trade','500 robux ', 'sold me a cheap account', 'money maker fr', 'W', 'i love you ', '120$ usd middleman','middle man 100%','W mans fr',' ILY', 'im gay for u']
pfp_list = ['https://media.discordapp.net/attachments/1003495706096566292/1008342052800561172/IMG_0632.jpg?width=431&height=439','https://media.discordapp.net/attachments/941719216564895824/982160044961464330/IMG_8081.jpg?width=314&height=558','https://media.discordapp.net/attachments/932643101653205042/981302072135786576/akiyama_mio_k_on_drawn_by_tansuke__e47b156c8369fb9ec343893ca4025e7b.jpg?width=584&height=559','https://media.discordapp.net/attachments/941998018687803392/950431166454976512/33c61a47c39596ce2931b74a0fc15fe7.jpg?width=390&height=390','https://media.discordapp.net/attachments/941998018687803392/950431855423914034/d62e2b8ca1eb16341fb693a1840aeb69.jpg?width=378&height=378','https://media.discordapp.net/attachments/941719215600197722/982964599743713290/9FD84EE9-1E16-402F-B4E1-CDB1A00007B6.gif?width=540&height=540','https://media.discordapp.net/attachments/941997997363961868/954322865044488192/b7d0e353e4d4229e51e6fdc5d2f7a4b8.jpg?width=559&height=559','https://media.discordapp.net/attachments/1040478127715004498/1042116796414705794/48BE37A2-3857-46AC-861C-186F566F9F02.gif?width=266&height=265','https://media.discordapp.net/attachments/845429189972852767/1025207826873864243/79f65773071c321c47d76402e3654b0b.gif?width=270&height=270']

os.system('cls')


class main:    
    
    def vouch(self):
        
        webhook = input('Webhook -> ')
        c = int(input('How many do u want to send -> '))
        
        tdelay = input('Delay? (y or n)')
        
        if tdelay == 'y':
            sdelay = True
        else:sdelay=False
        co = 0
        
        while True:     
           
            random.shuffle(userlist)
            random.shuffle(reasons)
            random.shuffle(pfp_list)
            
            if co >= c:
                break
            
            for user, reason, pfp in zip(userlist,reasons,pfp_list):
                
                delay = random.randint(720,1020)
                
                if sdelay:
                    print(f'Going to sleep for {delay} seconds')
                    time.sleep(delay)
        
                co += 1
                if co >= c:
                    break
                    
                try:
                    requests.post(webhook, json={'content': f'{reason}', 'username': f'{user}','avatar_url':f'{pfp}'})
                    print(f'Sent , {co}/{c}')
                except Exception as e:
                    print(f'Error: {e}')


if __name__ == '__main__':
    main = main()
    main.vouch()