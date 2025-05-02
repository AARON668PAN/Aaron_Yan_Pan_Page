# Phasespace Ros node

this package contains a wrapper of the phasespace api to track rigid bodies. The phasespace api used in this package is **5.3**  

### 1. Connecting to the Phasespace MoCap System:
- Open your preferred web browser on your computer or mobile device.
- In the address bar, enter the following:
    ```
    [IP address of the Phasespace system]
    ```
- On the login page, enter the credentials:
    - **Username:** `admin`
    - **Password:** `phasespace`
- Click on the 'Login' button or equivalent to access the system's dashboard.

### 2. Inspecting the System Components:
- After logging in, you'll be directed to the system's main dashboard.
    - **Cameras:** Navigate to the camera section to view the status and details of each attached camera.
    - **Trackers:** Check the trackers' section to view the status and details of all active and connected trackers.
    - **Session Profile:** Under this section, you can adjust settings specific to your current mocap session.
    
## Step 2.1: Prepare your devices for use

### Verify connected cameras
- Make sure all cameras are properly connected and functioning.

### Visit the Configuration Manager
- Navigate to `Hub Status` to overview the system's configuration and status.
  
![Configuration Manager](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/scanports-search.gif) 

### Pair your LED Driving devices with the system
![Tracker](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/ProductShot_MicroDriver.png) 
- All LED Driving devices need to be discovered and recognized by the system before being put to use.
- It's essential to designate one of these devices explicitly for use during the Calibration step.

### Place the device in "pairing" mode
1. To put the device into "pairing" mode, press and hold the white button.
2. Wait for the yellow LED to flash 3 times.

### Device Discovery
- After the "device discovery" step, deactivate the "pairing" mode by:
    1. Hold the white button until the device powers off (roughly 8 seconds).
    2. Press the white button once more to power it back on.

#### Demo: device discovery
![Device Discovery GIF](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/rfdevices-search.gif) 

#### Demo: designate a calibration device

![Designate Calibration Device GIF](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/rfdevices-calib.gif) 

## Create a Session Profile with all of your LED IDs accounted for

Once the devices have been discovered, it's imperative to specify the role of each device. The Profile we're about to craft will clarify the IDs broadcasted by every device, among other settings.

### Demo: Create the new session profile
![Create Session Profile GIF](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/profiles-add.gif)
![Edit Session Profile GIF](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/profiles-edit.gif)

### Demo: Add your device to the profile

![Add Device to Profile Image](https://github.com/RPL-CS-UCL/phasespace_ros_node/blob/main/phasespace_client/images/profile-add-dev.gif)

### 3. Calibrating the Phasespace System:
- Calibration is essential for optimal motion capture results.
    - **Downloading the Calibration Master:**
        1. Visit the [Phasespace official website](https://customers.phasespace.com/anonymous/Software/5.3) using login: anonymous, password: guest.
        2. Go to the 'Downloads' or similar section.
        3. Download the appropriate Calibration Master version. (Ubuntu 20.04 is found under experimental named "psclient-3")
        4. Save and run the software on your computer.   
           (this is done by typing "./master" in the terminal where you downloaded the Master client)
### 3.1. **System Connection**:
- **Master Access**: Always access the system through the Master.
- **IP Address**: Specify the correct IP address of the system.
    - **Note**: In our lab, all systems are accessible through the router.

### 3.2. **Starting Calibration**:
- After establishing a connection, navigate to the left column and select `Calibration`.
- Click on `Start` to begin the calibration procedure.

### 3.3. **Using the Calibration Wand**:
- Calibration is performed with the help of the calibration wand.
- **Pre-requisites**:
    - Ensure the calibration wand is equipped with a tracker.
    - The tracker must be associated with the system as a calibration device.
        - **Reference**: See the section above for detailed steps.

### 3.4. **During Calibration**:
- Move around with the calibration wand to cover as much of the mocap system's area as possible.
- The goal is to have the 2D camera views show substantial green regions, indicating the space is adequately covered.

### 3.5. **Data Optimization**:
- There are 4 stages in the optimization process.
- All stages must be completed for a successful calibration.
- **Optimization Results**:
    - The result displays as a cost function value.
    - Ideally, by the end of the 4 stages, the number should range between `2` and `0.8`.
        - **Note**: You can accept a result with a higher number, but the precision will decrease.

### 3.6. **Alignment**:
- After optimization, proceed with alignment.
    - This can be selected directly from the calibration window or found in the same menu as the calibration function on the Master program.

### 3.7. **Recommendation for Calibration**:
- It's advised to use `Automatic Snapshots` during calibration.
    - In this mode, holding the calibration wand, you can:
        1. Select the center of the reference frame.
        2. Define the X and Z axes (Phasespace's reference frame is XZY). Move the wand from the center towards the X and Z directions, touching the ground each time.
    - Upon collecting each of the three pieces of information (center, X, Z), the screen on the Master will flash green as a confirmation.


# Ros Node Installation

assuming that ROS noetic with catkin-tools has been installed in your machine, to install the package it is sufficient to create a catkin workspace and after that run:

```
catkin build phasespace
```

# Usage

to run the package first you need to ensure that the client computer is connected to the same subnet to which the phasespace is connected to. to run the package just run:

```
rosrun phasespace phasespace_node $PHASESPACE_IP rigid_object.json
```

instead of **$PHASESPACE_IP** you should use the current ip of the phasespace on the subnet (to know which is the phasespace ip there exist plenty of tools booth for ubuntu and android (NMAP on ubuntu netananalyzer on android), or accessing the router and check the connected device will do the job.

rigid_object.json contains all the information about your rigid body. for tracking your rigid you have to create a new one using the LED markers on the rigid body you want to track. To create the json file you need to use the master app that can be downloaded from [here](https://customers.phasespace.com/anonymous/Software/5.3/). Download the master client and in the bin folder you can find the master executable.

once you run it you have to select the markers on the rigid body that you want to track and after clicking on the left **OWL Trackers** and then click on the **create** button. To make the json file visible to the package move the file inside the **rigid_body_objects** in the package folder

Master app interface: 
![images that show the master app interface to create a rigid body json file](https://github.com/RPL-CS-UCL/phasesapce/blob/main/phasespace_client/images/create_json_rigid_body.png "master interface")

the ros node opens 3 topic:

1.  **\phasespace_cameras** which contains the rototraslation of the camera w.r.t. the reference frame
2.  **\phasespace_markers** which contains the rototraslation of each LED marker w.r.t. the reference frame
3.  **\phasespace_rigids** which contains the rototraslation of the **single** rigid body in the scene

# TO DO

1. adding multi rigid body support
2. adding scan function to automatically detect the phasespace server on the router 
3. adding flag to selc what information stream (now everything is published)
