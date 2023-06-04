import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre du jeu
largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu d'évitement")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Paramètres du personnage
perso_taille = 50
perso_x = largeur / 2 - perso_taille / 2
perso_y = hauteur - perso_taille - 10
perso_vitesse = 5

# Paramètres des obstacles
obstacle_taille = 50
obstacle_x = random.randint(0, largeur - obstacle_taille)
obstacle_y = -obstacle_taille
obstacle_vitesse = 3

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement du personnage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and perso_x > 0:
        perso_x -= perso_vitesse
    if touches[pygame.K_RIGHT] and perso_x < largeur - perso_taille:
        perso_x += perso_vitesse

    # Déplacement de l'obstacle
    obstacle_y += obstacle_vitesse
    if obstacle_y > hauteur:
        obstacle_x = random.randint(0, largeur - obstacle_taille)
        obstacle_y = -obstacle_taille

    # Collision entre le personnage et l'obstacle
    if obstacle_y + obstacle_taille >= perso_y and obstacle_y <= perso_y + perso_taille:
        if obstacle_x + obstacle_taille >= perso_x and obstacle_x <= perso_x + perso_taille:
            running = False

    # Effacer l'écran
    fenetre.fill(blanc)

    # Dessiner le personnage
    pygame.draw.rect(fenetre, noir, (perso_x, perso_y, perso_taille, perso_taille))

    # Dessiner l'obstacle
    pygame.draw.rect(fenetre, noir, (obstacle_x, obstacle_y, obstacle_taille, obstacle_taille))

    # Mettre à jour l'affichage
    pygame.display.update()
    clock.tick(60)

# Quitter le jeu
pygame.quit()

