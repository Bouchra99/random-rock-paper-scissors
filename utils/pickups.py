import pygame
import random
from utils.constants import screen, pick_sound, show_pickup

class PickupManager:
    def __init__(self):
        self.clone_img = pygame.image.load("assets/media/dna.png")
        self.freeze_img = pygame.image.load("assets/media/snowflake.png")
    
        self.SPAWN_INTERVAL = 5000  # 5 seconds between spawns
        self.PICKUP_LIFETIME = 4000  # 4 seconds before pickup disappears
        self.EFFECT_DURATION = 5000  # 5 seconds for effects
        
        self.pickup_types = [
            {'image': self.clone_img, 'effect': 'clone'},
            {'image': self.freeze_img, 'effect': 'freeze'}
        ]
        
        self.pickups = []
        self.last_spawn_time = 0
        self.active_effects = {}  # Track active effects per player
        
    def update(self, current_time):
        
        # check if 5 seconds passed before showing anoter pickup 
        if current_time - self.last_spawn_time > self.SPAWN_INTERVAL:
            self.show_pickup(current_time)
            self.last_spawn_time = current_time
            
        # Remove expired pickups
        self.pickups = [pickup for pickup in self.pickups 
                       if current_time - pickup['spawn_time'] < self.PICKUP_LIFETIME]
        
        # Update active effects
        self.update_effects(current_time)
    
    def show_pickup(self, current_time):
        pickup_type = random.choice(self.pickup_types)
        img = pickup_type['image']
        rect = img.get_rect()
        rect.x = random.randint(50, screen.get_width() - rect.width - 50)
        rect.y = random.randint(50, screen.get_height() - rect.height - 50)
        
        pickup = {
            'effect': pickup_type['effect'],
            'rect': rect,
            'img': img,
            'spawn_time': current_time
        }
        show_pickup.play()
        self.pickups.append(pickup)
    
    def check_collisions(self, game_objects):
        collected_pickups = []
        
        for pickup in self.pickups[:]:
            collision_found = False
            for obj_list in game_objects:
                if collision_found:
                    break
                for obj in obj_list:
                    if pickup['rect'].colliderect(obj['rect']):
                        self.apply_effect(pickup['effect'], obj, pygame.time.get_ticks())
                        collected_pickups.append(pickup)
                        self.pickups.remove(pickup)
                        collision_found = True
                        pick_sound.play() 
                        break
                    
        return collected_pickups
    
    def apply_effect(self, effect_type, target_object, current_time):
        player_name = target_object['name']
        
        if effect_type == 'clone':
            self.apply_clone_effect(target_object, current_time)
        elif effect_type == 'freeze':
            self.apply_freeze_effect(player_name, current_time)
    
    def apply_clone_effect(self, target_object, current_time):
        self.active_effects[f"{target_object['name']}_clone_{current_time}"] = {
            'type': 'clone',
            'target': target_object.copy(),  
            'start_time': current_time,
            'processed': False
        }
    
    def apply_freeze_effect(self, player_name, current_time):
        self.active_effects[f"{player_name}_freeze_{current_time}"] = {
            'type': 'freeze',
            'player': player_name,
            'start_time': current_time
        }
    
    def update_effects(self, current_time):

        expired_effects = []
        for effect_key, effect_data in self.active_effects.items():
            if current_time - effect_data['start_time'] > self.EFFECT_DURATION:
                expired_effects.append(effect_key)
        
        for effect_key in expired_effects:
            del self.active_effects[effect_key]
    
    def is_frozen(self, player_name, current_time):
        for effect_data in self.active_effects.values():
            if (effect_data['type'] == 'freeze' and 
                effect_data['player'] != player_name and
                current_time - effect_data['start_time'] < self.EFFECT_DURATION):
                return True
        return False
    
    def get_clone_effects(self):
        clone_effects = []
        for effect_key, effect_data in self.active_effects.items():
            if (effect_data['type'] == 'clone' and 
                not effect_data.get('processed', False)):
                clone_effects.append(effect_data)
                effect_data['processed'] = True
        return clone_effects
    
    def draw(self, screen):
        for pickup in self.pickups:
            screen.blit(pickup['img'], pickup['rect'])

