# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if not (x and y and z) ==(not x) or (not y) or (not z):
                result = 'Утверждение верное'
            else:
                resalt = 'Утверждение ложное'    
print(result)                

                