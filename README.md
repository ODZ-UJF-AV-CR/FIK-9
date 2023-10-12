# FIK-9 - High-altitude balloon dosimetry experiment

[Department of Radiation Dosimetry of the Nuclear Physics Institute of the Czech Academy of Sciences](http://www.ujf.cas.cz/en/departments/department-of-radiation-dosimetry/contact/) high-altitude balloon experiment

### Repo TODO
- [ ] Block diagram update
- [ ] PX4Firmware FMUv5
- [ ] (?) PX4Firmware extender with Lora device
- [ ] One direction Sik Modem Firmware 
- [ ] Ground Software 
- [ ] Car Software
- [ ] Standalone tracking device FW
- [ ] Payload FW

![Sw diagram](doc/img/fik_9_sw_data.png)

![Block diagram](doc/img/block_schematics.png)


### Scientific payload
(??)

### Supporting instruments
 - [ ] Cuav FMUv5 with PX4 Firmware
   - [ ] Sik telemetry
   - [ ] Lora Telemetry (TX/RX)
   - [ ] More advanced position estimation
   - [ ] (?) Driving cut device
   - [ ] Temperature measurement
   - [ ] Logging processed data from payload
 - [ ] Standalone tracking device
 - [ ] Cutting device

### Design features
  * Redundant telemetry link
  * Gondola orientation tracking and logging
  * Reliable IMU sensor processing and calibration
  * Possible of use relatively high-power payloads
  * Pre-flight continuous charging possible
  * Power monitoring and maximal uptime calculation relevant to actual temperature

### Flight data

### Links
  * [Facebook](https://www.facebook.com/balonfik/)
