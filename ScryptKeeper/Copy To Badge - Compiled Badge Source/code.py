import scryptkeeper

"""
                             
                                 ,,,,,,,, ,,* *                                 
                             ,,,,,*,*        * **,**                            
                        ,,,*,,,,,., ,*****,*,,,,,**,,. ..,,,,                   
                   **,,,,,,,,,,,,,*********,*,,,,*,,*,,,,,,**,*                 
                 *,,,,,,,,,,,,,,,,,,,   ,,,,***,,,,,,,,**,,,,**,*               
              .*,,*,,,,,,,,,,.  .,,,   .,,,,,,,,,.   ..,.,,,,,,,***             
            ,**,,,,.                  ,,,                 .,,.,,,***,           
          .,,,,,,.                                            , ,,,,,,          
         ,**,,,.    ,//*/////////*///* *,****** ,,*, .*# (        ,.,,,,        
       *,*,*,.  /*/*,/  .(/,*/(*//*(/, *,/* */*./*(##/((#((%#**,*   ,.,,,       
     **,,,,  //////(//.(( *, (#(/(( * .  * /***//(((/(#####/(*/*/ **   ,,,.     
    ****,  //*##//#((.(   ########(( ./ //*//.((((#(((/##/#/*/.,/* *,    ,,,    
  *,,,,   //*.######%#%##(##%##%#%%#(##/ *//((/(((/((((#%(*./**//.   # , , ,*   
 ,,,,.   #/(/(/.%(/#%%###(##%#(##%#%&%#%&//,////,(((#((###/..  %%%%(##.... ,,*  
***,      #/(//, %##%%%%%%%%&%.,%,##%%%//((  ,/((//(*(#  #%#%&%(,&#,*%&#,,. .,  
*,,*       #( ####%#%#%%%%#%&&#%&&%/%(%(/%../*///* .%&%%%%(%.&,& ,.&%# ,... ,   
.,,,,  .... (      . .#%%%&%&&&%&#%#%#(#%((#* %##&%%&&&@&&%%&&&&&%%*,....,.     
 ,,,* ..  .  #,(((/(*  ..##%&&%%&%##&%##&#(&&#%&&&&&&&&&&&&&%%%&%%&#/,,#*       
   ,,* .    /. #((//(/    ,((###%%##%%.#/ #&&&%@&&%%%&&%&&&&%%&&&#%%%%(( * ,
    , *******  ., .#//,      /(##(###%% ,%%%&&%###%##&&%&%%%&#%%%%%&%##,,   
**   *** ..**. **. #((/ %&           ##..#%#&#%##%%&@&&&#%%%&#%&%&%#%#( .  ,
     .***.. .. .    #  &&&@ &@&&(.  /(.*,.%&%%%#&&&%&&&%.%%#%###&%%%%( ,  
         ***, . ..&%%(# &@@&&&% /(/####(&  &&%%%%%%&&% .(%&&%&## ******* 
*        , /***..#####,(//  .#/.#/###.,.  * (.&&%&    #&%@&&%%% ***   ***       
      ***  ..**  (((##.   /#%%#%%#(, .  #  ,(#(/.%%##%##.   *(/ ***       
            **/.  (///     ( (%#%##%#(, ,#, #,(#%####./.   ###. . ***        
               ....  ,#   (*, #(,(*##(##,##(#(( (( ,,.  (.( ..... /**   
                 .... (/ #. . %%&(.#. /(,/#, .%# %%#   # //...  
            //  ...... (/#  ((#%#%%%%%##%%&%%#%%#* #(//. ...  **
              ./   .. .    ,/  #*#,##%# .#%#* # *./(*.    .   
               /  ,,  .      (*  , #%  ,/  %#.## /(         . 
            .        .,,       ((//*.*..,*.*( /((    
                          , ,     /*/((/((//**/.    ..          
                              , .  *///////*  .                     

                               The ScryptKeeper
                          Hackers Teaching Hackers 2021
                                 @syn-ack-zack

Powered by CircuitPython The ScryptKeeper is fully customizable by you. 
The USB-C port provides two serial streams, one of which is a Python REPL, 
allowing for interactive scripting live on the The ScryptKeeper. As a HID device, 
full keyboard and mouse emulation is possible and programmable by you.

To conserve the limited RAM, the code has been precompiled into .mpy files within the /lib directory. 
The original Python source code will be uploaded to GitHub for reference. 

Learn More: https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython

To demonstrate these capabilities the unlocked ScryptKeeper contains the following functionality
via the capacitive touch buttons. 

Bling Mode
----------
Description: Flashy lights purdy
Activate: Frontal Lobe Touch Pad
Next Bling: Nose Touch Pad
Exit Bling Mode: Mouth Touch Pad

Mouse Jiggler
-------------
Description: Uses mouse emulation to jiggle mouse 5px every 3 seconds
Activate: Nose Touch Pad while USB is plugged in
Exit Jiggler: Nose Touch Pad

Ducky Payload
-------------
Description: Just like a USB Rubber Ducky perform HID attacks with the DUCKY SCRIPT language
Edit 'duckyscript.txt' to alter the launched payload
Launch Payload: Mouth Touch Pad while USB is plugged in 

"""

scryptkeeper.main()