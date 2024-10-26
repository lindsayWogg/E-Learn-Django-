from PIL import Image

# Ouvrez l'image que vous souhaitez redimensionner
image = Image.open('/home/tumbu/Documents/git/static/images/lindsay.jpeg')

# Définissez la nouvelle taille (en pixels)
nouvelle_taille = (826, 550)  # Largeur x Hauteur

# Redimensionnez l'image en utilisant la méthode `resize`
image_redimensionnee = image.resize(nouvelle_taille)

# Enregistrez l'image redimensionnée dans un fichier
image_redimensionnee.save('/home/tumbu/Documents/git/static/images/lindsay.jpeg')

# Fermez l'image d'origine et l'image redimensionnée
image.close()
image_redimensionnee.close()

print("L'image a été redimensionnée avec succès.")
