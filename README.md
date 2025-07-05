# Motor Learning Research Project

## Preview

## Overview

This project is an interactive 2D side-scrolling platformer game developed to study motor learning and muscle coordination. The game serves as a behavioral experiment designed to run in PsychoPy and is controlled using the PSURP (PsychoPy Serial USB Response Pad) from Black Box Toolkit: [https://www.blackboxtoolkit.com/psurp.html](https://www.blackboxtoolkit.com/psurp.html).

Participants use the PSURP device to control an on-screen dinosaur that must trace static arcs displayed on the screen with high precision. Participants are scored based on how accurately they follow these arcs, with higher accuracy resulting in higher scores. This creates a performance-based feedback system that incentivizes motor control and learning.

The game is deliberately challenging and designed to influence gradual improvement over time, allowing researchers to measure motor learning processes across repeated exposures. During gameplay, participants may also undergo transcranial brain stimulation, enabling the study of brain-behavior relationships during complex motor tasks.

Simultaneously, force data from the PSURP controller are collected to provide detailed measures of response timing and motor execution. This multimodal setup supports the analysis of learning in a controlled valid task environment.

*Developed for the Action Control Lab, University of Oregon*

## Folder Structure

```
/Motor-Learning-Research-Project
├── Game/
│   ├── Assets
│   │   ├── bgs                     # backgrounds
│   │   ├── grounds                 # grounds for each level
│   │   ├── dino_frames             # each frame for dino animation
│   │   └── sounds                  # sounds used in game
│   │
│   ├── Data                        # data from trials goes here
│   └── Game.psyexp                 # the game itself
│
├── PSURP/                           # Communication PSURP device
│   └── PSURP.psyexp                # PsychoPy communication code
```
## Game Design

### Levels and Progression

The game features 15 levels, each with unique arc patterns and floor designs, complete with custom art and environments. The levels progressively increase in difficulty as players advance, requiring greater accuracy and featuring more complex arc paths.

Players must achieve at least 80% accuracy to advance to the next level.

Each level has 2 minutes to complete.


### Game Modes

**Mode 1 (Vertical Control Only)**
- Players can only control vertical movement, horizontal movement is static
- Designed to be easier, allowing players to focus on learning basic character control
- Ideal for initial skill acquisition and getting familiar with the control scheme

**Mode 2 (Vertical and Horizontal Control)**
- Players have complete control over both vertical and horizontal movement
- Requires significantly more motor skill and coordination
- Allows players to complete levels faster through strategic movement
- Provides greater challenge and skill development opportunities

In Mode 2, if players complete the level faster than the allowed time, the leftover time is converted into bonus score.

### Objective

The primary goal is to reach the metabone at the end of each level while tracing the arcs as accurately as possible. Players must maintain high precision throughout their path to the goal.  


## System Components

### Loading Routines

#### ResetPSURP
Initializes and resets the PSURP device at the start of the experiment. This ensures the controller is in a known state and clears any residual data before gameplay begins.

#### TARE & RUNE
Performs force calibration on the PSURP device. This zeros the baseline force values, accounting for drift or hand placement variations before gameplay starts.

 
### Main Menu
The main menu provides a centralized hub where participants can:
- Play the game
- Select game mode (Mode 1 or Mode 2)
- Navigate to the calibrator for device setup
- Access the About screen for project information
- Exit the game

### About Screen
Provides information about the research project, game mechanics, and level descriptions to orient participants before gameplay.

### Calibrator
**Required before gameplay begins.** The calibrator normalizes PSURP values and allows researchers to adjust settings based on individual participant strength levels and response characteristics.


### Level (Main Gameplay)
The core gameplay environment where participants navigate through static arcs and floor elements across 15 progressively challenging levels, each featuring unique art assets and difficulty configurations.

**Code Components:**

**DinoMovement**:
Handles all character movement mechanics, including input processing, physics, and animation state management.

**WorldController**:
Manages all environmental assets including floors, arcs, and backgrounds. Controls camera behavior and side-scrolling functionality to maintain proper game view.

**GoalController**:
Handles all player-world interactions, including collision detection for floors, arc tracing mechanics, and goal (meatbone) achievement detection.

**Timer**:
Manages level timing, tracks completion times, and determines whether players receive time bonuses for fast completion.

### Level Checker
Post-level evaluation system that assesses participant performance and determines progression eligibility based on accuracy scores and completion times.


## Data Output

All participant data is stored in the Data folder, including:
- Individual level performance scores
- Calibrator settings and force thresholds
- Accuracy measurements and trajectory data

### Development Timeline and Challenges

**Phase 1: Hardware Integration**  
This phase focused on setting up reliable, real-time communication with the Black Box Toolkit’s PSURP device. Custom code was developed to accurately read force values from the controller and to manage communication issues such as dropped signals or initialization errors, ensuring clean data collection throughout the experiment.


**Phase 2: Game Engine Development**  
The second phase focused on building a fully interactive game within PsychoPy’s Builder environment—despite it not being designed for game development. This stage required the creation of custom systems for character movement, gravity mechanics, and accuracy tracking. A side-scrolling camera system was developed from scratch, along with real-time scoring logic to assess motor performance based on how closely players followed the target paths.

**Phase 3: Asset Creation and Animation**  
The final phase enhanced the visual and interactive experience through custom art and animation. Character animations were implemented using frame-by-frame sequences, and consistent visual assets were created for all 15 levels.


### Technical Innovation

This project demonstrates how PsychoPy can be pushed far beyond its typical use in structured lab tasks. By integrating precise motor tracking with real-time physics, animation, and interactive gameplay, the system transforms a traditional behavioral task into a fully immersive experience.

This approach enables researchers to study motor learning, in a format that feels more natural and engaging to participants. At the same time, it maintains strict control over timing, stimuli, and data collection. The result is a hybrid system that bridges the gap between rigid lab protocols and the dynamic complexity of real-world motor behavior, opening new possibilities for how behavioral experiments can be designed and delivered.
