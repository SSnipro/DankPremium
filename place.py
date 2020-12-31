import random

# place :{
#     places :{
#         air: {
#             boss: [ghost]
#             bosspercentage: 10
#             coins: [200,400]
#         }
#         bank: {
#             boss:
#             bosspercentage: 
#             coins:
#         }
#         attic: {
#             bosspercent
#             boss:
#             coins:
#         }
#     }

# Search = [
#         "You searched the air and found some new unknown elements. You gained $300. \n\n你在空气里找到了一些新元素。你得到了 $300。",
#         "YOU ROBBED THE BANK AND GAINED $120. NOW RUN \n\n你抢劫了银行并得到了 $120。快跑!!!!!", 
#         "You tried to rob the bank and got shot. Might need to learn how to play dodgeball next time. \n\n你尝试去抢劫银行却被警察击中。下次练完躲避球再来吧。", 
#         "You begged on the street and got mistaken for a hobo. Did you forget that they don't give $ to beggers anymore? \n\n你在路上讨钱。你忘了他们不再给讨钱的人 $ 了么？", 
#         "You searched the school and got mistaken for a kidnapper. You got jailed. \n\n你搜索了学校但被误以为一个拐卖小孩的骗子。你入狱了。", 
#         "You searched the hospital, not konwing that it's a great mistake. You got COVID-19 and died. \n\n你搜索了医院，但被流感传染。你挂了。", 
#         "You searched the hospital and found a doctor's bag. You found a wallet with $20 inside. \n\n你搜索了医院并找到了一名医生的包。你获得了 $20。", 
#         "You found $40 in the attic. How long had it been here? \n\n你在阁楼找到了 $40。在这里待了多久了？", 
#         "You searched the haunted house and found a vault. You opened it and found $1000! Luckily there was no ghosts inside \n\n你搜索了鬼屋并找到了一个金库。你打开了它并找到了 $1000！幸好里面没有鬼。", 
#         "You searched a tree and found buried treasure worth $270. GG! \n\n你搜索了一棵树并找到了一批宝藏。你得到了 $270。 酷！", 
#         "You searched L - Park, not knowing it's a park for losers. Anyway, at least you got $9 from a bet with another kid. \n\n你搜索了 L - 公园，最终收获了 $9。", 
#         "You searched the haunted house and got murdered by a ghost. RIP. \n\n你尝试去搜索鬼屋。 你被 幽灵 给击败了。"
#         ]
        
place = {
    'Air':{
        'boss': ['Dementor','Ho-oh','Eagle','Plane'],
        'bosspercentage': 30,
        'coins': [[300,1500]]
    },
    'Bank':{
        'boss': ['FBI','SWAT','Local Police','Gengar'],
        'bosspercentage': 85,
        'coins': [[1200,20000]]
    },
    'Street':{
        'boss': ['bad guy','Local Police'],
        'bosspercentage': 15,
        'coins': [[0,0],[23,47]]
    },
    'School':{
        'boss': ['Security Guard','Local Police','Students','Guardian'],
        'bosspercentage': 50,
        'coins': [[0,250]]
    },
    'Hospital':{
        'boss': ['Local Police','COVID-19','Death','Psychopath'],
        'bosspercentage': 50,
        'coins': [[20,200]]
    },
    'Attic':{
        'boss': ['ur mom','Angry Boomers'],
        'bosspercentage': 5,
        'coins': [[40,200]]
    },
    'Haunted House':{
        'boss': ['Ghost','Guardian'],
        'bosspercentage': 50,
        'coins': [[0,0],[2000,10000]]
    },
    'Gold Mine':{
        'boss': [],
        'bosspercentage': 0,
        'coins': [[10000,50000]]
    },
    'Tree':{
        'boss': ['Pirate','Fake Branch','Guardian'],
        'bosspercentage': 40,
        'coins': [[0,50],[2000,10000]]
    },
    'L-Park':{
        'boss': ['Angry Boomers','Bully'],
        'bosspercentage': 30,
        'coins': [[1,7],[10,70]]
    },
    'Mystery Place':{
        'boss': ['Mystery Trainer','Mystery Head Evice','Mystery Master','Mystery Conqueror Xerneas'],
        'bosspercentage': 100,
        'coins': [[0,75000]]
    },
    'Ancient Battlegrounds':{
        'boss': ['Illegal Time Travellers'],
        'bosspercentage': 10,
        'coins': [[0,10000]]
    },
    'Warzone':{
        'boss': ['Army #1','Army #2'],
        'bosspercentage': 90,
        'coins': [[0,1000]]
    },
    'Graveyard':{
        'boss': ['Mutants','Zombies','Undead','Skeletons','R34P3R'],
        'bosspercentage': 55,
        'coins': [[0,100],[1000,10000]]
    },
    'DMII Factory':{
        'boss': ['DMII','Workers','Security Guards','Factory Owner & Bodyguards'],
        'bosspercentage': 85,
        'coins': [[5000,25000]]
    },
    'Ancient Ocean Ruins':{
        'boss': ['Oxygen Absorber','Wailord','Elder Guardian'],
        'bosspercentage': 65,
        'coins': [[100,15000]]
    }

    # search = ['Air','Bank','Street','School','Hospital','Attic','Haunted House','Gold Mine','Tree','L-Park','Mystery Place','Battlegrounds','Warzone','Graveyard','DMII Factory']
}

boss = {
    'Dementor':{
        'hp': 25,
        'atk': 50,
        'defence': 75,
        'speed': 50,
        'img': 'https://static.wikia.nocookie.net/harrypotter/images/4/49/DementorConceptArt.jpg/revision/latest/scale-to-width-down/700?cb=20150928152038'
    },
    'Ho-oh':{
        'hp': 53,
        'atk': 65,
        'defence': 45,
        'speed': 45,
        'img': 'https://3dwarehouse.sketchup.com/warehouse/v1.0/publiccontent/6e3aa080-be4c-488a-9db7-a34cc49f6000'
    },
    'Eagle':{
        'hp': 41,
        'atk': 53,
        'defence': 33,
        'speed': 69,
        'img': 'https://images.immediate.co.uk/production/volatile/sites/23/2019/12/GettyImages-138596308-ad71719.jpg?quality=90&resize=620%2C413'
    },
    'Plane':{
        'hp': 100,
        'atk': 10,
        'defence': 150,
        'speed': 75,
        'img': 'https://s3-prod.chicagobusiness.com/A321XLR_CFM_UAL_V07.jpg'
    },
    ####
    'FBI':{
        'hp': 75,
        'atk': 125,
        'defence': 50,
        'speed': 80,
        'img': 'https://tvline.com/wp-content/uploads/2020/08/fbi-most-wanted.jpg?w=620'
    },
    'SWAT':{
        'hp': 75,
        'atk': 175,
        'defence': 150,
        'speed': 40,
        'img': 'https://images.idgesg.net/images/article/2020/09/swatting_swat-team_raid_police_by-onfokus-getty-images-100856787-large.jpg'
    },
    'Local Police':{
        'hp': 60,
        'atk': 75,
        'defence': 25,
        'speed': 45,
        'img': 'https://www.nationalobserver.com/sites/nationalobserver.com/files/img/2020/07/16/toronto_police_cropped2_shutterstock.jpg'
    },
    'Gengar':{
        'hp': 20,
        'atk': 1000,
        'defence': 0,
        'speed': 40,
        'img': 'https://cdn.bulbagarden.net/upload/thumb/8/8a/Morty_Gengar.png/220px-Morty_Gengar.png'
    },
    ####
    'bad guy':{
        'hp': 75,
        'atk': 35,
        'defence': 15,
        'speed': 45,
        'img': 'https://i.ytimg.com/vi/PHBF7D1_Jr8/hqdefault.jpg'
    },
    ####
    'Security Guard':{
        'hp': 95,
        'atk': 75,
        'defence': 35,
        'speed': 45,
        'img': 'https://i.pinimg.com/originals/c5/c6/9b/c5c69b2b33ed7b1c1a044a9f39d5571f.jpg'
    },
    'Students':{
        'hp': 30,
        'atk': 35,
        'defence': 15,
        'speed': 25,
        'img': 'https://c.files.bbci.co.uk/36EB/production/_85695041_029224011-1.jpg'
    },
    'Guardian':{
        'hp': 75,
        'atk': 75,
        'defence': 75,
        'speed': 75,
        'img': 'https://i.ytimg.com/vi/ANQK1Bqsq88/maxresdefault.jpg'
    },
    ####
    'COVID-19':{
        'hp': 5,
        'atk': 100,
        'defence': 200,
        'speed': 150,
        'img': 'https://www.statnews.com/wp-content/uploads/2020/02/Coronavirus-CDC-645x645.jpg'
    },
    'Death:':{
        'hp': 100,
        'atk': 1000,
        'defence': 1000,
        'speed': 100,
        'img': 'https://1a3kls1q8u5etu6z53sktyqdif-wpengine.netdna-ssl.com/wp-content/uploads/2018/08/Death.jpg'
    }
}
class Place:
    name = ""
    boss = []
    coins = 0
    
    def __init__(self,name):
        self.name = name
        bosspercentage = place[name]['bosspercentage']
        boss = place[name]['boss']
        percent = random.randint(1,100)
        if percent >= bosspercentage:
            self.boss = Boss(random.choice(boss))
        rcoins = random.choice(place[name]['coins'])
        self.coins = random.randint(rcoins[0],rcoins[1])
        
    def __str__(self):
        return f"{self.name}:  boss: {self.boss}  coins: {self.coins}"

def random_destination():
    p1 = place.copy()
    d1g = Place( random.choice(list(p1.keys())) )
    del p1[d1g.name]
    d2g = Place( random.choice(list(p1.keys())) )
    del p1[d2g.name]
    d3g = Place( random.choice(list(p1.keys())) )
    del p1[d3g.name]
    return [d1g,d2g,d3g]

    

# d1g,d2g = random_destination()
# print(d1g.boss)
# print(d1g.coins)

#     boss :{
#         ghost :{
#             hp:
#             atk:
#             defence:
#             spd:
#         }
#         police :{
#             hp:
#             atk:
#             defence:
#             spd:
#         }
#         guardian :{
#             hp:
#             atk:
#             defence:
#             spd:
#         }
#     }
# }

class Boss:
    name = ''
    hp = 0
    atk = 0
    defence = 0
    speed = 0

    def __init__(self,name):
        self.name = name
        self.hp = boss[name]['hp']
        self.atk = boss[name]['atk']
        self.defence = boss[name]['defence']
        self.speed = boss[name]['speed']
        self.image = boss[name]['img']

    def __str__(self):
        return  f"{self.name}"



if __name__ == '__main__':
    print('test random_destination')
    dest = random_destination()
    for d in dest:
        print(d)
        print(d.boss)

