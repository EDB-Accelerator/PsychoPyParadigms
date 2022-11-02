/************* 
 * Door Test *
 *************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'door';  // from the Builder filename that created this script
let expInfo = {'sdan': '', 'session': '001', 'version': '1'};

// Start code blocks for 'Before Experiment'


function randomGet(start, end) {
    return Math.random() * (end - start) + start;
}
document.addEventListener('contextmenu',event => event.preventDefault());
timer = new util.Clock();


// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trials_12LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_12LoopBegin, trials_12LoopScheduler);
flowScheduler.add(trials_12LoopScheduler);
flowScheduler.add(trials_12LoopEnd);
const trials_1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_1LoopBegin, trials_1LoopScheduler);
flowScheduler.add(trials_1LoopScheduler);
flowScheduler.add(trials_1LoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const trials_11LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_11LoopBegin, trials_11LoopScheduler);
flowScheduler.add(trials_11LoopScheduler);
flowScheduler.add(trials_11LoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'img/doors1/p6r3.jpg', 'path': 'img/doors1/p6r3.jpg'},
    {'name': 'img/outcomes/7_reward.jpg', 'path': 'img/outcomes/7_reward.jpg'},
    {'name': 'img/doors2/p4r6.jpg', 'path': 'img/doors2/p4r6.jpg'},
    {'name': 'img/doors2/p6r7.jpg', 'path': 'img/doors2/p6r7.jpg'},
    {'name': 'instruction/start_task.jpg', 'path': 'instruction/start_task.jpg'},
    {'name': 'img/outcomes/2_punishment.jpg', 'path': 'img/outcomes/2_punishment.jpg'},
    {'name': 'img/doors1/p5r4.jpg', 'path': 'img/doors1/p5r4.jpg'},
    {'name': 'img/doors2/p7r5.jpg', 'path': 'img/doors2/p7r5.jpg'},
    {'name': 'img/doors1/p2r4.jpg', 'path': 'img/doors1/p2r4.jpg'},
    {'name': 'img/doors1/p7r1.jpg', 'path': 'img/doors1/p7r1.jpg'},
    {'name': 'img/outcomes/3_reward.jpg', 'path': 'img/outcomes/3_reward.jpg'},
    {'name': 'img/doors1/p2r3.jpg', 'path': 'img/doors1/p2r3.jpg'},
    {'name': 'img/doors2/p7r4.jpg', 'path': 'img/doors2/p7r4.jpg'},
    {'name': 'img/practice_outcome.jpg', 'path': 'img/practice_outcome.jpg'},
    {'name': 'img/doors2/p2r2.jpg', 'path': 'img/doors2/p2r2.jpg'},
    {'name': 'img/iti.jpg', 'path': 'img/iti.jpg'},
    {'name': 'img/outcomes/7_punishment.jpg', 'path': 'img/outcomes/7_punishment.jpg'},
    {'name': 'img/doors2/p7r3.jpg', 'path': 'img/doors2/p7r3.jpg'},
    {'name': 'instruction/ratings.jpg', 'path': 'instruction/ratings.jpg'},
    {'name': 'img/doors2/p3r6.jpg', 'path': 'img/doors2/p3r6.jpg'},
    {'name': 'instruction/practice_start.jpg', 'path': 'instruction/practice_start.jpg'},
    {'name': 'img/finalReward.jpg', 'path': 'img/finalReward.jpg'},
    {'name': 'img/doors1/p7r3.jpg', 'path': 'img/doors1/p7r3.jpg'},
    {'name': 'img/doors1/p4r6.jpg', 'path': 'img/doors1/p4r6.jpg'},
    {'name': 'img/doors1/p3r6.jpg', 'path': 'img/doors1/p3r6.jpg'},
    {'name': 'instruction/finish_1.30.20.JPG', 'path': 'instruction/finish_1.30.20.JPG'},
    {'name': 'img/doors2/p2r7.jpg', 'path': 'img/doors2/p2r7.jpg'},
    {'name': 'instruction/practice_inst.jpg', 'path': 'instruction/practice_inst.jpg'},
    {'name': 'img/doors2/p6r3.jpg', 'path': 'img/doors2/p6r3.jpg'},
    {'name': 'img/doors2/p2r5.jpg', 'path': 'img/doors2/p2r5.jpg'},
    {'name': 'img/doors2/p7r6.jpg', 'path': 'img/doors2/p7r6.jpg'},
    {'name': 'instruction/Slide5.jpg', 'path': 'instruction/Slide5.jpg'},
    {'name': 'img/after_VAS.jpg', 'path': 'img/after_VAS.jpg'},
    {'name': 'instruction/Slide7.jpg', 'path': 'instruction/Slide7.jpg'},
    {'name': 'img/doors1/p4r4.jpg', 'path': 'img/doors1/p4r4.jpg'},
    {'name': 'img/doors1/p1r3.jpg', 'path': 'img/doors1/p1r3.jpg'},
    {'name': 'img/doors1/p6r4.jpg', 'path': 'img/doors1/p6r4.jpg'},
    {'name': 'img/title.jpg', 'path': 'img/title.jpg'},
    {'name': 'img/doors2/p1r5.jpg', 'path': 'img/doors2/p1r5.jpg'},
    {'name': 'sound/reward.wav', 'path': 'sound/reward.wav'},
    {'name': 'instruction/Slide9.jpg', 'path': 'instruction/Slide9.jpg'},
    {'name': 'img/start_main_game.jpg', 'path': 'img/start_main_game.jpg'},
    {'name': 'img/doors1/p3r1.jpg', 'path': 'img/doors1/p3r1.jpg'},
    {'name': 'img/outcomes/1_punishment.jpg', 'path': 'img/outcomes/1_punishment.jpg'},
    {'name': 'img/doors2/p4r5.jpg', 'path': 'img/doors2/p4r5.jpg'},
    {'name': 'instruction/Slide4.jpg', 'path': 'instruction/Slide4.jpg'},
    {'name': 'instruction/Slide12.jpg', 'path': 'instruction/Slide12.jpg'},
    {'name': 'img/doors2/p1r2.jpg', 'path': 'img/doors2/p1r2.jpg'},
    {'name': 'instruction/Slide11.jpg', 'path': 'instruction/Slide11.jpg'},
    {'name': 'img/doors2/p2r1.jpg', 'path': 'img/doors2/p2r1.jpg'},
    {'name': 'img/doors1/p3r2.jpg', 'path': 'img/doors1/p3r2.jpg'},
    {'name': 'img/doors1/p7r6.jpg', 'path': 'img/doors1/p7r6.jpg'},
    {'name': 'img/outcomes/5_punishment.jpg', 'path': 'img/outcomes/5_punishment.jpg'},
    {'name': 'instruction/rest_slide.jpg', 'path': 'instruction/rest_slide.jpg'},
    {'name': 'img/doors1/p3r3.jpg', 'path': 'img/doors1/p3r3.jpg'},
    {'name': 'img/doors1/p4r3.jpg', 'path': 'img/doors1/p4r3.jpg'},
    {'name': 'img/fortuneResult18.jpg', 'path': 'img/fortuneResult18.jpg'},
    {'name': 'img/outcomes/1_reward.jpg', 'path': 'img/outcomes/1_reward.jpg'},
    {'name': 'video/18.mp4', 'path': 'video/18.mp4'},
    {'name': 'img/doors1/p7r7.jpg', 'path': 'img/doors1/p7r7.jpg'},
    {'name': 'video/16.mp4', 'path': 'video/16.mp4'},
    {'name': 'img/doors1/p5r3.jpg', 'path': 'img/doors1/p5r3.jpg'},
    {'name': 'img/doors1/p1r6.jpg', 'path': 'img/doors1/p1r6.jpg'},
    {'name': 'img/doors1/p1r7.jpg', 'path': 'img/doors1/p1r7.jpg'},
    {'name': 'img/doors2/p2r4.jpg', 'path': 'img/doors2/p2r4.jpg'},
    {'name': 'img/doors2/p1r1.jpg', 'path': 'img/doors2/p1r1.jpg'},
    {'name': 'instruction/Slide10.jpg', 'path': 'instruction/Slide10.jpg'},
    {'name': 'img/doors2/p4r7.jpg', 'path': 'img/doors2/p4r7.jpg'},
    {'name': 'img/doors1/p5r7.jpg', 'path': 'img/doors1/p5r7.jpg'},
    {'name': 'instruction/Slide2.jpg', 'path': 'instruction/Slide2.jpg'},
    {'name': 'img/doors1/p4r7.jpg', 'path': 'img/doors1/p4r7.jpg'},
    {'name': 'instruction/Slide14.jpg', 'path': 'instruction/Slide14.jpg'},
    {'name': 'img/doors1/p5r6.jpg', 'path': 'img/doors1/p5r6.jpg'},
    {'name': 'img/doors1/p2r1.jpg', 'path': 'img/doors1/p2r1.jpg'},
    {'name': 'img/doors1/p3r7.jpg', 'path': 'img/doors1/p3r7.jpg'},
    {'name': 'img/doors2/p5r5.jpg', 'path': 'img/doors2/p5r5.jpg'},
    {'name': 'img/outcomes/2_reward.jpg', 'path': 'img/outcomes/2_reward.jpg'},
    {'name': 'img/doors2/p1r4.jpg', 'path': 'img/doors2/p1r4.jpg'},
    {'name': 'img/doors2/p3r7.jpg', 'path': 'img/doors2/p3r7.jpg'},
    {'name': 'img/doors1/p7r5.jpg', 'path': 'img/doors1/p7r5.jpg'},
    {'name': 'instruction/Slide3.jpg', 'path': 'instruction/Slide3.jpg'},
    {'name': 'img/doors2/p6r4.jpg', 'path': 'img/doors2/p6r4.jpg'},
    {'name': 'img/doors1/p1r2.jpg', 'path': 'img/doors1/p1r2.jpg'},
    {'name': 'img/doors1/p1r4.jpg', 'path': 'img/doors1/p1r4.jpg'},
    {'name': 'img/doors2/p3r2.jpg', 'path': 'img/doors2/p3r2.jpg'},
    {'name': 'instruction/Slide0.jpg', 'path': 'instruction/Slide0.jpg'},
    {'name': 'img/doors2/p3r3.jpg', 'path': 'img/doors2/p3r3.jpg'},
    {'name': 'img/rest.jpg', 'path': 'img/rest.jpg'},
    {'name': 'img/doors1/p2r6.jpg', 'path': 'img/doors1/p2r6.jpg'},
    {'name': 'img/practice_door.jpg', 'path': 'img/practice_door.jpg'},
    {'name': 'img/doors2/p5r3.jpg', 'path': 'img/doors2/p5r3.jpg'},
    {'name': 'instruction/Slide13.jpg', 'path': 'instruction/Slide13.jpg'},
    {'name': 'img/doors2/p4r4.jpg', 'path': 'img/doors2/p4r4.jpg'},
    {'name': 'img/doors2/p2r3.jpg', 'path': 'img/doors2/p2r3.jpg'},
    {'name': 'instruction/end_slide.jpg', 'path': 'instruction/end_slide.jpg'},
    {'name': 'img/fortuneResult16.jpg', 'path': 'img/fortuneResult16.jpg'},
    {'name': 'sound/punishment.wav', 'path': 'sound/punishment.wav'},
    {'name': 'img/doors1/p6r2.jpg', 'path': 'img/doors1/p6r2.jpg'},
    {'name': 'img/doors2/p5r4.jpg', 'path': 'img/doors2/p5r4.jpg'},
    {'name': 'img/doors2/p4r2.jpg', 'path': 'img/doors2/p4r2.jpg'},
    {'name': 'img/doors1/p7r2.jpg', 'path': 'img/doors1/p7r2.jpg'},
    {'name': 'img/doors2/p6r2.jpg', 'path': 'img/doors2/p6r2.jpg'},
    {'name': 'img/doors2/p5r7.jpg', 'path': 'img/doors2/p5r7.jpg'},
    {'name': 'img/doors2/p1r3.jpg', 'path': 'img/doors2/p1r3.jpg'},
    {'name': 'img/doors2/p6r1.jpg', 'path': 'img/doors2/p6r1.jpg'},
    {'name': 'img/doors2/p5r2.jpg', 'path': 'img/doors2/p5r2.jpg'},
    {'name': 'instruction/start_main_game.jpg', 'path': 'instruction/start_main_game.jpg'},
    {'name': 'img/outcomes/6_reward.jpg', 'path': 'img/outcomes/6_reward.jpg'},
    {'name': 'img/outcomes/5_reward.jpg', 'path': 'img/outcomes/5_reward.jpg'},
    {'name': 'img/outcomes/4_reward.jpg', 'path': 'img/outcomes/4_reward.jpg'},
    {'name': 'img/doors2/p6r5.jpg', 'path': 'img/doors2/p6r5.jpg'},
    {'name': 'img/doors1/p1r5.jpg', 'path': 'img/doors1/p1r5.jpg'},
    {'name': 'img/doors1/p5r2.jpg', 'path': 'img/doors1/p5r2.jpg'},
    {'name': 'img/doors1/p6r6.jpg', 'path': 'img/doors1/p6r6.jpg'},
    {'name': 'img/doors2/p2r6.jpg', 'path': 'img/doors2/p2r6.jpg'},
    {'name': 'img/doors1/p6r7.jpg', 'path': 'img/doors1/p6r7.jpg'},
    {'name': 'img/outcomes/3_punishment.jpg', 'path': 'img/outcomes/3_punishment.jpg'},
    {'name': 'img/doors1/p7r4.jpg', 'path': 'img/doors1/p7r4.jpg'},
    {'name': 'img/outcomes/6_punishment.jpg', 'path': 'img/outcomes/6_punishment.jpg'},
    {'name': 'img/doors1/p3r4.jpg', 'path': 'img/doors1/p3r4.jpg'},
    {'name': 'img/VASCheck.jpg', 'path': 'img/VASCheck.jpg'},
    {'name': 'img/doors1/p4r2.jpg', 'path': 'img/doors1/p4r2.jpg'},
    {'name': 'instruction/Slide16.jpg', 'path': 'instruction/Slide16.jpg'},
    {'name': 'img/doors1/p4r1.jpg', 'path': 'img/doors1/p4r1.jpg'},
    {'name': 'img/doors1/p2r5.jpg', 'path': 'img/doors1/p2r5.jpg'},
    {'name': 'img/doors1/p4r5.jpg', 'path': 'img/doors1/p4r5.jpg'},
    {'name': 'instruction/Slide8.jpg', 'path': 'instruction/Slide8.jpg'},
    {'name': 'img/doors1/p2r7.jpg', 'path': 'img/doors1/p2r7.jpg'},
    {'name': 'img/doors1/p5r5.jpg', 'path': 'img/doors1/p5r5.jpg'},
    {'name': 'img/doors2/p3r1.jpg', 'path': 'img/doors2/p3r1.jpg'},
    {'name': 'video/16b.mp4', 'path': 'video/16b.mp4'},
    {'name': 'img/doors1/p6r1.jpg', 'path': 'img/doors1/p6r1.jpg'},
    {'name': 'img/doors2/p4r1.jpg', 'path': 'img/doors2/p4r1.jpg'},
    {'name': 'img/outcomes/4_punishment.jpg', 'path': 'img/outcomes/4_punishment.jpg'},
    {'name': 'img/doors2/p7r2.jpg', 'path': 'img/doors2/p7r2.jpg'},
    {'name': 'img/doors1/p1r1.jpg', 'path': 'img/doors1/p1r1.jpg'},
    {'name': 'img/doors2/p4r3.jpg', 'path': 'img/doors2/p4r3.jpg'},
    {'name': 'img/doors1/p6r5.jpg', 'path': 'img/doors1/p6r5.jpg'},
    {'name': 'img/doors1/p2r2.jpg', 'path': 'img/doors1/p2r2.jpg'},
    {'name': 'img/doors2/p6r6.jpg', 'path': 'img/doors2/p6r6.jpg'},
    {'name': 'img/doors2/p5r6.jpg', 'path': 'img/doors2/p5r6.jpg'},
    {'name': 'img/doors2/p1r6.jpg', 'path': 'img/doors2/p1r6.jpg'},
    {'name': 'img/doors1/p3r5.jpg', 'path': 'img/doors1/p3r5.jpg'},
    {'name': 'img/doors2/p7r1.jpg', 'path': 'img/doors2/p7r1.jpg'},
    {'name': 'img/doors2/p5r1.jpg', 'path': 'img/doors2/p5r1.jpg'},
    {'name': 'img/doors2/p1r7.jpg', 'path': 'img/doors2/p1r7.jpg'},
    {'name': 'instruction/Slide6.jpg', 'path': 'instruction/Slide6.jpg'},
    {'name': 'img/doors2/p3r5.jpg', 'path': 'img/doors2/p3r5.jpg'},
    {'name': 'instruction/practice_inst2.jpg', 'path': 'instruction/practice_inst2.jpg'},
    {'name': 'instruction/Slide1.jpg', 'path': 'instruction/Slide1.jpg'},
    {'name': 'img/doors1/p5r1.jpg', 'path': 'img/doors1/p5r1.jpg'},
    {'name': 'img/doors2/p7r7.jpg', 'path': 'img/doors2/p7r7.jpg'},
    {'name': 'instruction/Slide15.jpg', 'path': 'instruction/Slide15.jpg'},
    {'name': 'img/doors2/p3r4.jpg', 'path': 'img/doors2/p3r4.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var titleScreenClock;
var key_resp;
var image;
var timer;
var win;
var widthBank;
var heightBank;
var size_diff;
var doorOpenChanceMap;
var vasPreClock;
var vasPreCount;
var vasQuestionText;
var vasLabelText1;
var vasLabelText2;
var slider_2;
var vas_question_pre;
var vas_label1_pre;
var vas_label2_pre;
var key_resp_15;
var vasPreRecordClock;
var instructionClock;
var count;
var imgFile;
var key_resp_2;
var image_2;
var practiceClock;
var key_resp_3;
var mouse;
var level;
var width;
var height;
var img;
var practiceAnticipationClock;
var key_resp_9;
var practiceAwardClock;
var imgAward;
var practiceITIClock;
var imageITI;
var fortuneWheelClock;
var trialsCount;
var fortuneVideo;
var fortuneWheelResultImg;
var fortuneWheelResultClock;
var key_resp_5;
var image_3;
var doorImgShuffleClock;
var imgDir;
var imgList;
var pList;
var rList;
var doorStartScreenClock;
var image_4;
var key_resp_8;
var doorInitClock;
var doorClock;
var mouse_2;
var key_resp_7;
var imgDoor;
var doorAnticipationClock;
var key_resp_10;
var awardImg;
var rewardVSpunishment;
var awardClock;
var image_door_award;
var sound_1;
var noAwardClock;
var itiClock;
var image_5;
var restScreenClock;
var image_6;
var key_resp_11;
var vasClock;
var slider;
var vas_question;
var vas_label1;
var vas_label2;
var key_resp_14;
var vasRecordClock;
var afterVASClock;
var image_7;
var key_resp_12;
var finalRewardClock;
var image_8;
var key_resp_13;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "titleScreen"
  titleScreenClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'pix', 
    image : 'img/title.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  timer  = new util.Clock();
  win = psychoJS.window
  
  
  widthBank = []
  heightBank = []
  size_diff = 1/65;
  
  function pow(base, exponent) {
      return Math.pow(base, exponent);
  }
  
  for (var level1 = 0, _pj_a = 101; (level1 < _pj_a); level1 += 1) {
      width = (1024 * (0.1 + ((pow(level1, 1.7) * size_diff) * 0.05)));
      height = (768 * (0.1 + ((pow(level1, 1.7) * size_diff) * 0.05)));
      widthBank.push(width);
      heightBank.push(height);
  }
  
  doorOpenChanceMap = [0.007, 0.008, 0.009, 0.011, 0.012, 0.014, 0.016, 0.018, 0.02 ,
         0.023, 0.026, 0.029, 0.032, 0.036, 0.04 , 0.045, 0.049, 0.055,
         0.061, 0.067, 0.074, 0.081, 0.089, 0.097, 0.106, 0.115, 0.125,
         0.136, 0.147, 0.159, 0.171, 0.184, 0.198, 0.212, 0.227, 0.242,
         0.258, 0.274, 0.291, 0.309, 0.326, 0.345, 0.363, 0.382, 0.401,
         0.421, 0.44 , 0.46 , 0.48 , 0.5  , 0.52 , 0.54 , 0.56 , 0.579,
         0.599, 0.618, 0.637, 0.655, 0.674, 0.691, 0.709, 0.726, 0.742,
         0.758, 0.773, 0.788, 0.802, 0.816, 0.829, 0.841, 0.853, 0.864,
         0.875, 0.885, 0.894, 0.903, 0.911, 0.919, 0.926, 0.933, 0.939,
         0.945, 0.951, 0.955, 0.96 , 0.964, 0.968, 0.971, 0.974, 0.977,
         0.98 , 0.982, 0.984, 0.986, 0.988, 0.989, 0.991, 0.992, 0.993,
         0.994, 1.   ];
  // Initialize components for Routine "vasPre"
  vasPreClock = new util.Clock();
  vasPreCount = 0;
  vasQuestionText = "How anxious do you feel right now?";
  vasLabelText1 = "Not anxious";
  vasLabelText2 = "Very anxious";
  
  slider_2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_2',
    size: [1.0, 0.1], pos: [0, (- 0.3)], units: 'height',
    labels: undefined, ticks: [0, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color('LightGray'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  vas_question_pre = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_question_pre',
    text: '',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, 0.3], height: 0.12,  wrapWidth: 2.0, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  vas_label1_pre = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_label1_pre',
    text: '',
    font: 'Open Sans',
    units: 'pix', 
    pos: [(- 380), (- 170)], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  vas_label2_pre = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_label2_pre',
    text: '',
    font: 'Open Sans',
    units: 'pix', 
    pos: [380, (- 170)], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "vasPreRecord"
  vasPreRecordClock = new util.Clock();
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  count = 0;
  imgFile = (("instruction/Slide" + count.toString()) + ".jpg");
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "practice"
  practiceClock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  level = 50;
  width = widthBank[level];
  height = heightBank[level];
  img = new visual.ImageStim({"win": win, "image": "img/practice_door.jpg", "units": "pix", "size": [width, height]});
  
  
  
  // Initialize components for Routine "practiceAnticipation"
  practiceAnticipationClock = new util.Clock();
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceAward"
  practiceAwardClock = new util.Clock();
  imgAward = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgAward', units : 'pix', 
    image : 'img/practice_outcome.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "practiceITI"
  practiceITIClock = new util.Clock();
  imageITI = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageITI', units : 'pix', 
    image : 'img/iti.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "fortuneWheel"
  fortuneWheelClock = new util.Clock();
  trialsCount = 0;
  fortuneVideo = "video/18.mp4";
  
  fortuneWheelResultImg = "img/fortuneResult18.jpg";
  
  // Initialize components for Routine "fortuneWheelResult"
  fortuneWheelResultClock = new util.Clock();
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "doorImgShuffle"
  doorImgShuffleClock = new util.Clock();
  level = 50;
  width = widthBank[level];
  height = heightBank[level];
  doorOpenChanceMap = [0.007, 0.008, 0.009, 0.011, 0.012, 0.014, 0.016, 0.018, 0.02, 0.023, 0.026, 0.029, 0.032, 0.036, 0.04, 0.045, 0.049, 0.055, 0.061, 0.067, 0.074, 0.081, 0.089, 0.097, 0.106, 0.115, 0.125, 0.136, 0.147, 0.159, 0.171, 0.184, 0.198, 0.212, 0.227, 0.242, 0.258, 0.274, 0.291, 0.309, 0.326, 0.345, 0.363, 0.382, 0.401, 0.421, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.579, 0.599, 0.618, 0.637, 0.655, 0.674, 0.691, 0.709, 0.726, 0.742, 0.758, 0.773, 0.788, 0.802, 0.816, 0.829, 0.841, 0.853, 0.864, 0.875, 0.885, 0.894, 0.903, 0.911, 0.919, 0.926, 0.933, 0.939, 0.945, 0.951, 0.955, 0.96, 0.964, 0.968, 0.971, 0.974, 0.977, 0.98, 0.982, 0.984, 0.986, 0.988, 0.989, 0.991, 0.992, 0.993, 0.994, 1.0];
  if ((expInfo["version"] === 1)) {
      imgDir = "img/doors1/";
      imgList = ["img/doors1/p6r3.jpg", "img/doors1/p4r1.jpg", "img/doors1/p2r7.jpg", "img/doors1/p2r6.jpg", "img/doors1/p6r2.jpg", "img/doors1/p4r2.jpg", "img/doors1/p2r4.jpg", "img/doors1/p2r5.jpg", "img/doors1/p4r3.jpg", "img/doors1/p6r1.jpg", "img/doors1/p6r5.jpg", "img/doors1/p4r7.jpg", "img/doors1/p2r1.jpg", "img/doors1/p4r6.jpg", "img/doors1/p6r4.jpg", "img/doors1/p6r6.jpg", "img/doors1/p4r4.jpg", "img/doors1/p2r2.jpg", "img/doors1/p2r3.jpg", "img/doors1/p4r5.jpg", "img/doors1/p6r7.jpg", "img/doors1/p1r6.jpg", "img/doors1/p3r4.jpg", "img/doors1/p5r2.jpg", "img/doors1/p7r1.jpg", "img/doors1/p5r3.jpg", "img/doors1/p3r5.jpg", "img/doors1/p1r7.jpg", "img/doors1/p1r5.jpg", "img/doors1/p3r7.jpg", "img/doors1/p5r1.jpg", "img/doors1/p7r3.jpg", "img/doors1/p7r2.jpg", "img/doors1/p3r6.jpg", "img/doors1/p1r4.jpg", "img/doors1/p3r2.jpg", "img/doors1/p5r4.jpg", "img/doors1/p7r6.jpg", "img/doors1/p7r7.jpg", "img/doors1/p5r5.jpg", "img/doors1/p3r3.jpg", "img/doors1/p1r1.jpg", "img/doors1/p1r3.jpg", "img/doors1/p3r1.jpg", "img/doors1/p5r7.jpg", "img/doors1/p7r5.jpg", "img/doors1/p7r4.jpg", "img/doors1/p5r6.jpg", "img/doors1/p1r2.jpg"];
      pList = ["6", "4", "2", "2", "6", "4", "2", "2", "4", "6", "6", "4", "2", "4", "6", "6", "4", "2", "2", "4", "6", "1", "3", "5", "7", "5", "3", "1", "1", "3", "5", "7", "7", "3", "1", "3", "5", "7", "7", "5", "3", "1", "1", "3", "5", "7", "7", "5", "1"];
      rList = ["3", "1", "7", "6", "2", "2", "4", "5", "3", "1", "5", "7", "1", "6", "4", "6", "4", "2", "3", "5", "7", "6", "4", "2", "1", "3", "5", "7", "5", "7", "1", "3", "2", "6", "4", "2", "4", "6", "7", "5", "3", "1", "3", "1", "7", "5", "4", "6", "2"];
  } else {
      imgDir = "img/doors2/";
      imgList = ["img/doors2/p6r3.jpg", "img/doors2/p4r1.jpg", "img/doors2/p2r7.jpg", "img/doors2/p2r6.jpg", "img/doors2/p6r2.jpg", "img/doors2/p4r2.jpg", "img/doors2/p2r4.jpg", "img/doors2/p2r5.jpg", "img/doors2/p4r3.jpg", "img/doors2/p6r1.jpg", "img/doors2/p6r5.jpg", "img/doors2/p4r7.jpg", "img/doors2/p2r1.jpg", "img/doors2/p4r6.jpg", "img/doors2/p6r4.jpg", "img/doors2/p6r6.jpg", "img/doors2/p4r4.jpg", "img/doors2/p2r2.jpg", "img/doors2/p2r3.jpg", "img/doors2/p4r5.jpg", "img/doors2/p6r7.jpg", "img/doors2/p1r6.jpg", "img/doors2/p3r4.jpg", "img/doors2/p5r2.jpg", "img/doors2/p7r1.jpg", "img/doors2/p5r3.jpg", "img/doors2/p3r5.jpg", "img/doors2/p1r7.jpg", "img/doors2/p1r5.jpg", "img/doors2/p3r7.jpg", "img/doors2/p5r1.jpg", "img/doors2/p7r3.jpg", "img/doors2/p7r2.jpg", "img/doors2/p3r6.jpg", "img/doors2/p1r4.jpg", "img/doors2/p3r2.jpg", "img/doors2/p5r4.jpg", "img/doors2/p7r6.jpg", "img/doors2/p7r7.jpg", "img/doors2/p5r5.jpg", "img/doors2/p3r3.jpg", "img/doors2/p1r1.jpg", "img/doors2/p1r3.jpg", "img/doors2/p3r1.jpg", "img/doors2/p5r7.jpg", "img/doors2/p7r5.jpg", "img/doors2/p7r4.jpg", "img/doors2/p5r6.jpg", "img/doors2/p1r2.jpg"];
      pList = ["6", "4", "2", "2", "6", "4", "2", "2", "4", "6", "6", "4", "2", "4", "6", "6", "4", "2", "2", "4", "6", "1", "3", "5", "7", "5", "3", "1", "1", "3", "5", "7", "7", "3", "1", "3", "5", "7", "7", "5", "3", "1", "1", "3", "5", "7", "7", "5", "1"];
      rList = ["3", "1", "7", "6", "2", "2", "4", "5", "3", "1", "5", "7", "1", "6", "4", "6", "4", "2", "3", "5", "7", "6", "4", "2", "1", "3", "5", "7", "5", "7", "1", "3", "2", "6", "4", "2", "4", "6", "7", "5", "3", "1", "3", "1", "7", "5", "4", "6", "2"];
  }
  
  
  
  // Initialize components for Routine "doorStartScreen"
  doorStartScreenClock = new util.Clock();
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : 'pix', 
    image : 'img/start_main_game.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "doorInit"
  doorInitClock = new util.Clock();
  // Initialize components for Routine "door"
  doorClock = new util.Clock();
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  level = 50;
  width = widthBank[level];
  height = heightBank[level];
  imgDoor = new visual.ImageStim({"win": win, "image": "img/doors1/p1r1.jpg", "units": "pix", "size": [width, height]});
  
  // Initialize components for Routine "doorAnticipation"
  doorAnticipationClock = new util.Clock();
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  awardImg = "./img/outcomes/1_punishment.jpg";
  rewardVSpunishment = "punishment";
  
  // Initialize components for Routine "award"
  awardClock = new util.Clock();
  image_door_award = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_door_award', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 2.0,
    });
  sound_1.setVolume(1.0);
  // Initialize components for Routine "noAward"
  noAwardClock = new util.Clock();
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'img/iti.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "restScreen"
  restScreenClock = new util.Clock();
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : 'pix', 
    image : 'img/rest.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "vas"
  vasClock = new util.Clock();
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    size: [1.0, 0.1], pos: [0, (- 0.3)], units: 'height',
    labels: undefined, ticks: [0, 100],
    granularity: 0.0, style: ["RATING"],
    color: new util.Color('LightGray'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: 0, 
    flip: false,
  });
  
  vas_question = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_question',
    text: '',
    font: 'Open Sans',
    units: 'norm', 
    pos: [0, 0.3], height: 0.12,  wrapWidth: 3.0, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  vas_label1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_label1',
    text: '',
    font: 'Open Sans',
    units: 'pix', 
    pos: [(- 380), (- 170)], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  vas_label2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'vas_label2',
    text: '',
    font: 'Open Sans',
    units: 'pix', 
    pos: [380, (- 170)], height: 20.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "vasRecord"
  vasRecordClock = new util.Clock();
  // Initialize components for Routine "afterVAS"
  afterVASClock = new util.Clock();
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', units : 'pix', 
    image : 'img/after_VAS.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "finalReward"
  finalRewardClock = new util.Clock();
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', units : 'pix', 
    image : 'img/finalReward.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1024, 768],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials_12;
var currentLoop;
function trials_12LoopBegin(trials_12LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_12 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_12'
  });
  psychoJS.experiment.addLoop(trials_12); // add the loop to the experiment
  currentLoop = trials_12;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_12.forEach(function() {
    const snapshot = trials_12.getSnapshot();

    trials_12LoopScheduler.add(importConditions(snapshot));
    trials_12LoopScheduler.add(titleScreenRoutineBegin(snapshot));
    trials_12LoopScheduler.add(titleScreenRoutineEachFrame(snapshot));
    trials_12LoopScheduler.add(titleScreenRoutineEnd(snapshot));
    trials_12LoopScheduler.add(endLoopIteration(trials_12LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_12LoopEnd() {
  psychoJS.experiment.removeLoop(trials_12);

  return Scheduler.Event.NEXT;
}


var trials_1;
function trials_1LoopBegin(trials_1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_1'
  });
  psychoJS.experiment.addLoop(trials_1); // add the loop to the experiment
  currentLoop = trials_1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_1.forEach(function() {
    const snapshot = trials_1.getSnapshot();

    trials_1LoopScheduler.add(importConditions(snapshot));
    const trials_13LoopScheduler = new Scheduler(psychoJS);
    trials_1LoopScheduler.add(trials_13LoopBegin, trials_13LoopScheduler);
    trials_1LoopScheduler.add(trials_13LoopScheduler);
    trials_1LoopScheduler.add(trials_13LoopEnd);
    trials_1LoopScheduler.add(vasPreRecordRoutineBegin(snapshot));
    trials_1LoopScheduler.add(vasPreRecordRoutineEachFrame(snapshot));
    trials_1LoopScheduler.add(vasPreRecordRoutineEnd(snapshot));
    trials_1LoopScheduler.add(endLoopIteration(trials_1LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_13;
function trials_13LoopBegin(trials_13LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_13 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_13'
  });
  psychoJS.experiment.addLoop(trials_13); // add the loop to the experiment
  currentLoop = trials_13;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_13.forEach(function() {
    const snapshot = trials_13.getSnapshot();

    trials_13LoopScheduler.add(importConditions(snapshot));
    trials_13LoopScheduler.add(vasPreRoutineBegin(snapshot));
    trials_13LoopScheduler.add(vasPreRoutineEachFrame(snapshot));
    trials_13LoopScheduler.add(vasPreRoutineEnd(snapshot));
    trials_13LoopScheduler.add(endLoopIteration(trials_13LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_13LoopEnd() {
  psychoJS.experiment.removeLoop(trials_13);

  return Scheduler.Event.NEXT;
}


function trials_1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_1);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10000, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(instructionRoutineBegin(snapshot));
    trials_2LoopScheduler.add(instructionRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(instructionRoutineEnd(snapshot));
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_3'
  });
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_3.forEach(function() {
    const snapshot = trials_3.getSnapshot();

    trials_3LoopScheduler.add(importConditions(snapshot));
    trials_3LoopScheduler.add(practiceRoutineBegin(snapshot));
    trials_3LoopScheduler.add(practiceRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(practiceRoutineEnd(snapshot));
    trials_3LoopScheduler.add(practiceAnticipationRoutineBegin(snapshot));
    trials_3LoopScheduler.add(practiceAnticipationRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(practiceAnticipationRoutineEnd(snapshot));
    trials_3LoopScheduler.add(practiceAwardRoutineBegin(snapshot));
    trials_3LoopScheduler.add(practiceAwardRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(practiceAwardRoutineEnd(snapshot));
    trials_3LoopScheduler.add(practiceITIRoutineBegin(snapshot));
    trials_3LoopScheduler.add(practiceITIRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(practiceITIRoutineEnd(snapshot));
    trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    const trials_5LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_5LoopBegin, trials_5LoopScheduler);
    trialsLoopScheduler.add(trials_5LoopScheduler);
    trialsLoopScheduler.add(trials_5LoopEnd);
    const trials_7LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_7LoopBegin, trials_7LoopScheduler);
    trialsLoopScheduler.add(trials_7LoopScheduler);
    trialsLoopScheduler.add(trials_7LoopEnd);
    trialsLoopScheduler.add(doorImgShuffleRoutineBegin(snapshot));
    trialsLoopScheduler.add(doorImgShuffleRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(doorImgShuffleRoutineEnd(snapshot));
    const trials_8LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_8LoopBegin, trials_8LoopScheduler);
    trialsLoopScheduler.add(trials_8LoopScheduler);
    trialsLoopScheduler.add(trials_8LoopEnd);
    const trials_4LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_4LoopBegin, trials_4LoopScheduler);
    trialsLoopScheduler.add(trials_4LoopScheduler);
    trialsLoopScheduler.add(trials_4LoopEnd);
    const trials_9LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_9LoopBegin, trials_9LoopScheduler);
    trialsLoopScheduler.add(trials_9LoopScheduler);
    trialsLoopScheduler.add(trials_9LoopEnd);
    const trials_6LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_6LoopBegin, trials_6LoopScheduler);
    trialsLoopScheduler.add(trials_6LoopScheduler);
    trialsLoopScheduler.add(trials_6LoopEnd);
    const trials_10LoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(trials_10LoopBegin, trials_10LoopScheduler);
    trialsLoopScheduler.add(trials_10LoopScheduler);
    trialsLoopScheduler.add(trials_10LoopEnd);
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_5'
  });
  psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
  currentLoop = trials_5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_5.forEach(function() {
    const snapshot = trials_5.getSnapshot();

    trials_5LoopScheduler.add(importConditions(snapshot));
    trials_5LoopScheduler.add(fortuneWheelRoutineBegin(snapshot));
    trials_5LoopScheduler.add(fortuneWheelRoutineEachFrame(snapshot));
    trials_5LoopScheduler.add(fortuneWheelRoutineEnd(snapshot));
    trials_5LoopScheduler.add(endLoopIteration(trials_5LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_5LoopEnd() {
  psychoJS.experiment.removeLoop(trials_5);

  return Scheduler.Event.NEXT;
}


var trials_7;
function trials_7LoopBegin(trials_7LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_7 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_7'
  });
  psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
  currentLoop = trials_7;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_7.forEach(function() {
    const snapshot = trials_7.getSnapshot();

    trials_7LoopScheduler.add(importConditions(snapshot));
    trials_7LoopScheduler.add(fortuneWheelResultRoutineBegin(snapshot));
    trials_7LoopScheduler.add(fortuneWheelResultRoutineEachFrame(snapshot));
    trials_7LoopScheduler.add(fortuneWheelResultRoutineEnd(snapshot));
    trials_7LoopScheduler.add(endLoopIteration(trials_7LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_7LoopEnd() {
  psychoJS.experiment.removeLoop(trials_7);

  return Scheduler.Event.NEXT;
}


var trials_8;
function trials_8LoopBegin(trials_8LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_8 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_8'
  });
  psychoJS.experiment.addLoop(trials_8); // add the loop to the experiment
  currentLoop = trials_8;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_8.forEach(function() {
    const snapshot = trials_8.getSnapshot();

    trials_8LoopScheduler.add(importConditions(snapshot));
    trials_8LoopScheduler.add(doorStartScreenRoutineBegin(snapshot));
    trials_8LoopScheduler.add(doorStartScreenRoutineEachFrame(snapshot));
    trials_8LoopScheduler.add(doorStartScreenRoutineEnd(snapshot));
    trials_8LoopScheduler.add(endLoopIteration(trials_8LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_8LoopEnd() {
  psychoJS.experiment.removeLoop(trials_8);

  return Scheduler.Event.NEXT;
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 50, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_4'
  });
  psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
  currentLoop = trials_4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_4.forEach(function() {
    const snapshot = trials_4.getSnapshot();

    trials_4LoopScheduler.add(importConditions(snapshot));
    trials_4LoopScheduler.add(doorInitRoutineBegin(snapshot));
    trials_4LoopScheduler.add(doorInitRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(doorInitRoutineEnd(snapshot));
    trials_4LoopScheduler.add(doorRoutineBegin(snapshot));
    trials_4LoopScheduler.add(doorRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(doorRoutineEnd(snapshot));
    trials_4LoopScheduler.add(doorAnticipationRoutineBegin(snapshot));
    trials_4LoopScheduler.add(doorAnticipationRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(doorAnticipationRoutineEnd(snapshot));
    trials_4LoopScheduler.add(awardRoutineBegin(snapshot));
    trials_4LoopScheduler.add(awardRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(awardRoutineEnd(snapshot));
    trials_4LoopScheduler.add(noAwardRoutineBegin(snapshot));
    trials_4LoopScheduler.add(noAwardRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(noAwardRoutineEnd(snapshot));
    trials_4LoopScheduler.add(itiRoutineBegin(snapshot));
    trials_4LoopScheduler.add(itiRoutineEachFrame(snapshot));
    trials_4LoopScheduler.add(itiRoutineEnd(snapshot));
    trials_4LoopScheduler.add(endLoopIteration(trials_4LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_4);

  return Scheduler.Event.NEXT;
}


var trials_9;
function trials_9LoopBegin(trials_9LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_9 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_9'
  });
  psychoJS.experiment.addLoop(trials_9); // add the loop to the experiment
  currentLoop = trials_9;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_9.forEach(function() {
    const snapshot = trials_9.getSnapshot();

    trials_9LoopScheduler.add(importConditions(snapshot));
    trials_9LoopScheduler.add(restScreenRoutineBegin(snapshot));
    trials_9LoopScheduler.add(restScreenRoutineEachFrame(snapshot));
    trials_9LoopScheduler.add(restScreenRoutineEnd(snapshot));
    trials_9LoopScheduler.add(endLoopIteration(trials_9LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_9LoopEnd() {
  psychoJS.experiment.removeLoop(trials_9);

  return Scheduler.Event.NEXT;
}


var trials_6;
function trials_6LoopBegin(trials_6LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_6 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_6'
  });
  psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
  currentLoop = trials_6;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_6.forEach(function() {
    const snapshot = trials_6.getSnapshot();

    trials_6LoopScheduler.add(importConditions(snapshot));
    const trials_14LoopScheduler = new Scheduler(psychoJS);
    trials_6LoopScheduler.add(trials_14LoopBegin, trials_14LoopScheduler);
    trials_6LoopScheduler.add(trials_14LoopScheduler);
    trials_6LoopScheduler.add(trials_14LoopEnd);
    trials_6LoopScheduler.add(vasRecordRoutineBegin(snapshot));
    trials_6LoopScheduler.add(vasRecordRoutineEachFrame(snapshot));
    trials_6LoopScheduler.add(vasRecordRoutineEnd(snapshot));
    trials_6LoopScheduler.add(endLoopIteration(trials_6LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_14;
function trials_14LoopBegin(trials_14LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_14 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1000, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_14'
  });
  psychoJS.experiment.addLoop(trials_14); // add the loop to the experiment
  currentLoop = trials_14;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_14.forEach(function() {
    const snapshot = trials_14.getSnapshot();

    trials_14LoopScheduler.add(importConditions(snapshot));
    trials_14LoopScheduler.add(vasRoutineBegin(snapshot));
    trials_14LoopScheduler.add(vasRoutineEachFrame(snapshot));
    trials_14LoopScheduler.add(vasRoutineEnd(snapshot));
    trials_14LoopScheduler.add(endLoopIteration(trials_14LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_14LoopEnd() {
  psychoJS.experiment.removeLoop(trials_14);

  return Scheduler.Event.NEXT;
}


function trials_6LoopEnd() {
  psychoJS.experiment.removeLoop(trials_6);

  return Scheduler.Event.NEXT;
}


var trials_10;
function trials_10LoopBegin(trials_10LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_10 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_10'
  });
  psychoJS.experiment.addLoop(trials_10); // add the loop to the experiment
  currentLoop = trials_10;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_10.forEach(function() {
    const snapshot = trials_10.getSnapshot();

    trials_10LoopScheduler.add(importConditions(snapshot));
    trials_10LoopScheduler.add(afterVASRoutineBegin(snapshot));
    trials_10LoopScheduler.add(afterVASRoutineEachFrame(snapshot));
    trials_10LoopScheduler.add(afterVASRoutineEnd(snapshot));
    trials_10LoopScheduler.add(endLoopIteration(trials_10LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_10LoopEnd() {
  psychoJS.experiment.removeLoop(trials_10);

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_11;
function trials_11LoopBegin(trials_11LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_11 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_11'
  });
  psychoJS.experiment.addLoop(trials_11); // add the loop to the experiment
  currentLoop = trials_11;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_11.forEach(function() {
    const snapshot = trials_11.getSnapshot();

    trials_11LoopScheduler.add(importConditions(snapshot));
    trials_11LoopScheduler.add(finalRewardRoutineBegin(snapshot));
    trials_11LoopScheduler.add(finalRewardRoutineEachFrame(snapshot));
    trials_11LoopScheduler.add(finalRewardRoutineEnd(snapshot));
    trials_11LoopScheduler.add(endLoopIteration(trials_11LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_11LoopEnd() {
  psychoJS.experiment.removeLoop(trials_11);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var titleScreenComponents;
function titleScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'titleScreen'-------
    t = 0;
    titleScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    titleScreenComponents = [];
    titleScreenComponents.push(key_resp);
    titleScreenComponents.push(image);
    
    titleScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function titleScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'titleScreen'-------
    // get current time
    t = titleScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    titleScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function titleScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'titleScreen'-------
    titleScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "titleScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var sliderStarted;
var _key_resp_15_allKeys;
var vasPreComponents;
function vasPreRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vasPre'-------
    t = 0;
    vasPreClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sliderStarted = false;
    
    slider_2.reset()
    vas_question_pre.setText(vasQuestionText);
    vas_label1_pre.setText(vasLabelText1);
    vas_label2_pre.setText(vasLabelText2);
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    vasPreComponents = [];
    vasPreComponents.push(slider_2);
    vasPreComponents.push(vas_question_pre);
    vasPreComponents.push(vas_label1_pre);
    vasPreComponents.push(vas_label2_pre);
    vasPreComponents.push(key_resp_15);
    
    vasPreComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vasPreRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vasPre'-------
    // get current time
    t = vasPreClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (slider_2.markerPos) {
        sliderStarted = true;
    }
    
    
    // *slider_2* updates
    if (t >= 0.0 && slider_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_2.tStart = t;  // (not accounting for frame time here)
      slider_2.frameNStart = frameN;  // exact frame index
      
      slider_2.setAutoDraw(true);
    }

    
    // *vas_question_pre* updates
    if (t >= 0.0 && vas_question_pre.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_question_pre.tStart = t;  // (not accounting for frame time here)
      vas_question_pre.frameNStart = frameN;  // exact frame index
      
      vas_question_pre.setAutoDraw(true);
    }

    
    // *vas_label1_pre* updates
    if (t >= 0.0 && vas_label1_pre.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_label1_pre.tStart = t;  // (not accounting for frame time here)
      vas_label1_pre.frameNStart = frameN;  // exact frame index
      
      vas_label1_pre.setAutoDraw(true);
    }

    
    // *vas_label2_pre* updates
    if (t >= 0.0 && vas_label2_pre.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_label2_pre.tStart = t;  // (not accounting for frame time here)
      vas_label2_pre.frameNStart = frameN;  // exact frame index
      
      vas_label2_pre.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vasPreComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vasPreRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vasPre'-------
    vasPreComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if (sliderStarted) {
        trials_13.finished = true;
    }
    
    psychoJS.experiment.addData('slider_2.response', slider_2.getRating());
    psychoJS.experiment.addData('slider_2.rt', slider_2.getRT());
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "vasPre" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var vasPreRecordComponents;
function vasPreRecordRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vasPreRecord'-------
    t = 0;
    vasPreRecordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    vasPreRecordComponents = [];
    
    vasPreRecordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vasPreRecordRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vasPreRecord'-------
    // get current time
    t = vasPreRecordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vasPreRecordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vasPreRecordRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vasPreRecord'-------
    vasPreRecordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_1.addData("displayed", vasQuestionText);
    trials_1.addData("vas_response", slider_2.getRating());
    trials_1.addData("vas_label", ((vasLabelText1 + ",") + vasLabelText2));
    trials_1.addData("section", "VAS");
    if ((vasPreCount === 0)) {
        vasLabelText1 = "Not at all";
        vasLabelText2 = "Very much";
        vasQuestionText = "How much do you feel like taking part in the task?";
    }
    if ((vasPreCount === 1)) {
        vasLabelText1 = "Not at all tired";
        vasLabelText2 = "Very tired";
        vasQuestionText = "How tired are you right now?";
    }
    if ((vasPreCount === 2)) {
        vasLabelText1 = "Worst mood ever";
        vasLabelText2 = "Best mood ever";
        vasQuestionText = "Think about your mood right now. \nHow would you describe it?";
    }
    vasPreCount += 1;
    
    // the Routine "vasPreRecord" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instruction'-------
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    imgFile = (("instruction/Slide" + count.toString()) + ".jpg");
    
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    image_2.setImage(imgFile);
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(key_resp_2);
    instructionComponents.push(image_2);
    
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instruction'-------
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space', 'r', 'y', 'n'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instruction'-------
    instructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_2.addData("section", (("Instruction (page:" + count.toString()) + ")"));
    trials_2.addData("displayed", imgFile);
    if ((count === 0)) {
        if (((key_resp_2.keys === "y") || (key_resp_2.keys === "Y"))) {
            count += 1;
        } else {
            if (((key_resp_2.keys === "n") || (key_resp_2.keys === "N"))) {
                trials_2.finished = true;
            }
        }
    } else {
        if ((count === 16)) {
            if (((key_resp_2.keys === "r") || (key_resp_2.keys === "R"))) {
                count = 1;
            } else {
                trials_2.finished = true;
            }
        } else {
            if ((key_resp_2.keys === "space")) {
                count += 1;
            }
        }
    }
    
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var gotValidClick;
var practiceTrialStartTime;
var practiceComponents;
function practiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice'-------
    t = 0;
    practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    img.setAutoDraw(false);
    width = widthBank[level];
    height = heightBank[level];
    img.size = [width, height];
    level = 50;
    img.setAutoDraw(true);
    practiceTrialStartTime = timer.getTime();
    
    // keep track of which components have finished
    practiceComponents = [];
    practiceComponents.push(key_resp_3);
    practiceComponents.push(mouse);
    
    practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var finalWidth;
var finalHeight;
function practiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice'-------
    // get current time
    t = practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if (((timer.getTime() - practiceTrialStartTime) > 10)) {
        finalWidth = width;
        finalHeight = height;
        continueRoutine = false;
    }
    if ((mouse.getPressed()[0] === 1)) {
        level += 1;
        level = Math.min(100, level);
    } else {
        if ((mouse.getPressed()[2] === 1)) {
            level -= 1;
            level = Math.max(0, level);
        }
    }
    img.setAutoDraw(false);
    width = widthBank[level];
    height = heightBank[level];
    img.size = [width, height];
    img.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var _mouseButtons;
var randomDuration;
var randomAnticipation;
function practiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice'-------
    practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    trials_3.addData("door locked level", level);
    trials_3.addData("door duration (sec)", (timer.getTime() - practiceTrialStartTime).toString());
    trials_3.addData("displayed", "img/practice_door.jpg");
    width = widthBank[level];
    height = heightBank[level];
    randomDuration = randomGet(1.5, 3.5);
    randomAnticipation = randomGet(2, 4);
    
    // the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_9_allKeys;
var routineStartTime;
var practiceAnticipationComponents;
function practiceAnticipationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practiceAnticipation'-------
    t = 0;
    practiceAnticipationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    routineStartTime = timer.getTime();
    
    // keep track of which components have finished
    practiceAnticipationComponents = [];
    practiceAnticipationComponents.push(key_resp_9);
    
    practiceAnticipationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practiceAnticipationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practiceAnticipation'-------
    // get current time
    t = practiceAnticipationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['qq'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
      }
    }
    
    if (((timer.getTime() - routineStartTime) > randomAnticipation)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceAnticipationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceAnticipationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practiceAnticipation'-------
    practiceAnticipationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        }
    
    key_resp_9.stop();
    trials_3.addData("door anticipation time (sec)", (timer.getTime() - routineStartTime).toString());
    
    // the Routine "practiceAnticipation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practiceAwardComponents;
function practiceAwardRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practiceAward'-------
    t = 0;
    practiceAwardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    imgAward.setPos([0, ((- height) * 0.028)]);
    imgAward.setSize([(width * 0.235), (height * 0.464)]);
    routineStartTime = timer.getTime();
    
    // keep track of which components have finished
    practiceAwardComponents = [];
    practiceAwardComponents.push(imgAward);
    
    practiceAwardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practiceAwardRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practiceAward'-------
    // get current time
    t = practiceAwardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imgAward* updates
    if (t >= 0.0 && imgAward.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgAward.tStart = t;  // (not accounting for frame time here)
      imgAward.frameNStart = frameN;  // exact frame index
      
      imgAward.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imgAward.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imgAward.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceAwardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceAwardRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practiceAward'-------
    practiceAwardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_3.addData("award displayed duration (sec)", (timer.getTime() - routineStartTime).toString());
    
    return Scheduler.Event.NEXT;
  };
}


var practiceITIComponents;
function practiceITIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practiceITI'-------
    t = 0;
    practiceITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    img.setAutoDraw(false);
    imgAward.setAutoDraw(false);
    routineStartTime = timer.getTime();
    
    // keep track of which components have finished
    practiceITIComponents = [];
    practiceITIComponents.push(imageITI);
    
    practiceITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practiceITIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practiceITI'-------
    // get current time
    t = practiceITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imageITI* updates
    if (t >= 0.0 && imageITI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageITI.tStart = t;  // (not accounting for frame time here)
      imageITI.frameNStart = frameN;  // exact frame index
      
      imageITI.setAutoDraw(true);
    }

    frameRemains = 0.0 + randomDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageITI.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageITI.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceITIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practiceITI'-------
    practiceITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_3.addData("iti duration (sec)", (timer.getTime() - routineStartTime).toString());
    trials_3.addData("section", "Practice");
    
    // the Routine "practiceITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var movieClock;
var movie;
var fortuneWheelComponents;
function fortuneWheelRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fortuneWheel'-------
    t = 0;
    fortuneWheelClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    movieClock = new util.Clock();
    movie = new visual.MovieStim({
      win: psychoJS.window,
      name: 'movie',
      units: 'pix',
      movie: fortuneVideo,
      pos: [0, 0],
      size: [366, 457],
      ori: 0.0,
      opacity: undefined,
      loop: false,
      noAudio: false,
      });
    // keep track of which components have finished
    fortuneWheelComponents = [];
    fortuneWheelComponents.push(movie);
    
    fortuneWheelComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fortuneWheelRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fortuneWheel'-------
    // get current time
    t = fortuneWheelClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie* updates
    if (t >= 0.0 && movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie.tStart = t;  // (not accounting for frame time here)
      movie.frameNStart = frameN;  // exact frame index
      
      movie.setAutoDraw(true);
      movie.play();
    }

    frameRemains = 0.0 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie.setAutoDraw(false);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fortuneWheelComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fortuneWheelRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fortuneWheel'-------
    fortuneWheelComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    movie.stop();
    if ((trialsCount === 0)) {
        fortuneVideo = "video/16.mp4";
    } else {
        if ((trialsCount === 1)) {
            fortuneVideo = "video/16b.mp4";
        }
    }
    
    trials_5.addData("section", "Playing Fortune Wheel");
    trials_5.addData("displayed", fortuneVideo);
    if ((trialsCount === 0)) {
        fortuneWheelResultImg = "img/fortuneResult18.jpg";
    } else {
        if ((trialsCount === 1)) {
            fortuneWheelResultImg = "img/fortuneResult16.jpg";
        } else {
            if ((trialsCount === 2)) {
                fortuneWheelResultImg = "img/fortuneResult16.jpg";
            }
        }
    }
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var fortuneWheelResultComponents;
function fortuneWheelResultRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fortuneWheelResult'-------
    t = 0;
    fortuneWheelResultClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    image_3.setImage(fortuneWheelResultImg);
    // keep track of which components have finished
    fortuneWheelResultComponents = [];
    fortuneWheelResultComponents.push(key_resp_5);
    fortuneWheelResultComponents.push(image_3);
    
    fortuneWheelResultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fortuneWheelResultRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fortuneWheelResult'-------
    // get current time
    t = fortuneWheelResultClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fortuneWheelResultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fortuneWheelResultRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fortuneWheelResult'-------
    fortuneWheelResultComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    trials_7.addData("section", "Fortune Wheel Result displayed");
    trials_7.addData("displayed", fortuneWheelResultImg);
    
    // the Routine "fortuneWheelResult" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var imgOrder;
var doorImgShuffleComponents;
function doorImgShuffleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'doorImgShuffle'-------
    t = 0;
    doorImgShuffleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    function shuffle(array) {
      let currentIndex = array.length,  randomIndex;
    
      // While there remain elements to shuffle.
      while (currentIndex != 0) {
    
        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
    
        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex], array[currentIndex]];
      }
    
      return array;
    }
    
    imgOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    imgOrder = shuffle(imgOrder)
    //continueRoutine = false
    // keep track of which components have finished
    doorImgShuffleComponents = [];
    
    doorImgShuffleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doorImgShuffleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'doorImgShuffle'-------
    // get current time
    t = doorImgShuffleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    doorImgShuffleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var trials4Count;
function doorImgShuffleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'doorImgShuffle'-------
    doorImgShuffleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials4Count = 0;
    
    // the Routine "doorImgShuffle" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var doorStartScreenComponents;
function doorStartScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'doorStartScreen'-------
    t = 0;
    doorStartScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    doorStartScreenComponents = [];
    doorStartScreenComponents.push(image_4);
    doorStartScreenComponents.push(key_resp_8);
    
    doorStartScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doorStartScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'doorStartScreen'-------
    // get current time
    t = doorStartScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    doorStartScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function doorStartScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'doorStartScreen'-------
    doorStartScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    trials_8.addData("section", "Doorgame Start Screen Displayed");
    trials_8.addData("displayed", "img/start_main_game.jpg");
    
    // the Routine "doorStartScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var doorInitComponents;
function doorInitRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'doorInit'-------
    t = 0;
    doorInitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    doorInitComponents = [];
    
    doorInitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doorInitRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'doorInit'-------
    // get current time
    t = doorInitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    doorInitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var doorImgIdx;
var doorImg;
var p;
var r;
function doorInitRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'doorInit'-------
    doorInitComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    doorImgIdx = imgOrder[trials4Count];
    doorImg = imgList[doorImgIdx];
    p = pList[doorImgIdx];
    r = rList[doorImgIdx];
    randomDuration = randomGet(1.5, 3.5);
    randomAnticipation = randomGet(2, 4);
    trials_4.addData("displayed", doorImg);
    trials_4.addData("door(r)", r);
    trials_4.addData("door(p)", p);
    
    doorImg = doorImg.replace('./', '');
    // the Routine "doorInit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var doorTrialStartTime;
var doorComponents;
function doorRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'door'-------
    t = 0;
    doorClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    gotValidClick = false; // until a click is received
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    level = 50;
    width = widthBank[level];
    height = heightBank[level];
    imgDoor = new visual.ImageStim({"win": win, "image": doorImg, "units": "pix", "size": [width, height]});
    imgDoor.setAutoDraw(false);
    img.size = [width, height];
    imgDoor.setAutoDraw(true);
    doorTrialStartTime = timer.getTime();
    
    // keep track of which components have finished
    doorComponents = [];
    doorComponents.push(mouse_2);
    doorComponents.push(key_resp_7);
    
    doorComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doorRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'door'-------
    // get current time
    t = doorClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if (((timer.getTime() - doorTrialStartTime) > 10)) {
        finalWidth = width;
        finalHeight = height;
        continueRoutine = false;
    }
    if ((mouse.getPressed()[0] === 1)) {
        level += 1;
        level = Math.min(100, level);
    } else {
        if ((mouse.getPressed()[2] === 1)) {
            level -= 1;
            level = Math.max(0, level);
        }
    }
    img.setAutoDraw(false);
    width = widthBank[level];
    height = heightBank[level];
    imgDoor.size = [width, height];
    imgDoor.setAutoDraw(true);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    doorComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function doorRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'door'-------
    doorComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouse_2.getPos();
    _mouseButtons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', _mouseButtons[2]);
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    trials_4.addData("door locked level", level);
    trials_4.addData("door duration (sec)", (timer.getTime() - doorTrialStartTime).toString());
    width = widthBank[level];
    height = heightBank[level];
    randomDuration = randomGet(1.5, 3.5);
    
    // the Routine "door" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_10_allKeys;
var doorOpenChance;
var randomNum;
var door_opened;
var soundFile;
var doorAnticipationComponents;
function doorAnticipationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'doorAnticipation'-------
    t = 0;
    doorAnticipationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    routineStartTime = timer.getTime();
    doorOpenChance = doorOpenChanceMap[level];
    randomNum = randomGet(0, 1);
    door_opened = false;
    soundFile = "sound/reward.wav";
    if ((randomNum > doorOpenChance)) {
        door_opened = false;
        trials_4.addData("award type", "door not opened");
        trials_4.addData("award", "0");
    } else {
        door_opened = true;
    }
    if ((randomGet(0, 1) > 0.5)) {
        rewardVSpunishment = "punishment";
        awardImg = (("img/outcomes/" + p) + "_punishment.jpg");
        soundFile = "sound/punishment.wav";
        trials_4.addData("award type", "punishment");
        trials_4.addData("award", ("-" + p));
    } else {
        rewardVSpunishment = "reward";
        awardImg = (("img/outcomes/" + r) + "_reward.jpg");
        trials_4.addData("award type", "reward");
        trials_4.addData("award", ("+" + r));
    }
    
    // keep track of which components have finished
    doorAnticipationComponents = [];
    doorAnticipationComponents.push(key_resp_10);
    
    doorAnticipationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doorAnticipationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'doorAnticipation'-------
    // get current time
    t = doorAnticipationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['qq'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
      }
    }
    
    if (((timer.getTime() - routineStartTime) > randomAnticipation)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    doorAnticipationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function doorAnticipationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'doorAnticipation'-------
    doorAnticipationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        }
    
    key_resp_10.stop();
    trials_4.addData("door anticipation time (sec)", (timer.getTime() - routineStartTime).toString());
    
    // the Routine "doorAnticipation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var awardComponents;
function awardRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'award'-------
    t = 0;
    awardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    image_door_award.setPos([0, ((- height) * 0.028)]);
    image_door_award.setSize([(width * 0.235), (height * 0.464)]);
    image_door_award.setImage(awardImg);
    if ((door_opened === true)) {
        routineStartTime = timer.getTime();
    } else {
        continueRoutine = false;
    }
    
    sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: soundFile,
    secs: 2.0,
    });
    sound_1.secs=2.0;
    sound_1.setVolume(1.0);
    // keep track of which components have finished
    awardComponents = [];
    awardComponents.push(image_door_award);
    awardComponents.push(sound_1);
    
    awardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function awardRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'award'-------
    // get current time
    t = awardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_door_award* updates
    if (t >= 0.0 && image_door_award.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_door_award.tStart = t;  // (not accounting for frame time here)
      image_door_award.frameNStart = frameN;  // exact frame index
      
      image_door_award.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_door_award.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_door_award.setAutoDraw(false);
    }
    // start/stop sound_1
    if (t >= 0.0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (2.0 > 0.5) {  sound_1.stop();  // stop the sound (if longer than duration)
        sound_1.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    awardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function awardRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'award'-------
    awardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((door_opened === true)) {
        trials_4.addData((awardImg + " displayed duration (sec)"), (timer.getTime() - routineStartTime).toString());
    }
    
    sound_1.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var noAwardComponents;
function noAwardRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'noAward'-------
    t = 0;
    noAwardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((door_opened === false)) {
        routineStartTime = timer.getTime();
    } else {
        continueRoutine = true;
    }
    
    // keep track of which components have finished
    noAwardComponents = [];
    
    noAwardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function noAwardRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'noAward'-------
    // get current time
    t = noAwardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((timer.getTime() - routineStartTime) > 2)) {
        continueRoutine = true;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    noAwardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function noAwardRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'noAward'-------
    noAwardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((door_opened === false)) {
        trials_4.addData("award (not displayed) displayed duration (sec)", (timer.getTime() - routineStartTime).toString());
    }
    
    // the Routine "noAward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var itiComponents;
function itiRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'iti'-------
    t = 0;
    itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    imgDoor.setAutoDraw(false);
    image_door_award.setAutoDraw(false);
    routineStartTime = timer.getTime();
    
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(image_5);
    
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function itiRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'iti'-------
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + randomDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'iti'-------
    itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_4.addData("section", "Door Game (playing main game)");
    trials4Count += 1;
    trials_4.addData("iti duration (sec)", (timer.getTime() - routineStartTime).toString());
    
    // the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_11_allKeys;
var restScreenComponents;
function restScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'restScreen'-------
    t = 0;
    restScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    restScreenComponents = [];
    restScreenComponents.push(image_6);
    restScreenComponents.push(key_resp_11);
    
    restScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'restScreen'-------
    // get current time
    t = restScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_6* updates
    if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }

    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'restScreen'-------
    restScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    trials_9.addData("section", "Rest Screen Displayed");
    trials_9.addData("displayed", "img/rest.jpg");
    vasPreCount = 0;
    vasQuestionText = "How anxious do you feel right now?";
    vasLabelText1 = "Not anxious";
    vasLabelText2 = "Very anxious";
    
    // the Routine "restScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_14_allKeys;
var vasComponents;
function vasRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vas'-------
    t = 0;
    vasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider.reset()
    vas_question.setText(vasQuestionText);
    sliderStarted = false;
    
    vas_label1.setText(vasLabelText1);
    vas_label2.setText(vasLabelText2);
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    // keep track of which components have finished
    vasComponents = [];
    vasComponents.push(slider);
    vasComponents.push(vas_question);
    vasComponents.push(vas_label1);
    vasComponents.push(vas_label2);
    vasComponents.push(key_resp_14);
    
    vasComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vasRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vas'-------
    // get current time
    t = vasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    
    // *vas_question* updates
    if (t >= 0.0 && vas_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_question.tStart = t;  // (not accounting for frame time here)
      vas_question.frameNStart = frameN;  // exact frame index
      
      vas_question.setAutoDraw(true);
    }

    if (slider.markerPos) {
        sliderStarted = true;
    }
    
    
    // *vas_label1* updates
    if (t >= 0.0 && vas_label1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_label1.tStart = t;  // (not accounting for frame time here)
      vas_label1.frameNStart = frameN;  // exact frame index
      
      vas_label1.setAutoDraw(true);
    }

    
    // *vas_label2* updates
    if (t >= 0.0 && vas_label2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vas_label2.tStart = t;  // (not accounting for frame time here)
      vas_label2.frameNStart = frameN;  // exact frame index
      
      vas_label2.setAutoDraw(true);
    }

    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }

    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vasComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vasRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vas'-------
    vasComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('slider.response', slider.getRating());
    if (sliderStarted) {
        trials_14.finished = true;
    }
    
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "vas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var vasRecordComponents;
function vasRecordRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'vasRecord'-------
    t = 0;
    vasRecordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    vasRecordComponents = [];
    
    vasRecordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function vasRecordRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'vasRecord'-------
    // get current time
    t = vasRecordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    vasRecordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vasRecordRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'vasRecord'-------
    vasRecordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trials_6.addData("displayed", vasQuestionText);
    trials_6.addData("vas_response", slider.getRating());
    trials_6.addData("vas_label", ((vasLabelText1 + ",") + vasLabelText2));
    trials_6.addData("section", "VAS");
    if ((vasPreCount === 0)) {
        vasLabelText1 = "Not at all";
        vasLabelText2 = "Very much";
        vasQuestionText = "How much do you feel like taking part in the task?";
    } else {
        if ((vasPreCount === 1)) {
            vasLabelText1 = "Not at all tired";
            vasLabelText2 = "Very tired";
            vasQuestionText = "How tired are you right now?";
        } else {
            if ((vasPreCount === 2)) {
                vasLabelText1 = "Worst mood ever";
                vasLabelText2 = "Best mood ever";
                vasQuestionText = "Think about your mood right now. \nHow would you describe it?";
            }
        }
    }
    vasPreCount += 1;
    
    // the Routine "vasRecord" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var afterVASComponents;
function afterVASRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'afterVAS'-------
    t = 0;
    afterVASClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    if ((trialsCount === 2)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    afterVASComponents = [];
    afterVASComponents.push(image_7);
    afterVASComponents.push(key_resp_12);
    
    afterVASComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function afterVASRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'afterVAS'-------
    // get current time
    t = afterVASClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_7* updates
    if (t >= 0.0 && image_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_7.tStart = t;  // (not accounting for frame time here)
      image_7.frameNStart = frameN;  // exact frame index
      
      image_7.setAutoDraw(true);
    }

    
    // *key_resp_12* updates
    if (t >= 0.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    afterVASComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function afterVASRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'afterVAS'-------
    afterVASComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    trialsCount += 1;
    trials_10.addData("section", "after-VAS screen displayed");
    trials_10.addData("displayed", "img/after_VAS.jpg");
    
    // the Routine "afterVAS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_13_allKeys;
var finalRewardComponents;
function finalRewardRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'finalReward'-------
    t = 0;
    finalRewardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    // keep track of which components have finished
    finalRewardComponents = [];
    finalRewardComponents.push(image_8);
    finalRewardComponents.push(key_resp_13);
    
    finalRewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function finalRewardRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'finalReward'-------
    // get current time
    t = finalRewardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_8* updates
    if (t >= 0.0 && image_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_8.tStart = t;  // (not accounting for frame time here)
      image_8.frameNStart = frameN;  // exact frame index
      
      image_8.setAutoDraw(true);
    }

    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }

    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    finalRewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finalRewardRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'finalReward'-------
    finalRewardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    trials_11.addData("section", "final-reward screen displayed");
    trials_11.addData("displayed", "img/finalReward.jpg");
    
    // the Routine "finalReward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  level = 50;
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  level = 50;
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
