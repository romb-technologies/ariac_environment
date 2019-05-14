# Ariac Gazebo environment

A Gazebo simulation environment adapted from the [ARIAC competition](http://gazebosim.org/ariac) environment (2017 edition).

## Installation

Install dependencies (must be invoked from workspace root!)

```
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y -r
```
then build the package and source the workspace setup file.

## Running the simulation

Launch the ARIAC world and spawn a P3-DX robot with fake localization.
```
roslaunch ariac_environment ariac_p3dx_fakeloc_rviz.launch
```
To drive the robot manually using the keyboard, launch (from another terminal):
```
roslaunch ariac_environment teleop_keyboard.launch
```
## Development notes

TODO: add navigation functionality ...

### Naming conventions

Launch files shall be named according to the following pattern (values in parentheses are optional):
```
<(gazebo environment name)>_<robot_type>_<(localization)>_<(control)>_<(visualization)>.launch
```
e.g.
```
ariac_p3dx_fakeloc_rviz.launch
```
Launches the Ariac Gazebo environment, with a p3dx model, fake localization, no control and RViz visualization.

