#  A.4. Implementation
##  A.4.1. System Startup
  1. Boot from the kernel diskette.
  2. Insert the root floppy when prompted.
  3. When prompted for a /usr diskette, say 'Y'.
  4. Insert the mp3blaster diskette and press **Enter**.


* * *
##  A.4.2. Verify that the /usr diskette loaded properly
```
bash# mount
bash# ls -lR /usr
```

---
* * *
##  A.4.3. Check the audio device initialization
```
bash# dmesg | more
```

---
If everything worked there should be a line or two indicating that the kernel found the audio hardware. The example below shows how the kernel might report a Yamaha integrated sound system.
```
ymfpci: YMF740C at 0xf4000000 IRQ 10
ac97_codec: AC97 Audio codec, id: 0x4144:0x5303 (Analog Devices AD1819)

```

---
* * *
##  A.4.4. Test audio output
```
bash# echo "Garbage" > /dev/dsp
```

---
A short burst of static coming from the PC speakers indicates that sound is working.
* * *
##  A.4.5. Play a sample file
Insert the diskette containing the sample audio file.
```
mount /dev/fd0 /home
bash# /usr/bin/mp3blaster
```

---
Use mp3blaster to select and play the file `/home/torvalds-says-linux.mp3`. Use mp3blaster's mixer controls to adjust the volume as needed.
* * *
##  A.4.6. System shutdown
Bring the system down gracefully with the **shutdown** command.
* * *
