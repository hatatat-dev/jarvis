# Jarvis

Jarvis is the name of the team 21919A competing at [VEX Robotics](https://www.vexrobotics.com/) in 2022-2023.

This GitHub repository contains
* the main program [jarvis.v5blocks](jarvis.v5blocks) for VEXcode V5 development environment [codev5.vex.com](https://codev5.vex.com/),
* [bundle.py](bundle.py) command-line tool in Python for packing and unpacking v5blocks format for review and collaboration, and
* result of unpacking of the main program into [.workspace](jarvis.v5blocks.workspace), [.cpp](jarvis.v5blocks.cpp) and [.base](jarvis.v5blocks.base) parts.

## Loading the program to the robot

To load the program to the robot,
1. Get a local copy of the repository by cloning it with git or GitHub Desktop, or downloading [develop.zip](https://github.com/hatatat-dev/jarvis/archive/refs/heads/develop.zip) archive from GitHub,
1. Open VEXcode V5 development environment [codev5.vex.com](https://codev5.vex.com/) in a browser,
1. In the top **left** menu, click on `File`, then click on `Load From Your Device`,
1. Navigate to the local copy of the repository and select the jarvis.v5blocks file,
1. See the program blocks successfully loaded on the screen,
1. In the top **right** menu, click on `Brain`, then click on `Connect`,
1. Follow the prompts, click `Continue` and select the robot,
1. See the successful connection enabling `Download` button in the top **right** menu,
1. In the top **right** menu, click on `Download` and load the program to the robot,
1. (Optionally) in the top **right** menu, click on `Start` to start the program on the robot.

## Saving the program to the GitHub repository

To save the program to the GitHub repository,
1. Have the program version you want to save open in VEXcode V5 development environment,
1. In the top **left** menu, click on `File`, then click on `Save To Your Device`,
1. See the program downloaded to a local file with extension .v5blocks, possibly in `Downloads` folder as `VEXcode Project.v5blocks` or `jarvis.v5blocks`,
1. In case there already existed a file with the same name browser may add a number in parenthesis to the file name to distinguish the versions,
1. Overwrite `jarvis.v5blocks` in the local repository with the new file,
1. Commit the change with git or GitHub Desktop to `develop` branch of the repository,
1. Push the changes to the `origin` (actual GitHub repository),
1. Review the history of the `develop` branch in GitHub repository to see the changes at [github.com/hatatat-dev/jarvis/commits/develop](https://github.com/hatatat-dev/jarvis/commits/develop)

Enjoy the robotics!
