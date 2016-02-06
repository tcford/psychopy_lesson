![Paradigm structure](./gui_shots/psychopyDocBanner2.gif)

Welcome to Psychopy 101
-

Psychopy is a free software package written in the Python programming language for creating and running cognitive/psychophysics experiments.  This introductory class is aimed at beginners and does not require any programming experience.

Setting up
-
*To be completed*

Looping through conditions
-

Now that we have our movie structure:

![Paradigm structure](./gui_shots/Flow.png)

We can add the movie's scene components.

Click on *Stimulus* in the **Flow** to open the scene, then click <img src="./gui_shots/image.png" alt="Drawing" style="width: 30px;"/> in the **Components** panel.  
A box pops up with several options for the image. Notice the default duration of an image is 1 second.

In the *Image* dialoge box, we need tell *Psychopy* where to look for this component of the scene.  
In your *Psychopy* folder, there is a subdirectory called *'images'*. This subdirectory holds images that can be used in for this scene. Lets use the cat_eyes.jpeg file. In the *Image* dialoge box, enter the path to the file like so:  
![image path](./gui_shots/image_path1.png)
Click OK

We can test to see if this works by running the movie. Click the Run icon <img src="./gui_shots/run.png" alt="Drawing" style="width: 20px;"/> on the top right of the *Psychopy* window. Enter '001' as the participant number.

In your *Psychopy* directory, you will now see a *'data'* subdirectory with the data saved in the form of 001_filename_date.csv. We will discuss the contents of the .csv later.

The movie works, but usually there are many scenes in a movie, and in psychological experiments the scene is often repeated.

In the **Flow**, click the *Insert Loop* button.
Click the first dot immediately following *Stimulus* and the second dot immediately before it. A dialog box apears with several options. Name it 'trials', the stimulus will loop 5 times by default.  
Run <img src="./gui_shots/run.png" alt="Drawing" style="width: 20px;"/> the experiment again.

You will have noticed that there was only one presentation of the kitten scene, any idea why? The kitten scene was actually presented for 1 second, 5 times, but there was no gap between the scenes. 

An interstimulus interval (ISI) is required to separate each scene. In the **Components** panel, click *Custom* then the <img src="./gui_shots/ISI_button.png" alt="Drawing" style="width: 30px;"/>. The default ISI is 0.5 seconds. Click OK, there is now a pink shaded area for 0.5 seconds.  
Put the ISI before the image by changing the start time of the <img src="./gui_shots/image.png" alt="Drawing" style="width: 30px;"/> to 0.5 and the duration to 1.0. 
![image path](./gui_shots/ISI.png)
Run <img src="./gui_shots/run.png" alt="Drawing" style="width: 20px;"/> the movie again.

So we have 5 scene presentations, but what about recording a response? Let's add a button press for reaction time and accuracy.  
Click on the <img src="./gui_shots/keyboard.png" alt="Drawing" style="width: 30px;"/> in the **Components** panel. There are several options again, type 'space' into the *Allowed keys* box to indicate a response by spacebar press. Click OK and the key response appears in the workspace.

Click again on the <img src="./gui_shots/image.png" alt="Drawing" style="width: 30px;"/> in the scene, and change the duration of the image to 0. Now the picture will be presented until the spacebar is pressed.

![image path](./gui_shots/stim_complete.png)

We now have instructions and a scene that flashes for 1 second 5 times, and we can record a response. Click <img src="./gui_shots/run.png" alt="Drawing" style="width: 20px;"/>

Lets check out the data.
 
This is good, but we can also loop through different scenes. 

Let's use a new example. Imagine that *Psychopy* is in the pizza delivery business.  
*Psychopy* needs to collect the pizza order and deliver it to the customer, then receive the money. *Psychopy* looks at the list of pizzas to be delivered, and delivers each in turn until there are no more. Similarly, *Psychopy* can collect an image from a list, deliver it to the participant, and then receives a response, continuing until the list is done.

This list can be saved to an excel spreadsheet. In your *images* subdirectory, there is a file called datafile.xlsx. This contains a ready-made list.

![properties icon](./gui_shots/spreadsheet.png)

Like the path we entered to the kitten image earlier, the column *images* has a list of paths to images.  
There are additional columns in the spreadsheet, in the pizza example, these can be thought of as the drink and a dessert that accompany the pizza. The drink and dessert in each row are specific to the pizza in that row.

Lets set it up. In this example we will use images of gorillas, kittens and hedgehogs. The instructions are:

*You will see pictures*

*Press left for gorillas*  
*Press right for kittens*  
*Press up for hedgehogs*

*Press spacebar to continue*

Click on *Instructions* in the **Flow**, and select <img src="./gui_shots/text.png" alt="Drawing" style="width: 30px;"/>. Type the above into the *Text* box.

To tell *Psychopy* where to look for the datafile, click on *trials* in the **Flow** and select *Browse...*. Select the datafile.xlsx and hit OK. The path to the file is now in the dialog box, and below there will be a summary of what is included. In this spreadsheet there are 10 rows (conditions) with 3 columns (parameters) as shown below.

![properties icon](./gui_shots/loop_prop.png)

Now, to tell *Psychopy* to deliver the images from this list, click on *Stimulus* in the **Flow**, and the <img src="./gui_shots/image.png" alt="Drawing" style="width: 30px;"/>. In the *Image* box, type '\$images'. The \$ tells *Psychopy* to look for the column called *images* in the excel spreadsheet. Change the associated dropdown box to *set every repeat*. The image Properties should look like this:  
![properties icon](./gui_shots/image_prop.png)
Click OK.

We now need to record the amount of money received following pizza delivery, or the button press recieved following the image delivery. Click the <img src="./gui_shots/keyboard.png" alt="Drawing" style="width: 30px;"/> and type ' 'left', 'right', 'up' ' into *Allowed keys*. In the *Store* dropdown, select *first key*. Finally, click the box to *Store correct* and enter '\$correct_ ans' in the *Correct answer* box. As with the image properties, this tells *PsychoPy* to look in the correct_ans column in the excel spreadsheet. Your Properties should resemble the image below.

![properties icon](./gui_shots/cor_ans.png)

Your scene should now look like this:

![image path](./gui_shots/stim_complete.png)

Let's do it! Click <img src="./gui_shots/run.png" alt="Drawing" style="width: 20px;"/>


**[Using the Python Pandas library to explore the data](./psychopy_stats.html)**

