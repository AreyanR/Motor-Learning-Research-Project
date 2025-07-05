# Motor Learning Research Project

## Preview

## Overview

This project is an interactive 2D side-scrolling platformer game developed to study motor learning and muscle coordination. The game serves as a behavioral experiment designed to run in PsychoPy and is controlled using the PSURP (PsychoPy Serial USB Response Pad) from Black Box Toolkit: [https://www.blackboxtoolkit.com/psurp.html](https://www.blackboxtoolkit.com/psurp.html).

Participants use the PSURP device to control an on-screen dinosaur that must trace static arcs displayed on the screen with high precision. Participants are scored based on how accurately they follow these arcs, with higher accuracy resulting in higher scores. This creates a performance-based feedback system that incentivizes motor control and learning.

The game is deliberately challenging and designed to elicit gradual improvement over time, allowing researchers to measure motor learning processes across repeated exposures. During gameplay, participants may also undergo transcranial brain stimulation, enabling the study of brain-behavior relationships during complex motor tasks.

Simultaneously, force data from the PSURP controller are collected to provide detailed measures of response timing and motor execution. This multimodal setup supports the analysis of learning in a controlled valid task environment.

*Developed for the Action Control Lab, University of Oregon*

## Folder Structure

```
/Motor-Learning-Research-Project
├── Game/                            # Game used for trials
│   ├── Assets
│   │   ├── bgs                     # backgrounds
│   │   ├── grounds                 # grounds for each level
│   │   ├── dino_frames             # each frame for dino animation
│   │   └── sounds                  # 3 sounds used in game
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

Each level has 2:00 minutes to complete.


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
- Access the About screen for project information
- Navigate to the calibrator for device setup
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

The project evolved through several distinct phases, each presenting unique technical hurdles:

**Phase 1: Hardware Integration**
The first stage centered on establishing stable, real-time communication with the Black Box PSURP device. This involved designing custom protocols for accurate data acquisition, building robust error handling for connection reliability.



**Phase 2: Game Engine Development**
Next, the focus shifted to building an interactive game within PsychoPy’s experimental framework—an unconventional environment for game development. This required implementing custom systems for physics-based movement, arc collisions, and precision tracking. A smooth side-scrolling camera system was built from scratch, along with real-time scoring logic to evaluate path accuracy and motor performance.

**Phase 3: Asset Creation and Animation**
The final phase refined the user experience through cohesive visuals and responsive animation. Frame-by-frame character animations were implemented using PsychoPy’s stimulus system, and consistent art assets were developed across all 15 levels. Asset loading and rendering were also optimized to ensure smooth, uninterrupted gameplay during experimental trials.


### Technical Innovation

This project reimagines how PsychoPy can be used, extending it beyond traditional lab tasks into a more interactive and immersive research platform. By combining precise motor control tracking with engaging gameplay, it transforms standard experimental procedures into dynamic experiences without sacrificing scientific precision.

The system allows researchers to study motor learning, adaptation, and sensorimotor integration in a way that feels more natural to participants, while still maintaining tight control over variables. It bridges the gap between the structured environment of the lab and the complexity of real-world motor behavior, offering a new approach to designing behavioral experiments that are both rigorous and relevant.
