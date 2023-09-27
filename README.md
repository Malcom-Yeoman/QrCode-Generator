# QrCode-Generator

Générateur de QR Code simple et efficace basé sur Flask et la bibliothèque Python qrcode. Transformez rapidement n'importe quelle chaîne de texte en un QR Code scannable.

![Aperçu de l'application](QrCode-Generator.png)

## Fonctionnalités

- Génération rapide de QR Code: Convertit n'importe quelle chaîne de texte en un QR Code en quelques secondes.
- Compatible avec tous les lecteurs de QR Code: Les codes générés sont standardisés et peuvent être lus par n'importe quelle application ou hardware de lecteur de QR Code.
- Personnalisable: Vous pouvez facilement adapter le générateur à vos besoins, changer les couleurs, la taille, etc.

## Comment l'utiliser ?

1. Installation:
    - Assurez-vous d'avoir Python installé sur votre machine.
    - Clonez le dépôt sur votre machine locale.
    - Installez les dépendances nécessaires à l'aide de pip install -r requirements.txt (assurez-vous de créer un environnement virtuel si nécessaire).
    - Lancez l'application avec python app.py.
    - Accédez à http://127.0.0.1:5000/ dans votre navigateur.
2. Génération de QR Code:
    - Entrez la chaîne de texte pour laquelle vous souhaitez générer un QR Code.
    - Cliquez sur "Générer".
    - Votre QR Code sera affiché à l'écran.

## Personnalisation

- Couleurs: Vous pouvez changer les couleurs de remplissage et d'arrière-plan lors de la génération de l'image du QR Code dans app.py.
- Taille et bordure: Les dimensions du QR Code (taille des cases et largeur de la bordure) peuvent également être modifiées dans app.py.

## Contribution

Si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une issue ou à soumettre une pull request. Toutes les contributions sont les bienvenues!