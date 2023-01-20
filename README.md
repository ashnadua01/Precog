PreCog Recruitment Task: Analysis and Classification of ~ 20GB Judicial Data by Development Data Lab.

DIRECTORY STRUCTURE:
|                |--- CaseLoadGraphs
|                |--- DispositionGraphs
|---- Analysis --|--- GIFS-representingTrend
|                |--- GenderBias
|                |--- PendingCaseGraphs
|                |--- src (main analysis code)
|
|                     
|              
|                      |--- images
|---- Classification --|--- src (main classification code)
|                    
|                  
|--- Reference -- India Shape
|
|--- README.md
|
|--- Report.pdf
|
|--- gifmake.py

LIBRARIES REQUIRED: pandas, matplotlib, plotly, seaborn, numpy, geopandas, os, sklearn


HOW TO RUN:

ANALYSIS:
1. DispositionGraph.ipynb is a Jupyter Notebok. In order to run it, run all cells.
2. GenderBias.ipynb is a Jupyter Notebok. In order to run it, run all cells.
3. PendingCasesPlot-Colab.ipynb is a Colab Notebook. In order to run it, upload data on Google Colab or mount Google Drive, then run all cells.
4. caseLoad.ipynb is a Jupyter Notebok. In order to run it, run all cells.

CLASSIFICATION:
1. dataCreation.ipynb is a Jupyter Notebook. In order to run it, run all cells. It saves the data of only one year at a time, therefore run it for 2010 to 2018.
2.classification.ipynb is a Jupyter Notebook. In order to run it, run all cells. 

METHOD / APPROACH:

ANALYSIS:
Method for each analysis has been discussed in the Report.pdf.

CLASSIFICATION:
Necessary preprocessing was done to create a pandas dataframe containing the data of only the required features, i.e Acts, Section, Type, Purpose, Disposition and Bailable. After this, the data was split into test and train, and sklearn library was used to train the decision tree classifier (best output).
