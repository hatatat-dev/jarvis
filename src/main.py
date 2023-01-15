#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain_inertial = Inertial(Ports.PORT8)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_inertial, 319.19, 320, 255, MM, 1)
Intake = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
Flywheel_motor_a = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
Flywheel_motor_b = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
Flywheel = MotorGroup(Flywheel_motor_a, Flywheel_motor_b)
Expansion = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)

def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    drivetrain_inertial.calibrate()
    while drivetrain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)



# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # stop the motors if the brain is calibrating
            if drivetrain_inertial.is_calibrating():
                left_drive_smart.stop()
                right_drive_smart.stop()
                while drivetrain_inertial.is_calibrating():
                    sleep(25, MSEC)
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
            # check the buttonL1/buttonL2 status
            # to control Intake
            if controller_1.buttonL1.pressing():
                Intake.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                Intake.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                Intake.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control Flywheel
            if controller_1.buttonR1.pressing():
                Flywheel.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                Flywheel.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                Flywheel.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)
#endregion VEXcode Generated Robot Configuration
vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
myVariable = 0
test = 0
message1 = Event()
Driver = Event()

def cat():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("    /\\_____/\\")
    brain.screen.next_row()
    brain.screen.print("   /  o   o  \\")
    brain.screen.next_row()
    brain.screen.print("  ( ==  ^  == )")
    brain.screen.next_row()
    brain.screen.print("   )         (")
    brain.screen.next_row()
    brain.screen.print("  (           )")
    brain.screen.next_row()
    brain.screen.print(" ( /  \\   /  \\ )")
    brain.screen.next_row()
    brain.screen.print("(__(__)___(__)__)")
    brain.screen.next_row()

def Cat_animation():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   / o   o   \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  o   o  \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /   o   o \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  o   o  \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  -   -  \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  o   o  \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  -   -  \\")
    wait(0.5, SECONDS)
    brain.screen.set_cursor(2, 1)
    brain.screen.clear_row(2)
    brain.screen.set_cursor(brain.screen.row(), 1)
    brain.screen.print("   /  o   o  \\")

def when_started1():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    pass

def onauton_autonomous_0():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    drivetrain.set_drive_velocity(100, PERCENT)
    Intake.set_velocity(100, PERCENT)
    Flywheel.set_velocity(100, PERCENT)
    Flywheel.spin(REVERSE)
    # right
    drivetrain.drive_for(REVERSE, 27, INCHES, wait=True)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    # roller
    drivetrain.drive(FORWARD)
    wait(0.5, SECONDS)
    Intake.spin_for(FORWARD, 260, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 4, INCHES, wait=True)
    # right low goal
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    Intake.spin(REVERSE)
    wait(2, SECONDS)
    Intake.stop()

def ondriver_drivercontrol_0():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    # use while testing
    cat()
    Flywheel.set_velocity(65, PERCENT)
    Intake.set_velocity(100, PERCENT)
    controller_1.screen.print(Flywheel.torque(TorqueUnits.NM), precision=6 if vexcode_controller_1_precision is None else vexcode_controller_1_precision)
    brain.screen.print("VEXcode")
    while True:
        Cat_animation()
        wait(5, MSEC)

def ondriver_drivercontrol_1():
    global myVariable, test, message1, Driver, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    while True:
        if controller_1.buttonY.pressing():
            Expansion.spin_for(FORWARD, 90, DEGREES, wait=True)
        wait(5, MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )
    driver_control_task_1 = Thread( ondriver_drivercontrol_1 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()
    driver_control_task_1.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()