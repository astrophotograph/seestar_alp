# Seestar Alpaca API Commands

This document lists all the `method_sync` API calls used in the Seestar Alpaca API.

## Overview

The Seestar Alpaca API uses a common pattern for synchronous method calls with the `method_sync` action. These calls are made to the endpoint:

```
PUT {{base_url}}/api/v1/telescope/{{dev_num}}/action
```

With form URL encoded body parameters:
- `Action: method_sync`
- `Parameters`: JSON formatted parameters specific to each command
- `ClientID`: Client identifier (typically 1)
- `ClientTransactionID`: Transaction identifier (typically 999)

## Available Commands

### Camera Controls

- **set_control_value**
  - Sets camera control values like gain
  - Example parameters: `{"method":"set_control_value", "params":["gain",80]}`

### Heater Controls

- **pi_output_set2**
  - Controls heater state and value
  - Example parameters: `{"method":"pi_output_set2", "params":{"heater":{"state":true,"value":90}}}`

### File Management

- **get_albums**
  - Retrieves album information

- **set_img_name_field**
  - Sets image naming field configuration

- **set_sequence_group_name**
  - Sets the name for a sequence group of images

- **get_img_name_field**
  - Gets the current image naming field configuration

### Telescope Functions

- **scope_park**
  - Parks the telescope

- **scope_move_to_horizon**
  - Moves the telescope to the horizon position

- **scope_speed_move**
  - Moves the telescope at a specified speed and direction
  - Example for fast movement: `{"method":"scope_speed_move","params":{"speed":1000,"angle":90,"dur_sec":4}}`
  - Example for stopping: `{"method":"scope_speed_move","params":{"speed":0,"angle":0,"dur_sec":3}}`
  - Parameters:
    - `speed`: Movement speed (0 to stop)
    - `angle`: Direction angle in degrees (0-360)
    - `dur_sec`: Duration in seconds

- **get_focuser_position**
  - Gets the current focuser position

- **start_auto_focuse**
  - Starts the auto-focus process

- **stop_auto_focuse**
  - Stops the auto-focus process

### Filter Wheel Functions

- **get_wheel_position**
  - Gets the current filter wheel position

- **get_wheel_state**
  - Gets the current filter wheel state

- **get_wheel_setting**
  - Gets filter wheel settings

- **set_wheel_position**
  - Sets the filter wheel position
  - Example parameters for different filters:
    - LP filter: `params=[2]`
    - IR Cut filter: `params=[1]`
    - Dark filter: `params=[0]`

### Plate Solving

- **start_solve**
  - Starts the plate solving process

- **get_solve_result**
  - Gets the current plate solving result

- **get_last_solve_result**
  - Gets the last plate solving result

### Polar Alignment

- **start_polar_align**
  - Starts the polar alignment procedure

- **stop_polar_align**
  - Stops the polar alignment procedure

### Dark Frame Creation

- **start_create_dark**
  - Starts dark frame creation

- **stop_create_dark**
  - Stops dark frame creation

### System Functions

- **pi_reboot**
  - Reboots the Raspberry Pi

- **pi_shutdown**
  - Shuts down the Raspberry Pi

- **pi_get_ap**
  - Gets access point information

- **get_disk_volume**
  - Gets disk volume information

### Settings and Status

- **get_app_setting**
  - Gets application settings

- **iscope_get_app_state**
  - Gets the application state

- **get_camera_exp_and_bin**
  - Gets camera exposure and binning settings

- **get_camera_state**
  - Gets camera state

- **get_controls**
  - Gets control settings

- **get_image_save_path**
  - Gets the image save path

- **get_setting**
  - Gets general settings

- **get_stack_info**
  - Gets stacking information

- **get_test_setting**
  - Gets test settings

- **get_user_location**
  - Gets user location information

- **get_view_state**
  - Gets view state

### Coordinates and Position

- **scope_get_equ_coord**
  - Gets equatorial coordinates

- **scope_get_horiz_coord**
  - Gets horizontal coordinates

- **scope_get_ra_dec**
  - Gets right ascension and declination

### Image Stacking

- **iscope_start_stack**
  - Starts image stacking

- **iscope_stop_view**
  - Stops the view

### Control Management

- **set_setting**
  - Sets various settings
  - Example for control grabbing: `{"method": "set_setting", "params": {"master_cli": true}}`
  - Example for control release: `{"method": "set_setting", "params": {"master_cli": false}}`
  - Example for exposure settings: `{"method": "set_setting", "params": {"exp_ms": {"stack_l": 10000, "continuous": 500}}}`
  - Example for auto-exposure brightness: `{"method": "set_setting", "params": {"ae_bri_percent": 90}}`
  - Example for dithering: `{"method": "set_setting", "params": {"stack_dither": {"pix": 50, "interval": 15, "enable": true}}}`
  - Example for horizontal calibration: `{"method": "set_setting", "params": {"auto_3ppa_calib": true}}`
  - Example for light enhancement: `{"method": "set_setting", "params": {"stack_lenhance": true}}`
  - Example for auto-focus after goto: `{"method": "set_setting", "params": {"auto_af": true}}`
  - Example for stacking after goto: `{"method": "set_setting", "params": {"stack_after_goto": false}}`

- **set_app_setting**
  - Sets application-specific settings
  - Example for goto target name: `{"method":"set_app_setting","params":[{"goto_target_name":"Kai_goto_target_name"}]}`
  - Example for air compatibility: `{"method":"set_app_setting", "params":{"air_compatible":true}}`

- **set_stack_setting**
  - Configures image stacking settings
  - Example: `{"method":"set_stack_setting", "params":{ "save_discrete_frame": true, "save_discrete_ok_frame": true, "light_duration_min": -1}}`

- **set_sequence_setting**
  - Configures sequence settings
  - Example for setting group name: `{"method":"set_sequence_setting","params":[{"group_name":"kai_Sombrerro"}]}`
