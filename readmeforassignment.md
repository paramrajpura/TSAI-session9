# Session 9 assignment of EPAi4.0

##Sequence Types
The topic covers following sections:

                    Sequence Types
                    Mutable Sequences
                    Lists vs Tuples
                    Copying Sequences
                    Slicing
                    Custom Sequences
                    Sorting Sequences
                    List Comprehensions


#### Problem definition

This assignment's problem statement is formulated as follows:


1. A regular strictly convex polygon is a polygon that has the following characteristics:

    all interior angles are less than 180
    all sides have equal length
   
2. For a regular strictly convex polygon with:

    n edges (=n vertices)
    R circumradius
    interior angle
    edge length
    apothem
    area
    perimeter

3.  Objective 1 [pts:400]:

    Create a Polygon Class:
        where initializer takes in:
            number of edges/vertices
            circumradius
        that can provide these properties:
            # edges
            # vertices
            interior angle
            edge length
            apothem
            area
            perimeter
        that has these functionalities:
            a proper __repr__ function
            implements equality (==) based on # vertices and circumradius (__eq__)
            implements > based on number of vertices only (__gt__)

   
4.  Objective 2 [pts:600]:

    Implement a Custom Polygon sequence type:
        where initializer takes in:
            number of vertices for largest polygon in the sequence
            common circumradius for all polygons
        that can provide these properties:
            max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
        that has these functionalities:
            functions as a sequence type (__getitem__)
            supports the len() function (__len__)
            has a proper representation (__repr__)

5.  Results:

    Implement these 2 classes as a separate module. Access these modules in Google Colab or Deep Note or local Notebook
    (late you'd need to upload to GitHub)
    Run Objective 1 module to show that the functionalities are implemented properly
    Run Objective 2 module and show which polygon is efficient for n = 25
    You are submitting a link to your GitHub repo, where we can find the 2 modules and your notebook in which you have 
    called and tested them on GitHub Actions.
    All your code must be publicly accessible (make sure to open all links in an incognito window before submitting)

