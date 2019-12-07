import sys
from operator import itemgetter
import math

runda=0

my_queen=[]
sites_xy=[]
max_mines=False
zerglings="NO ZERGLING RUSH SPOTTED"
center=[960, 500]

class calc():
    def mapping():
        distances_start=[]
        
        for i in range(num_sites):
            site_distance_x=abs(int(my_queen[0])-int(sites_xy[i][1]))
            site_distance_y=abs(int(my_queen[0])-int(sites_xy[i][2]))
            site_distance=round(math.sqrt(site_distance_x**2+site_distance_y**2))
            distances_start.append([i, site_distance])
    
        distances_start.sort(key=itemgetter(1))
        mapping_list=distances_start[:6][0]
        
        
       # c = [row for row in num_sites if mapping_list in row[0]]
        
        
        
    
    def distance():
        distances=[]
        
        for i in range(num_sites):
            site_distance_x=abs(int(my_queen[0])-int(sites_xy[i][1]))
            site_distance_y=abs(int(my_queen[0])-int(sites_xy[i][2]))
            site_distance=round(math.sqrt(site_distance_x**2+site_distance_y**2))
            distances.append([i, site_distance])
    
        distances.sort(key=itemgetter(1))
        print(distances, file=sys.stderr)
        return distances
        
    def distance_start():
        distances_start=[]
        
        for i in range(num_sites):
            site_distance_x=abs(int(my_queen[0])-int(sites_xy[i][1]))
            site_distance_y=abs(int(my_queen[0])-int(sites_xy[i][2]))
            site_distance=round(math.sqrt(site_distance_x**2+site_distance_y**2))
            distances_start.append([i, site_distance])
    
        distances_start.sort(key=itemgetter(1))
        return distances_start
    
    def distances_from_center():
        distances_center=[]
        
        for i in range(num_sites):
            distance_x=abs(int(center[0])-int(sites_xy[i][1]))
            distance_y=abs(int(center[1])-int(sites_xy[i][2]))
            center_distance=round(math.sqrt(distance_x**2+distance_y**2))
            distances_center.append([i, center_distance])
    
        distances_center.sort(key=itemgetter(1))
        return distances_center
    
    def distances_zerglings():
        zerglings=[]
        distances_zerglings=[]
        
        if len(units)>4:
            for i in range(len(units[0])-1):
                if units[i][2]==1 and units[i][3]==0 and units[i][4]>7:
                    zerglings.append([i, units[0], units[1]])
        
        if len(zerglings)>2:
            for i in range(len(zerglings[0])):
                zerg_distance_x=abs(my_queen[0])-(zerglings[i][1])
                zerg_distance_y=abs(int(my_queen[0])-int(zerglings[i][2]))
                zerg_distance=round(math.sqrt(zerg_distance_x**2+zerg_distance_y**2))
                if zerg_distance<400:
                    distances_zerglings.append([i, zerg_distance])
       
        print("distances_zerglings", file=sys.stderr)
        print(distances_zerglings, file=sys.stderr)
        distances_zerglings.sort(key=itemgetter(1))
        return distances_zerglings
        
    def train():
        if my_barracks==[]:
            return "TRAIN"
        if my_barracks!=[]:
            return "TRAIN "+ str(my_barracks[-1])

                
    def mines_upgrade():
            if my_mines!=[]:
                if my_mines[0][1]<my_mines[0][2]:
                    print("mines upgrade 1st", file=sys.stderr)
                    return "BUILD "+ str(my_mines[0][0]) + " MINE"
                else:
                    if len(my_mines)==2 and my_mines[1][1]<my_mines[1][2]:
                        print("mines upgrade 2nd", file=sys.stderr)
                        return "BUILD "+ str(my_mines[1][0]) + " MINE"
                    else:
                        if len(my_mines)==3 and my_mines[2][1]<my_mines[2][2]:
                            print("mines upgrade 3rd", file=sys.stderr)
                            return "BUILD "+ str(my_mines[2][0]) + " MINE"
                        else:
                            return "DONT"
            else:
                return "DONT"
                
    def build():
        for i in range(len(distances_start)):
            closest=distances_start[i][0]
            closest_site=sites[closest][4]
            
            if attitude.sites_amount()=="big map":
                additional=1
            else:
                additional=0
            if calc.mines_upgrade()!="DONT":
                return calc.mines_upgrade()
            if behaviour.zergling_rush()!="DONT":
                return behaviour.zergling_rush()
            if behaviour.anti_zergling_rush()!="DONT":
                return behaviour.anti_zergling_rush()
            if behaviour.panic_tower()!="DONT":
                return behaviour.panic_tower()
            if behaviour.take_middle()!="DONT":
                return behaviour.take_middle()
            if behaviour.tending_towers()!="DONT":
                return behaviour.tending_towers()
                
            start_i=int(distances_start[i][0])
            
            if closest_site!=0 and sites[closest][3]!=1:
                if len(my_mines)<2+additional and runda<25:
                    #if sites[closest][1]<10:
                    #    return "BUILD "+ str(distances_start[i][0]) + " TOWER"
                    #else:
                    return "BUILD "+ str(start_i) + " MINE"       
                else:
                    if len(my_barracks)<1:
                        return "BUILD "+ str(start_i) + " BARRACKS-KNIGHT"    
                    else: 
                        if len(my_towers)<1:
                            #return "BUILD "+ str(calc.distances_from_center()[0][0]) + " TOWER"
                            return "BUILD "+ str(start_i) + " TOWER"
                        else:
                            if 1200>sites_xy[start_i][1]>700:
                                return "BUILD "+ str(start_i) + " TOWER"
                            else:
                                if sites[closest][1]>20:
                                    return "BUILD "+ str(start_i) + " MINE"
                                else:
                                    return "BUILD "+ str(start_i) + " BARRACKS-KNIGHT"

class listers():
    def mines():
        my_mines=[]
    
        for i in range(len(sites)-1):
            if sites[i][4]==0 and sites[i][3]==0:
                my_mines.append([sites[i][0], sites[i][5], sites[i][2]])
        return my_mines
    
    def barracks():
        my_barracks=[]
    
        for i in range(len(sites)-1):
            if sites[i][4]==0 and sites[i][3]==2:
                my_barracks.append(sites[i][0])
        print(my_barracks, file=sys.stderr)
        return my_barracks
        
    def enemy_barracks():
        enemy_barracks=[]
    
        for i in range(len(sites)-1):
            if sites[i][4]==1 and sites[i][3]==2:
                enemy_barracks.append(sites[i][0])
        print("enemy barracks", file=sys.stderr)        
        print(enemy_barracks, file=sys.stderr)
        return enemy_barracks
    
    def towers():
        my_towers=[]
    
        for i in range(len(sites)):
            if sites[i][4]==0 and sites[i][3]==1:
                my_towers.append([sites[i][0], sites[i][6]])#sprawdz przypisanie wiezy
        print(my_towers, file=sys.stderr)
        return my_towers
        
class behaviour():
    def tending_towers():
        if len(my_towers)==1:
            if my_towers[0][1]<400:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[0][0]) + " TOWER"
            else:
                return "DONT"
        elif len(my_towers)==2:
            if my_towers[0][1]<400:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[0][0]) + " TOWER"
            elif my_towers[1][1]<350:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[1][0]) + " TOWER"
            else:
                return "DONT"
        elif len(my_towers)==3:
            if my_towers[0][1]<400:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[0][0]) + " TOWER"
            elif my_towers[1][1]<350:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[1][0]) + " TOWER"
            elif my_towers[2][1]<400:
                print("tending towers", file=sys.stderr)
                return "BUILD "+ str(my_towers[2][0]) + " TOWER"
            else:
                return "DONT"
        else:
            return "DONT"
    
    def zergling_rush():
        if queens_start_hp<45 and my_barracks==[]:
            print("ZERGLINGS RUSH!", file=sys.stderr)
            return "BUILD "+ str(distances_start[i][0]) + " BARRACKS-KNIGHT"
        else:
            if queens_start_hp<40 and my_towers==[]:
                print("ZERGLINGS RUSH!", file=sys.stderr)
                return "BUILD "+ str(calc.distances_from_center()[0][0]) + " TOWER"
            return "DONT"
            
    def anti_zergling_rush():
        if zerglings=="AHEAD" and my_towers==[]:
            print("ZERGLINGS SPOTTED!", file=sys.stderr)
            return "BUILD "+ str(distances_start[i][0]) + " TOWER"
        else:
            return "DONT"
            
    def take_middle():
        e=str(calc.distances_from_center()[0][0])
        if max_mines==True and sites[e][4]!=-1:
            print("Take middle!!", file=sys.stderr)
            return "BUILD "+ str(calc.distances_from_center()[0][0]) + " TOWER"
        else:
            return "DONT"
    
    def panic_tower():
        distances_now=calc.distance()
        if attitude.risk()=="HIGH":
            print("IN RISK!!!", file=sys.stderr)
            return "BUILD "+ str(sites[distances_now][0]) + " TOWER"
        else:
            return "DONT"
    
    
class attitude():
    def sites_amount():
        if len(sites)>20:
            return "big map"
        else:
            return "small map"
            
    def queen_hp():
        if my_queen[4]>100:
            return "high hp"
        if 100>my_queen[4]>40:
            return "mid hp"
        else:
            return "low hp"
            
    def risk():
        if len(calc.distances_zerglings())>3:
            return "HIGH"
        else:
            return "LOW"
        
        
        
            
################            

num_sites = int(input())
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites_xy.append([site_id, x, y, radius])
    
#print(sites_xy[1][1], file=sys.stderr)

# game loop
randomizer=1


while True:
    runda+=1
    sites=[]
    units=[]
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        
        sites.append([site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2])
    
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        units.append([x, y, owner, unit_type, health])
        if unit_type==-1 and owner==0:
            my_queen=([x, y, owner, unit_type, health])
        if unit_type==-1 and owner==1:
            enemy_queen=([x, y, owner, unit_type, health])
        
        
        
        
        
        
    if runda==1:
        distances_start=calc.distance_start()
        queens_start_hp=int(my_queen[4])
        
    if 6>runda>2:
        if listers.enemy_barracks()!=[]:
            zerglings="AHEAD"
            
            
    calc.mapping()        
    distances = calc.distance()
    print(distances, file=sys.stderr)
    
 
    my_mines=listers.mines()
    my_barracks=listers.barracks()
    my_towers=listers.towers()
    
    
    build_command=calc.build()
    print(build_command)

    train_command=calc.train()
    print(train_command)
