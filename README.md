# cda_project

Nathan final project thoughts... 
Here's what I've found so far - looking at healthcare data at the county level in the US. There are 3143 counties (according to google). Found the following so far.
- state death rates - so, if can't go by county, can go by states because counties can be combined into state-level data.
- county level medicare spending, enrollments, etc. for 2014
- county population demographic data by race
- county demographic data - race, education, income, number of cars per household, and on and on
- county food access data with income data
Wondering if we could do some classification and clustering to see what variables are most associated with clustering and classification? Could also try to predict/forecast healthcare spending or predict maybe disease rates? If we have, or can get, locations of hospitals for counties, perhaps use some modeling to predict _where_ hospitals should be located? What hospitals to shut down and which ones to keep? See if there are differences in healthcare and access to food based on different demographics? Use ML to help determine which communities might be underserved? We haven't done it in class, but maybe some mapping/spatial analytics to find the "best" locations for healthcare facilities? Cluster counties based on some predictors to see commonalities between counties and what counties are perhaps over-served and which ones are underserved? Explore the relationships between different social demographics and access to healthcare, healthcare costs, and maybe develop a model that assigns weights to the different predictors.

data sources
- data.world had several useful sources that i have put together in a "project" on their site - it covers a lot of the county-level data described above
- usda has good data on grocery stores that is also connected to other data https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data.aspx
- https://data.census.gov/table/ACSSPP1Y2022.S0201?q=United%20States&t=Health:Health%20Insurance&g=010XX00US,$0500000 - not sure if this link will work but i've downloaded the data
