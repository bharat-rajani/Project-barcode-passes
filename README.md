# Project-barcode-passes

This project is based on automated creation of event passes with barcode and realtime detection and authentication of barcode.

Before :
![alt text](https://github.com/bharat-rajani/Project-barcode-passes/blob/master/TYFPASSES.jpg)
After :



Scenerio: To prevent the forgery of event passes so that unauthenticated people are not allowed to attend the event.

Solution: 

Module 1: Creating barcode passes.

I solved this problem by creating 5000 EAN(European Article Number) type barcodes and pasting them on our college-level event passes.These 5000 passes are created automatically. Code for creation of passes is in "barcoded_passes.py".


Module 2:Authenticating the passes.


Authentication system was created to scan a pass for only one time and then return a "Duplicate Pass" string on successive scans.

Key features:

*Rich analytics on scanned pass data.
*Exported all the data into excel.
*Show the time of scan.
*Show the name of person who allotted pass to the attendee.

Module 3:

In above module I used a barcode scanner for scanning the passes.In this module I completely removed the usage of barcode scanner hardware.
All the passes are now detected with deep learning algorithms and openCV.After detection these passes are scanned.
This module is in development stage and it makes this project as pure python magic.
