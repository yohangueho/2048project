# 2048project

Bonjour, le jeu auquel vous êtes en train de jouer est le fameux 2048 ! Bienvenue, j'espère que vous êtes prêts à vous amuser !

Oui ! Je suis en effet impatient de jouer à votre jeu (que je ne connais pas du tout). Mais, quel est le but ?

Et bien, permettez moi de vous le présenter. Le but du 2048 est d'atteindre le carré 2048 ! Tout était dans le titre. Pour cela, vous aurez besoin d'empiler, de combiner des carrés pour atteindre ce fameux carré 2048. Vous remarquerez que 2048 est égal à 2^11. Tout le jeu est basé sur les puissances de 2. Chaque étape est un carré lié à une puissance de 2. Ainsi, il faudra d'abord atteindre les carrés 2,4,8,16,32,64,128,256,512,1024 avant d'atteindre celui de 2048. Et lorsque vous arrivez à 2048, c'est gagné ! Mais vous pouvez continuer, pour plus de fun, avec 4096, 8192, etc... jusqu'à 2^17 = 131072 !!

Ce jeu à l'air très addicitf ! Mais dites moi, comment fonctionne-t-il ?

C'est très simple mon ami ! Vous allez comprendre très (très très très) rapidement ;) Vous commencerez toujoursa avec une plateau de 16 cases, disposées en carré de 4 cases de côté. Tout d'abord, appuyez sur "start" ("commencer") afin de commencer la partie. Ce bouton permettra à l'ordinateur de disposer aléatoirement 2 cases sur le plateau, avec les valeurs aléatoires de 2 ou 4. Et maintenant, à vous de jouer ! Appuyez sur les boutons "left" ("gauche"), "right" ("droite"), "down" ("bas") ou "up" ("haut") afin de bouger les cases. Si 2 mêmes carrés se trouvent sur la même ligne sans obstacle, alors ils fusionneront ! Et à chaque coup, un nouveau carré au hasard, prenant la valeur de 2 ou 4, se crée sur le plateau ! À vous d'être assez malin pour aller jusqu'à 2048 ! !

Oh ! je vois, donc il faudrait se placer dans un coin afin de concentrer tous les gros carrés au même endroit... Intéresant ! Mais, avant que j'y joue, j'aimerai que vous m'expliquiez un petit peu votre code... Qu'est ce qui se cache derrière cette si belle interface graphique ?

Haha, merci mon ami, vous êtes sympathique. Je vais tout vous dire ! Le coeur du jeu se trouve dans la fonction left. Il faut d'abord comprendre que le plateau de jeu est traduit sous forme de matrice 4*4 pour l'ordinateur. Ainsi, il associe à chaque case une couleur et une valeur. Lorsque vous appuirez sur le bouton "left", une série de condition sera vérifiée afin de bouger les carrés vers la gauche. Ce serait un peu long à détailler, mais l'ordinateur vérifie si 2 même carrés se trouvent côte à côte, ou séparés par des cases vides, (donc il fusionneront) ou alors s'il n'y a que des cases vides à gauche d'un carré (auquel cas les carrés seront tout simplement déplacés vers la gauche). Enfin bref, tout un  tas de conditions à vérifier, qui sont détaillées avec les commentaires du code.
Ensuite, pour les autre mouvements, la même fonctione est utilisée ! Sauf qu'il y a au préalable une rotation de la matrice pour que le mouvement s'effectue dans le bon sens. Par exemple, pour le mouvement "haut", l'ordinateur va faire une rotation de la matrice vers la gauche, et il pourra alors effectuer les vérifications de "left", et re fera ensuite une rotation de la matrice vers la droite, afin de la remettre dans le bon sens. Cela évite d'écrire les conditions pour chaque mouvement (ce qui serait long !)

Très ingénieux, je dois l'avouer. Mais, quelque chose me turlupine, d'autres boutons sont présents, et je ne parle pas anglais, pouvez vous m'en dire plus quant à ces "lOAadD" ou "sAaveE" ?

Évidemment, je suis là pour ça ;) Je vous ai déjà expliqué "start" ("commencer"). Passons à "stop". Aucune excuse de barrière de langue, nous avons le même mot en anglais ! Haha, je vous taquine... Le bouton "stop" ("stop") vous demandera d'abord si vous voulez enregistrer votre partie avant de fermer le jeu, puis le fermera enenregistrant, ou non, votre partie. Votre partie peut être enregistrée avec la fonction "save" ("enregistrer"). L'ordinateur enregistrera directement votre partie avec comme nom le numéro de partie. Exemple, s'il y a déjà 4 parties d'enregistrées, alors la vôtre portera le nom "5".
Et finalement, la fonction "load" ("charger") vous permettra de reprendre une partie que vous auriez préalablement enregistrée ! N'est-ce pas magnifique ? Enfin, tout cela est expliqué dans le code, vous pouvez toujours y jeter un oeil pour mieux comprendre.

Et bien, ce jeu m'a lair vraiment bien fait ! Je pense que je vais tout de suite y jouer afin de me faire mon propre avis :)

Bonne partie ! Et bonne chance, ce jeu est addictif, et peut vous mettre or de vous si vous ne réussissez pas .. ;)

""" Some hours later... """

Alors, mon ami, vous avez pu tester mon jeu ?

Oui, et je n'ai fait que de perdre... Je n'arrive jamais à atteindre 2048 !!! Je suis bloqué à chaque fois à 1024 ! Donc j'enregistre à chaque fois que j'y arrive pour repartir de ce point. C'est très intelligent d'avoir fait ça !

Voilà qui fait plaisir à entendre ! Merci ! Continuez de bien vous amuser ;)

De la part de Mariam, Yanis et Yohan.