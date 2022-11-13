# Phonon-labs
Updated 25.08
### Prerequisite
* Jupyter notebook installed with packages *scipy*, *numpy* and *matplotlib*
### Before you start
* Before you start you will have to istall *ipywidgets* package. So follow the steps at this homepage:[https://ipywidgets.readthedocs.io/en/latest/user_install.html](https://ipywidgets.readthedocs.io/en/latest/user_install.html).
* If you want to save the animation as a mp4 file, then you have to install the package *ffnmpg*. Otherwise, the "save animation" button will do nothing. To install ffmpeg do for example in Windows in he comand line run:
<p align="center">
  conda install -c conda-forge ffmpeg
</p>
or
<p align="center">
  pip install ffmpeg
</p>
or install ImageMagick tool, which you can find here:\\
[https://imagemagick.org/script/download.php](https://imagemagick.org/script/download.php). \\
In the last case, image magic might turn out to be useful in doing other image manipulations

### Usage
Download both *RunnerPhonon.ipynb* and *cphonon.ipynb* and open *RunnerPhonon.ipynb* in your notebook.
Left click on the first cell containing *%run cphonon.ipynb* on the first line. Then press "ctrl + enter" two times on your keyboard. It will run the program in the *cphonon.ipynb* and start the interactive lab.
The output just below the cell should look like this:

![alt text](https://github.com/AndrissP/Phonon-labs/blob/master/Example.png "Logo Title Text 1")

The output contains two figures, many widgets that control the figures. Widgets are there to be touched and moved. The two figures should automatically update whenever you change some position of a widget. The lowest button *"Create animation"* will create an animation with the chosen parameters. The *"Save animation to mp4"* will create an animation with the chosen parameters and instead of displaying it, it will save to the current folder with a name "PhononOscil_Mode_a_SpringC_b_N_c.mp4", where in (a,b,c) places are the corresponding values from the chosen ones. The animation creation does not happen instantly but takes from a few up to 30 seconds. Please be patient. The creation time depends highly on the frequency. If the frequency is low (for example < 1 our unit) the animation will be creating more frames, thus taking longer time. You can usually increase the frequency and not changing the physics much by increasing the spring constant. 

When the animation appears it should appear with a slider and several interactive buttons. Enjoy them. The "-"/"+" buttons at the sides increase/decrease the speed of the animation, the next ones jump to the beginning/end of the animation, and the next ones: jump one frame further/back. Other buttons, I think, are intuitive.

I might happen that the output is put in a small window where you have to scroll down to see something and which is very uncomfortable. To solve this, on the command line press Cell/Current Outputs/ Toggle Scrolling and re-execute the *%run cphonon.ipynb* cell. Now the output should be distributed all the way bellow the input cell.


#### Issues:
* Sometimes the interface crushes - the figures stop being interactive and the animation does not get created animore. In this case "Kernel/Restart Kernel" only wont work. You need to press "Kernel/Restart Kernel" and then refresh the page so that everything would work well again.


### If you want to see what is inside
If you want to see what the program really does, open also *cphonon.ipynb*. You can run cell by cell by clicking *"ctrl + enter"*. You can also uncomment cell containing the variables (for example containig only #A) and run these cells to see the outputs of each cell. Shortcut for (un-) commenting is *"ctrl + /"*. You can also add your own code add print your own variables. 
