Title: Visual GUI for training elementary handwritten digit & alphabet classifier
Date: 2018-04-21 17:00
Slug: visual-ml-trainer
Summary: Main focus was to put together a system design to interface a visual GUI with a backend classifier

Elementary handwritten digit and alphabet classifier using supervised learning as part of the class COMP 549 - Human Computer Interaction. The main objective was to put into practice design principles taught in the class and system design.

![block\_diagram]({attach}../images/diy/handwritten.gif)

## The GUI walkthorough
The app is structured into 4 panes. The left side has 3 panes and right side 3 panes.

 - The upper-left pane is the object you want to test/analyze.
 - mid-left pane control events on what is given to test on upper-left pane.
 - low-left pane simple bar graph that gives the accuracy and maps to the label being identified.
 - upper-right pane graphs performance comparison between different versions of the model.
 - mid-right pane graphs a set of parameters used to tune and improve the overall accuracy of ANN. Also displays individual performance against each setting.
 - bottom-right pane has control knobs(sliders) to experiment with different ranges of parameter settings and to see how they affect performance/accuracy of current model being tested.

## what it does

 * Lets you experiment and save different versions of ANN you find the settings and accuracy to be appealing.
 * Collect different versions of ANN.

checkout the source at [visual GUI for classifier](https://github.com/rihbyne/watch-ml-behave)
