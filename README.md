# sprint-4

https://sprint-four-dc1y.onrender.com/


Used Car Data.
Introduction: In this project I will use a Used Cars database to provide an understanding of car price vs the different characteristics of a car. 
These characteristics include model year, odometer, cylinder, paint color and car type. 

Process: The database is firstly processed by filling in missing values in the model_year, cylinder, and odometer columns.
I did that by grouping by model year and filling in with their respective median. The model Mercedes sprinter van had no odometer 
therefore had no median to fill in with. I took care of those missing values independently. Moreover, the paint color had some
missing values and those were filled in with unknown. I lastly created a  Boolean column out of is 4_wd. 

Visuals:The first visual is a  distribution of Price depending on Brand, Cylinders, Paint color and Type. The x axis is price
with y axis being frequency or count. The color is choosen from the dropdown menu. The second visual is a scatterplot with
Mean price by brand and Model Year. The user can pick from different color representing brad while the x axis depicts year and y axis 
is frequency.

