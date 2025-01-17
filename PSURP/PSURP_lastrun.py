#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on January 14, 2025, at 14:44
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

# Run 'Before Experiment' code from code_trial
Base71Lookup = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'PSURP'  # from the Builder filename that created this script
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
        originPath='C:\\Users\\actioncontrollab\\Desktop\\motor-learning-research-project\\PSURP\\PSURP_lastrun.py',
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
            logging.getLevel('exp')
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
    
    # --- Initialize components for Routine "reset_PSURP" ---
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
    
    # --- Initialize components for Routine "trail" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='Loading forces...',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_trial
    from psychopy import core
    import time
    import serial
    
    ser = serial.Serial("COM4",230400, timeout= 1)
    
    
    
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
    
    # --- Prepare to start Routine "reset_PSURP" ---
    # create an object to store info about Routine reset_PSURP
    reset_PSURP = data.Routine(
        name='reset_PSURP',
        components=[t_reset_PSURP],
    )
    reset_PSURP.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for reset_PSURP
    reset_PSURP.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    reset_PSURP.tStart = globalClock.getTime(format='float')
    reset_PSURP.status = STARTED
    thisExp.addData('reset_PSURP.started', reset_PSURP.tStart)
    reset_PSURP.maxDuration = None
    # keep track of which components have finished
    reset_PSURPComponents = reset_PSURP.components
    for thisComponent in reset_PSURP.components:
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
    
    # --- Run Routine "reset_PSURP" ---
    reset_PSURP.forceEnded = routineForceEnded = not continueRoutine
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
            reset_PSURP.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reset_PSURP.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reset_PSURP" ---
    for thisComponent in reset_PSURP.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for reset_PSURP
    reset_PSURP.tStop = globalClock.getTime(format='float')
    reset_PSURP.tStopRefresh = tThisFlipGlobal
    thisExp.addData('reset_PSURP.stopped', reset_PSURP.tStop)
    # Run 'End Routine' code from code
    ser.flush()
    ser.write("X".encode())
    
    # clear out the data from the IO buffers (Fresh commands)
    # the "X" command puts tje PSURP into command mode
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if reset_PSURP.maxDurationReached:
        routineTimer.addTime(-reset_PSURP.maxDuration)
    elif reset_PSURP.forceEnded:
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
    ser.write("RUNE\n".encode())
    
    # the rune command sets the PSURP to streaming mode. (for getting vals)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if RUNE.maxDurationReached:
        routineTimer.addTime(-RUNE.maxDuration)
    elif RUNE.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "trail" ---
    # create an object to store info about Routine trail
    trail = data.Routine(
        name='trail',
        components=[feedback_text],
    )
    trail.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_trial
    ser.flush()
    
    strMsg = ""
    intCounter = 0
    strSerialData = ""
    
    output = ""
    outputlength = 0
    
    B0HighByte = 0
    B0LowByte = 0
    B0ForceInGrams = 0
    B0ForceInNewtons = 0
    
    B1HighByte = 0
    B1LowByte = 0
    B1ForceInGrams = 0
    B1ForceInNewtons = 0
    
    B2HighByte = 0
    B2LowByte = 0
    B2ForceInGrams = 0
    B2ForceInNewtons = 0
    
    B3HighByte = 0
    B3LowByte = 0
    B3ForceInGrams = 0
    B3ForceInNewtons = 0
    
    B4HighByte = 0
    B4LowByte = 0
    B4ForceInGrams = 0
    B4ForceInNewtons = 0
    # store start times for trail
    trail.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    trail.tStart = globalClock.getTime(format='float')
    trail.status = STARTED
    thisExp.addData('trail.started', trail.tStart)
    trail.maxDuration = None
    # keep track of which components have finished
    trailComponents = trail.components
    for thisComponent in trail.components:
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
    
    # --- Run Routine "trail" ---
    trail.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        
        # if feedback_text is starting this frame...
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            # update status
            feedback_text.status = STARTED
            feedback_text.setAutoDraw(True)
        
        # if feedback_text is active this frame...
        if feedback_text.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_trial
        if intCounter == 0:
            strMsg = ""
            strMsg += "BUT0 BUT1 BUT2 BUT3 BUT4 TTL\n"
            strMsg += "Base 71: 00 00 00 00 00 00\n"
            strMsg += "G: 0000 0000 0000 0000 0000 g\n"
            strMsg += "N: 0.0000 0.0000 0.0000 0.0000 0.0000 N\n"
            strMsg += "Sample: 0000\n"
            strMsg += "Press 'q' to quit.\n"
        
            feedback_text.text = strMsg
            win.flip()
        
        while intCounter < 5000:
            keys = event.getKeys()
            if keys:
                if keys[0] == 'q':  # Quit key (only works during samples)
                    ser.flush()
                    ser.write("X".encode())  
                    ser.flush()
                    ser.close()
                    core.quit()
        
            intCounter = intCounter + 1
            strSerialData = ser.readline()  
        
            strMsg = ""
            strMsg += "BUT0 BUT1 BUT2 BUT3 BUT4 TTL\n"
        
            output = strSerialData.decode()  
            outputlength = len(output)
        
            if outputlength == 12:
                strMsg += "Base 71: " + output[0]
                strMsg += "" + output[1]
                strMsg += "" + output[2]
                strMsg += "" + output[3]
                strMsg += "" + output[4]
                strMsg += "" + output[5]
                strMsg += "" + output[6]
                strMsg += "" + output[7]
                strMsg += "" + output[8]
                strMsg += "" + output[9]
                strMsg += "" + output[10] + "\n\n"
        
                for i in range(71):
                    if Base71Lookup[i] == output[0]:
                        B0HighByte = i
                    if Base71Lookup[i] == output[2]:
                        B1HighByte = i
                    if Base71Lookup[i] == output[4]:
                        B2HighByte = i
                    if Base71Lookup[i] == output[6]:
                        B3HighByte = i
                    if Base71Lookup[i] == output[8]:
                        B4HighByte = i
        
                for i in range(71):
                    if Base71Lookup[i] == output[1]:
                        B0LowByte = i
                    if Base71Lookup[i] == output[3]:
                        B1LowByte = i
                    if Base71Lookup[i] == output[5]:
                        B2LowByte = i
                    if Base71Lookup[i] == output[7]:
                        B3LowByte = i
                    if Base71Lookup[i] == output[9]:
                        B4LowByte = i
        
                B4ForceInGrams = 0
                B4ForceInNewtons = 0
                B0ForceInGrams = ((B0HighByte * 71) + B0LowByte)
                B0ForceInNewtons = B0ForceInGrams * 0.0098
                B1ForceInGrams = ((B1HighByte * 71) + B1LowByte)
                B1ForceInNewtons = B1ForceInGrams * 0.0098
                B2ForceInGrams = ((B2HighByte * 71) + B2LowByte)
                B2ForceInNewtons = B2ForceInGrams * 0.0098
                B3ForceInGrams = ((B3HighByte * 71) + B3LowByte)
                B3ForceInNewtons = B3ForceInGrams * 0.0098
                B4ForceInGrams = ((B4HighByte * 71) + B4LowByte)
                B4ForceInNewtons = B4ForceInGrams * 0.0098
        
                TTL = output[10]
        
                strMsg += "G: {:04d} ".format(B0ForceInGrams)
                strMsg += "{:04d} ".format(B1ForceInGrams)
                strMsg += "{:04d} ".format(B2ForceInGrams)
                strMsg += "{:04d} ".format(B3ForceInGrams)
                strMsg += "{:04d} ".format(B4ForceInGrams)
                strMsg += TTL + "\n\n"
        
                strMsg += "N: {:0.4f} ".format(B0ForceInNewtons)
                strMsg += "{:0.4f} ".format(B1ForceInNewtons)
                strMsg += "{:0.4f} ".format(B2ForceInNewtons)
                strMsg += "{:0.4f} ".format(B3ForceInNewtons)
                strMsg += "{:0.4f} ".format(B4ForceInNewtons)
                strMsg += TTL + "\n\n"
        
                strMsg += "Sample: {:04d}\n\n".format(intCounter)
                strMsg += "Press 'q' to quit."
        
                feedback_text.text = strMsg
        
                ser.reset_input_buffer()  # This clears the serial buffer so it doesn't overfill. This means you will miss samples!
                win.flip()
        
        
        
        
        
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
            trail.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trail.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trail" ---
    for thisComponent in trail.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for trail
    trail.tStop = globalClock.getTime(format='float')
    trail.tStopRefresh = tThisFlipGlobal
    thisExp.addData('trail.stopped', trail.tStop)
    thisExp.nextEntry()
    # the Routine "trail" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from code_trial
    ser.flush()
    ser.write("X".encode())
    ser.flush()
    ser.close()
    
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
