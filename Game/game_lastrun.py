#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on January 16, 2025, at 00:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from DinoMovement
Base71Lookup = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'game'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1000,800]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\Users\\areya\\Desktop\\work\\motor-learning-research-project\\Game\\game_lastrun.py',
        savePickle=True, saveWideText=False,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "resetPSURP" ---
    t_reset_PSURP = visual.TextStim(win=win, name='t_reset_PSURP',
        text='reseting PSURP',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TARE" ---
    t_tare = visual.TextStim(win=win, name='t_tare',
        text='loading each cell with 1 sec delay (5 seconds)',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "RUNE" ---
    T_RUNE = visual.TextStim(win=win, name='T_RUNE',
        text='Entering streaming mode ...',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "MainMenu" ---
    TitleText = visual.TextStim(win=win, name='TitleText',
        text='Main Menu',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    start_button = visual.Rect(
        win=win, name='start_button',
        width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    StartGame = visual.TextStim(win=win, name='StartGame',
        text='Start Game',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    exit_button = visual.Rect(
        win=win, name='exit_button',
        width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
        ori=0.0, pos=(0, -.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    Exit = visual.TextStim(win=win, name='Exit',
        text='Exit',
        font='Arial',
        pos=(0, -.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    controller_selection = visual.Rect(
        win=win, name='controller_selection',
        width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
        ori=0.0, pos=(0, -.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    control_feedback = visual.TextStim(win=win, name='control_feedback',
        text='Controller',
        font='Arial',
        pos=(0, -.1), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    # Run 'Begin Experiment' code from code
    # Default control method
    selected_control = "Keyboard"
    
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "MainGame" ---
    dino_image = visual.ImageStim(
        win=win,
        name='dino_image', 
        image='Assets/dino.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    floor1 = visual.Rect(
        win=win, name='floor1',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(-.5,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    floor2 = visual.Rect(
        win=win, name='floor2',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(0,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    meatbone_image = visual.ImageStim(
        win=win,
        name='meatbone_image', 
        image='Assets/meat_bone.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    score_text = visual.TextStim(win=win, name='score_text',
        text='Score: 0',
        font='Arial',
        pos=(0.55, 0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    timer_text = visual.TextStim(win=win, name='timer_text',
        text='00 : 00',
        font='Arial',
        pos=(-0.55,0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    # Run 'Begin Experiment' code from DinoMovement
    from psychopy.hardware import keyboard
    from psychopy.visual import Rect
    import time
    
    import serial
    
    # Initialize the serial connection for PSURP
    #ser = serial.Serial("COM4", 230400, timeout=0.1)  # Replace "COM4" with your port
    #ser.flush()
    #ser.write("X".encode())  # Initialize PSURP
    #ser.write("RUNE\n".encode())  # Enter streaming mode
    
    
    B0ForceInNewtons = 0
    B1ForceInNewtons = 0
    B2ForceInNewtons = 0
    B3ForceInNewtons = 0
    B4ForceInNewtons = 0
    
    # Thresholds for movement
    move_threshold = 2  # Adjust based on PSURP sensitivity
    jump_threshold = 3.0  # Adjust based on PSURP sensitivity
    
    # Initialize the Keyboard
    kb = keyboard.Keyboard()
    
    
    MIN_FORCE = 0.2  # Minimum force to start movement
    FORCE_MULTIPLIER = 0.001  # Adjust this to control how much force affects movement
    
    # Dino movement variables
    dino_pos = [-0.5, -0.3]  # Starting position [x, y]
    dino_speed = 0  # Initial vertical speed
    gravity = -0.00006  # Downward acceleration 0.00006
    jump_speed = 0.005  # Jumping speed
    move_speed = 0.01  # Horizontal movement speed
    ground_offset = 0.03  # Offset to avoid sinking into the ground visually
    min_x = -0.6  # Left boundary
    max_x = 5.3
    respawn_position = [-0.5, -0.3]  # Starting position for Dino
    
    # Get the floor vertices from the Floor Controller
    floor1_vertices = floor1.vertices  # Assuming 'floor' is a Polygon or Rect stimulus
    
    # Calculate the floor's top and fall threshold
    floor_top = max(v[1] for v in floor1_vertices)  # Highest point of the floor
    fall_threshold = min(v[1] for v in floor1_vertices) - 1  # Slightly below the lowest floor point
    
    
    # Function to check if Dino is on the floor
    def is_on_floor(dino_pos):
        """Check if Dino's bottom is within the bounds of floor1 or floor2."""
        dino_bottom = dino_pos[1] - (dino_image.size[1] / 2)  # Dino's bottom Y-position
    
        # Floor1 bounds
        x_min1 = min(v[0] for v in floor1_vertices)
        x_max1 = max(v[0] for v in floor1_vertices)
        
        # Floor2 bounds
        x_min2 = min(v[0] for v in floor2_vertices)
        x_max2 = max(v[0] for v in floor2_vertices)
    
        # Check floor1 or floor2
        on_floor1 = x_min1 <= dino_pos[0] <= x_max1 and dino_bottom <= floor1_top
        on_floor2 = x_min2 <= dino_pos[0] <= x_max2 and dino_bottom <= floor2_top
    
        return on_floor1 or on_floor2
        
        
        
    # Animation-related variables
    frame_paths = [
        "Assets/dino_frames/f1.png", "Assets/dino_frames/f2.png", 
        "Assets/dino_frames/f3.png", "Assets/dino_frames/f4.png", 
        "Assets/dino_frames/f5.png", "Assets/dino_frames/f6.png", 
        "Assets/dino_frames/f7.png", "Assets/dino_frames/f8.png", 
        "Assets/dino_frames/f9.png", "Assets/dino_frames/f10.png", 
        "Assets/dino_frames/f11.png", "Assets/dino_frames/f12.png"
    ]
    
    
    
    frame_index = 0  # Start with the first frame
    frame_index_update_counter = 0  # Counter to manage animation speed
    total_frames = len(frame_paths)  # Total number of frames in the animation
    
    # Initialize the Dino's first frame
    dino_image.image = frame_paths[frame_index]
    
    
    
    
    # Run 'Begin Experiment' code from worldController
    from psychopy.visual import Rect, ImageStim, ShapeStim
    import math
    
    
    
    # Function to calculate vertices of a Rect stimulus
    def calculate_rect_vertices(rect):
        """Calculate the vertices of a Rect stimulus."""
        half_width = rect.width / 2
        half_height = rect.height / 2
        center_x, center_y = rect.pos
        vertices = [
            [center_x - half_width, center_y - half_height],  # Bottom-left
            [center_x + half_width, center_y - half_height],  # Bottom-right
            [center_x + half_width, center_y + half_height],  # Top-right
            [center_x - half_width, center_y + half_height],  # Top-left
        ]
        return vertices
    
    # Camera variables
    camera_offset_x = 0  # Tracks the camera offset to follow Dino
    camera_speed = 0.004  # Adjust this speed as needed
    # Background properties
    background_width = 2.0  # Width of a single background image
    background_height = 1.0
    background_image = 'Assets/7.png'  # Path to your custom background image
    
    # Create two background images for seamless scrolling
    background1 = ImageStim(win, image=background_image, size=[background_width, background_height], pos=[0, 0])
    background2 = ImageStim(win, image=background_image, size=[background_width, background_height], pos=[background_width, 0])
    
    # Floor1 properties
    floor1_height = 0.3
    floor1_width = 0.5
    floor1_pos = [-0.5, -0.5]
    
    floor1 = Rect(
        win=win,
        width=floor1_width,
        height=floor1_height,
        pos=floor1_pos,
        fillColor="black",
        lineColor=None
    )
    floor1_vertices = calculate_rect_vertices(floor1)
    
    # Floor2 properties - Place it further into the map
    floor2_x_static = 5.0  # Fixed X position where floor2 appears
    floor2_height = 0.3
    floor2_width = 0.5
    
    floor2 = Rect(
        win=win,
        width=floor2_width,
        height=floor2_height,
        pos=[floor2_x_static, -0.5],
        fillColor="black",
        lineColor=None
    )
    floor2_vertices = calculate_rect_vertices(floor2)
    
    
    # Floor thresholds
    floor1_top = max(v[1] for v in floor1_vertices)
    floor2_top = max(v[1] for v in floor2_vertices)
    
    
    
    #meat bone
    
    meatbone_size = [0.15, 0.09]  # Example size (width, height)
    meatbone_image.size = meatbone_size
    offset = 0.01  # Adjust to align the meatbone properly with floor2
    
    
    #arc stuff
    
    # Arc properties
    arc1_center = [0.3, 0.0]
    arc1_radius = 0.2
    arc1_start_angle = 0
    arc1_end_angle = 180
    
    # Arc 2 Properties
    arc2_center = [1, -0.1]  # Different position
    arc2_radius = 0.3         # Different radius
    arc2_start_angle = 0
    arc2_end_angle = 180
    
    
    # Arc 3 Properties
    arc3_center = [1.8, 0]  # Position Arc 3 further into the map
    arc3_radius = 0.25         # Choose a radius for Arc 3
    arc3_start_angle = 0
    arc3_end_angle = 180
    
    
    # Generate vertices for Arc 1
    arc1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc1_start_angle + i * (arc1_end_angle - arc1_start_angle) / 50)
        x = arc1_center[0] + arc1_radius * math.cos(angle)
        y = arc1_center[1] + arc1_radius * math.sin(angle)
        arc1_vertices.append((x, y))
    
    # Generate vertices for Arc 2
    arc2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc2_start_angle + i * (arc2_end_angle - arc2_start_angle) / 50)
        x = arc2_center[0] + arc2_radius * math.cos(angle)
        y = arc2_center[1] + arc2_radius * math.sin(angle)
        arc2_vertices.append((x, y))
        
        
    
    # Generate vertices for Arc 3
    arc3_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc3_start_angle + i * (arc3_end_angle - arc3_start_angle) / 50)
        x = arc3_center[0] + arc3_radius * math.cos(angle)
        y = arc3_center[1] + arc3_radius * math.sin(angle)
        arc3_vertices.append((x, y))
    
        
        
    # Create the arc ShapeStim
    arc1 = ShapeStim(
        win=win,
        vertices=arc1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    # Create Arc 2 ShapeStim
    arc2 = ShapeStim(
        win=win,
        vertices=arc2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Different color for clarity
        fillColor=None
    )
    
    
    # Create Arc 3 ShapeStim
    arc3 = ShapeStim(
        win=win,
        vertices=arc3_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    # Run 'Begin Experiment' code from GoalController
    
    meatbone_collided = False  # Track whether the meatbone has been stomped
    score = 0
    arc1_touched_vertices = []
    arc2_touched_vertices = []
    arc3_touched_vertices = []
    
    touch_threshold = 0.05
    
    collision_threshold = 0.1  # You can adjust this to fit your game scale
    # Run 'Begin Experiment' code from Timer
    level_timer = core.Clock()  # Initialize the timer
    time_limit = 120  # Set the time limit in seconds (e.g., 2 minutes)
    
    
    # --- Initialize components for Routine "EndGameScreen" ---
    end_score_text = visual.TextStim(win=win, name='end_score_text',
        text='Score: ',
        font='Arial',
        pos=(0, .2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "resetPSURP" ---
    # create an object to store info about Routine resetPSURP
    resetPSURP = data.Routine(
        name='resetPSURP',
        components=[t_reset_PSURP],
    )
    resetPSURP.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for resetPSURP
    resetPSURP.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    resetPSURP.tStart = globalClock.getTime(format='float')
    resetPSURP.status = STARTED
    thisExp.addData('resetPSURP.started', resetPSURP.tStart)
    resetPSURP.maxDuration = None
    # keep track of which components have finished
    resetPSURPComponents = resetPSURP.components
    for thisComponent in resetPSURP.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resetPSURP" ---
    resetPSURP.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t_reset_PSURP* updates
        
        # if t_reset_PSURP is starting this frame...
        if t_reset_PSURP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t_reset_PSURP.frameNStart = frameN  # exact frame index
            t_reset_PSURP.tStart = t  # local t and not account for scr refresh
            t_reset_PSURP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t_reset_PSURP, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 't_reset_PSURP.started')
            # update status
            t_reset_PSURP.status = STARTED
            t_reset_PSURP.setAutoDraw(True)
        
        # if t_reset_PSURP is active this frame...
        if t_reset_PSURP.status == STARTED:
            # update params
            pass
        
        # if t_reset_PSURP is stopping this frame...
        if t_reset_PSURP.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > t_reset_PSURP.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                t_reset_PSURP.tStop = t  # not accounting for scr refresh
                t_reset_PSURP.tStopRefresh = tThisFlipGlobal  # on global time
                t_reset_PSURP.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_reset_PSURP.stopped')
                # update status
                t_reset_PSURP.status = FINISHED
                t_reset_PSURP.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            resetPSURP.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resetPSURP.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resetPSURP" ---
    for thisComponent in resetPSURP.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for resetPSURP
    resetPSURP.tStop = globalClock.getTime(format='float')
    resetPSURP.tStopRefresh = tThisFlipGlobal
    thisExp.addData('resetPSURP.stopped', resetPSURP.tStop)
    # Run 'End Routine' code from code_2
    #ser.flush()
    #ser.write("X".encode())
    
    # clear out the data from the IO buffers (Fresh commands)
    # the "X" command puts tje PSURP into command mode
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if resetPSURP.maxDurationReached:
        routineTimer.addTime(-resetPSURP.maxDuration)
    elif resetPSURP.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "TARE" ---
    # create an object to store info about Routine TARE
    TARE = data.Routine(
        name='TARE',
        components=[t_tare],
    )
    TARE.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for TARE
    TARE.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TARE.tStart = globalClock.getTime(format='float')
    TARE.status = STARTED
    thisExp.addData('TARE.started', TARE.tStart)
    TARE.maxDuration = None
    # keep track of which components have finished
    TAREComponents = TARE.components
    for thisComponent in TARE.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TARE" ---
    TARE.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t_tare* updates
        
        # if t_tare is starting this frame...
        if t_tare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t_tare.frameNStart = frameN  # exact frame index
            t_tare.tStart = t  # local t and not account for scr refresh
            t_tare.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t_tare, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 't_tare.started')
            # update status
            t_tare.status = STARTED
            t_tare.setAutoDraw(True)
        
        # if t_tare is active this frame...
        if t_tare.status == STARTED:
            # update params
            pass
        
        # if t_tare is stopping this frame...
        if t_tare.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > t_tare.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                t_tare.tStop = t  # not accounting for scr refresh
                t_tare.tStopRefresh = tThisFlipGlobal  # on global time
                t_tare.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 't_tare.stopped')
                # update status
                t_tare.status = FINISHED
                t_tare.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            TARE.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TARE.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TARE" ---
    for thisComponent in TARE.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TARE
    TARE.tStop = globalClock.getTime(format='float')
    TARE.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TARE.stopped', TARE.tStop)
    # Run 'End Routine' code from tare_code
    """
    ser.write("TAR0\n".encode())
    time.sleep(1)
    ser.write("TAR1\n".encode())
    time.sleep(1)
    ser.write("TAR2\n".encode())
    time.sleep(1)
    ser.write("TAR3\n".encode())
    time.sleep(1)
    ser.write("TAR4\n".encode())
    time.sleep(1)
    
    """
    # the tar command zeros out all of the force messurements
    # halt for one second to make sure command was processed 
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if TARE.maxDurationReached:
        routineTimer.addTime(-TARE.maxDuration)
    elif TARE.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "RUNE" ---
    # create an object to store info about Routine RUNE
    RUNE = data.Routine(
        name='RUNE',
        components=[T_RUNE],
    )
    RUNE.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for RUNE
    RUNE.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    RUNE.tStart = globalClock.getTime(format='float')
    RUNE.status = STARTED
    thisExp.addData('RUNE.started', RUNE.tStart)
    RUNE.maxDuration = None
    # keep track of which components have finished
    RUNEComponents = RUNE.components
    for thisComponent in RUNE.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RUNE" ---
    RUNE.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T_RUNE* updates
        
        # if T_RUNE is starting this frame...
        if T_RUNE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T_RUNE.frameNStart = frameN  # exact frame index
            T_RUNE.tStart = t  # local t and not account for scr refresh
            T_RUNE.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T_RUNE, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'T_RUNE.started')
            # update status
            T_RUNE.status = STARTED
            T_RUNE.setAutoDraw(True)
        
        # if T_RUNE is active this frame...
        if T_RUNE.status == STARTED:
            # update params
            pass
        
        # if T_RUNE is stopping this frame...
        if T_RUNE.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > T_RUNE.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                T_RUNE.tStop = t  # not accounting for scr refresh
                T_RUNE.tStopRefresh = tThisFlipGlobal  # on global time
                T_RUNE.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T_RUNE.stopped')
                # update status
                T_RUNE.status = FINISHED
                T_RUNE.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            RUNE.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RUNE.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RUNE" ---
    for thisComponent in RUNE.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for RUNE
    RUNE.tStop = globalClock.getTime(format='float')
    RUNE.tStopRefresh = tThisFlipGlobal
    thisExp.addData('RUNE.stopped', RUNE.tStop)
    # Run 'End Routine' code from Code_RUNE
    #ser.write("RUNE\n".encode())
    
    # the rune command sets the PSURP to streaming mode. (for getting vals)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if RUNE.maxDurationReached:
        routineTimer.addTime(-RUNE.maxDuration)
    elif RUNE.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    GameLoop = data.TrialHandler2(
        name='GameLoop',
        nReps=999.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(GameLoop)  # add the loop to the experiment
    thisGameLoop = GameLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGameLoop.rgb)
    if thisGameLoop != None:
        for paramName in thisGameLoop:
            globals()[paramName] = thisGameLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisGameLoop in GameLoop:
        currentLoop = GameLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisGameLoop.rgb)
        if thisGameLoop != None:
            for paramName in thisGameLoop:
                globals()[paramName] = thisGameLoop[paramName]
        
        # --- Prepare to start Routine "MainMenu" ---
        # create an object to store info about Routine MainMenu
        MainMenu = data.Routine(
            name='MainMenu',
            components=[TitleText, start_button, StartGame, exit_button, Exit, controller_selection, control_feedback, mouse],
        )
        MainMenu.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        # Update the feedback text to display the currently selected control method
        control_feedback.text = f"Selected Control: {selected_control}"
        
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
        # store start times for MainMenu
        MainMenu.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        MainMenu.tStart = globalClock.getTime(format='float')
        MainMenu.status = STARTED
        thisExp.addData('MainMenu.started', MainMenu.tStart)
        MainMenu.maxDuration = None
        # keep track of which components have finished
        MainMenuComponents = MainMenu.components
        for thisComponent in MainMenu.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "MainMenu" ---
        # if trial has changed, end Routine now
        if isinstance(GameLoop, data.TrialHandler2) and thisGameLoop.thisN != GameLoop.thisTrial.thisN:
            continueRoutine = False
        MainMenu.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TitleText* updates
            
            # if TitleText is starting this frame...
            if TitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TitleText.frameNStart = frameN  # exact frame index
                TitleText.tStart = t  # local t and not account for scr refresh
                TitleText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TitleText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TitleText.started')
                # update status
                TitleText.status = STARTED
                TitleText.setAutoDraw(True)
            
            # if TitleText is active this frame...
            if TitleText.status == STARTED:
                # update params
                pass
            
            # *start_button* updates
            
            # if start_button is starting this frame...
            if start_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_button.frameNStart = frameN  # exact frame index
                start_button.tStart = t  # local t and not account for scr refresh
                start_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'start_button.started')
                # update status
                start_button.status = STARTED
                start_button.setAutoDraw(True)
            
            # if start_button is active this frame...
            if start_button.status == STARTED:
                # update params
                pass
            
            # *StartGame* updates
            
            # if StartGame is starting this frame...
            if StartGame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                StartGame.frameNStart = frameN  # exact frame index
                StartGame.tStart = t  # local t and not account for scr refresh
                StartGame.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(StartGame, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StartGame.started')
                # update status
                StartGame.status = STARTED
                StartGame.setAutoDraw(True)
            
            # if StartGame is active this frame...
            if StartGame.status == STARTED:
                # update params
                pass
            
            # *exit_button* updates
            
            # if exit_button is starting this frame...
            if exit_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                exit_button.frameNStart = frameN  # exact frame index
                exit_button.tStart = t  # local t and not account for scr refresh
                exit_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(exit_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exit_button.started')
                # update status
                exit_button.status = STARTED
                exit_button.setAutoDraw(True)
            
            # if exit_button is active this frame...
            if exit_button.status == STARTED:
                # update params
                pass
            
            # *Exit* updates
            
            # if Exit is starting this frame...
            if Exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Exit.frameNStart = frameN  # exact frame index
                Exit.tStart = t  # local t and not account for scr refresh
                Exit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Exit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Exit.started')
                # update status
                Exit.status = STARTED
                Exit.setAutoDraw(True)
            
            # if Exit is active this frame...
            if Exit.status == STARTED:
                # update params
                pass
            
            # *controller_selection* updates
            
            # if controller_selection is starting this frame...
            if controller_selection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                controller_selection.frameNStart = frameN  # exact frame index
                controller_selection.tStart = t  # local t and not account for scr refresh
                controller_selection.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(controller_selection, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'controller_selection.started')
                # update status
                controller_selection.status = STARTED
                controller_selection.setAutoDraw(True)
            
            # if controller_selection is active this frame...
            if controller_selection.status == STARTED:
                # update params
                pass
            
            # *control_feedback* updates
            
            # if control_feedback is starting this frame...
            if control_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                control_feedback.frameNStart = frameN  # exact frame index
                control_feedback.tStart = t  # local t and not account for scr refresh
                control_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(control_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'control_feedback.started')
                # update status
                control_feedback.status = STARTED
                control_feedback.setAutoDraw(True)
            
            # if control_feedback is active this frame...
            if control_feedback.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code
            # Check if the mouse is clicked and which button is clicked
            if mouse.isPressedIn(start_button):  # Start button
                continueRoutine = False  # End the Main Menu routine
            
            if mouse.isPressedIn(exit_button):  # Exit button
                core.quit()  # Quit the experiment
                
            if mouse.isPressedIn(controller_selection):
                # Add a delay to prevent rapid toggling (debounce)
                core.wait(0.2)
                
                # Toggle between "Keyboard" and "PSURP"
                if selected_control == "Keyboard":
                    selected_control = "PSURP"
                    ser.flush()
                else:
                    selected_control = "Keyboard"
                
                # Update the feedback text
                control_feedback.text = f"Selected Control: {selected_control}"
            
            
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                MainMenu.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MainMenu.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "MainMenu" ---
        for thisComponent in MainMenu.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for MainMenu
        MainMenu.tStop = globalClock.getTime(format='float')
        MainMenu.tStopRefresh = tThisFlipGlobal
        thisExp.addData('MainMenu.stopped', MainMenu.tStop)
        # store data for GameLoop (TrialHandler)
        GameLoop.addData('mouse.x', mouse.x)
        GameLoop.addData('mouse.y', mouse.y)
        GameLoop.addData('mouse.leftButton', mouse.leftButton)
        GameLoop.addData('mouse.midButton', mouse.midButton)
        GameLoop.addData('mouse.rightButton', mouse.rightButton)
        GameLoop.addData('mouse.time', mouse.time)
        # the Routine "MainMenu" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "MainGame" ---
        # create an object to store info about Routine MainGame
        MainGame = data.Routine(
            name='MainGame',
            components=[dino_image, floor1, floor2, meatbone_image, score_text, timer_text],
        )
        MainGame.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from DinoMovement
        dino_pos = [-0.5, -0.3]  # Reset Dino's position
        dino_speed = 0  # Reset vertical speed
        
        # Run 'Begin Routine' code from worldController
        camera_offset_x = 0
        # Run 'Begin Routine' code from GoalController
        score = 0  # Reset the score
        arc1_touched_vertices = []
        arc2_touched_vertices = []
        arc3_touched_vertices = []
        meatbone_collided = False
        # Run 'Begin Routine' code from Timer
        
        level_timer.reset()  # Reset the timer at the start of the MainGame routine
        
        
        # store start times for MainGame
        MainGame.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        MainGame.tStart = globalClock.getTime(format='float')
        MainGame.status = STARTED
        thisExp.addData('MainGame.started', MainGame.tStart)
        MainGame.maxDuration = None
        # keep track of which components have finished
        MainGameComponents = MainGame.components
        for thisComponent in MainGame.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "MainGame" ---
        # if trial has changed, end Routine now
        if isinstance(GameLoop, data.TrialHandler2) and thisGameLoop.thisN != GameLoop.thisTrial.thisN:
            continueRoutine = False
        MainGame.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *dino_image* updates
            
            # if dino_image is starting this frame...
            if dino_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dino_image.frameNStart = frameN  # exact frame index
                dino_image.tStart = t  # local t and not account for scr refresh
                dino_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dino_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dino_image.started')
                # update status
                dino_image.status = STARTED
                dino_image.setAutoDraw(True)
            
            # if dino_image is active this frame...
            if dino_image.status == STARTED:
                # update params
                pass
            
            # *floor1* updates
            
            # if floor1 is starting this frame...
            if floor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                floor1.frameNStart = frameN  # exact frame index
                floor1.tStart = t  # local t and not account for scr refresh
                floor1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(floor1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'floor1.started')
                # update status
                floor1.status = STARTED
                floor1.setAutoDraw(True)
            
            # if floor1 is active this frame...
            if floor1.status == STARTED:
                # update params
                pass
            
            # *floor2* updates
            
            # if floor2 is starting this frame...
            if floor2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                floor2.frameNStart = frameN  # exact frame index
                floor2.tStart = t  # local t and not account for scr refresh
                floor2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(floor2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'floor2.started')
                # update status
                floor2.status = STARTED
                floor2.setAutoDraw(True)
            
            # if floor2 is active this frame...
            if floor2.status == STARTED:
                # update params
                pass
            
            # *meatbone_image* updates
            
            # if meatbone_image is starting this frame...
            if meatbone_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                meatbone_image.frameNStart = frameN  # exact frame index
                meatbone_image.tStart = t  # local t and not account for scr refresh
                meatbone_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(meatbone_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'meatbone_image.started')
                # update status
                meatbone_image.status = STARTED
                meatbone_image.setAutoDraw(True)
            
            # if meatbone_image is active this frame...
            if meatbone_image.status == STARTED:
                # update params
                pass
            
            # *score_text* updates
            
            # if score_text is starting this frame...
            if score_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                score_text.frameNStart = frameN  # exact frame index
                score_text.tStart = t  # local t and not account for scr refresh
                score_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(score_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'score_text.started')
                # update status
                score_text.status = STARTED
                score_text.setAutoDraw(True)
            
            # if score_text is active this frame...
            if score_text.status == STARTED:
                # update params
                pass
            
            # *timer_text* updates
            
            # if timer_text is starting this frame...
            if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_text.frameNStart = frameN  # exact frame index
                timer_text.tStart = t  # local t and not account for scr refresh
                timer_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timer_text.started')
                # update status
                timer_text.status = STARTED
                timer_text.setAutoDraw(True)
            
            # if timer_text is active this frame...
            if timer_text.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from DinoMovement
            
            # Initialize key state flags
            left_pressed = False
            right_pressed = False
            up_pressed = False
            
            # Handle input based on the selected control method
            if selected_control == "Keyboard":
                # Process keyboard input
                keys_pressed = kb.getKeys(['left', 'right', 'up'], waitRelease=False, clear=False)
                for key in keys_pressed:
                    if key.name == 'left':
                        left_pressed = True
                    if key.name == 'right':
                        right_pressed = True
                    if key.name == 'up':
                        up_pressed = True
                        
                        
            if selected_control == "PSURP":
                # Read serial data
                ser.flushInput()
                strSerialData = ser.readline()
                if len(strSerialData.decode()) == 12:
                    output = strSerialData.decode()
                    
                    # Calculate forces
                    B0HighByte = Base71Lookup.index(output[0])
                    B0LowByte = Base71Lookup.index(output[1])
                    B1HighByte = Base71Lookup.index(output[2])
                    B1LowByte = Base71Lookup.index(output[3])
                    B2HighByte = Base71Lookup.index(output[4])
                    B2LowByte = Base71Lookup.index(output[5])
                    
                    # Calculate forces in Newtons
                    B0ForceInNewtons = ((B0HighByte * 71) + B0LowByte) * 0.0098
                    B1ForceInNewtons = ((B1HighByte * 71) + B1LowByte) * 0.0098
                    B2ForceInNewtons = ((B2HighByte * 71) + B2LowByte) * 0.0098
                    
                    # Apply forces directly to movement
                    if B0ForceInNewtons > MIN_FORCE:
                        dino_speed = B0ForceInNewtons * FORCE_MULTIPLIER  # Jump height based on force
                        
                    if B1ForceInNewtons > MIN_FORCE and dino_pos[0] > min_x:
                        move_amount = B1ForceInNewtons * FORCE_MULTIPLIER
                        dino_pos[0] -= move_amount  # Left movement based on force
                        dino_image.size = [-1 * abs(dino_image.size[0]), dino_image.size[1]]
                        
                    if B2ForceInNewtons > MIN_FORCE and dino_pos[0] < max_x:
                        move_amount = B2ForceInNewtons * FORCE_MULTIPLIER
                        dino_pos[0] += move_amount  # Right movement based on force
                        dino_image.size = [abs(dino_image.size[0]), dino_image.size[1]]
            
            
                        
             
            # Apply gravity to Dino's vertical speed
            dino_speed += gravity
            
            # Check if Dino is on the floor
            if is_on_floor(dino_pos) and dino_speed <= 0:  # Falling or stationary
                dino_pos[1] = floor1_top + (dino_image.size[1] / 2) - ground_offset  # Align Dino with the floor
                dino_speed = 0  # Reset vertical speed
            
            # Respawn if Dino falls below the floor threshold
            if dino_pos[1] < fall_threshold:
                continueRoutine = False  # Stop the MainGame routine
                
            # Jumping logic: Allow jump whenever the 'up' key is pressed
            if up_pressed:  # Check if the up key is pressed
                dino_speed = jump_speed  # Apply upward movement
            
            # Update Dino's vertical position
            dino_pos[1] += dino_speed
            
            # Continuous horizontal movement
            if left_pressed and dino_pos[0] > min_x:
                dino_pos[0] -= move_speed  # Move Dino to the left
                dino_image.size = [-1 * abs(dino_image.size[0]), dino_image.size[1]]
            
            if right_pressed and dino_pos[0] < max_x:
                dino_pos[0] += move_speed  # Move Dino to the right
                dino_image.size = [abs(dino_image.size[0]), dino_image.size[1]]  # Reset Dino to face right
            
            # Update Dino's position
            # dino_image.pos = dino_pos  # Use both X and Y values of dino_pos
            dino_image.pos = [dino_pos[0] - camera_offset_x, dino_pos[1]]
            
            
            
            keys_pressed = kb.getKeys(['o'], waitRelease=False, clear=False)
            if 'o' in [key.name for key in keys_pressed]:
                print(f"Dino Position: X = {dino_pos[0]:.3f}, Y = {dino_pos[1]:.3f}")
                print(f"Meatbone Position: {meatbone_x, meatbone_y}")
                
                
                
            
            # Update the Dino's animation
            if (frame_index_update_counter % 4) == 0:  # Adjust 4 to control animation speed
                dino_image.image = frame_paths[frame_index]  # Update the current frame
            
                # Advance to the next frame
                frame_index += 1
                if frame_index >= total_frames:
                    frame_index = 0  # Loop back to the first frame
            
            
            
            # Increment the animation frame counter
            frame_index_update_counter += 1
            
            
            # Run 'Each Frame' code from worldController
            # Get Dino's position from your Dino movement code
            # Assume dino_pos[0] tracks Dino's X position (horizontal movement)
            
            # Update the camera offset based on Dino's X position
            camera_offset_x += camera_speed  # The camera offset follows Dino's position
            
            # Move backgrounds relative to Dino's position (seamless wrap-around)
            background1.pos = [-(camera_offset_x % background_width), 0]
            background2.pos = [background1.pos[0] + background_width, 0]
            
            # Update floor positions relative to Dino's position
            floor1.pos = [floor1_pos[0] - camera_offset_x, floor1.pos[1]]
            floor2.pos = [floor2_x_static - camera_offset_x, floor2.pos[1]]  # Floor2 moves with Dino
            
            
            # Update meatbone position to match floor2's top
            meatbone_x = floor2.pos[0]  # Update X position based on floor2
            meatbone_y = floor2_top + (meatbone_size[1] / 2) - offset  # Keep the meatbone on top of floor2
            meatbone_image.pos = [meatbone_x, meatbone_y]
            
            
            # Update the arc position relative to the camera offset
            # Update Arc 1 Position
            arc1.pos = [arc1_center[0] - camera_offset_x, arc1_center[1]]
            
            # Update Arc 2 Position
            arc2.pos = [arc2_center[0] - camera_offset_x, arc2_center[1]]
            
            arc3.pos = [arc3_center[0] - camera_offset_x, arc3_center[1]]
            
            # Draw the backgrounds and floors
            background1.draw()
            background2.draw()
            floor1.draw()
            floor2.draw()
            arc1.draw()
            arc2.draw()
            arc3.draw()
            
            # Run 'Each Frame' code from GoalController
            dino_relative_x = dino_pos[0] - camera_offset_x
            dino_relative_y = dino_pos[1]
            # Check for collision based on proximity to the updated position
            dx = dino_relative_x - meatbone_x
            dy = dino_relative_y - meatbone_y
            
            # Define a collision threshold (adjust based on the visual scale of your game)
            # Check for collision
            if not meatbone_collided and (dx ** 2 + dy ** 2) ** 0.5 <= collision_threshold:
                print("Dino ate the meatbone!")
                meatbone_image.opacity = 0  # Make the meatbone disappear
                meatbone_collided = True  # Prevent further collision checks
                #continueRoutine = False
            
            for vertex in arc1_vertices:
                # Adjust Arc 1 vertex for its X-offset (+1)
                adjusted_vertex_x = vertex[0] + 0.3  # Move Arc 1 vertices by 1 unit to the right
                adjusted_vertex_y = vertex[1] # Y remains unchanged, apply the same adjustment as Arc 2 if needed
            
                # Calculate distance between Dino and the adjusted vertex of Arc 1
                distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                # Check if Dino is close enough to "touch" the adjusted vertex
                if distance <= touch_threshold and vertex not in arc1_touched_vertices:
                    arc1_touched_vertices.append(vertex)
                    score += 1  # Increment the score for Arc 1
            
            
            for vertex in arc2_vertices:
                # Adjust Arc 2 vertex for its X-offset (+2)
                adjusted_vertex_x = vertex[0] + 1  # Move Arc 2 vertices by 2 units to the right
                adjusted_vertex_y = vertex[1] - 0.1 # Y remains unchanged
                
                # Calculate distance between Dino and the adjusted vertex of Arc 2
                distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                # Check if Dino is close enough to "touch" the adjusted vertex
                if distance <= touch_threshold and vertex not in arc2_touched_vertices:
                    arc2_touched_vertices.append(vertex)
                    score += 1  # Increment the score for Arc 2
                    
                    
            for vertex in arc3_vertices:
                # Adjust Arc 3 vertex for its static X-offset
                adjusted_vertex_x = vertex[0] + 1.8  # Offset Arc 3 vertices by 3.5 units to the right
                adjusted_vertex_y = vertex[1]  # Offset Arc 3 vertices by -0.2 units vertically
            
                # Calculate distance between Dino and the adjusted vertex of Arc 3
                distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
            
                # Check if Dino is close enough to "touch" the adjusted vertex
                if distance <= touch_threshold and vertex not in arc3_touched_vertices:
                    arc3_touched_vertices.append(vertex)
                    score += 1  # Increment the score for Arc 3
                        
            score_text.text = str(score)
            
            
            
            # Run 'Each Frame' code from Timer
            # Calculate remaining time
            time_remaining = time_limit - level_timer.getTime()
            
            # Check if time is up
            if time_remaining <= 0:
                print("Time's up! Returning to MainMenu.")
                continueRoutine = False  # End the MainGame routine
                time_remaining = 0  # Prevent negative time display
            
            # Format the timer as MM:SS
            minutes = int(time_remaining) // 60
            seconds = int(time_remaining) % 60
            
            # Update the timer display (assumes a Text Component named 'timer_text')
            timer_text.text = str(f"{minutes}:{seconds:02d}")
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                MainGame.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MainGame.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "MainGame" ---
        for thisComponent in MainGame.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for MainGame
        MainGame.tStop = globalClock.getTime(format='float')
        MainGame.tStopRefresh = tThisFlipGlobal
        thisExp.addData('MainGame.stopped', MainGame.tStop)
        # Run 'End Routine' code from DinoMovement
        dino_pos = [-0.5, -0.3]  # Reset Dino's position
        # Run 'End Routine' code from GoalController
        global total_touched_vertices, total_possible_vertices
        total_touched_vertices = len(arc1_touched_vertices) + len(arc2_touched_vertices) + len(arc3_touched_vertices)
        total_possible_vertices = len(arc1_vertices) + len(arc2_vertices) + len(arc3_vertices)
        
        # the Routine "MainGame" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "EndGameScreen" ---
        # create an object to store info about Routine EndGameScreen
        EndGameScreen = data.Routine(
            name='EndGameScreen',
            components=[end_score_text],
        )
        EndGameScreen.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        
        # Calculate the percentage
        if total_possible_vertices > 0:
            percentage = (total_touched_vertices / total_possible_vertices) * 100
        else:
            percentage = 0  # Avoid division by zero
        
        # Update the text for the end screen
        end_score_text.text = (
            f"You hit {total_touched_vertices} out of {total_possible_vertices} vertices!\n"
            f"That's {percentage:.2f}%!"
        )
        
        # store start times for EndGameScreen
        EndGameScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EndGameScreen.tStart = globalClock.getTime(format='float')
        EndGameScreen.status = STARTED
        thisExp.addData('EndGameScreen.started', EndGameScreen.tStart)
        EndGameScreen.maxDuration = None
        # keep track of which components have finished
        EndGameScreenComponents = EndGameScreen.components
        for thisComponent in EndGameScreen.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EndGameScreen" ---
        # if trial has changed, end Routine now
        if isinstance(GameLoop, data.TrialHandler2) and thisGameLoop.thisN != GameLoop.thisTrial.thisN:
            continueRoutine = False
        EndGameScreen.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *end_score_text* updates
            
            # if end_score_text is starting this frame...
            if end_score_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_score_text.frameNStart = frameN  # exact frame index
                end_score_text.tStart = t  # local t and not account for scr refresh
                end_score_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_score_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_score_text.started')
                # update status
                end_score_text.status = STARTED
                end_score_text.setAutoDraw(True)
            
            # if end_score_text is active this frame...
            if end_score_text.status == STARTED:
                # update params
                pass
            
            # if end_score_text is stopping this frame...
            if end_score_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > end_score_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    end_score_text.tStop = t  # not accounting for scr refresh
                    end_score_text.tStopRefresh = tThisFlipGlobal  # on global time
                    end_score_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'end_score_text.stopped')
                    # update status
                    end_score_text.status = FINISHED
                    end_score_text.setAutoDraw(False)
            # Run 'Each Frame' code from code_3
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EndGameScreen.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndGameScreen.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EndGameScreen" ---
        for thisComponent in EndGameScreen.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EndGameScreen
        EndGameScreen.tStop = globalClock.getTime(format='float')
        EndGameScreen.tStopRefresh = tThisFlipGlobal
        thisExp.addData('EndGameScreen.stopped', EndGameScreen.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if EndGameScreen.maxDurationReached:
            routineTimer.addTime(-EndGameScreen.maxDuration)
        elif EndGameScreen.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'GameLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # Run 'End Experiment' code from DinoMovement
    #ser.flush()
    #ser.write("X".encode())  # Exit command mode
    #ser.close()
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
