# architecture scratch
 
## Functionalities:
Given a relative distance and normal vector, and projectile weight and air resistance coefficient, choose a launch parabola that 
1. hits the target
2. launch velocity and launch angle are both possible  (for angles close to straight up, very little power would be available to us)
3. doesn't hit the ceiling 

Determine the relative distance and normal vector of the glyph based on a camera image.
    
Determine the radius of the projectile based on a camera image. (for air resistance calcs)

Determine the weight of the projectile based on sensor input.

Coordinate the firing of a projectile safely.
- Human loads projectile and presses a button
- This can happen in parallel:
    - Camera pose acquired by identifying glyph
    - Calculate air coefficient 
- Calculate a launch parabola. If one exists that meets the constraints, "READY" LED turns on.
- Human presses button. Winch and stopper move into position. Winch releases. Projectile fires.
- Repeat


## Rough file structure:
### main.py
- Initial calibration of sensors (drive winch and stopper to their limit switches)
- Coordinate the firing of projectiles

### sense.py
- Function to get camera pose (relative distance and normal vector of the glyph)
- Function to estimate projectile radius based on camera input
- Function which returns the weight of the projectile.

### motor.py
- Wrappers for setting winch, stopper motors to desired positions based on sensor input
- Any other motor helper functions

### calc.py
- Functions which calculate the launch velocity and angle to hit a target (specified as a position vector and normal vector)

