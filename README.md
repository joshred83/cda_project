# cda_project

Nathan final project thoughts... 
Here's what I've found so far - looking at healthcare data at the county level in the US. There are 3143 counties (according to google). Found the following so far.
- state death rates - so, if can't go by county, can go by states because counties can be combined into state-level data.
- county level medicare spending, enrollments, etc. for 2014
- county population demographic data by race
- county demographic data - race, education, income, number of cars per household, and on and on
- county food access data with income data

Project Ideas:
- Wondering if we could do some classification and clustering to see what variables are most associated with clustering and classification?
**Josh** *I would also like to do some cluster analysis. I'm not sure about classification, because it requires a target.*

- Could also try to predict/forecast healthcare spending or predict maybe disease rates? If we have, or can get, locations of hospitals for counties, perhaps use some modeling to predict _where_ hospitals should be located?
**Josh** *I think this could be very difficult unless we have a narrow scope. Hospital funding, hospital staff, urban/rural, connected medical school, areas of specialization. Getting the locations of hospitals and placing them in geographic boundaries is doable. Figuring out what we're looking for and how to measure it would be more difficult.*

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

**Josh** *So, just be clear on this... I have done similar things. The general process would be: Identify geographic regions and pull them from the census.* 

*Download the TIGERS shape files and get them into a workable form (they use GEOIDs which are derived from census FIPS codes.) Connect the census data to the shapefiles using geopandas. Plot it to make sure it looks right. Get geocoded POI data (hospital locations, grocery stores ...whatever) from a different vendor. Use geopandas functions to merge the data. The geopandas API makes it pretty easy to determine wither a point (POI) is within a shape (census boundary)*

*You are working with multiple datasets at this point, so it's probably best to get the data organized with some reasonable variables early on. Unfortunately, you do need all three datasets. The tigerfiles act as a bridge between census regions and individual points.*

*The upside is that maps make good visuals, especially if you can show that your clustering has some interesting geographic patterns.*

*A note on doing this on a national scale, counties are not demographically homogenous. I think it's usually preferred to work at the tract/block levels because the borders are more thoughtfully designed.  There are about 84,000 tracts and between 200k and 250k block groups.*

*****Soneeka- I like both the ideas shared above. To add more to the pot of ideas-

Idea #1- Starting with the idea we were discussing when we met about Real Estate-
Property Prices in US in past years- Factors affecting, Predicted growth or drop in prices based on economic and social factors at play in a particular demographic area
Multiple Data source -for property prices- MBA, census for population, average income etc economic data from FRED(federal Reserve, US treasury and FHFA
Looking at historic real estate values for past few years form residential properties sold, rate of interest, Rate of inflation, Population growth, Annual Income Growth, new construction etc for past 3-4 years as training data and predicting the coming years projection for may be Single Family- Medium priced property in the selected area.
We can do Linear Regression
If we make it finding the factors affecting or influencing then we could do Regression Tree
We can apply Gradient Boosting to the model to do some variable selection and re do the models with selected variables

Idea #2- Stock price prediction- selecting a stock or S&P etc and study its movement and try to predict the future movement based on historic trend, economic data, seasonality and industry credentials.Methodology similar to  RE analysis. We can get data from Yahoo finance and economic data and look for industry specific data.

Josh - I've shared several ideas that I believe hold a lot of potential. My only request is that we aim to use datasets not commonly used for demonstrations or tutorials.  


Nathan
- so we've got the hospital thing and answering several questions about what we find in the data - connecting/merging that with other datasets. In regards to the note about counties not being demographically homogenous - I think that's ok - we can mention it as a concern but having 84,000 to 200k to 250k data points might be too much data?
- real estate - interesting ideas and a list of models to apply to answer questions is good i think
- stock price prediction - this would require some exponential smoothing models and possibly some time series - not sure how much i know about those topics yet. also a thought - at what extent of prediction? a day? week? month? longer (year(s))? shorter (hours, minutes, etc.)?
- also shared on teams today about the NCAA tournament thing on kaggle
- thoughts on which one to proceed? i agree that we don't use data commonly used in demos/tutorials.


Final Ideas - Data and Research Questions
- Grocery Store - data = ; research question =
- Data Scientist salary - data = ; research question =
- Real Estate - data = ; research question =
- BISG - data = ; research question = 
- NCAA - data = previous years winners and losers, rank of teams in tournaments - probabilities of different seeded teams beating others, season data - scoring, etc.; research question = can we leverage a combination of ML methods to predict the winner of the March Madness tournament?
