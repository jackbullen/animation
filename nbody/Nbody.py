import numpy as np

class CelestialBody:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.zeros(3, dtype=float) 

    def compute_force(self, other):
        '''
        this method is called on a body and takes another body as an argument
        
        Return the force exerted on this body by other.
        '''
        G = 6.67430e-11 
        r = other.position - self.position  
        distance = np.linalg.norm(r) 

        force_magnitude = G * self.mass * other.mass / (distance ** 2)
        force_direction = r / distance

        force = force_magnitude * force_direction
        return force

    def update(self, dt):
        acceleration = self.force / self.mass 
        self.velocity += acceleration * dt  
        self.position += self.velocity * dt 
        self.force = np.zeros(3, dtype=float) 
        
class System:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def compute_interactions(self):
        """
        Compute and update forces between all pairs of celestial bodies in the system.
        """
        for i, body1 in enumerate(self.bodies):
            for j, body2 in enumerate(self.bodies):

                if i != j: # Exclude self-interaction

                    force = body1.compute_force(body2)  
                    body1.force += force 

    def update(self, dt):
        '''
        this gets called after compute_interactions and updates the position and velocity of each body
        '''
        for body in self.bodies:
            body.update(dt) 

    def reset_forces(self):
        """
        reset the net forces, should be called after each time step to prepare for the next iteration.
        """
        for body in self.bodies:
            body.force = np.zeros(3, dtype=float)