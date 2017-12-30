# Installing Jupyter Notebook and R on your computer

1. First, download and install Anaconda on your computer. You can download it here: [https://www.continuum.io/downloads](https://www.continuum.io/downloads) WARNING: It will take up 845MB of your hard drive. Install the version for Python 3.5. **IF YOU HAVE ALREADY INSTALL ANACONDA FOR A PREVIOUS CLASS, YOU DO NOT NEED TO DO THIS AGAIN.**
2. Open your terminal (Mac) or Command Prompt (Windows) and type: `conda list`
3. If a big stream of text goes by, you've got Anaconda installed.
4. If you get an error or nothing happens, come find me. **STOP HERE IF YOU GET AN ERROR MESSAGE**.
5. Let's update Anaconda by typing in your terminal `conda update conda` and then type `y` when it asks if you want to update the packages.
6. Now let's create an environment for us to work in. Type `conda create --name dataviz python=3 jupyter` into your terminal and say yes to the installation. What this does is it creates a whole new python environment that won't interfere with any python environments you have set up before (Mac users: Apple installs Python 2.7 in your system and messing with it can have disastrous consequences for your machine. Thus, environments).
7. Activate your new environment by typing `source activate dataviz` on a Mac/Linux and `activate dataviz` on a Windows machine.
8. Now let's install R and a ton of packages. To do that, we'll use Anaconda's R Essentials. Type `conda install r-essentials` and wait for it to finish.
9. Let's check if Jupyter Notebook is installed correctly by typing `jupyter notebook` and watching to see if a browser pops up with stuff in it. It should use your default browser.
10. On the top right of the browser, you should see a dropdown menu called New. Click that, and go down to Notebooks and R. Click R.
11. In the new window, in the first cell, type the following: `words <- "Hello World!"`. Then hit enter and type `print(words)`
12. Underneath the Cell dropdown menu, you'll see a triangle pointing to the right into a line. Clicking that executes your command (which you want to do). Or, you can hold shift and hit enter to execute the command. When you do that, it should say "Hello World!" below the cell with your code in it.
13. Marvel at what you have done. You've created an entire virtual environment, installed software into it without harming your computer, opened up a browser based code editor and executed some R. Cool, eh?
14. Go to File > Close and Halt.
15. Go to your terminal and hit control C and say yes to shutting down he Jupyter server.
16. Your last step of the day: Type `source deactivate` on a Mac/Linux or `deactivate` on Windows. This exits out of your environment and returns you to your normal computer. We will do that every time we use this dataviz environment: We'll activate it when we start and deactivate it when we stop.
