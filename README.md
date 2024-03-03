# cda_project
<font color='darkblue'> Josh's color</font> 

Nathan final project thoughts... 
Here's what I've found so far - looking at healthcare data at the county level in the US. There are 3143 counties (according to google). Found the following so far.
- state death rates - so, if can't go by county, can go by states because counties can be combined into state-level data.
- county level medicare spending, enrollments, etc. for 2014
- county population demographic data by race
- county demographic data - race, education, income, number of cars per household, and on and on
- county food access data with income data

Project Ideas:
- Wondering if we could do some classification and clustering to see what variables are most associated with clustering and classification?
<font color='darkblue'>I would also like to do some cluster analysis. I'm not sure about classification, because it requires a target. </font> 

- Could also try to predict/forecast healthcare spending or predict maybe disease rates? If we have, or can get, locations of hospitals for counties, perhaps use some modeling to predict _where_ hospitals should be located?
<font color='darkblue'>I think this could be *very* difficult unless we have a narrow scope. Hospital funding, hospital staff, urban/rural, connected medical school, areas of specialization. Getting the locations of hospitals and placing them in geographic boundaries is doable. Figuring out what we're looking for and how to measure it would be more difficult.   </font> 

- What hospitals to shut down and which ones to keep?
- See if there are differences in healthcare and access to food based on different demographics?
- Use ML to help determine which communities might be underserved?
- We haven't done it in class, but maybe some mapping/spatial analytics to find the "best" locations for healthcare facilities?
- Cluster counties based on some predictors to see commonalities between counties and what counties are perhaps over-served and which ones are underserved?
- Explore the relationships between different social demographics and access to healthcare, healthcare costs, and maybe develop a model that assigns weights to the different predictors.

data sources
- data.world had several useful sources that i have put together in a "project" on their site - it covers a lot of the county-level data described above
- usda has good data on grocery stores that is also connected to other data https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data.aspx
- https://data.census.gov/table/ACSSPP1Y2022.S0201?q=United%20States&t=Health:Health%20Insurance&g=010XX00US,$0500000 - not sure if this link will work but i've downloaded the data

<font color='darkblue'>So, just be clear on this... I have done similar things. The general process would be:
Identify geographic regions and pull them from the census. 

Download the TIGERS shape files and get them into a workable form (they use GEOIDs which are derived from census FIPS codes.)
Connect the census data to the shapefiles using geopandas. Plot it to make sure it looks right. 
Get geocoded POI data (hospital locations, grocery stores ...whatever) from a different vendor. 
Use geopandas functions to merge the data. The geopandas API makes it pretty easy to determine wither a point (POI) is
within a shape (census boundary) 

You are working with multiple datasets at this point, so it's probably best to get the data organized with some reasonable variables 
early on. Unfortunately, you do need all three datasets. The tigerfiles act as a bridge between census regions and individual points.

The upside is that maps can make good visualizations.  </font> 

