import json
firms_profit={}#этот словарь хранит прибыль каждой компании
profits=[]#список чтобы хранить прибыль всех +
with open("firms.txt","r",encoding="utf-8") as file:
    lines=file.readlines()
    for line in lines:
        name,d,revenue,cost=line.split()#d нам не нужно
        profit=int(revenue)-int(cost)
        firms_profit[name]=profit
        if profit>0:
            profits.append(profit)
avarage_profit=sum(profits)/len(profits) if profits else 0
result=[firms_profit,{"avarage_profit": avarage_profit}]# список хранит 2 словаря компании+прибыль, средняя прибыль

with open("firms_profit.txt","w",encoding="utf-8") as outfile:
    json.dump(result,outfile,ensure_ascii=False,indent=4)