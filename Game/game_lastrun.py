#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on December 19, 2024, at 13:52
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
_winSize = [800,800]
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
        originPath='C:\\Users\\Max Hoac\\Desktop\\Areyan\\motor-learning-research-project\\Game\\game_lastrun.py',
        savePickle=True, saveWideText=True,
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
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


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
    
    # --- Initialize components for Routine "MainGame" ---
    background1 = visual.ImageStim(
        win=win,
        name='background1', 
        image='Assets/7.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    dino_image = visual.ImageStim(
        win=win,
        name='dino_image', 
        image='Assets/dino.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    floor1 = visual.Rect(
        win=win, name='floor1',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(-.5,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    floor2 = visual.Rect(
        win=win, name='floor2',
        width=(.5,0.3)[0], height=(.5,0.3)[1],
        ori=0.0, pos=(0,-.5), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    human_image = visual.ImageStim(
        win=win,
        name='human_image', 
        image='Assets/stickFigure/stick_figure_normal.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    # Run 'Begin Experiment' code from DinoMovement
    from psychopy.hardware import keyboard
    
    # Initialize the Keyboard
    kb = keyboard.Keyboard()
    
    # Dino movement variables
    dino_pos = [-0.5, -0.3]  # Starting position [x, y]
    dino_speed = 0  # Initial vertical speed
    gravity = -0.00006  # Downward acceleration
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
    
    # Run 'Begin Experiment' code from worldController
    from psychopy.visual import Rect, ImageStim
    
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
    
    
    # Run 'Begin Experiment' code from GoalController
    # Human goal size
    human_size = [0.2, 0.2]  # Example size (width, height)
    human_image.size = human_size
    offset = 0.01  # Adjust to align the human properly with floor2
    
    human_collision_image = "Assets\stickFigure\squished.png"
    
    
    human_collided = False
    
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
    
    # --- Prepare to start Routine "MainGame" ---
    # create an object to store info about Routine MainGame
    MainGame = data.Routine(
        name='MainGame',
        components=[background1, dino_image, floor1, floor2, human_image],
    )
    MainGame.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
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
    MainGame.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background1* updates
        
        # if background1 is starting this frame...
        if background1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background1.frameNStart = frameN  # exact frame index
            background1.tStart = t  # local t and not account for scr refresh
            background1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background1.started')
            # update status
            background1.status = STARTED
            background1.setAutoDraw(True)
        
        # if background1 is active this frame...
        if background1.status == STARTED:
            # update params
            pass
        
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
        
        # *human_image* updates
        
        # if human_image is starting this frame...
        if human_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            human_image.frameNStart = frameN  # exact frame index
            human_image.tStart = t  # local t and not account for scr refresh
            human_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(human_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'human_image.started')
            # update status
            human_image.status = STARTED
            human_image.setAutoDraw(True)
        
        # if human_image is active this frame...
        if human_image.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from DinoMovement
        keys_pressed = kb.getKeys(['left', 'right', 'up'], waitRelease=False, clear=False)
        
        # Initialize key state flags
        left_pressed = False
        right_pressed = False
        up_pressed = False
        
        # Update key state flags based on keys currently pressed
        for key in keys_pressed:
            if key.name == 'left':
                left_pressed = True
            if key.name == 'right':
                right_pressed = True
            if key.name == 'up':
                up_pressed = True
        
        # Apply gravity to Dino's vertical speed
        dino_speed += gravity
        
        # Check if Dino is on the floor
        if is_on_floor(dino_pos) and dino_speed <= 0:  # Falling or stationary
            dino_pos[1] = floor1_top + (dino_image.size[1] / 2) - ground_offset  # Align Dino with the floor
            dino_speed = 0  # Reset vertical speed
        
        # Respawn if Dino falls below the floor threshold
        if dino_pos[1] < fall_threshold:
            print("Dino fell below threshold, respawning...")
            dino_pos = respawn_position[:]  # Reset Dino to starting position
            dino_speed = 0  # Reset vertical speed
        
        # Jumping logic: Allow jump whenever the 'up' key is pressed
        if up_pressed:  # Check if the up key is pressed
            dino_speed = jump_speed  # Apply upward movement
        
        # Update Dino's vertical position
        dino_pos[1] += dino_speed
        
        # Continuous horizontal movement
        if left_pressed and dino_pos[0] > min_x:
            dino_pos[0] -= move_speed  # Move Dino to the left
        if right_pressed and dino_pos[0] < max_x:
            dino_pos[0] += move_speed  # Move Dino to the right
        
        # Update Dino's position
        dino_image.pos = [0, dino_pos[1]]  # Center Dino horizontally, only update vertical
        
        
        keys_pressed = kb.getKeys(['o'], waitRelease=False, clear=False)
        if 'o' in [key.name for key in keys_pressed]:
            print(f"Dino Position: X = {dino_pos[0]:.3f}, Y = {dino_pos[1]:.3f}")
        
        # Run 'Each Frame' code from worldController
        # Get Dino's position from your Dino movement code
        # Assume dino_pos[0] tracks Dino's X position (horizontal movement)
        
        # Update the camera offset based on Dino's X position
        camera_offset_x = dino_pos[0]  # The camera offset follows Dino's position
        
        # Move backgrounds relative to Dino's position (seamless wrap-around)
        background1.pos = [-(camera_offset_x % background_width), 0]
        background2.pos = [background1.pos[0] + background_width, 0]
        
        # Update floor positions relative to Dino's position
        floor1.pos = [floor1_pos[0] - camera_offset_x, floor1.pos[1]]  # Floor1 moves with Dino
        floor2.pos = [floor2_x_static - camera_offset_x, floor2.pos[1]]  # Floor2 moves with Dino
        
        # Draw the backgrounds and floors
        background1.draw()
        background2.draw()
        floor1.draw()
        floor2.draw()
        
        """
        # Debugging: Check positions if needed
        if 'p' in kb.getKeys(['p'], waitRelease=False):
            print(f"Background1 Position: {background1.pos}, Background2 Position: {background2.pos}")
            print(f"Floor1 Position: {floor1.pos}, Floor2 Position: {floor2.pos}")
            print(f"Dino Position: {dino_pos}")
        
        """
        # Run 'Each Frame' code from GoalController
        # Update human position to match floor2's top
        human_x = floor2.pos[0]  # Update X position based on floor2
        human_y = floor2_top + (human_size[1] / 2) - offset  # Keep the human on top of floor2
        
        human_pos = [human_x, human_y]
        human_image.pos = human_pos
        
        
        if not human_collided and -0.05 <= human_x <= 0.05 and -0.140 <= dino_pos[1] <= -0.125:
            print("Dino stomped the human!")
            human_image.image = human_collision_image  # Change to collision image 
            human_collided = True  # Set collision flag to prevent further updates
        
        # Check if the 'p' key is pressed to print human position
        keys_pressed = kb.getKeys(['p'], waitRelease=False)
        if 'p' in [key.name for key in keys_pressed]:
            print(f"Human Position: X = {human_pos[0]:.3f}, Y = {human_pos[1]:.3f}")
         
        
        
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
    thisExp.nextEntry()
    # the Routine "MainGame" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
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
    logging.flush()


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
    logging.flush()
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
