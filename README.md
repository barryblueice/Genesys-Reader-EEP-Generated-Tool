# Genesys Reader EEP Generated Tool
A tool to generate EEP file which can use for customizing your Genesys Reader Identificaion.

<img width="761" height="765" alt="image" src="https://github.com/user-attachments/assets/31211429-067c-47ff-947c-66d03de5dd6c" />

Currently Supported:

 - The GL3224 and earlier models that support firmware flashing for controllers. Newer controllers model like GL3227E and GL3231S don't have eep support (only can write firmware).

# How To Use:

1.Download `Genesys Reader EEP Generated Tool.exe` and `MultiTool 2.1.2.5` from [Releases](https://github.com/barryblueice/Genesys-Reader-EEP-Generated-Tool/releases/latest).

2. Generated EEP File by using tool.

3. Open MultiTool Software.<br>If supported Genesys Reader is not detected, all function will disable:

<img width="646" height="286" alt="image" src="https://github.com/user-attachments/assets/5167839a-98fc-45a2-b3b3-3eb188d3faf2" />

after recognized Genesys Reader, all function will enable.

<img width="643" height="291" alt="image" src="https://github.com/user-attachments/assets/7b142e2c-23c5-4935-ae2b-0903026bc901" />

4. Click `F/W & EEPROM`, enter `EEPROM/Flash Writer`:

<img width="588" height="683" alt="image" src="https://github.com/user-attachments/assets/8215eae0-0315-499c-881e-65785ae681b2" />

5. First erase SPI, to make sure we can operate SPI:

<img width="584" height="697" alt="image" src="https://github.com/user-attachments/assets/0c738790-b37d-4563-bbba-ea77edf408f5" />

If SPI working well, then will display this message:

<img width="586" height="681" alt="image" src="https://github.com/user-attachments/assets/d4a2e2b3-92f5-4aef-acdd-ba29cfa55528" />

If SPI is not support or SPI cannot operate, then will display this message:

<img width="575" height="685" alt="image" src="https://github.com/user-attachments/assets/7f9f9420-fdda-4d58-8b0f-baf559027db9" />

You need to add SPI parameters in `Config` folders or checking spi if soldering well.

6. Click `Load eep file`, loads the eep file we generated:

<img width="582" height="683" alt="image" src="https://github.com/user-attachments/assets/7535344f-542f-4e09-ab4c-bc32f0ee99cb" />

After loading eep file, we can edit the eep parameters.

<img width="583" height="687" alt="image" src="https://github.com/user-attachments/assets/d5735f82-421c-4960-ac12-3085faa97777" />

If reporting on error `String define error`:

<img width="585" height="689" alt="image" src="https://github.com/user-attachments/assets/25aefdb6-2f7a-4264-b1a5-be95e23de221" />

that means Card-Str cannot empty. However, it will not affect the normal operation of the firmware.

If Card-Str in generated eep file is empty, then after writing firmware & EEP Setting, there will be three spaces before the device name. That's a really strange bug for MultiTool.

To fix this bug, you need to define Card-Str first in Generated Tool, then delete it in the MultiTool EEP Setting.

7. Click `Load FW File` to load Genesys Reader Firmware:

<img width="580" height="692" alt="image" src="https://github.com/user-attachments/assets/7f6881ba-38a6-4317-893a-d537539788d9" />

After loading complete, checking `Write EEP File & F/W`:

<img width="580" height="692" alt="image" src="https://github.com/user-attachments/assets/93e23176-8187-48a5-82fb-f8c132886059" />

8. Then clicking `Write F/W` to writing firmware & EEP setting:

<img width="580" height="692" alt="image" src="https://github.com/user-attachments/assets/052c45cd-f20d-43b0-99f2-d446ee27991a" />

9. If successfully to writing firmware, then will display this message or similiar message:
<img width="586" height="686" alt="image" src="https://github.com/user-attachments/assets/0874d786-98eb-48f2-a8f3-9d97e5d0ac12" />

10. Re-plugging your Genesys Reader to apply new firmware & EEP setting.
