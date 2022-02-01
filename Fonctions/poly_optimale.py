#Gestion des exceptions de la fonction poly

##Recap de la fonction pythagore
def poly_optimale(x, borne_inf, borne_sup):
    
    ########################################################################################
    ## Cas1 = String
    ########################################################################################
    if type(x) == str:  ##Si x est un str
        #raise Exception('poly Not Applicable with Str')
        x = int(input()) ##Saisie d'une nouvelle valeur numérique de x

    ########################################################################################
    ## Cas2 = Complexe
    ########################################################################################
    elif type(x) == complex :
      x = x.real ##On récupère la partie réelle du nombre et on réaffecte la valeur de x
    
    ########################################################################################
    ## Cas3 = Entier négatif
    ########################################################################################
    elif (type(x) in [int, float]) and x < 0 :
        x = abs(x) ##Récupérer la variable a (valeur absolue)

     
    ########################################################################################
    ## Cas4 : Grand nombre
    ########################################################################################
    elif (len(str(x)) > borne_sup):
      while(len(str(x)) > borne_sup):  ##On force l'utilisateur à resaisir le nombre tel que la longueur est sup à la borne_sup, j'introduits le while.
          print("le nombre a saisie comporte plus de {} digit, Veuillez le resaisir".format(borne_sup))
          x = int(input())

    ########################################################################################
    ## Cas5 : Petit nombre
    ########################################################################################
    elif (len(str(x)) < borne_inf):
      while(len(str(x)) < borne_inf):  ##On force l'utilisateur à resaisir le nombre tel que la longueur est inf à la borne_inf, j'introduits le while.
          print("le nombre a saisie comporte moins de {} digit, Veuillez le resaisir".format(borne_inf))
          x = int(input())

        
    return poly(x) ##Appel à la fonction poly pour calculer la polynome 


print(poly_optimale(3, 2, 10))

