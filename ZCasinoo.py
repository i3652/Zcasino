## TP-1 Zcasino ##
### Le joueur mise un numéro entre 0 et 49 ###
#### Il dépose la mise souhaitée ####
##### Les numéros pairs sont noirs, les impairs rouges #####
###### Le croupier fait tourner la roulette et la bille s'arrête sur ######
###### le numéro gagnant. ######
####### Si le numéro est le même que celui du joueur alors : #######
# Le joueur remporte sa mise + 3 fois sa mise #
## Si la couleur est la même alors : ## 
### Le joueur remporte sa mise + 50% de sa mise. ###
#### Si le numéro et la couleur diffèrent alors : ####
##### Le joueur perd sa mise. #####
import random

cash = 1000
print ("Votre montant de départ est de", cash, '$')
 
continuer_partie = True
while continuer_partie:
# Le joueur choisi le numéro sur lequel il effectuera une mise #
 
    numero = input('Choisissez un numéro situé entre 0 et 49:')
    while int(numero) <= 0 or int(numero) >= 50:
        numero = input('Choisissez un numéro situé entre 0 et 49:')
    if int(numero) % 2 == 0:
        print ('Vous misez sur le', numero, 'noir')
    else:
        print ('Vous misez sur le', numero, 'rouge')
 
 # Le joueur détermine maintenant sa mise #
 
    mise_joueur = input ('Quelle sommes souhaitez-vous miser ?')
    while int(mise_joueur) > int(cash):
        print('Fond non disponible')
        mise_joueur = input('Quelle sommes souhaitez-vous miser ?')
    else :
        print('mise de', mise_joueur, '$')
 
# Les jeux sont faits, rien ne va plus #
 
    print('Les jeux sont faits, rien ne va plus!')
 
# Le croupier fait tourner la roulette et le résultat est annoncé #
 
    num_gagnant = random.randint(1,49)
    if num_gagnant % 2 == 0:
        print('Le numéro gagnant est', num_gagnant, 'noir')
    else:
        print('Le numéro gagnant est', num_gagnant, 'rouge')
 
# Le croupier compare maintenant le numéro gagnant avec celui du joueur #
 
# Les numéros sont identiques #
 
    if int(numero) == int(num_gagnant):
        cash = cash + (3 * int(mise_joueur))
        print('Bravo! Vous remportez 3 fois votre mise')
        print ('Votre capital est maintenant de', cash, '$')
 
# Les numéros sont de couleurs noirs #
 
    elif int(numero) % 2 == 0 and int(num_gagnant) % 2 == 0:
        cash = int(cash) + (0.5 * int(mise_joueur))
        print('Pas mal! Vous remportez 50% de votre mise')
        print('Votre capital est maintenant de', cash, '$')
 
# Les numéros sont de couleurs rouges #
 
    elif int(numero) % 2 != 0 and int(num_gagnant) % 2 != 0:
        cash = int(cash) + (0.5 * int(mise_joueur))
        print('Pas mal! Vous remportez 50% de votre mise')
        print('Votre capital est maintenant de', cash, '$')
 
# Les numéros sont tout à fait différents #
 
    else:
        cash = int(cash) - int(mise_joueur)
        print('Vous venez de perdre votre mise')
        print('Votre capital est maintenant de', cash, '$')
 
# Le joueur n'a plus d'argent #
 
    if cash <= 0:
        print( 'Vous voilà sans un sous, prière de quitter la table SVP')
        continuer_partie = False
 
# Le joueur désire-t-il continuer la partie #
 
    quitter = input('Souhaitez-vous quitter la table de jeu? (O/N)')
    if quitter == 'O' or quitter == 'o':
        print('À bientot!')
        continuer = False
        break