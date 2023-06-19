
rub_goal: float = 83.99
usd_input: float = 1.0

alpha: float = 0.001

weight: float = 0.5

def train(weight: float) -> float:
    
    pred: float = 0.0
    
    while pred > rub_goal + 0.00000001 or pred < rub_goal - 0.00000001:
        pred = usd_input * weight
        
        #error = (pred - rub_goal) ** 2
        
        delta = rub_goal - pred
        delta_weight = (delta * usd_input) * alpha
        
        weight += delta_weight
        
    
    return weight

weight = train(weight)

def neural_network(weight: float, usd: float, rub: float) -> float:
    
    if usd != 0:
        prediction = usd * weight
        prediction = round(prediction, 2)
    else:
        prediction = rub / weight
        prediction = round(prediction, 2)
    
    return prediction

#print(f"200 долларов переводя в рубли стоят {neural_network(weight, 1.0, 0)} рублей")
#print(f"300 долларов переводя в рубли стоят {neural_network(weight, 300.0, 0)} рублей")
#print(f"1000 долларов переводя в рубли стоят {neural_network(weight, 1000.0, 0)} рублей")
#print(f"10000 рублей в долларах это {neural_network(weight, 0, 10000.0)} долларов")

print("Нейроконвертер валюты.\nСуть программы в том, что у вас на компьютере учиться нейросеть во время работы программы. \n(если вы видите это сообщение, значит нейросеть уже обучена).\nЧтобы выйти нажмите CTRL+C\n\nТочность нейросети до ста миллионых валюты\n\n")

while True:
    try:
        menu: str = input("Из рубля в доллар - 1.\nИз долларов в рубли - 2.\n>>> ")
        value: float = float(input("Количество валюты: "))
        
        if menu == "1":
            
            result: float = neural_network(weight, 0, value)
            print(f"{value} рублей это {result} долларов\n")
            
        elif menu == "2":
            
            result: float = neural_network(weight, value, 0)
            print(f"{value} долларов это {result} рублей\n")
            
        else:
            print("Такой опции не существует\n")
            
        
        
    except TypeError:
        print("\n\nВведите количество валюты в качестве числа.")
    except KeyboardInterrupt:
        print("\n\nВы вышли из программы.")
        break        
