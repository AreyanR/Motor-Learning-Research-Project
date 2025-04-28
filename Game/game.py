#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on April 27, 2025, at 20:54
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

# Run 'Before Experiment' code from DinoMovement_L1
Base71Lookup = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# Run 'Before Experiment' code from DinoMovement_L2
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
        originPath='D:\\Users\\areya\\Desktop\\work\\Motor-Learning-Research-Project\\Game\\game.py',
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
    # create speaker 'lose_sound_L1'
    deviceManager.addDevice(
        deviceName='lose_sound_L1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'eat_sound_L1'
    deviceManager.addDevice(
        deviceName='eat_sound_L1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'win_sound_L1'
    deviceManager.addDevice(
        deviceName='win_sound_L1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'fail_sound_L1'
    deviceManager.addDevice(
        deviceName='fail_sound_L1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'lose_sound_L2'
    deviceManager.addDevice(
        deviceName='lose_sound_L2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'eat_sound_L2'
    deviceManager.addDevice(
        deviceName='eat_sound_L2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'win_sound_L2'
    deviceManager.addDevice(
        deviceName='win_sound_L2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'fail_sound_L2'
    deviceManager.addDevice(
        deviceName='fail_sound_L2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
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
        ori=0.0, pos=(0, -.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    Exit = visual.TextStim(win=win, name='Exit',
        text='Exit',
        font='Arial',
        pos=(0, -.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
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
    mode_feedback = visual.TextStim(win=win, name='mode_feedback',
        text='Mode: ',
        font='Arial',
        pos=(0, -.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    mode_button = visual.Rect(
        win=win, name='mode_button',
        width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
        ori=0.0, pos=(0, -.2), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    # Run 'Begin Experiment' code from code
    # Default control method
    # starts game in keyboard mode
    selected_control = "Keyboard"
    selected_diff = "1"
    thisExp.savePickle = False
    thisExp.saveWideText = False  # stops saving the .csv or .tsv file
    
    win_threshold = 10  # Percentage needed to win
    
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Level_1" ---
    dino_image_L1 = visual.ImageStim(
        win=win,
        name='dino_image_L1', 
        image='Assets/dino.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    floor1_L1 = visual.Rect(
        win=win, name='floor1_L1',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(-.5,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    floor2_L1 = visual.Rect(
        win=win, name='floor2_L1',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(0,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    meatbone_image_L1 = visual.ImageStim(
        win=win,
        name='meatbone_image_L1', 
        image='Assets/meat_bone.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    score_text_L1 = visual.TextStim(win=win, name='score_text_L1',
        text='Score: 0',
        font='Arial',
        pos=(0.55, 0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    timer_text_L1 = visual.TextStim(win=win, name='timer_text_L1',
        text='00 : 00',
        font='Arial',
        pos=(-0.55,0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    # Run 'Begin Experiment' code from DinoMovement_L1
    from psychopy.hardware import keyboard
    from psychopy.visual import Rect
    import time
    
    import serial
    from psychopy.visual import Circle
    
    # Initialize the Keyboard
    kb = keyboard.Keyboard()
    
    #PSURP Inits
    """
    # Initialize the serial connection for PSURP
    ser = serial.Serial("COM4", 230400, timeout=0.1)  # Replace "COM4" with your port
    ser.flush()
    ser.write("X".encode())  # Initialize PSURP
    ser.write("RUNE\n".encode())  # Enter streaming mode
    """
    
    # Trail settings
    trail_positions = []  # Stores Dino's previous positions
    trail_length = 35  # Maximum number of trail dots
    trail_dot_size = 0.005  # Size of each dot for trail 
    trail_dots = []  # List of Circle stimuli for the trail
    trail_color = 'yellow'  # Color of the trail dots
    trail_frame_counter = 0  # Counter to control trail dot spawning
    trail_interval = 5  # Spawn a dot every 5 frames
    
    
    #Button 0 and button 2 force properties
    B0ForceInNewtons = 0
    B2ForceInNewtons = 0
    MIN_FORCE = 0.4  # Minimum force to start movement
    FORCE_MULTIPLIER = 0.001  # Adjust this to control how much force affects movement
    
    # Dino movement variables
    dino_pos = [0, -0.3]  # Starting position [x, y]
    dino_speed = 0  # Initial vertical speed
    gravity = -0.0003  # Downward acceleration 0.00006
    jump_speed = 0.005  # Jumping speed
    move_speed = 0.01  # Horizontal movement speed
    ground_offset = 0.03  # Offset to avoid sinking into the ground visually
    min_x = -0.6  # Left boundary
    max_x = 19 # right boundary
    respawn_position = [0, -0.3]  # Starting position for Dino
    
    
    
    # Floor properties
    
    floor1_vertices = floor1_L1.vertices  # Get floor1_L1 vertices
    floor_top = max(v[1] for v in floor1_vertices)  # Highest point of floor1_L1
    fall_threshold = min(v[1] for v in floor1_vertices) - 0.2  # Slightly below the lowest floor point
    
    
    # Function to check if Dino is on the floor
    def is_on_floor(dino_pos):
        """Check if Dino's bottom is within the bounds of floor1_L1 or floor2_L1."""
        dino_bottom = dino_pos[1] - (dino_image_L1.size[1] / 2)  # Dino's bottom Y-position
    
        # floor1_L1 bounds
        x_min1 = min(v[0] for v in floor1_vertices)
        x_max1 = max(v[0] for v in floor1_vertices)
        
        # floor2_L1 bounds
        x_min2 = min(v[0] for v in floor2_vertices)
        x_max2 = max(v[0] for v in floor2_vertices)
    
        # Check floor1_L1 or floor2_L1
        on_floor1 = x_min1 <= dino_pos[0] <= x_max1 and dino_bottom <= floor1_top
        on_floor2 = x_min2 <= dino_pos[0] <= x_max2 and dino_bottom <= floor2_top
    
        return on_floor1 or on_floor2
        
    #calculates the psurp forces
    def calculate_psurp_forces(serial_data):
        """Extract and calculate forces from PSURP serial data."""
        if len(serial_data.decode()) == 12:
            output = serial_data.decode()
            
            # Calculate forces
            B0HighByte = Base71Lookup.index(output[0])
            B0LowByte = Base71Lookup.index(output[1])
            B2HighByte = Base71Lookup.index(output[4])
            B2LowByte = Base71Lookup.index(output[5])
            
            # Forces in Newtons
            B0ForceInNewtons = ((B0HighByte * 71) + B0LowByte) * 0.0098
            B2ForceInNewtons = ((B2HighByte * 71) + B2LowByte) * 0.0098
            
            return B0ForceInNewtons, B2ForceInNewtons
        
        return 0, 0  # Default forces if data is invalid
    
    
    
    # image path for dino animation
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
    dino_image_L1.image = frame_paths[frame_index]
    
    
    
    
    # Run 'Begin Experiment' code from worldController_L1
    from psychopy.visual import Rect, ImageStim, ShapeStim
    import math
    
    dirt_texture = 'Assets/ground1.png'
    
    #height factors for arcs (Y position)
    low_arc = -0.2  
    reg_arc = 0
    high_arc = 0.05
    
    small_arc_size = 0.2  # Smallest arc radius
    med_arc_size = 0.27  # Medium arc radius
    large_arc_size = 0.35  # Largest arc radius
    
    wiggle_thickness = 0.05  # Adjust thickness for all wiggle arcs
    
    meatbone_size = [0.15, 0.09]  # Example size (width, height)
    
    
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
    camera_speed = 0.003  # Adjust this speed as needed 0.003
    # Background properties
    background_width = 2.0  # Width of a single background image
    background_height = 1.0
    background_image_L1 = 'Assets/7.png'  # Path to your custom background image
    
    # Create two background images for seamless scrolling
    background1_L1 = ImageStim(win, image=background_image_L1, size=[background_width, background_height], pos=[0, 0])
    background2_L1 = ImageStim(win, image=background_image_L1, size=[background_width, background_height], pos=[background_width, 0])
    
    # floor1_L1 properties
    floor1_height = 0.3
    floor1_width = 0.5
    floor1_pos = [0, -0.5]
    
    floor1_L1 = visual.ImageStim(
        win=win,
        image=dirt_texture,
        size=(floor1_width, floor1_height),  # Set the size to match the floor dimensions
        pos=floor1_pos,
        interpolate=True
    )
    floor1_vertices = calculate_rect_vertices(floor1_L1)
    
    # floor2_L1 properties - Place it further into the map
    floor2_x_static = 1  # Fixed X position where floor2_L1 appears18.5
    floor2_height = 0.3
    floor2_width = 0.5
    
    floor2_L1 = visual.ImageStim(
        win=win,
        image=dirt_texture,
        size=(floor2_width, floor2_height),  # Set the size to match the floor dimensions
        pos=[floor2_x_static, -0.5],  # Position of floor2_L1
        interpolate=True
    )
    floor2_vertices = calculate_rect_vertices(floor2_L1)
    
    
    # Floor thresholds
    floor1_top = max(v[1] for v in floor1_vertices)
    floor2_top = max(v[1] for v in floor2_vertices)
    
    
    
    #meat bone
    
    meatbone_size = [0.12, 0.06]  # Example size (width, height)
    meatbone_image_L1.size = meatbone_size
    offset = 0.01  # Adjust to align the meatbone properly with floor2_L1
    
    
    #arc stuff
    
    # Arc 1 Properties
    arc1_L1_x = 0.3
    arc1_L1_center = [arc1_L1_x, reg_arc]
    arc1_L1_radius = small_arc_size
    arc1_L1_start_angle = 0
    arc1_L1_end_angle = 180
    
    # Arc 2 Properties
    arc2_L1_x = 1.0
    arc2_L1_center = [arc2_L1_x, low_arc]
    arc2_L1_radius = med_arc_size
    arc2_L1_start_angle = 0
    arc2_L1_end_angle = 180
    
    # Arc 3 Properties
    arc3_L1_x = 2.2
    arc3_L1_center = [arc3_L1_x, high_arc]
    arc3_L1_radius = large_arc_size
    arc3_L1_start_angle = 0
    arc3_L1_end_angle = 180
    
    # Arc 4 Properties
    arc4_L1_x = 3.4
    arc4_L1_center = [arc4_L1_x, low_arc]
    arc4_L1_radius = small_arc_size
    arc4_L1_start_angle = 0
    arc4_L1_end_angle = 180
    
    # Arc 5 Properties
    arc5_L1_x = 4.6
    arc5_L1_center = [arc5_L1_x, reg_arc]
    arc5_L1_radius = large_arc_size
    arc5_L1_start_angle = 0
    arc5_L1_end_angle = 180
    
    # Arc 6 Properties
    arc6_L1_x = 5.8
    arc6_L1_center = [arc6_L1_x, high_arc]
    arc6_L1_radius = med_arc_size
    arc6_L1_start_angle = 0
    arc6_L1_end_angle = 180
    
    # Arc 7 Properties
    arc7_L1_x = 7.0
    arc7_L1_center = [arc7_L1_x, low_arc]
    arc7_L1_radius = large_arc_size
    arc7_L1_start_angle = 0
    arc7_L1_end_angle = 180
    
    # Arc 8 Properties
    arc8_L1_x = 8.5
    arc8_L1_center = [arc8_L1_x, high_arc]
    arc8_L1_radius = med_arc_size
    arc8_L1_start_angle = 0
    arc8_L1_end_angle = 180
    
    
    
    
    # Generate vertices for Arc 1
    arc1_L1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc1_L1_start_angle + i * (arc1_L1_end_angle - arc1_L1_start_angle) / 50)
        x = arc1_L1_center[0] + arc1_L1_radius * math.cos(angle)
        y = arc1_L1_center[1] + arc1_L1_radius * math.sin(angle)
        arc1_L1_vertices.append((x, y))
    
    # Generate vertices for Arc 2
    arc2_L1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc2_L1_start_angle + i * (arc2_L1_end_angle - arc2_L1_start_angle) / 50)
        x = arc2_L1_center[0] + arc2_L1_radius * math.cos(angle)
        y = arc2_L1_center[1] + arc2_L1_radius * math.sin(angle)
        arc2_L1_vertices.append((x, y))
        
        
    
    # Generate vertices for Arc 3
    arc3_L1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc3_L1_start_angle + i * (arc3_L1_end_angle - arc3_L1_start_angle) / 50)
        x = arc3_L1_center[0] + arc3_L1_radius * math.cos(angle)
        y = arc3_L1_center[1] + arc3_L1_radius * math.sin(angle)
        arc3_L1_vertices.append((x, y))
    
    # Generate vertices for Arc 4
    arc4_L1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc4_L1_start_angle + i * (arc4_L1_end_angle - arc4_L1_start_angle) / 50)
        x = arc4_L1_center[0] + arc4_L1_radius * math.cos(angle)
        y = arc4_L1_center[1] + arc4_L1_radius * math.sin(angle)
        arc4_L1_vertices.append((x, y))
    
    
    # Generate vertices for Arc 5
    arc5_L1_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc5_L1_start_angle + i * (arc5_L1_end_angle - arc5_L1_start_angle) / 50)
        x = arc5_L1_center[0] + arc5_L1_radius * math.cos(angle)
        y = arc5_L1_center[1] + arc5_L1_radius * math.sin(angle)
        arc5_L1_vertices.append((x, y))
        
    
    arc6_L1_vertices = []
    for i in range(51):
        angle = math.radians(arc6_L1_start_angle + i * (arc6_L1_end_angle - arc6_L1_start_angle) / 50)
        x = arc6_L1_center[0] + arc6_L1_radius * math.cos(angle)
        y = arc6_L1_center[1] + arc6_L1_radius * math.sin(angle)
        arc6_L1_vertices.append((x, y))
    
    # Arc 7 vertices
    arc7_L1_vertices = []
    for i in range(51):
        angle = math.radians(arc7_L1_start_angle + i * (arc7_L1_end_angle - arc7_L1_start_angle) / 50)
        x = arc7_L1_center[0] + arc7_L1_radius * math.cos(angle)
        y = arc7_L1_center[1] + arc7_L1_radius * math.sin(angle)
        arc7_L1_vertices.append((x, y))
    
    # Arc 8 vertices
    arc8_L1_vertices = []
    for i in range(51):
        angle = math.radians(arc8_L1_start_angle + i * (arc8_L1_end_angle - arc8_L1_start_angle) / 50)
        x = arc8_L1_center[0] + arc8_L1_radius * math.cos(angle)
        y = arc8_L1_center[1] + arc8_L1_radius * math.sin(angle)
        arc8_L1_vertices.append((x, y))
        
    # Create the arc ShapeStim
    arc1_L1 = ShapeStim(
        win=win,
        vertices=arc1_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    # Create Arc 2 ShapeStim
    arc2_L1 = ShapeStim(
        win=win,
        vertices=arc2_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Different color for clarity
        fillColor=None
    )
    
    
    # Create Arc 3 ShapeStim
    arc3_L1 = ShapeStim(
        win=win,
        vertices=arc3_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    # Create Arc 4 ShapeStim
    arc4_L1 = ShapeStim(
        win=win,
        vertices=arc4_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    # Create Arc 5 ShapeStim
    arc5_L1 = ShapeStim(
        win=win,
        vertices=arc5_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    arc6_L1 = ShapeStim(
        win=win,
        vertices=arc6_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    arc7_L1 = ShapeStim(
        win=win,
        vertices=arc7_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    arc8_L1 = ShapeStim(
        win=win,
        vertices=arc8_L1_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    def create_wiggle_arc(center, radius, thickness, color='blue', opacity=0.5):
        """Generate a thick wiggle room arc for a given arc."""
        outer_arc_vertices = []
        inner_arc_vertices = []
    
        for i in range(51):  # 50 segments for smoothness
            angle = math.radians(i * (180 / 50))  # Same angles as original arc
    
            # Outer arc (slightly larger)
            outer_x = center[0] + (radius + thickness) * math.cos(angle)
            outer_y = center[1] + (radius + thickness) * math.sin(angle)
            outer_arc_vertices.append((outer_x, outer_y))
    
            # Inner arc (slightly smaller)
            inner_x = center[0] + (radius - thickness) * math.cos(angle)
            inner_y = center[1] + (radius - thickness) * math.sin(angle)
            inner_arc_vertices.append((inner_x, inner_y))
    
        # Reverse inner arc vertices to create a closed shape
        inner_arc_vertices.reverse()
        thick_wiggle_arc_vertices = outer_arc_vertices + inner_arc_vertices
    
        # Create and return the wiggle room arc
        return ShapeStim(
            win=win,
            vertices=thick_wiggle_arc_vertices,
            closeShape=True,  # Fill between outer and inner arcs
            lineWidth=0,  # No outline needed
            lineColor=None,
            fillColor=color,
            opacity=opacity
        )
    
    
    # Generate wiggle arcs for all arcs
    wiggle_arc1_L1 = create_wiggle_arc(arc1_L1_center, arc1_L1_radius, wiggle_thickness)
    wiggle_arc2_L1 = create_wiggle_arc(arc2_L1_center, arc2_L1_radius, wiggle_thickness)
    wiggle_arc3_L1 = create_wiggle_arc(arc3_L1_center, arc3_L1_radius, wiggle_thickness)
    wiggle_arc4_L1 = create_wiggle_arc(arc4_L1_center, arc4_L1_radius, wiggle_thickness)
    wiggle_arc5_L1 = create_wiggle_arc(arc5_L1_center, arc5_L1_radius, wiggle_thickness)
    wiggle_arc6_L1 = create_wiggle_arc(arc6_L1_center, arc6_L1_radius, wiggle_thickness)
    wiggle_arc7_L1 = create_wiggle_arc(arc7_L1_center, arc7_L1_radius, wiggle_thickness)
    wiggle_arc8_L1 = create_wiggle_arc(arc8_L1_center, arc8_L1_radius, wiggle_thickness)
    
    
    
    
    
    
    # Run 'Begin Experiment' code from GoalController_L1
    
    meatbone_collided = False  # Track whether the meatbone has been stomped
    arc1_touched_vertices_L1 = []
    arc2_touched_vertices_L1 = []
    arc3_touched_vertices_L1 = []
    arc4_touched_vertices_L1 = []
    arc5_touched_vertices_L1 = []
    arc6_touched_vertices_L1 = []
    arc7_touched_vertices_L1 = []
    arc8_touched_vertices_L1 = []
    
    touch_threshold_L1 = 0.04 # touch threshold for the arcs
    
    meat_collision_threshold = 0.1  # You can adjust this to fit your game scale
    
    
    # Track if Dino is in the wiggle room defualt is not touching so false
    wiggle_room = False  
    
    
    # Run 'Begin Experiment' code from Timer_L1
    level_timer = core.Clock()  # Initialize the timer
    time_limit = 120  # Set the time limit in seconds (2 minutes)
    
    lose_sound_L1 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='lose_sound_L1',    name='lose_sound_L1'
    )
    lose_sound_L1.setVolume(1.0)
    eat_sound_L1 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='eat_sound_L1',    name='eat_sound_L1'
    )
    eat_sound_L1.setVolume(1.0)
    
    # --- Initialize components for Routine "Level_1_checker" ---
    end_score_text_L1 = visual.TextStim(win=win, name='end_score_text_L1',
        text='Score: ',
        font='Arial',
        pos=(0, .2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    win_sound_L1 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='win_sound_L1',    name='win_sound_L1'
    )
    win_sound_L1.setVolume(1.0)
    fail_sound_L1 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='fail_sound_L1',    name='fail_sound_L1'
    )
    fail_sound_L1.setVolume(1.0)
    
    # --- Initialize components for Routine "Level_2" ---
    dino_image_L2 = visual.ImageStim(
        win=win,
        name='dino_image_L2', 
        image='Assets/dino.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    floor1_L2 = visual.Rect(
        win=win, name='floor1_L2',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(-.5,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    floor2_L2 = visual.Rect(
        win=win, name='floor2_L2',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(0,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    meatbone_image_L2 = visual.ImageStim(
        win=win,
        name='meatbone_image_L2', 
        image='Assets/meat_bone.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    score_text_L2 = visual.TextStim(win=win, name='score_text_L2',
        text='Score: 0',
        font='Arial',
        pos=(0.55, 0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    timer_text_L2 = visual.TextStim(win=win, name='timer_text_L2',
        text='00 : 00',
        font='Arial',
        pos=(-0.55,0.45), draggable=False, height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    # Run 'Begin Experiment' code from DinoMovement_L2
    from psychopy.hardware import keyboard
    from psychopy.visual import Rect
    import time
    
    import serial
    from psychopy.visual import Circle
    
    # Initialize the Keyboard
    kb = keyboard.Keyboard()
    
    #PSURP Inits
    """
    # Initialize the serial connection for PSURP
    ser = serial.Serial("COM4", 230400, timeout=0.1)  # Replace "COM4" with your port
    ser.flush()
    ser.write("X".encode())  # Initialize PSURP
    ser.write("RUNE\n".encode())  # Enter streaming mode
    """
    
    # Trail settings
    trail_positions = []  # Stores Dino's previous positions
    trail_length = 35  # Maximum number of trail dots
    trail_dot_size = 0.005  # Size of each dot for trail 
    trail_dots = []  # List of Circle stimuli for the trail
    trail_color = 'yellow'  # Color of the trail dots
    trail_frame_counter = 0  # Counter to control trail dot spawning
    trail_interval = 5  # Spawn a dot every 5 frames
    
    
    #Button 0 and button 2 force properties
    B0ForceInNewtons = 0
    B2ForceInNewtons = 0
    MIN_FORCE = 0.4  # Minimum force to start movement
    FORCE_MULTIPLIER = 0.001  # Adjust this to control how much force affects movement
    
    # Dino movement variables
    dino_pos = [0, -0.3]  # Starting position [x, y]
    dino_speed = 0  # Initial vertical speed
    gravity = -0.0003  # Downward acceleration 0.00006
    jump_speed = 0.005  # Jumping speed
    move_speed = 0.01  # Horizontal movement speed
    ground_offset = 0.03  # Offset to avoid sinking into the ground visually
    min_x = -0.6  # Left boundary
    max_x = 19 # right boundary
    respawn_position = [0, -0.3]  # Starting position for Dino
    
    
    
    # Floor properties
    
    floor1_vertices = floor1_L2.vertices  # Get floor1_L2 vertices
    floor_top = max(v[1] for v in floor1_vertices)  # Highest point of floor1_L2
    fall_threshold = min(v[1] for v in floor1_vertices) - 0.2  # Slightly below the lowest floor point
    
    
    # Function to check if Dino is on the floor
    def is_on_floor(dino_pos):
        """Check if Dino's bottom is within the bounds of floor1_L2 or floor2_L2."""
        dino_bottom = dino_pos[1] - (dino_image_L2.size[1] / 2)  # Dino's bottom Y-position
    
        # floor1_L2 bounds
        x_min1 = min(v[0] for v in floor1_vertices)
        x_max1 = max(v[0] for v in floor1_vertices)
        
        # floor2_L2 bounds
        x_min2 = min(v[0] for v in floor2_vertices)
        x_max2 = max(v[0] for v in floor2_vertices)
    
        # Check floor1_L2 or floor2_L2
        on_floor1 = x_min1 <= dino_pos[0] <= x_max1 and dino_bottom <= floor1_top
        on_floor2 = x_min2 <= dino_pos[0] <= x_max2 and dino_bottom <= floor2_top
    
        return on_floor1 or on_floor2
        
    #calculates the psurp forces
    def calculate_psurp_forces(serial_data):
        """Extract and calculate forces from PSURP serial data."""
        if len(serial_data.decode()) == 12:
            output = serial_data.decode()
            
            # Calculate forces
            B0HighByte = Base71Lookup.index(output[0])
            B0LowByte = Base71Lookup.index(output[1])
            B2HighByte = Base71Lookup.index(output[4])
            B2LowByte = Base71Lookup.index(output[5])
            
            # Forces in Newtons
            B0ForceInNewtons = ((B0HighByte * 71) + B0LowByte) * 0.0098
            B2ForceInNewtons = ((B2HighByte * 71) + B2LowByte) * 0.0098
            
            return B0ForceInNewtons, B2ForceInNewtons
        
        return 0, 0  # Default forces if data is invalid
    
    
    
    # image path for dino animation
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
    dino_image_L2.image = frame_paths[frame_index]
    
    
    
    
    # Run 'Begin Experiment' code from worldController_L2
    from psychopy.visual import Rect, ImageStim, ShapeStim
    import math
    
    dirt_texture = 'Assets/ground1.png'
    
    #height factors for arcs (Y position)
    low_arc = -0.2  
    reg_arc = 0
    high_arc = 0.05
    
    small_arc_size = 0.2  # Smallest arc radius
    med_arc_size = 0.27  # Medium arc radius
    large_arc_size = 0.35  # Largest arc radius
    
    wiggle_thickness = 0.05  # Adjust thickness for all wiggle arcs
    
    meatbone_size = [0.15, 0.09]  # Example size (width, height)
    
    
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
    camera_speed = 0.003  # Adjust this speed as needed 0.003
    # Background properties
    background_width = 2.0  # Width of a single background image
    background_height = 1.0
    background_image_L2 = 'Assets/1.png'  # Path to your custom background image
    
    # Create two background images for seamless scrolling
    background1_L2 = ImageStim(win, image=background_image_L2, size=[background_width, background_height], pos=[0, 0])
    background2_L2 = ImageStim(win, image=background_image_L2, size=[background_width, background_height], pos=[background_width, 0])
    
    # floor1_L2 properties
    floor1_height = 0.3
    floor1_width = 0.5
    floor1_pos = [0, -0.5]
    
    floor1_L2 = visual.ImageStim(
        win=win,
        image=dirt_texture,
        size=(floor1_width, floor1_height),  # Set the size to match the floor dimensions
        pos=floor1_pos,
        interpolate=True
    )
    floor1_vertices = calculate_rect_vertices(floor1_L2)
    
    # floor2_L2 properties - Place it further into the map
    floor2_x_static = 1  # Fixed X position where floor2_L2 appears18.5
    floor2_height = 0.3
    floor2_width = 0.5
    
    floor2_L2 = visual.ImageStim(
        win=win,
        image=dirt_texture,
        size=(floor2_width, floor2_height),  # Set the size to match the floor dimensions
        pos=[floor2_x_static, -0.5],  # Position of floor2_L2
        interpolate=True
    )
    floor2_vertices = calculate_rect_vertices(floor2_L2)
    
    
    # Floor thresholds
    floor1_top = max(v[1] for v in floor1_vertices)
    floor2_top = max(v[1] for v in floor2_vertices)
    
    
    
    #meat bone
    
    meatbone_size = [0.12, 0.06]  # Example size (width, height)
    meatbone_image_L2.size = meatbone_size
    offset = 0.01  # Adjust to align the meatbone properly with floor2_L2
    
    
    #arc stuff
    
    # Arc 1 Properties
    arc1_L2_x = 0.3
    arc1_L2_center = [arc1_L2_x, low_arc]
    arc1_L2_radius = small_arc_size
    arc1_L2_start_angle = 0
    arc1_L2_end_angle = 180
    
    # Arc 2 Properties
    arc2_L2_x = 1.0
    arc2_L2_center = [arc2_L2_x, low_arc]
    arc2_L2_radius = med_arc_size
    arc2_L2_start_angle = 0
    arc2_L2_end_angle = 180
    
    # Arc 3 Properties
    arc3_L2_x = 2.2
    arc3_L2_center = [arc3_L2_x, high_arc]
    arc3_L2_radius = large_arc_size
    arc3_L2_start_angle = 0
    arc3_L2_end_angle = 180
    
    # Arc 4 Properties
    arc4_L2_x = 3.4
    arc4_L2_center = [arc4_L2_x, low_arc]
    arc4_L2_radius = small_arc_size
    arc4_L2_start_angle = 0
    arc4_L2_end_angle = 180
    
    # Arc 5 Properties
    arc5_L2_x = 4.6
    arc5_L2_center = [arc5_L2_x, reg_arc]
    arc5_L2_radius = large_arc_size
    arc5_L2_start_angle = 0
    arc5_L2_end_angle = 180
    
    # Arc 6 Properties
    arc6_L2_x = 5.8
    arc6_L2_center = [arc6_L2_x, high_arc]
    arc6_L2_radius = med_arc_size
    arc6_L2_start_angle = 0
    arc6_L2_end_angle = 180
    
    # Arc 7 Properties
    arc7_L2_x = 7.0
    arc7_L2_center = [arc7_L2_x, low_arc]
    arc7_L2_radius = large_arc_size
    arc7_L2_start_angle = 0
    arc7_L2_end_angle = 180
    
    # Arc 8 Properties
    arc8_L2_x = 8.5
    arc8_L2_center = [arc8_L2_x, high_arc]
    arc8_L2_radius = med_arc_size
    arc8_L2_start_angle = 0
    arc8_L2_end_angle = 180
    
    
    
    
    # Generate vertices for Arc 1
    arc1_L2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc1_L2_start_angle + i * (arc1_L2_end_angle - arc1_L2_start_angle) / 50)
        x = arc1_L2_center[0] + arc1_L2_radius * math.cos(angle)
        y = arc1_L2_center[1] + arc1_L2_radius * math.sin(angle)
        arc1_L2_vertices.append((x, y))
    
    # Generate vertices for Arc 2
    arc2_L2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc2_L2_start_angle + i * (arc2_L2_end_angle - arc2_L2_start_angle) / 50)
        x = arc2_L2_center[0] + arc2_L2_radius * math.cos(angle)
        y = arc2_L2_center[1] + arc2_L2_radius * math.sin(angle)
        arc2_L2_vertices.append((x, y))
        
        
    
    # Generate vertices for Arc 3
    arc3_L2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc3_L2_start_angle + i * (arc3_L2_end_angle - arc3_L2_start_angle) / 50)
        x = arc3_L2_center[0] + arc3_L2_radius * math.cos(angle)
        y = arc3_L2_center[1] + arc3_L2_radius * math.sin(angle)
        arc3_L2_vertices.append((x, y))
    
    # Generate vertices for Arc 4
    arc4_L2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc4_L2_start_angle + i * (arc4_L2_end_angle - arc4_L2_start_angle) / 50)
        x = arc4_L2_center[0] + arc4_L2_radius * math.cos(angle)
        y = arc4_L2_center[1] + arc4_L2_radius * math.sin(angle)
        arc4_L2_vertices.append((x, y))
    
    
    # Generate vertices for Arc 5
    arc5_L2_vertices = []
    for i in range(51):  # 50 segments for smoothness
        angle = math.radians(arc5_L2_start_angle + i * (arc5_L2_end_angle - arc5_L2_start_angle) / 50)
        x = arc5_L2_center[0] + arc5_L2_radius * math.cos(angle)
        y = arc5_L2_center[1] + arc5_L2_radius * math.sin(angle)
        arc5_L2_vertices.append((x, y))
        
    
    arc6_L2_vertices = []
    for i in range(51):
        angle = math.radians(arc6_L2_start_angle + i * (arc6_L2_end_angle - arc6_L2_start_angle) / 50)
        x = arc6_L2_center[0] + arc6_L2_radius * math.cos(angle)
        y = arc6_L2_center[1] + arc6_L2_radius * math.sin(angle)
        arc6_L2_vertices.append((x, y))
    
    # Arc 7 vertices
    arc7_L2_vertices = []
    for i in range(51):
        angle = math.radians(arc7_L2_start_angle + i * (arc7_L2_end_angle - arc7_L2_start_angle) / 50)
        x = arc7_L2_center[0] + arc7_L2_radius * math.cos(angle)
        y = arc7_L2_center[1] + arc7_L2_radius * math.sin(angle)
        arc7_L2_vertices.append((x, y))
    
    # Arc 8 vertices
    arc8_L2_vertices = []
    for i in range(51):
        angle = math.radians(arc8_L2_start_angle + i * (arc8_L2_end_angle - arc8_L2_start_angle) / 50)
        x = arc8_L2_center[0] + arc8_L2_radius * math.cos(angle)
        y = arc8_L2_center[1] + arc8_L2_radius * math.sin(angle)
        arc8_L2_vertices.append((x, y))
        
    # Create the arc ShapeStim
    arc1_L2 = ShapeStim(
        win=win,
        vertices=arc1_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    # Create Arc 2 ShapeStim
    arc2_L2 = ShapeStim(
        win=win,
        vertices=arc2_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Different color for clarity
        fillColor=None
    )
    
    
    # Create Arc 3 ShapeStim
    arc3_L2 = ShapeStim(
        win=win,
        vertices=arc3_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    # Create Arc 4 ShapeStim
    arc4_L2 = ShapeStim(
        win=win,
        vertices=arc4_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    # Create Arc 5 ShapeStim
    arc5_L2 = ShapeStim(
        win=win,
        vertices=arc5_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',  # Set color as desired
        fillColor=None
    )
    
    
    arc6_L2 = ShapeStim(
        win=win,
        vertices=arc6_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    arc7_L2 = ShapeStim(
        win=win,
        vertices=arc7_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    arc8_L2 = ShapeStim(
        win=win,
        vertices=arc8_L2_vertices,
        closeShape=False,
        lineWidth=4,
        lineColor='white',
        fillColor=None
    )
    
    def create_wiggle_arc(center, radius, thickness, color='blue', opacity=0.5):
        """Generate a thick wiggle room arc for a given arc."""
        outer_arc_vertices = []
        inner_arc_vertices = []
    
        for i in range(51):  # 50 segments for smoothness
            angle = math.radians(i * (180 / 50))  # Same angles as original arc
    
            # Outer arc (slightly larger)
            outer_x = center[0] + (radius + thickness) * math.cos(angle)
            outer_y = center[1] + (radius + thickness) * math.sin(angle)
            outer_arc_vertices.append((outer_x, outer_y))
    
            # Inner arc (slightly smaller)
            inner_x = center[0] + (radius - thickness) * math.cos(angle)
            inner_y = center[1] + (radius - thickness) * math.sin(angle)
            inner_arc_vertices.append((inner_x, inner_y))
    
        # Reverse inner arc vertices to create a closed shape
        inner_arc_vertices.reverse()
        thick_wiggle_arc_vertices = outer_arc_vertices + inner_arc_vertices
    
        # Create and return the wiggle room arc
        return ShapeStim(
            win=win,
            vertices=thick_wiggle_arc_vertices,
            closeShape=True,  # Fill between outer and inner arcs
            lineWidth=0,  # No outline needed
            lineColor=None,
            fillColor=color,
            opacity=opacity
        )
    
    
    # Generate wiggle arcs for all arcs
    wiggle_arc1_L2 = create_wiggle_arc(arc1_L2_center, arc1_L2_radius, wiggle_thickness)
    wiggle_arc2_L2 = create_wiggle_arc(arc2_L2_center, arc2_L2_radius, wiggle_thickness)
    wiggle_arc3_L2 = create_wiggle_arc(arc3_L2_center, arc3_L2_radius, wiggle_thickness)
    wiggle_arc4_L2 = create_wiggle_arc(arc4_L2_center, arc4_L2_radius, wiggle_thickness)
    wiggle_arc5_L2 = create_wiggle_arc(arc5_L2_center, arc5_L2_radius, wiggle_thickness)
    wiggle_arc6_L2 = create_wiggle_arc(arc6_L2_center, arc6_L2_radius, wiggle_thickness)
    wiggle_arc7_L2 = create_wiggle_arc(arc7_L2_center, arc7_L2_radius, wiggle_thickness)
    wiggle_arc8_L2 = create_wiggle_arc(arc8_L2_center, arc8_L2_radius, wiggle_thickness)
    
    
    
    
    
    
    # Run 'Begin Experiment' code from GoalController_L2
    
    meatbone_collided = False  # Track whether the meatbone has been stomped
    arc1_touched_vertices_L2 = []
    arc2_touched_vertices_L2 = []
    arc3_touched_vertices_L2 = []
    arc4_touched_vertices_L2 = []
    arc5_touched_vertices_L2 = []
    arc6_touched_vertices_L2 = []
    arc7_touched_vertices_L2 = []
    arc8_touched_vertices_L2 = []
    
    touch_threshold_L2 = 0.04 # touch threshold for the arcs
    
    meat_collision_threshold = 0.1  # You can adjust this to fit your game scale
    
    
    # Track if Dino is in the wiggle room defualt is not touching so false
    wiggle_room = False  
    
    
    # Run 'Begin Experiment' code from Timer_L2
    level_timer = core.Clock()  # Initialize the timer
    time_limit = 120  # Set the time limit in seconds (2 minutes)
    
    lose_sound_L2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='lose_sound_L2',    name='lose_sound_L2'
    )
    lose_sound_L2.setVolume(1.0)
    eat_sound_L2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='eat_sound_L2',    name='eat_sound_L2'
    )
    eat_sound_L2.setVolume(1.0)
    
    # --- Initialize components for Routine "Level_2_checker" ---
    end_score_text_L2 = visual.TextStim(win=win, name='end_score_text_L2',
        text='Score: ',
        font='Arial',
        pos=(0, .2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    win_sound_L2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='win_sound_L2',    name='win_sound_L2'
    )
    win_sound_L2.setVolume(1.0)
    fail_sound_L2 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='fail_sound_L2',    name='fail_sound_L2'
    )
    fail_sound_L2.setVolume(1.0)
    
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
    """
    ser.flush()
    ser.write("X".encode())
    """
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
    """
    ser.write("RUNE\n".encode())
    """
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
            components=[TitleText, start_button, StartGame, exit_button, Exit, controller_selection, control_feedback, mode_feedback, mode_button, mouse],
        )
        MainMenu.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        # Update the feedback button text to display the currently selected control method
        control_feedback.text = f"Selected Control: {selected_control}"
        mode_feedback.text = f"Mode: {selected_diff}"
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
                # update status
                control_feedback.status = STARTED
                control_feedback.setAutoDraw(True)
            
            # if control_feedback is active this frame...
            if control_feedback.status == STARTED:
                # update params
                pass
            
            # *mode_feedback* updates
            
            # if mode_feedback is starting this frame...
            if mode_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mode_feedback.frameNStart = frameN  # exact frame index
                mode_feedback.tStart = t  # local t and not account for scr refresh
                mode_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mode_feedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                mode_feedback.status = STARTED
                mode_feedback.setAutoDraw(True)
            
            # if mode_feedback is active this frame...
            if mode_feedback.status == STARTED:
                # update params
                pass
            
            # *mode_button* updates
            
            # if mode_button is starting this frame...
            if mode_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mode_button.frameNStart = frameN  # exact frame index
                mode_button.tStart = t  # local t and not account for scr refresh
                mode_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mode_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                mode_button.status = STARTED
                mode_button.setAutoDraw(True)
            
            # if mode_button is active this frame...
            if mode_button.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code
            # Check if the mouse is clicked and which button is clicked
            if mouse.isPressedIn(start_button):
                continueRoutine = False  # End MainMenu
            
            if mouse.isPressedIn(exit_button):  # Exit button
                core.quit()  # Quit the experiment
                
            if mouse.isPressedIn(controller_selection):
                # Add a delay to prevent rapid toggling (doesnt switch too fast)
                core.wait(0.2)
                
                # Toggle between "Keyboard" and "PSURP"
                if selected_control == "Keyboard":
                    selected_control = "PSURP"
                    ser.flush()
                else:
                    selected_control = "Keyboard"
                
                # Update the feedback text
                control_feedback.text = f"Selected Control: {selected_control}"
                
                
            
            if mouse.isPressedIn(mode_button):
                # Add a delay to prevent rapid toggling (debounce)
                core.wait(0.2)
                
                # Toggle between "Easy (1)" and "Hard (2)" modes
                if selected_diff == "1":
                    selected_diff = "2"
                else:
                    selected_diff = "1"
                
                # Update the feedback text
                mode_feedback.text = f"Mode: {selected_diff}"
                
                
            
            
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
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
        
        # set up handler to look after randomisation of conditions etc
        Level_1_Loop = data.TrialHandler2(
            name='Level_1_Loop',
            nReps=1000.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(Level_1_Loop)  # add the loop to the experiment
        thisLevel_1_Loop = Level_1_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLevel_1_Loop.rgb)
        if thisLevel_1_Loop != None:
            for paramName in thisLevel_1_Loop:
                globals()[paramName] = thisLevel_1_Loop[paramName]
        
        for thisLevel_1_Loop in Level_1_Loop:
            currentLoop = Level_1_Loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisLevel_1_Loop.rgb)
            if thisLevel_1_Loop != None:
                for paramName in thisLevel_1_Loop:
                    globals()[paramName] = thisLevel_1_Loop[paramName]
            
            # --- Prepare to start Routine "Level_1" ---
            # create an object to store info about Routine Level_1
            Level_1 = data.Routine(
                name='Level_1',
                components=[dino_image_L1, floor1_L1, floor2_L1, meatbone_image_L1, score_text_L1, timer_text_L1, lose_sound_L1, eat_sound_L1],
            )
            Level_1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from DinoMovement_L1
            dino_pos = [0, -0.3]  # Reset Dino's position
            dino_speed = 0  # Reset vertical speed
            # Initialize the trail dots
            trail_dots = [
                Circle(win, radius=trail_dot_size, fillColor=trail_color, lineColor=None, pos=[-1, -1])
                for _ in range(trail_length)
            ]
            
            # Run 'Begin Routine' code from worldController_L1
            camera_offset_x = 0
            # Run 'Begin Routine' code from GoalController_L1
            score = 0  # Reset the score
            
            meatbone_collided = False
            meatbone_image_L1.opacity = 1
            
            
            wiggle_room = False  
            
            arc1_touched_vertices_L1 = []
            arc2_touched_vertices_L1 = []
            arc3_touched_vertices_L1 = []
            arc4_touched_vertices_L1 = []
            arc5_touched_vertices_L1 = []
            arc6_touched_vertices_L1 = []
            arc7_touched_vertices_L1 = []
            arc8_touched_vertices_L1 = []
            # Run 'Begin Routine' code from Timer_L1
            
            level_timer.reset()  # Reset the timer at the start of the MainGame routine
            
            
            lose_sound_L1.setSound('Assets/sounds/lose.mp3', hamming=True)
            lose_sound_L1.setVolume(1.0, log=False)
            lose_sound_L1.seek(0)
            eat_sound_L1.setSound('Assets/sounds/eat.mp3', hamming=True)
            eat_sound_L1.setVolume(1.0, log=False)
            eat_sound_L1.seek(0)
            # store start times for Level_1
            Level_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Level_1.tStart = globalClock.getTime(format='float')
            Level_1.status = STARTED
            thisExp.addData('Level_1.started', Level_1.tStart)
            Level_1.maxDuration = None
            # keep track of which components have finished
            Level_1Components = Level_1.components
            for thisComponent in Level_1.components:
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
            
            # --- Run Routine "Level_1" ---
            # if trial has changed, end Routine now
            if isinstance(Level_1_Loop, data.TrialHandler2) and thisLevel_1_Loop.thisN != Level_1_Loop.thisTrial.thisN:
                continueRoutine = False
            Level_1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *dino_image_L1* updates
                
                # if dino_image_L1 is starting this frame...
                if dino_image_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dino_image_L1.frameNStart = frameN  # exact frame index
                    dino_image_L1.tStart = t  # local t and not account for scr refresh
                    dino_image_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dino_image_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dino_image_L1.status = STARTED
                    dino_image_L1.setAutoDraw(True)
                
                # if dino_image_L1 is active this frame...
                if dino_image_L1.status == STARTED:
                    # update params
                    pass
                
                # *floor1_L1* updates
                
                # if floor1_L1 is starting this frame...
                if floor1_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    floor1_L1.frameNStart = frameN  # exact frame index
                    floor1_L1.tStart = t  # local t and not account for scr refresh
                    floor1_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(floor1_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    floor1_L1.status = STARTED
                    floor1_L1.setAutoDraw(True)
                
                # if floor1_L1 is active this frame...
                if floor1_L1.status == STARTED:
                    # update params
                    pass
                
                # *floor2_L1* updates
                
                # if floor2_L1 is starting this frame...
                if floor2_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    floor2_L1.frameNStart = frameN  # exact frame index
                    floor2_L1.tStart = t  # local t and not account for scr refresh
                    floor2_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(floor2_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    floor2_L1.status = STARTED
                    floor2_L1.setAutoDraw(True)
                
                # if floor2_L1 is active this frame...
                if floor2_L1.status == STARTED:
                    # update params
                    pass
                
                # *meatbone_image_L1* updates
                
                # if meatbone_image_L1 is starting this frame...
                if meatbone_image_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    meatbone_image_L1.frameNStart = frameN  # exact frame index
                    meatbone_image_L1.tStart = t  # local t and not account for scr refresh
                    meatbone_image_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(meatbone_image_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    meatbone_image_L1.status = STARTED
                    meatbone_image_L1.setAutoDraw(True)
                
                # if meatbone_image_L1 is active this frame...
                if meatbone_image_L1.status == STARTED:
                    # update params
                    pass
                
                # *score_text_L1* updates
                
                # if score_text_L1 is starting this frame...
                if score_text_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_text_L1.frameNStart = frameN  # exact frame index
                    score_text_L1.tStart = t  # local t and not account for scr refresh
                    score_text_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_text_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    score_text_L1.status = STARTED
                    score_text_L1.setAutoDraw(True)
                
                # if score_text_L1 is active this frame...
                if score_text_L1.status == STARTED:
                    # update params
                    pass
                
                # *timer_text_L1* updates
                
                # if timer_text_L1 is starting this frame...
                if timer_text_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer_text_L1.frameNStart = frameN  # exact frame index
                    timer_text_L1.tStart = t  # local t and not account for scr refresh
                    timer_text_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer_text_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    timer_text_L1.status = STARTED
                    timer_text_L1.setAutoDraw(True)
                
                # if timer_text_L1 is active this frame...
                if timer_text_L1.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from DinoMovement_L1
                
                # Initialize key state flags
                left_pressed = False
                right_pressed = False
                up_pressed = False
                
                # Handle input based on the selected control method
                
                # Process keyboard input
                if selected_control == "Keyboard":
                    keys_pressed = kb.getKeys(['left', 'right', 'up'], waitRelease=False, clear=False)
                    for key in keys_pressed:
                        if key.name == 'left':
                            left_pressed = True
                        if key.name == 'right':
                            right_pressed = True
                        if key.name == 'up':
                            up_pressed = True
                            
                # Process PSURP input            
                if selected_control == "PSURP":
                    # Read serial data
                    ser.flushInput()
                    strSerialData = ser.readline()
                    B0ForceInNewtons, B2ForceInNewtons = calculate_psurp_forces(strSerialData)
                
                    # Apply difficulty-specific movement
                    if selected_diff == "1":
                        # Constant movement for Easy mode
                        if B2ForceInNewtons > MIN_FORCE and dino_pos[0] < max_x:
                            dino_pos[0] += 0.005  # Constant movement speed (adjust as needed)
                            dino_image_L1.size = [abs(dino_image_L1.size[0]), dino_image_L1.size[1]]  # Face right
                
                    elif selected_diff == "2":
                        # Proportional movement for Hard mode (current implementation)
                        if B2ForceInNewtons > MIN_FORCE and dino_pos[0] < max_x:
                            move_amount = B2ForceInNewtons * FORCE_MULTIPLIER
                            dino_pos[0] += move_amount  # Movement based on force
                            dino_image_L1.size = [abs(dino_image_L1.size[0]), dino_image_L1.size[1]]  # Face right
                
                    # Jump logic remains the same for both difficulties
                    if B0ForceInNewtons > MIN_FORCE:
                        dino_speed = B0ForceInNewtons * FORCE_MULTIPLIER  # Jump height based on force
                
                
                            
                 
                # Apply gravity to Dino's vertical speed
                dino_speed += gravity
                
                # Check if Dino is on the floor (keeps dino on top of floor)
                if is_on_floor(dino_pos) and dino_speed <= 0:  # Falling or stationary
                    dino_pos[1] = floor1_top + (dino_image_L1.size[1] / 2) - ground_offset  # Align Dino with the floor
                    dino_speed = 0  # Reset vertical speed
                
                # Respawn if Dino falls below the floor threshold
                if dino_pos[1] < fall_threshold:
                    lose_sound_L1.play()
                    continueRoutine = False  # Stop the MainGame routine
                    
                # Jumping logic: Allow jump whenever the 'up' key is pressed
                if up_pressed:  # Check if the up key is pressed
                    dino_speed = jump_speed  # Apply upward movement
                
                # Update Dino's vertical position
                dino_pos[1] += dino_speed
                
                # Continuous horizontal movement
                if left_pressed and dino_pos[0] > min_x:
                    dino_pos[0] -= move_speed  # Move Dino to the left
                    dino_image_L1.size = [-1 * abs(dino_image_L1.size[0]), dino_image_L1.size[1]]
                
                if right_pressed and dino_pos[0] < max_x:
                    dino_pos[0] += move_speed  # Move Dino to the right
                    dino_image_L1.size = [abs(dino_image_L1.size[0]), dino_image_L1.size[1]]  # Reset Dino to face right
                
                # Update Dino's position
                # dino_image_L1.pos = dino_pos  # Use both X and Y values of dino_pos
                dino_image_L1.pos = [dino_pos[0] - camera_offset_x, dino_pos[1]]
                
                # Increment the frame counter for trail updates
                trail_frame_counter += 1
                
                # Check if it's time to spawn a new dot
                if trail_frame_counter >= trail_interval:
                    if len(trail_positions) >= trail_length:
                        trail_positions.pop(0)  # Remove the oldest position if trail is full
                
                    # Add Dino's current position to the trail
                    trail_positions.append(dino_pos[:])  # Add a copy of Dino's current position
                
                    trail_frame_counter = 0  # Reset the counter
                
                # Update the trail dots' positions
                for i, pos in enumerate(trail_positions):
                    trail_dots[i].pos = [pos[0] - camera_offset_x, pos[1]]  # Adjust for camera offset
                
                
                # Update the Dino's animation
                if (frame_index_update_counter % 4) == 0:  # Adjust 4 to control animation speed
                    dino_image_L1.image = frame_paths[frame_index]  # Update the current frame
                
                    # Advance to the next frame
                    frame_index += 1
                    if frame_index >= total_frames:
                        frame_index = 0  # Loop back to the first frame
                
                
                
                # Increment the animation frame counter
                frame_index_update_counter += 1
                
                
                # Run 'Each Frame' code from worldController_L1
                
                # Update the camera offset based on Dino's X position
                camera_offset_x += camera_speed  # The camera offset follows Dino's position
                
                # Move backgrounds relative to Dino's position (seamless wrap-around)
                background1_L1.pos = [-(camera_offset_x % background_width), 0]
                background2_L1.pos = [background1_L1.pos[0] + background_width, 0]
                
                # Update floor positions relative to Dino's position
                floor1_L1.pos = [floor1_pos[0] - camera_offset_x, floor1_L1.pos[1]]
                floor2_L1.pos = [floor2_x_static - camera_offset_x, floor2_L1.pos[1]]  # floor2_L1 moves with Dino
                
                
                # Update meatbone position to match floor2_L1's top
                meatbone_x = floor2_L1.pos[0]  # Update X position based on floor2_L1
                meatbone_y = floor2_top + (meatbone_size[1] / 2) - offset  # Keep the meatbone on top of floor2_L1
                meatbone_image_L1.pos = [meatbone_x, meatbone_y]
                
                
                # Update the arc position relative to the camera offset
                # Update Arc 1 Position
                arc1_L1.pos = [arc1_L1_center[0] - camera_offset_x, arc1_L1_center[1]]
                wiggle_arc1_L1.pos = arc1_L1.pos  # Keep wiggle room on top
                
                # Update Arc 2 Position
                arc2_L1.pos = [arc2_L1_center[0] - camera_offset_x, arc2_L1_center[1]]
                wiggle_arc2_L1.pos = arc2_L1.pos  # Keep wiggle room on top
                arc3_L1.pos = [arc3_L1_center[0] - camera_offset_x, arc3_L1_center[1]]
                wiggle_arc3_L1.pos = arc3_L1.pos  # Keep wiggle room on top
                # Update Arc 4 Position
                arc4_L1.pos = [arc4_L1_center[0] - camera_offset_x, arc4_L1_center[1]]
                wiggle_arc4_L1.pos = arc4_L1.pos  # Keep wiggle room on top
                # Update Arc 5 Position
                arc5_L1.pos = [arc5_L1_center[0] - camera_offset_x, arc5_L1_center[1]]
                wiggle_arc5_L1.pos = arc5_L1.pos  # Keep wiggle room on top
                
                arc6_L1.pos = [arc6_L1_center[0] - camera_offset_x, arc6_L1_center[1]]
                wiggle_arc6_L1.pos = arc6_L1.pos
                
                # Update Arc 7 Position
                arc7_L1.pos = [arc7_L1_center[0] - camera_offset_x, arc7_L1_center[1]]
                wiggle_arc7_L1.pos = arc7_L1.pos
                
                # Update Arc 8 Position
                arc8_L1.pos = [arc8_L1_center[0] - camera_offset_x, arc8_L1_center[1]]
                wiggle_arc8_L1.pos = arc8_L1.pos
                
                
                
                # Draw the backgrounds and floors
                background1_L1.draw()
                background2_L1.draw()
                floor1_L1.draw()
                floor2_L1.draw()
                wiggle_arc1_L1.draw()
                wiggle_arc2_L1.draw()
                wiggle_arc3_L1.draw()
                wiggle_arc4_L1.draw()
                wiggle_arc5_L1.draw()
                wiggle_arc6_L1.draw()
                wiggle_arc7_L1.draw()
                wiggle_arc8_L1.draw()
                
                
                arc1_L1.draw()
                arc2_L1.draw()
                arc3_L1.draw()
                arc4_L1.draw()
                arc5_L1.draw()
                arc6_L1.draw()
                arc7_L1.draw()
                arc8_L1.draw()
                
                # Draw the trail dots
                for dot in trail_dots:
                    dot.draw()
                
                # Run 'Each Frame' code from GoalController_L1
                dino_relative_x = dino_pos[0] - camera_offset_x
                dino_relative_y = dino_pos[1]
                # Check for collision based on proximity to the updated position
                dx = dino_relative_x - meatbone_x
                dy = dino_relative_y - meatbone_y
                
                if camera_offset_x >= max_x:
                    lose_sound_L1.play()
                    continueRoutine = False  # Ends the current routine
                    
                if dino_relative_x < -0.8 or dino_relative_x > 0.8:  # Adjust bounds based on screen width
                    lose_sound_L1.play()
                    continueRoutine = False  # Ends the current routine
                
                # Check for collision for meatbone
                if not meatbone_collided and (dx ** 2 + dy ** 2) ** 0.5 <= meat_collision_threshold:
                    print("Dino ate the meatbone!")
                    meatbone_image_L1.opacity = 0  # Make the meatbone disappear
                    meatbone_collided = True  # Prevent further collision checks
                    eat_sound_L1.play()
                    continueRoutine = False
                
                # Check for collision for ARCS
                for vertex in arc1_L1_vertices:
                    # Adjust Arc 1 vertex for its X-offset (+1)
                    adjusted_vertex_x = vertex[0] + arc1_L1_x   # Move Arc 1 vertices by 1 unit to the right
                    adjusted_vertex_y = vertex[1] + reg_arc # Y remains unchanged, apply the same adjustment as Arc 2 if needed
                
                    # Calculate distance between Dino and the adjusted vertex of Arc 1
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L1 and vertex not in arc1_touched_vertices_L1:
                        arc1_touched_vertices_L1.append(vertex)
                        score += 1  # Increment the score for Arc 1
                
                
                for vertex in arc2_L1_vertices:
                    # Adjust Arc 2 vertex for its X-offset (+2)
                    adjusted_vertex_x = vertex[0] + arc2_L1_x   # Move Arc 2 vertices by 2 units to the right
                    adjusted_vertex_y = vertex[1] + low_arc # Y remains unchanged
                    
                    # Calculate distance between Dino and the adjusted vertex of Arc 2
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L1 and vertex not in arc2_touched_vertices_L1:
                        arc2_touched_vertices_L1.append(vertex)
                        score += 1  # Increment the score for Arc 2
                        
                        
                for vertex in arc3_L1_vertices:
                    # Adjust Arc 3 vertex for its static X-offset
                    adjusted_vertex_x = vertex[0] + arc3_L1_x   # Offset Arc 3 vertices by 3.5 units to the right
                    adjusted_vertex_y = vertex[1] + high_arc  # Offset Arc 3 vertices by -0.2 units vertically
                
                    # Calculate distance between Dino and the adjusted vertex of Arc 3
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L1 and vertex not in arc3_touched_vertices_L1:
                        arc3_touched_vertices_L1.append(vertex)
                        score += 1  # Increment the score for Arc 3
                        
                for vertex in arc4_L1_vertices:
                    adjusted_vertex_x = vertex[0] + arc4_L1_x   # Offset Arc 4 vertices
                    adjusted_vertex_y = vertex[1] + low_arc  # Y position remains the same
                
                    # Calculate distance between Dino and Arc 4
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is close enough, count as a touch
                    if distance <= touch_threshold_L1 and vertex not in arc4_touched_vertices_L1:
                        arc4_touched_vertices_L1.append(vertex)
                        score += 1  # Increment score
                
                for vertex in arc5_L1_vertices:
                    adjusted_vertex_x = vertex[0] + arc5_L1_x   # Offset Arc 5 vertices
                    adjusted_vertex_y = vertex[1] + reg_arc  # Y position remains the same
                
                    # Calculate distance between Dino and Arc 5
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is close enough, count as a touch
                    if distance <= touch_threshold_L1 and vertex not in arc5_touched_vertices_L1:
                        arc5_touched_vertices_L1.append(vertex)
                        score += 1  # Increment score
                
                for vertex in arc6_L1_vertices:
                    adjusted_vertex_x = vertex[0] + arc6_L1_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1 and vertex not in arc6_touched_vertices_L1:
                        arc6_touched_vertices_L1.append(vertex)
                        score += 1
                
                # Arc 7 touch detection
                for vertex in arc7_L1_vertices:
                    adjusted_vertex_x = vertex[0] + arc7_L1_x 
                    adjusted_vertex_y = vertex[1] + arc7_L1_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1 and vertex not in arc7_touched_vertices_L1:
                        arc7_touched_vertices_L1.append(vertex)
                        score += 1
                
                # Arc 8 touch detection
                for vertex in arc8_L1_vertices:
                    adjusted_vertex_x = vertex[0] + arc8_L1_x 
                    adjusted_vertex_y = vertex[1] + arc8_L1_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1 and vertex not in arc8_touched_vertices_L1:
                        arc8_touched_vertices_L1.append(vertex)
                        score += 1
                
                # WIGGLE ROOM STUFF
                
                
                # Reset to false at the start of each frame
                wiggle_room = False  
                for vertex in wiggle_arc1_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc1_L1_x 
                    adjusted_vertex_y = vertex[1] + reg_arc 
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L1:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                        
                        
                for vertex in wiggle_arc2_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc2_L1_x 
                    adjusted_vertex_y = vertex[1] + low_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L1:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                        
                        
                        
                for vertex in wiggle_arc3_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc3_L1_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L1:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                
                
                for vertex in wiggle_arc4_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc4_L1_x   # Offset Arc 4 vertices
                    adjusted_vertex_y = vertex[1] + low_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, mark as safe
                    if distance <= touch_threshold_L1:
                        wiggle_room = True  
                        break  # Stop checking once inside
                
                
                for vertex in wiggle_arc5_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc5_L1_x   # Offset Arc 5 vertices
                    adjusted_vertex_y = vertex[1] + reg_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, mark as safe
                    if distance <= touch_threshold_L1:
                        wiggle_room = True  
                        break  # Stop checking once inside
                        
                for vertex in wiggle_arc6_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc6_L1_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1:
                        wiggle_room = True
                        break
                # Arc 7 wiggle room
                for vertex in wiggle_arc7_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc7_L1_x 
                    adjusted_vertex_y = vertex[1] + arc7_L1_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1:
                        wiggle_room = True
                        break
                
                # Arc 8 wiggle room
                for vertex in wiggle_arc8_L1.vertices:
                    adjusted_vertex_x = vertex[0] + arc8_L1_x 
                    adjusted_vertex_y = vertex[1] + arc8_L1_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L1:
                        wiggle_room = True
                        break
                
                        
                        
                score_text_L1.text = str(score) # update Score
                
                
                
                # Run 'Each Frame' code from Timer_L1
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
                
                # Update the timer display
                timer_text_L1.text = str(f"{minutes}:{seconds:02d}")
                
                
                # *lose_sound_L1* updates
                
                # if lose_sound_L1 is stopping this frame...
                if lose_sound_L1.status == STARTED:
                    if bool(False) or lose_sound_L1.isFinished:
                        # keep track of stop time/frame for later
                        lose_sound_L1.tStop = t  # not accounting for scr refresh
                        lose_sound_L1.tStopRefresh = tThisFlipGlobal  # on global time
                        lose_sound_L1.frameNStop = frameN  # exact frame index
                        # update status
                        lose_sound_L1.status = FINISHED
                        lose_sound_L1.stop()
                
                # *eat_sound_L1* updates
                
                # if eat_sound_L1 is stopping this frame...
                if eat_sound_L1.status == STARTED:
                    if bool(False) or eat_sound_L1.isFinished:
                        # keep track of stop time/frame for later
                        eat_sound_L1.tStop = t  # not accounting for scr refresh
                        eat_sound_L1.tStopRefresh = tThisFlipGlobal  # on global time
                        eat_sound_L1.frameNStop = frameN  # exact frame index
                        # update status
                        eat_sound_L1.status = FINISHED
                        eat_sound_L1.stop()
                
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
                        playbackComponents=[lose_sound_L1, eat_sound_L1]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Level_1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Level_1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Level_1" ---
            for thisComponent in Level_1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Level_1
            Level_1.tStop = globalClock.getTime(format='float')
            Level_1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Level_1.stopped', Level_1.tStop)
            # Run 'End Routine' code from DinoMovement_L1
            dino_pos = [-0.5, -0.3]  # Reset Dino's position
            trail_positions.clear()  # Remove all stored positions
            # Run 'End Routine' code from GoalController_L1
            global total_touched_vertices_L1, total_possible_vertices_L1
            
            total_touched_vertices_L1 = (
                len(arc1_touched_vertices_L1) + len(arc2_touched_vertices_L1) + len(arc3_touched_vertices_L1) +
                len(arc4_touched_vertices_L1) + len(arc5_touched_vertices_L1) + len(arc6_touched_vertices_L1) +
                len(arc7_touched_vertices_L1) + len(arc8_touched_vertices_L1)
            )
            
            total_possible_vertices_L1 = (
                len(arc1_L1_vertices) + len(arc2_L1_vertices) + len(arc3_L1_vertices) +
                len(arc4_L1_vertices) + len(arc5_L1_vertices) + len(arc6_L1_vertices) +
                len(arc7_L1_vertices) + len(arc8_L1_vertices)
            )
            
            score = 0
            # the Routine "Level_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Level_1_checker" ---
            # create an object to store info about Routine Level_1_checker
            Level_1_checker = data.Routine(
                name='Level_1_checker',
                components=[end_score_text_L1, win_sound_L1, fail_sound_L1],
            )
            Level_1_checker.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Checker_L1
            import csv
            # Calculate the percentage
            if total_possible_vertices_L1 > 0:
                percentage = (total_touched_vertices_L1 / total_possible_vertices_L1) * 100
            else:
                percentage = 0  # Avoid division by zero
                
            
            # Update the text for the end screen
            end_score_text_L1.text = (
                f"You hit {total_touched_vertices_L1} out of {total_possible_vertices_L1} vertices\n"
                f"{percentage:.2f}%"
            )
            
            # Start 3 second timer
            end_screen_timer = core.CountdownTimer(3)
            
            
            win_sound_L1.setSound('Assets/sounds/win.mp3', hamming=True)
            win_sound_L1.setVolume(1.0, log=False)
            win_sound_L1.seek(0)
            fail_sound_L1.setSound('Assets/sounds/level_failed.mp3', hamming=True)
            fail_sound_L1.setVolume(1.0, log=False)
            fail_sound_L1.seek(0)
            # store start times for Level_1_checker
            Level_1_checker.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Level_1_checker.tStart = globalClock.getTime(format='float')
            Level_1_checker.status = STARTED
            thisExp.addData('Level_1_checker.started', Level_1_checker.tStart)
            Level_1_checker.maxDuration = None
            # keep track of which components have finished
            Level_1_checkerComponents = Level_1_checker.components
            for thisComponent in Level_1_checker.components:
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
            
            # --- Run Routine "Level_1_checker" ---
            # if trial has changed, end Routine now
            if isinstance(Level_1_Loop, data.TrialHandler2) and thisLevel_1_Loop.thisN != Level_1_Loop.thisTrial.thisN:
                continueRoutine = False
            Level_1_checker.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *end_score_text_L1* updates
                
                # if end_score_text_L1 is starting this frame...
                if end_score_text_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    end_score_text_L1.frameNStart = frameN  # exact frame index
                    end_score_text_L1.tStart = t  # local t and not account for scr refresh
                    end_score_text_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(end_score_text_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    end_score_text_L1.status = STARTED
                    end_score_text_L1.setAutoDraw(True)
                
                # if end_score_text_L1 is active this frame...
                if end_score_text_L1.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from Checker_L1
                # Keep showing the end screen until 3 seconds pass
                if end_screen_timer.getTime() <= 0:
                    continueRoutine = False
                
                
                # *win_sound_L1* updates
                
                # if win_sound_L1 is stopping this frame...
                if win_sound_L1.status == STARTED:
                    if bool(False) or win_sound_L1.isFinished:
                        # keep track of stop time/frame for later
                        win_sound_L1.tStop = t  # not accounting for scr refresh
                        win_sound_L1.tStopRefresh = tThisFlipGlobal  # on global time
                        win_sound_L1.frameNStop = frameN  # exact frame index
                        # update status
                        win_sound_L1.status = FINISHED
                        win_sound_L1.stop()
                
                # *fail_sound_L1* updates
                
                # if fail_sound_L1 is stopping this frame...
                if fail_sound_L1.status == STARTED:
                    if bool(False) or fail_sound_L1.isFinished:
                        # keep track of stop time/frame for later
                        fail_sound_L1.tStop = t  # not accounting for scr refresh
                        fail_sound_L1.tStopRefresh = tThisFlipGlobal  # on global time
                        fail_sound_L1.frameNStop = frameN  # exact frame index
                        # update status
                        fail_sound_L1.status = FINISHED
                        fail_sound_L1.stop()
                
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
                        playbackComponents=[win_sound_L1, fail_sound_L1]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Level_1_checker.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Level_1_checker.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Level_1_checker" ---
            for thisComponent in Level_1_checker.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Level_1_checker
            Level_1_checker.tStop = globalClock.getTime(format='float')
            Level_1_checker.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Level_1_checker.stopped', Level_1_checker.tStop)
            # Run 'End Routine' code from Checker_L1
            
            
            thisExp.addData('Participant ID', expInfo['participant'])
            thisExp.addData('Session', expInfo['session'])
            thisExp.addData('Date', expInfo['date'])
            thisExp.addData('Score', total_touched_vertices_L1)
            thisExp.addData('Percentage', percentage)
            
            filename = f"data/{expInfo['participant']}_summary.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Participant ID', 'Session', 'Date', 'Score', 'Percentage'])
                writer.writerow([expInfo['participant'], expInfo['session'], expInfo['date'], total_touched_vertices_L1, percentage])
            
            # Decide pass/fail and play correct sound
            if percentage >= win_threshold and meatbone_collided:
                Level_1_Loop.finished = True
                win_sound_L1.play()
            else:
                Level_1_Loop.finished = False
                fail_sound_L1.play()
                
            total_touched_vertices_L1 = 0
            total_possible_vertices_L1 = 0
            meatbone_collided = False
            # the Routine "Level_1_checker" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1000.0 repeats of 'Level_1_Loop'
        
        
        # set up handler to look after randomisation of conditions etc
        Level_2_Loop = data.TrialHandler2(
            name='Level_2_Loop',
            nReps=1000.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(Level_2_Loop)  # add the loop to the experiment
        thisLevel_2_Loop = Level_2_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLevel_2_Loop.rgb)
        if thisLevel_2_Loop != None:
            for paramName in thisLevel_2_Loop:
                globals()[paramName] = thisLevel_2_Loop[paramName]
        
        for thisLevel_2_Loop in Level_2_Loop:
            currentLoop = Level_2_Loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisLevel_2_Loop.rgb)
            if thisLevel_2_Loop != None:
                for paramName in thisLevel_2_Loop:
                    globals()[paramName] = thisLevel_2_Loop[paramName]
            
            # --- Prepare to start Routine "Level_2" ---
            # create an object to store info about Routine Level_2
            Level_2 = data.Routine(
                name='Level_2',
                components=[dino_image_L2, floor1_L2, floor2_L2, meatbone_image_L2, score_text_L2, timer_text_L2, lose_sound_L2, eat_sound_L2],
            )
            Level_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from DinoMovement_L2
            dino_pos = [0, -0.3]  # Reset Dino's position
            dino_speed = 0  # Reset vertical speed
            # Initialize the trail dots
            trail_dots = [
                Circle(win, radius=trail_dot_size, fillColor=trail_color, lineColor=None, pos=[-1, -1])
                for _ in range(trail_length)
            ]
            
            # Run 'Begin Routine' code from worldController_L2
            camera_offset_x = 0
            # Run 'Begin Routine' code from GoalController_L2
            score = 0  # Reset the score
            
            meatbone_collided = False
            meatbone_image_L2.opacity = 1
            
            
            wiggle_room = False  
            
            arc1_touched_vertices_L2 = []
            arc2_touched_vertices_L2 = []
            arc3_touched_vertices_L2 = []
            arc4_touched_vertices_L2 = []
            arc5_touched_vertices_L2 = []
            arc6_touched_vertices_L2 = []
            arc7_touched_vertices_L2 = []
            arc8_touched_vertices_L2 = []
            # Run 'Begin Routine' code from Timer_L2
            
            level_timer.reset()  # Reset the timer at the start of the MainGame routine
            
            
            lose_sound_L2.setSound('Assets/sounds/lose.mp3', hamming=True)
            lose_sound_L2.setVolume(1.0, log=False)
            lose_sound_L2.seek(0)
            eat_sound_L2.setSound('Assets/sounds/eat.mp3', hamming=True)
            eat_sound_L2.setVolume(1.0, log=False)
            eat_sound_L2.seek(0)
            # store start times for Level_2
            Level_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Level_2.tStart = globalClock.getTime(format='float')
            Level_2.status = STARTED
            thisExp.addData('Level_2.started', Level_2.tStart)
            Level_2.maxDuration = None
            # keep track of which components have finished
            Level_2Components = Level_2.components
            for thisComponent in Level_2.components:
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
            
            # --- Run Routine "Level_2" ---
            # if trial has changed, end Routine now
            if isinstance(Level_2_Loop, data.TrialHandler2) and thisLevel_2_Loop.thisN != Level_2_Loop.thisTrial.thisN:
                continueRoutine = False
            Level_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *dino_image_L2* updates
                
                # if dino_image_L2 is starting this frame...
                if dino_image_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dino_image_L2.frameNStart = frameN  # exact frame index
                    dino_image_L2.tStart = t  # local t and not account for scr refresh
                    dino_image_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dino_image_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dino_image_L2.status = STARTED
                    dino_image_L2.setAutoDraw(True)
                
                # if dino_image_L2 is active this frame...
                if dino_image_L2.status == STARTED:
                    # update params
                    pass
                
                # *floor1_L2* updates
                
                # if floor1_L2 is starting this frame...
                if floor1_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    floor1_L2.frameNStart = frameN  # exact frame index
                    floor1_L2.tStart = t  # local t and not account for scr refresh
                    floor1_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(floor1_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    floor1_L2.status = STARTED
                    floor1_L2.setAutoDraw(True)
                
                # if floor1_L2 is active this frame...
                if floor1_L2.status == STARTED:
                    # update params
                    pass
                
                # *floor2_L2* updates
                
                # if floor2_L2 is starting this frame...
                if floor2_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    floor2_L2.frameNStart = frameN  # exact frame index
                    floor2_L2.tStart = t  # local t and not account for scr refresh
                    floor2_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(floor2_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    floor2_L2.status = STARTED
                    floor2_L2.setAutoDraw(True)
                
                # if floor2_L2 is active this frame...
                if floor2_L2.status == STARTED:
                    # update params
                    pass
                
                # *meatbone_image_L2* updates
                
                # if meatbone_image_L2 is starting this frame...
                if meatbone_image_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    meatbone_image_L2.frameNStart = frameN  # exact frame index
                    meatbone_image_L2.tStart = t  # local t and not account for scr refresh
                    meatbone_image_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(meatbone_image_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    meatbone_image_L2.status = STARTED
                    meatbone_image_L2.setAutoDraw(True)
                
                # if meatbone_image_L2 is active this frame...
                if meatbone_image_L2.status == STARTED:
                    # update params
                    pass
                
                # *score_text_L2* updates
                
                # if score_text_L2 is starting this frame...
                if score_text_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    score_text_L2.frameNStart = frameN  # exact frame index
                    score_text_L2.tStart = t  # local t and not account for scr refresh
                    score_text_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(score_text_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    score_text_L2.status = STARTED
                    score_text_L2.setAutoDraw(True)
                
                # if score_text_L2 is active this frame...
                if score_text_L2.status == STARTED:
                    # update params
                    pass
                
                # *timer_text_L2* updates
                
                # if timer_text_L2 is starting this frame...
                if timer_text_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer_text_L2.frameNStart = frameN  # exact frame index
                    timer_text_L2.tStart = t  # local t and not account for scr refresh
                    timer_text_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer_text_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    timer_text_L2.status = STARTED
                    timer_text_L2.setAutoDraw(True)
                
                # if timer_text_L2 is active this frame...
                if timer_text_L2.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from DinoMovement_L2
                
                # Initialize key state flags
                left_pressed = False
                right_pressed = False
                up_pressed = False
                
                # Handle input based on the selected control method
                
                # Process keyboard input
                if selected_control == "Keyboard":
                    keys_pressed = kb.getKeys(['left', 'right', 'up'], waitRelease=False, clear=False)
                    for key in keys_pressed:
                        if key.name == 'left':
                            left_pressed = True
                        if key.name == 'right':
                            right_pressed = True
                        if key.name == 'up':
                            up_pressed = True
                            
                # Process PSURP input            
                if selected_control == "PSURP":
                    # Read serial data
                    ser.flushInput()
                    strSerialData = ser.readline()
                    B0ForceInNewtons, B2ForceInNewtons = calculate_psurp_forces(strSerialData)
                
                    # Apply difficulty-specific movement
                    if selected_diff == "1":
                        # Constant movement for Easy mode
                        if B2ForceInNewtons > MIN_FORCE and dino_pos[0] < max_x:
                            dino_pos[0] += 0.005  # Constant movement speed (adjust as needed)
                            dino_image_L2.size = [abs(dino_image_L2.size[0]), dino_image_L2.size[1]]  # Face right
                
                    elif selected_diff == "2":
                        # Proportional movement for Hard mode (current implementation)
                        if B2ForceInNewtons > MIN_FORCE and dino_pos[0] < max_x:
                            move_amount = B2ForceInNewtons * FORCE_MULTIPLIER
                            dino_pos[0] += move_amount  # Movement based on force
                            dino_image_L2.size = [abs(dino_image_L2.size[0]), dino_image_L2.size[1]]  # Face right
                
                    # Jump logic remains the same for both difficulties
                    if B0ForceInNewtons > MIN_FORCE:
                        dino_speed = B0ForceInNewtons * FORCE_MULTIPLIER  # Jump height based on force
                
                
                            
                 
                # Apply gravity to Dino's vertical speed
                dino_speed += gravity
                
                # Check if Dino is on the floor (keeps dino on top of floor)
                if is_on_floor(dino_pos) and dino_speed <= 0:  # Falling or stationary
                    dino_pos[1] = floor1_top + (dino_image_L2.size[1] / 2) - ground_offset  # Align Dino with the floor
                    dino_speed = 0  # Reset vertical speed
                
                # Respawn if Dino falls below the floor threshold
                if dino_pos[1] < fall_threshold:
                    lose_sound_L2.play()
                    continueRoutine = False  # Stop the MainGame routine
                    
                # Jumping logic: Allow jump whenever the 'up' key is pressed
                if up_pressed:  # Check if the up key is pressed
                    dino_speed = jump_speed  # Apply upward movement
                
                # Update Dino's vertical position
                dino_pos[1] += dino_speed
                
                # Continuous horizontal movement
                if left_pressed and dino_pos[0] > min_x:
                    dino_pos[0] -= move_speed  # Move Dino to the left
                    dino_image_L2.size = [-1 * abs(dino_image_L2.size[0]), dino_image_L2.size[1]]
                
                if right_pressed and dino_pos[0] < max_x:
                    dino_pos[0] += move_speed  # Move Dino to the right
                    dino_image_L2.size = [abs(dino_image_L2.size[0]), dino_image_L2.size[1]]  # Reset Dino to face right
                
                # Update Dino's position
                # dino_image_L2.pos = dino_pos  # Use both X and Y values of dino_pos
                dino_image_L2.pos = [dino_pos[0] - camera_offset_x, dino_pos[1]]
                
                # Increment the frame counter for trail updates
                trail_frame_counter += 1
                
                # Check if it's time to spawn a new dot
                if trail_frame_counter >= trail_interval:
                    if len(trail_positions) >= trail_length:
                        trail_positions.pop(0)  # Remove the oldest position if trail is full
                
                    # Add Dino's current position to the trail
                    trail_positions.append(dino_pos[:])  # Add a copy of Dino's current position
                
                    trail_frame_counter = 0  # Reset the counter
                
                # Update the trail dots' positions
                for i, pos in enumerate(trail_positions):
                    trail_dots[i].pos = [pos[0] - camera_offset_x, pos[1]]  # Adjust for camera offset
                
                
                # Update the Dino's animation
                if (frame_index_update_counter % 4) == 0:  # Adjust 4 to control animation speed
                    dino_image_L2.image = frame_paths[frame_index]  # Update the current frame
                
                    # Advance to the next frame
                    frame_index += 1
                    if frame_index >= total_frames:
                        frame_index = 0  # Loop back to the first frame
                
                
                
                # Increment the animation frame counter
                frame_index_update_counter += 1
                
                
                # Run 'Each Frame' code from worldController_L2
                
                # Update the camera offset based on Dino's X position
                camera_offset_x += camera_speed  # The camera offset follows Dino's position
                
                # Move backgrounds relative to Dino's position (seamless wrap-around)
                background1_L2.pos = [-(camera_offset_x % background_width), 0]
                background2_L2.pos = [background1_L2.pos[0] + background_width, 0]
                
                # Update floor positions relative to Dino's position
                floor1_L2.pos = [floor1_pos[0] - camera_offset_x, floor1_L2.pos[1]]
                floor2_L2.pos = [floor2_x_static - camera_offset_x, floor2_L2.pos[1]]  # floor2_L2 moves with Dino
                
                
                # Update meatbone position to match floor2_L2's top
                meatbone_x = floor2_L2.pos[0]  # Update X position based on floor2_L2
                meatbone_y = floor2_top + (meatbone_size[1] / 2) - offset  # Keep the meatbone on top of floor2_L2
                meatbone_image_L2.pos = [meatbone_x, meatbone_y]
                
                
                # Update the arc position relative to the camera offset
                # Update Arc 1 Position
                arc1_L2.pos = [arc1_L2_center[0] - camera_offset_x, arc1_L2_center[1]]
                wiggle_arc1_L2.pos = arc1_L2.pos  # Keep wiggle room on top
                
                # Update Arc 2 Position
                arc2_L2.pos = [arc2_L2_center[0] - camera_offset_x, arc2_L2_center[1]]
                wiggle_arc2_L2.pos = arc2_L2.pos  # Keep wiggle room on top
                arc3_L2.pos = [arc3_L2_center[0] - camera_offset_x, arc3_L2_center[1]]
                wiggle_arc3_L2.pos = arc3_L2.pos  # Keep wiggle room on top
                # Update Arc 4 Position
                arc4_L2.pos = [arc4_L2_center[0] - camera_offset_x, arc4_L2_center[1]]
                wiggle_arc4_L2.pos = arc4_L2.pos  # Keep wiggle room on top
                # Update Arc 5 Position
                arc5_L2.pos = [arc5_L2_center[0] - camera_offset_x, arc5_L2_center[1]]
                wiggle_arc5_L2.pos = arc5_L2.pos  # Keep wiggle room on top
                
                arc6_L2.pos = [arc6_L2_center[0] - camera_offset_x, arc6_L2_center[1]]
                wiggle_arc6_L2.pos = arc6_L2.pos
                
                # Update Arc 7 Position
                arc7_L2.pos = [arc7_L2_center[0] - camera_offset_x, arc7_L2_center[1]]
                wiggle_arc7_L2.pos = arc7_L2.pos
                
                # Update Arc 8 Position
                arc8_L2.pos = [arc8_L2_center[0] - camera_offset_x, arc8_L2_center[1]]
                wiggle_arc8_L2.pos = arc8_L2.pos
                
                
                
                # Draw the backgrounds and floors
                background1_L2.draw()
                background2_L2.draw()
                floor1_L2.draw()
                floor2_L2.draw()
                wiggle_arc1_L2.draw()
                wiggle_arc2_L2.draw()
                wiggle_arc3_L2.draw()
                wiggle_arc4_L2.draw()
                wiggle_arc5_L2.draw()
                wiggle_arc6_L2.draw()
                wiggle_arc7_L2.draw()
                wiggle_arc8_L2.draw()
                
                
                arc1_L2.draw()
                arc2_L2.draw()
                arc3_L2.draw()
                arc4_L2.draw()
                arc5_L2.draw()
                arc6_L2.draw()
                arc7_L2.draw()
                arc8_L2.draw()
                
                # Draw the trail dots
                for dot in trail_dots:
                    dot.draw()
                
                # Run 'Each Frame' code from GoalController_L2
                dino_relative_x = dino_pos[0] - camera_offset_x
                dino_relative_y = dino_pos[1]
                # Check for collision based on proximity to the updated position
                dx = dino_relative_x - meatbone_x
                dy = dino_relative_y - meatbone_y
                
                if camera_offset_x >= max_x:
                    lose_sound_L2.play()
                    continueRoutine = False  # Ends the current routine
                    
                if dino_relative_x < -0.8 or dino_relative_x > 0.8:  # Adjust bounds based on screen width
                    lose_sound_L2.play()
                    continueRoutine = False  # Ends the current routine
                
                # Check for collision for meatbone
                if not meatbone_collided and (dx ** 2 + dy ** 2) ** 0.5 <= meat_collision_threshold:
                    print("Dino ate the meatbone!")
                    meatbone_image_L2.opacity = 0  # Make the meatbone disappear
                    meatbone_collided = True  # Prevent further collision checks
                    eat_sound_L2.play()
                    continueRoutine = False
                
                # Check for collision for ARCS
                for vertex in arc1_L2_vertices:
                    # Adjust Arc 1 vertex for its X-offset (+1)
                    adjusted_vertex_x = vertex[0] + arc1_L2_x   # Move Arc 1 vertices by 1 unit to the right
                    adjusted_vertex_y = vertex[1] + low_arc # Y remains unchanged, apply the same adjustment as Arc 2 if needed
                
                    # Calculate distance between Dino and the adjusted vertex of Arc 1
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L2 and vertex not in arc1_touched_vertices_L2:
                        arc1_touched_vertices_L2.append(vertex)
                        score += 1  # Increment the score for Arc 1
                
                
                for vertex in arc2_L2_vertices:
                    # Adjust Arc 2 vertex for its X-offset (+2)
                    adjusted_vertex_x = vertex[0] + arc2_L2_x   # Move Arc 2 vertices by 2 units to the right
                    adjusted_vertex_y = vertex[1] + low_arc # Y remains unchanged
                    
                    # Calculate distance between Dino and the adjusted vertex of Arc 2
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L2 and vertex not in arc2_touched_vertices_L2:
                        arc2_touched_vertices_L2.append(vertex)
                        score += 1  # Increment the score for Arc 2
                        
                        
                for vertex in arc3_L2_vertices:
                    # Adjust Arc 3 vertex for its static X-offset
                    adjusted_vertex_x = vertex[0] + arc3_L2_x   # Offset Arc 3 vertices by 3.5 units to the right
                    adjusted_vertex_y = vertex[1] + high_arc  # Offset Arc 3 vertices by -0.2 units vertically
                
                    # Calculate distance between Dino and the adjusted vertex of Arc 3
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # Check if Dino is close enough to "touch" the adjusted vertex
                    if distance <= touch_threshold_L2 and vertex not in arc3_touched_vertices_L2:
                        arc3_touched_vertices_L2.append(vertex)
                        score += 1  # Increment the score for Arc 3
                        
                for vertex in arc4_L2_vertices:
                    adjusted_vertex_x = vertex[0] + arc4_L2_x   # Offset Arc 4 vertices
                    adjusted_vertex_y = vertex[1] + low_arc  # Y position remains the same
                
                    # Calculate distance between Dino and Arc 4
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is close enough, count as a touch
                    if distance <= touch_threshold_L2 and vertex not in arc4_touched_vertices_L2:
                        arc4_touched_vertices_L2.append(vertex)
                        score += 1  # Increment score
                
                for vertex in arc5_L2_vertices:
                    adjusted_vertex_x = vertex[0] + arc5_L2_x   # Offset Arc 5 vertices
                    adjusted_vertex_y = vertex[1] + reg_arc  # Y position remains the same
                
                    # Calculate distance between Dino and Arc 5
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is close enough, count as a touch
                    if distance <= touch_threshold_L2 and vertex not in arc5_touched_vertices_L2:
                        arc5_touched_vertices_L2.append(vertex)
                        score += 1  # Increment score
                
                for vertex in arc6_L2_vertices:
                    adjusted_vertex_x = vertex[0] + arc6_L2_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2 and vertex not in arc6_touched_vertices_L2:
                        arc6_touched_vertices_L2.append(vertex)
                        score += 1
                
                # Arc 7 touch detection
                for vertex in arc7_L2_vertices:
                    adjusted_vertex_x = vertex[0] + arc7_L2_x 
                    adjusted_vertex_y = vertex[1] + arc7_L2_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2 and vertex not in arc7_touched_vertices_L2:
                        arc7_touched_vertices_L2.append(vertex)
                        score += 1
                
                # Arc 8 touch detection
                for vertex in arc8_L2_vertices:
                    adjusted_vertex_x = vertex[0] + arc8_L2_x 
                    adjusted_vertex_y = vertex[1] + arc8_L2_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2 and vertex not in arc8_touched_vertices_L2:
                        arc8_touched_vertices_L2.append(vertex)
                        score += 1
                
                # WIGGLE ROOM STUFF
                
                
                # Reset to false at the start of each frame
                wiggle_room = False  
                for vertex in wiggle_arc1_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc1_L2_x 
                    adjusted_vertex_y = vertex[1] + reg_arc 
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L2:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                        
                        
                for vertex in wiggle_arc2_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc2_L2_x 
                    adjusted_vertex_y = vertex[1] + low_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L2:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                        
                        
                        
                for vertex in wiggle_arc3_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc3_L2_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, set to False
                    if distance <= touch_threshold_L2:
                        wiggle_room = True  
                        break  # No need to check further, Dino is inside
                
                
                for vertex in wiggle_arc4_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc4_L2_x   # Offset Arc 4 vertices
                    adjusted_vertex_y = vertex[1] + low_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, mark as safe
                    if distance <= touch_threshold_L2:
                        wiggle_room = True  
                        break  # Stop checking once inside
                
                
                for vertex in wiggle_arc5_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc5_L2_x   # Offset Arc 5 vertices
                    adjusted_vertex_y = vertex[1] + reg_arc
                
                    # Calculate distance between Dino and wiggle room vertex
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                
                    # If Dino is inside the wiggle room, mark as safe
                    if distance <= touch_threshold_L2:
                        wiggle_room = True  
                        break  # Stop checking once inside
                        
                for vertex in wiggle_arc6_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc6_L2_x 
                    adjusted_vertex_y = vertex[1] + high_arc
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2:
                        wiggle_room = True
                        break
                # Arc 7 wiggle room
                for vertex in wiggle_arc7_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc7_L2_x 
                    adjusted_vertex_y = vertex[1] + arc7_L2_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2:
                        wiggle_room = True
                        break
                
                # Arc 8 wiggle room
                for vertex in wiggle_arc8_L2.vertices:
                    adjusted_vertex_x = vertex[0] + arc8_L2_x 
                    adjusted_vertex_y = vertex[1] + arc8_L2_center[1]
                    distance = ((dino_pos[0] - adjusted_vertex_x) ** 2 + (dino_pos[1] - adjusted_vertex_y) ** 2) ** 0.5
                    if distance <= touch_threshold_L2:
                        wiggle_room = True
                        break
                
                        
                        
                score_text_L2.text = str(score) # update Score
                
                
                
                # Run 'Each Frame' code from Timer_L2
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
                
                # Update the timer display
                timer_text_L2.text = str(f"{minutes}:{seconds:02d}")
                
                
                # *lose_sound_L2* updates
                
                # if lose_sound_L2 is stopping this frame...
                if lose_sound_L2.status == STARTED:
                    if bool(False) or lose_sound_L2.isFinished:
                        # keep track of stop time/frame for later
                        lose_sound_L2.tStop = t  # not accounting for scr refresh
                        lose_sound_L2.tStopRefresh = tThisFlipGlobal  # on global time
                        lose_sound_L2.frameNStop = frameN  # exact frame index
                        # update status
                        lose_sound_L2.status = FINISHED
                        lose_sound_L2.stop()
                
                # *eat_sound_L2* updates
                
                # if eat_sound_L2 is stopping this frame...
                if eat_sound_L2.status == STARTED:
                    if bool(False) or eat_sound_L2.isFinished:
                        # keep track of stop time/frame for later
                        eat_sound_L2.tStop = t  # not accounting for scr refresh
                        eat_sound_L2.tStopRefresh = tThisFlipGlobal  # on global time
                        eat_sound_L2.frameNStop = frameN  # exact frame index
                        # update status
                        eat_sound_L2.status = FINISHED
                        eat_sound_L2.stop()
                
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
                        playbackComponents=[lose_sound_L2, eat_sound_L2]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Level_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Level_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Level_2" ---
            for thisComponent in Level_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Level_2
            Level_2.tStop = globalClock.getTime(format='float')
            Level_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Level_2.stopped', Level_2.tStop)
            # Run 'End Routine' code from DinoMovement_L2
            dino_pos = [-0.5, -0.3]  # Reset Dino's position
            trail_positions.clear()  # Remove all stored positions
            # Run 'End Routine' code from GoalController_L2
            global total_touched_vertices_L2, total_possible_vertices_L2
            
            total_touched_vertices_L2 = (
                len(arc1_touched_vertices_L2) + len(arc2_touched_vertices_L2) + len(arc3_touched_vertices_L2) +
                len(arc4_touched_vertices_L2) + len(arc5_touched_vertices_L2) + len(arc6_touched_vertices_L2) +
                len(arc7_touched_vertices_L2) + len(arc8_touched_vertices_L2)
            )
            
            total_possible_vertices_L2 = (
                len(arc1_L2_vertices) + len(arc2_L2_vertices) + len(arc3_L2_vertices) +
                len(arc4_L2_vertices) + len(arc5_L2_vertices) + len(arc6_L2_vertices) +
                len(arc7_L2_vertices) + len(arc8_L2_vertices)
            )
            
            score = 0
            # the Routine "Level_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Level_2_checker" ---
            # create an object to store info about Routine Level_2_checker
            Level_2_checker = data.Routine(
                name='Level_2_checker',
                components=[end_score_text_L2, win_sound_L2, fail_sound_L2],
            )
            Level_2_checker.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Checker_L2
            import csv
            # Calculate the percentage
            if total_possible_vertices_L2 > 0:
                percentage = (total_touched_vertices_L2 / total_possible_vertices_L2) * 100
            else:
                percentage = 0  # Avoid division by zero
                
            
            # Update the text for the end screen
            end_score_text_L2.text = (
                f"You hit {total_touched_vertices_L2} out of {total_possible_vertices_L2} vertices\n"
                f"{percentage:.2f}%"
            )
            
            # Start 3 second timer
            end_screen_timer = core.CountdownTimer(3)
            
            
            win_sound_L2.setSound('Assets/sounds/win.mp3', hamming=True)
            win_sound_L2.setVolume(1.0, log=False)
            win_sound_L2.seek(0)
            fail_sound_L2.setSound('Assets/sounds/level_failed.mp3', hamming=True)
            fail_sound_L2.setVolume(1.0, log=False)
            fail_sound_L2.seek(0)
            # store start times for Level_2_checker
            Level_2_checker.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Level_2_checker.tStart = globalClock.getTime(format='float')
            Level_2_checker.status = STARTED
            thisExp.addData('Level_2_checker.started', Level_2_checker.tStart)
            Level_2_checker.maxDuration = None
            # keep track of which components have finished
            Level_2_checkerComponents = Level_2_checker.components
            for thisComponent in Level_2_checker.components:
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
            
            # --- Run Routine "Level_2_checker" ---
            # if trial has changed, end Routine now
            if isinstance(Level_2_Loop, data.TrialHandler2) and thisLevel_2_Loop.thisN != Level_2_Loop.thisTrial.thisN:
                continueRoutine = False
            Level_2_checker.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *end_score_text_L2* updates
                
                # if end_score_text_L2 is starting this frame...
                if end_score_text_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    end_score_text_L2.frameNStart = frameN  # exact frame index
                    end_score_text_L2.tStart = t  # local t and not account for scr refresh
                    end_score_text_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(end_score_text_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    end_score_text_L2.status = STARTED
                    end_score_text_L2.setAutoDraw(True)
                
                # if end_score_text_L2 is active this frame...
                if end_score_text_L2.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from Checker_L2
                # Keep showing the end screen until 3 seconds pass
                if end_screen_timer.getTime() <= 0:
                    continueRoutine = False
                
                
                # *win_sound_L2* updates
                
                # if win_sound_L2 is stopping this frame...
                if win_sound_L2.status == STARTED:
                    if bool(False) or win_sound_L2.isFinished:
                        # keep track of stop time/frame for later
                        win_sound_L2.tStop = t  # not accounting for scr refresh
                        win_sound_L2.tStopRefresh = tThisFlipGlobal  # on global time
                        win_sound_L2.frameNStop = frameN  # exact frame index
                        # update status
                        win_sound_L2.status = FINISHED
                        win_sound_L2.stop()
                
                # *fail_sound_L2* updates
                
                # if fail_sound_L2 is stopping this frame...
                if fail_sound_L2.status == STARTED:
                    if bool(False) or fail_sound_L2.isFinished:
                        # keep track of stop time/frame for later
                        fail_sound_L2.tStop = t  # not accounting for scr refresh
                        fail_sound_L2.tStopRefresh = tThisFlipGlobal  # on global time
                        fail_sound_L2.frameNStop = frameN  # exact frame index
                        # update status
                        fail_sound_L2.status = FINISHED
                        fail_sound_L2.stop()
                
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
                        playbackComponents=[win_sound_L2, fail_sound_L2]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Level_2_checker.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Level_2_checker.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Level_2_checker" ---
            for thisComponent in Level_2_checker.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Level_2_checker
            Level_2_checker.tStop = globalClock.getTime(format='float')
            Level_2_checker.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Level_2_checker.stopped', Level_2_checker.tStop)
            # Run 'End Routine' code from Checker_L2
            
            
            thisExp.addData('Participant ID', expInfo['participant'])
            thisExp.addData('Session', expInfo['session'])
            thisExp.addData('Date', expInfo['date'])
            thisExp.addData('Score', total_touched_vertices_L2)
            thisExp.addData('Percentage', percentage)
            
            filename = f"data/{expInfo['participant']}_summary.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Participant ID', 'Session', 'Date', 'Score', 'Percentage'])
                writer.writerow([expInfo['participant'], expInfo['session'], expInfo['date'], total_touched_vertices_L2, percentage])
            
            # Decide pass/fail and play correct sound
            if percentage >= win_threshold and meatbone_collided:
                Level_2_Loop.finished = True
                win_sound_L2.play()
            else:
                Level_2_Loop.finished = False
                fail_sound_L2.play()
                
            total_touched_vertices_L2 = 0
            total_possible_vertices_L2 = 0
            meatbone_collided = False
            # the Routine "Level_2_checker" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1000.0 repeats of 'Level_2_Loop'
        
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'GameLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if GameLoop.trialList in ([], [None], None):
        params = []
    else:
        params = GameLoop.trialList[0].keys()
    # save data for this loop
    GameLoop.saveAsText(filename + 'GameLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    # Run 'End Experiment' code from DinoMovement_L1
    """
    ser.flush()
    ser.write("X".encode())  # Exit command mode
    ser.close()
    """
    # Run 'End Experiment' code from DinoMovement_L2
    """
    ser.flush()
    ser.write("X".encode())  # Exit command mode
    ser.close()
    """
    
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
