import pygame
import random
import math

class Ant(pygame.sprite.Sprite):
    def __init__(self, base_image, anim_images):
        super().__init__()
        self.base_image = pygame.transform.scale(base_image, (30, 30))
        self.anim_images = [pygame.transform.scale(img, (30, 30)) for img in anim_images]
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(0, 570)
        self.base_speed = random.uniform(1.0, 3.0)  # Base speed varies per ant
        self.speed = self.base_speed
        self.velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.acceleration = pygame.math.Vector2(0, 0)
        self.max_speed = 3
        self.max_force = 0.1
        self.pause_time = 0
        self.frame_index = 0
        self.frame_duration = max(1, int(10 / self.speed))  # Frame duration based on speed
        self.frame_count = 0

    def update_image(self):
        angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x))
        if self.frame_count >= self.frame_duration:
            self.frame_count = 0
            self.frame_index = (self.frame_index + 1) % len(self.anim_images)
        else:
            self.frame_count += 1
        self.image = pygame.transform.rotate(self.anim_images[self.frame_index], angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def apply_force(self, force):
        self.acceleration += force

    def seek(self, target):
        desired = (target - pygame.math.Vector2(self.rect.center)).normalize() * self.max_speed
        steer = (desired - self.velocity).normalize() * self.max_force
        return steer

    def avoid_ants(self, ants):
        avoid_force = pygame.math.Vector2(0, 0)
        for ant in ants:
            if ant != self:
                distance = pygame.math.Vector2(self.rect.center) - pygame.math.Vector2(ant.rect.center)
                if 0 < distance.length() < 50:  # Avoid if too close
                    avoid_force += distance.normalize()
        return avoid_force

    def update(self, ants):
        if self.pause_time > 0:
            self.pause_time -= 1
            self.image = pygame.transform.rotate(self.base_image, math.degrees(math.atan2(-self.velocity.y, self.velocity.x)) - 90)
            return

        if random.random() < 0.01:
            self.pause_time = random.randint(30, 300)  # Random pause duration

        # Randomly change direction
        if random.random() < 0.05:
            random_target = pygame.math.Vector2(
                random.uniform(0, 800),
                random.uniform(0, 600)
            )
            force = self.seek(random_target)
            self.apply_force(force)

        # Avoid other ants
        avoid_force = self.avoid_ants(ants)
        self.apply_force(avoid_force)

        self.velocity += self.acceleration
        self.velocity = self.velocity.normalize() * self.speed
        self.rect.center += self.velocity
        self.acceleration *= 0

        # Keep within screen bounds
        if self.rect.left < 0 or self.rect.right > 800:
            self.velocity.x = -self.velocity.x
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocity.y = -self.velocity.y

        self.frame_duration = max(1, int(10 / self.speed))  # Adjust frame duration based on speed
        self.update_image()
