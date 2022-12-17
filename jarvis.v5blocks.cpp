// Make sure all required headers are included.
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>


#include "vex.h"

using namespace vex;

// Brain should be defined by default
brain Brain;


// START V5 MACROS
#define waitUntil(condition)                                                   \
  do {                                                                         \
    wait(5, msec);                                                             \
  } while (!(condition))

#define repeat(iterations)                                                     \
  for (int iterator = 0; iterator < iterations; iterator++)
// END V5 MACROS


// Robot configuration code.
controller Controller1 = controller(primary);
motor leftMotorA = motor(PORT20, ratio18_1, false);
motor leftMotorB = motor(PORT10, ratio18_1, false);
motor_group LeftDriveSmart = motor_group(leftMotorA, leftMotorB);
motor rightMotorA = motor(PORT11, ratio18_1, true);
motor rightMotorB = motor(PORT1, ratio18_1, true);
motor_group RightDriveSmart = motor_group(rightMotorA, rightMotorB);
inertial DrivetrainInertial = inertial(PORT8);
smartdrive Drivetrain = smartdrive(LeftDriveSmart, RightDriveSmart, DrivetrainInertial, 319.19, 320, 255, mm, 1);

motor Intake = motor(PORT5, ratio18_1, false);

motor FlywheelMotorA = motor(PORT13, ratio6_1, false);
motor FlywheelMotorB = motor(PORT14, ratio6_1, true);
motor_group Flywheel = motor_group(FlywheelMotorA, FlywheelMotorB);

motor Expansion = motor(PORT7, ratio18_1, false);


void calibrateDrivetrain() {
  wait(200, msec);
  Brain.Screen.print("Calibrating");
  Brain.Screen.newLine();
  Brain.Screen.print("Inertial");
  DrivetrainInertial.calibrate();
  while (DrivetrainInertial.isCalibrating()) {
    wait(25, msec);
  }

  // Clears the screen and returns the cursor to row 1, column 1.
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1, 1);
}



// Generated code.



// define variable for remote controller enable/disable
bool RemoteControlCodeEnabled = true;
// define variables used for controlling motors based on controller inputs
bool Controller1LeftShoulderControlMotorsStopped = true;
bool Controller1RightShoulderControlMotorsStopped = true;
bool DrivetrainLNeedsToBeStopped_Controller1 = true;
bool DrivetrainRNeedsToBeStopped_Controller1 = true;

// define a task that will handle monitoring inputs from Controller1
int rc_auto_loop_function_Controller1() {
  // process the controller input every 20 milliseconds
  // update the motors based on the input values
  while(true) {
    if(RemoteControlCodeEnabled) {
      // stop the motors if the brain is calibrating
      if (DrivetrainInertial.isCalibrating()) {
        LeftDriveSmart.stop();
        RightDriveSmart.stop();
        while (DrivetrainInertial.isCalibrating()) {
          wait(25, msec);
        }
      }
      
      // calculate the drivetrain motor velocities from the controller joystick axies
      // left = Axis3
      // right = Axis2
      int drivetrainLeftSideSpeed = Controller1.Axis3.position();
      int drivetrainRightSideSpeed = Controller1.Axis2.position();
      
      // check if the value is inside of the deadband range
      if (drivetrainLeftSideSpeed < 5 && drivetrainLeftSideSpeed > -5) {
        // check if the left motor has already been stopped
        if (DrivetrainLNeedsToBeStopped_Controller1) {
          // stop the left drive motor
          LeftDriveSmart.stop();
          // tell the code that the left motor has been stopped
          DrivetrainLNeedsToBeStopped_Controller1 = false;
        }
      } else {
        // reset the toggle so that the deadband code knows to stop the left motor nexttime the input is in the deadband range
        DrivetrainLNeedsToBeStopped_Controller1 = true;
      }
      // check if the value is inside of the deadband range
      if (drivetrainRightSideSpeed < 5 && drivetrainRightSideSpeed > -5) {
        // check if the right motor has already been stopped
        if (DrivetrainRNeedsToBeStopped_Controller1) {
          // stop the right drive motor
          RightDriveSmart.stop();
          // tell the code that the right motor has been stopped
          DrivetrainRNeedsToBeStopped_Controller1 = false;
        }
      } else {
        // reset the toggle so that the deadband code knows to stop the right motor next time the input is in the deadband range
        DrivetrainRNeedsToBeStopped_Controller1 = true;
      }
      
      // only tell the left drive motor to spin if the values are not in the deadband range
      if (DrivetrainLNeedsToBeStopped_Controller1) {
        LeftDriveSmart.setVelocity(drivetrainLeftSideSpeed, percent);
        LeftDriveSmart.spin(forward);
      }
      // only tell the right drive motor to spin if the values are not in the deadband range
      if (DrivetrainRNeedsToBeStopped_Controller1) {
        RightDriveSmart.setVelocity(drivetrainRightSideSpeed, percent);
        RightDriveSmart.spin(forward);
      }
      // check the ButtonL1/ButtonL2 status to control Intake
      if (Controller1.ButtonL1.pressing()) {
        Intake.spin(forward);
        Controller1LeftShoulderControlMotorsStopped = false;
      } else if (Controller1.ButtonL2.pressing()) {
        Intake.spin(reverse);
        Controller1LeftShoulderControlMotorsStopped = false;
      } else if (!Controller1LeftShoulderControlMotorsStopped) {
        Intake.stop();
        // set the toggle so that we don't constantly tell the motor to stop when the buttons are released
        Controller1LeftShoulderControlMotorsStopped = true;
      }
      // check the ButtonR1/ButtonR2 status to control Flywheel
      if (Controller1.ButtonR1.pressing()) {
        Flywheel.spin(forward);
        Controller1RightShoulderControlMotorsStopped = false;
      } else if (Controller1.ButtonR2.pressing()) {
        Flywheel.spin(reverse);
        Controller1RightShoulderControlMotorsStopped = false;
      } else if (!Controller1RightShoulderControlMotorsStopped) {
        Flywheel.stop();
        // set the toggle so that we don't constantly tell the motor to stop when the buttons are released
        Controller1RightShoulderControlMotorsStopped = true;
      }
    }
    // wait before repeating the process
    wait(20, msec);
  }
  return 0;
}

task rc_auto_loop_task_Controller1(rc_auto_loop_function_Controller1);

// Include the V5 Library
#include "vex.h"
  
// Allows for easier use of the VEX Library
using namespace vex;

competition Competition;

// User defined function
void myblockfunction_cat();
// User defined function
void myblockfunction_Cat_animation();

int Brain_precision = 0, Console_precision = 0, Controller1_precision = 0;

float myVariable, test;

event message1 = event();
event Driver = event();

// User defined function
void myblockfunction_cat() {
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1, 1);
  Brain.Screen.print("    /\\_____/\\");
  Brain.Screen.newLine();
  Brain.Screen.print("   /  o   o  \\");
  Brain.Screen.newLine();
  Brain.Screen.print("  ( ==  ^  == )");
  Brain.Screen.newLine();
  Brain.Screen.print("   )         (");
  Brain.Screen.newLine();
  Brain.Screen.print("  (           )");
  Brain.Screen.newLine();
  Brain.Screen.print(" ( /  \\   /  \\ )");
  Brain.Screen.newLine();
  Brain.Screen.print("(__(__)___(__)__)");
  Brain.Screen.newLine();
}

// User defined function
void myblockfunction_Cat_animation() {
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   / o   o   \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  o   o  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /   o  o  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  o   o  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  -   -  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  o   o  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  -   -  \\");
  wait(0.5, seconds);
  Brain.Screen.setCursor(2, 1);
  Brain.Screen.clearLine(2);
  Brain.Screen.setCursor(Brain.Screen.row(), 1);
  Brain.Screen.print("   /  o   o  \\");
}

// "when started" hat block
int whenStarted1() {
  return 0;
}

// "when autonomous" hat block
int onauton_autonomous_0() {
  Drivetrain.setDriveVelocity(100.0, percent);
  Intake.setVelocity(100.0, percent);
  Flywheel.setVelocity(100.0, percent);
  Flywheel.spin(reverse);
  Drivetrain.drive(forward);
  wait(0.5, seconds);
  Intake.spinFor(forward, 70.0, degrees, true);
  Drivetrain.driveFor(reverse, 4.0, inches, true);
  Drivetrain.turnFor(right, 90.0, degrees, true);
  wait(1.0, seconds);
  Intake.spin(reverse);
  wait(2.0, seconds);
  Flywheel.stop();
  Intake.stop();
  Driver.broadcast();
  return 0;
}

// "when driver control" hat block
int ondriver_drivercontrol_0() {
  while (true) {
    if (Controller1.ButtonY.pressing()) {
      Expansion.spinFor(forward, 90.0, degrees, true);
    }
  wait(5, msec);
  }
  return 0;
}

// "when I receive Driver" hat block
void onevent_Driver_0() {
}

// Used to find the format string for printing numbers with the
// desired number of decimal places
const char* printToController1_numberFormat() {
  // look at the current precision setting to find the format string
  switch(Controller1_precision){
    case 0:  return "%.0f"; // 0 decimal places (1)
    case 1:  return "%.1f"; // 1 decimal place  (0.1)
    case 2:  return "%.2f"; // 2 decimal places (0.01)
    case 3:  return "%.3f"; // 3 decimal places (0.001)
    default: return "%f"; // use the print system default for everthing else
  }
}

// "when driver control" hat block
int ondriver_drivercontrol_1() {
  // use while testing
  myblockfunction_cat();
  Flywheel.setVelocity(75.0, percent);
  Intake.setVelocity(100.0, percent);
  Controller1.Screen.print(printToController1_numberFormat(), static_cast<float>(Flywheel.torque(Nm)));
  Brain.Screen.print("VEXcode");
  while (true) {
    myblockfunction_Cat_animation();
  wait(5, msec);
  }
  return 0;
}

void VEXcode_driver_task() {
  // Start the driver control tasks....
  vex::task drive0(ondriver_drivercontrol_0);
vex::task drive1(ondriver_drivercontrol_1);
  while(Competition.isDriverControl() && Competition.isEnabled()) {this_thread::sleep_for(10);}
  drive0.stop();
drive1.stop();
  return;
}

void VEXcode_auton_task() {
  // Start the auton control tasks....
  vex::task auto0(onauton_autonomous_0);
  while(Competition.isAutonomous() && Competition.isEnabled()) {this_thread::sleep_for(10);}
  auto0.stop();
  return;
}



int main() {
  vex::competition::bStopTasksBetweenModes = false;
  Competition.autonomous(VEXcode_auton_task);
  Competition.drivercontrol(VEXcode_driver_task);

  // Calibrate the Drivetrain
  calibrateDrivetrain();

  // register event handlers
  Driver(onevent_Driver_0);

  wait(15, msec);
  // post event registration

  // set default print color to black
  printf("\033[30m");

  // wait for rotation sensor to fully initialize
  wait(30, msec);

  whenStarted1();
}