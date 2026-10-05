# ecps216_hackathon

Simple burglar deterrent

I (Autumn) live in DTLA on the ground floor of an apartment building and semi-regularly end up with people hopping the fence onto my patio and stealing my stuff (e.g. plant lights). The idea for this project is to create a simple system that will attempt to deter someone in a way that doesn't contribute to the surveillance state. The basic concept is to use a capacitive sensor that detects someone grabbing the fence to jump over, a speaker exciter that will play a loud, unpleasant noise, and a system to send an email. To make the system more robust to real-world conditions, it will also integrate a moisture sensor that will prevent the capacitive sensors from triggering based on e.g. rain.

Parts:
MPR121, 12-channel capacitive sensor
Moisture sensor
Speaker exciter
Raspberry Pi

Phase 1:
Basic code to read sensor data, determine a touch, and output audio and an email.
Autumn: speaker output/DAC
Andrew: read capacitive sensor, basic decision code
Jonathan: moisture sensor, email sending
