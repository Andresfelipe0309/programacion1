homocisteina= float(input('Ingrese su nivel de homocisteina'))
trigliceridos=float(input('Ingrese su nivel de trigliceridos'))

if trigliceridos < 150  :

    print("Su estado de trigliceridos es optimo")

elif trigliceridos >= 150 and trigliceridos<=199  :
      print("Su estado de trigliceridos esta sobre el limite optimo")
      
elif trigliceridos >=200 and trigliceridos<= 499:
    print("Su estado de triglicéridos es alto")
    
else:
    print("Su estado de triglicéridos es muy alto")
    
    
if homocisteina >=2 and homocisteina<15:
    print("El nivel de homocisteina es optimo")
    
elif homocisteina >=15 and homocisteina<30:
     print("El nivel de homocisteina esta sobre el limite optimo")
     
elif homocisteina >=30 and homocisteina<100:
     print("El nivel de homocisteina esta alto")

else:
     print("El nivel de homocisteina es muy alto")