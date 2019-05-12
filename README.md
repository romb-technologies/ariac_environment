# Ariac Gazebo environment

A Gazebo simulation environment adapted from the [ARIAC competition](http://gazebosim.org/ariac) environment (2017 edition).

## Installation

Install dependencies (must be invoked from workspace root!)

```
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y -r
```
then build the package and source the workspace setup file.

## Running the simulation

Launch the ARIAC world and spawn a P3-DX robot.
```
roslaunch ariac_environment p3dx_in_ariac_world.launch
```

## Development notes

...adding navigation functionality ...

### Naming conventions

Launch file naming ...
```
<(gazebo environment name)>_<robot_type>_<(localization)>_<(control)>.launch
```


