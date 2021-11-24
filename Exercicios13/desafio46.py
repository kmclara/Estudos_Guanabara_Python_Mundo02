import time 
import emoji 

#Contagem regressiva + pausa de um segundo: 
for t in range (10, 0, -1):
    time.sleep(1)
    print(t)
print("FELIZ ANO NOVO!!!")
print(emoji.emojize(":grinning_face_with_big_eyes:"))
