# FIK-9 - High-altitude balloon dosimetry experiment

[Department of Radiation Dosimetry of the Nuclear Physics Institute of the Czech Academy of Sciences](http://www.ujf.cas.cz/en/departments/department-of-radiation-dosimetry/contact/) high-altitude balloon experiment

![FIK-9 just before takeoff](doc/img/FIK-9_takeoff.jpg)

![FIK-9 rescue team on touch down site](doc/img/FIK-9_rescue_team.jpg)


### Repo TODO for documenting
- [ ] Block diagram update
- [x] Correct submodule version PX4Firmware FMUv5
- [x] Link to the used one-way Sik Modem Firmware 
- [ ] Ground Software description
- [ ] Rescue cars Software description
- [ ] Standalone tracking device FW
- [ ] Payload FW and scripts

![Sw diagram](doc/img/fik_9_sw_data.png)

![Block diagram](doc/img/block_schematics.png)

![FIK-9 gondola opened after touch down](doc/img/FIK-9_gondola_opened_after_touchdown.jpg)

### Used Scientific payload

 - [AIRDOS04A Prototype](https://github.com/UniversalScientificTechnologies/AIRDOS04) 
 - [LABDOS01B](https://github.com/UniversalScientificTechnologies/LABDOS01)
 - [LABDOS01A](https://github.com/UniversalScientificTechnologies/LABDOS01/tree/LABDOS01A)
 - PiTED?
 - MiniPIX
 -

### The used experiment support devices and technologies

 - CUAV V5+ FMUv5 with customised PX4 Firmware supporting
   - [433 MHz Sik telemetry (one-way TX only firmware)](https://docs.thunderfly.cz/avionics/TFSIK01/)
   - [868 MHz Lora Telemetry (TX only)](https://docs.thunderfly.cz/avionics/TFLORA01/)
   - [TFHT01 Temperature and humidity sensors](https://docs.thunderfly.cz/avionics/TFHT01/)
   - [TF-ATMON Logging of data from the payload](https://docs.thunderfly.cz/instruments/TF-ATMON)
 - Standalone 433 MHz CW transmitter

### Design features

  * Redundant telemetry link
  * Gondola orientation tracking and logging
  * Reliable IMU sensor processing and calibration
  * Possible use of relatively high-power payloads
  * Pre-flight continuous charging possible
  * Power monitoring and maximal uptime calculation relevant to actual temperature

### Flight data

![Screenshots of FIK-9 trajectory just before touch down](doc/img/FIK-9_landing_trajectory.png)

![Comparison of radiation captured by LABDOS01B and AIRDOS04 prototype](doc/img/LABDOS01B_AIRDOS04_raw_data.png)



### Links
  * [Facebook](https://www.facebook.com/balonfik/)
