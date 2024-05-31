### Squirrels in N.Y. parks

Have you ever wondered how many squirrels are in New York City parks? No? Here are the stats anyway.
"NYC OPEN DATA WEEK MULTI-PARK SQUIRREL COUNT

The Squirrel Census is a multimedia science, design, and storytelling project focusing on the Eastern gray (Sciurus carolinensis). They count squirrels and present their findings to the public. 

On March 1, 2020 — with the help of 72 volunteer Squirrel Sighters, as well as NYC Open Data — they performed a sample count in 24 New York City parks, and gathered other material data. Four hundred and thirty-three squirrel sightings were tallied. The methodology was less focused on total squirrel numbers per hectare and more attuned to the stories — of squirrels, humans, and parks". www.thesquirrelcensus.com/data

#### Data Analysis: Squirrel Population in NYC Parks

**Stats Overview**:
1. **Population Count**: The number of squirrels observed in New York City parks.
2. **Observation Duration**: The average time observers spend sighting squirrels.
3. **Color Distribution**: The color variations among the squirrels in the parks.

Check the dataset for more info.
-----------
#### Main Question:

"Is there a significant difference in the eating habits between squirrels that approach people and those that do not?"

**Activity Analyzed**:
Sighters in the park recorded the activities of squirrels, including whether they were eating. The data shows the following proportions:
- **Squirrels that approach humans and eat**: 0.2059 (20.59%)
- **Squirrels that do not approach humans and eat**: 0.0717 (7.17%)

#### Statistical Analysis:
To determine if there is a statistically significant difference in the eating habits between the two groups of squirrels, I conducted the two-proportion z-test (Python). This test helps to understand if the observed difference in eating behavior is due to chance or if it reflects a true difference in the population of squirrels in N.Y. parks.

#### Results:
The analysis indicates that squirrels that approach humans are significantly more likely to eat compared to those that do not approach humans. The proportion of eating squirrels is significantly higher among those that approach people.

**Steps in Statistical Analysis**:
1. **Hypotheses**:
   - Null Hypothesis (H0): There is no difference in the proportion of squirrels eating between those that approach humans and those that do not.
   - Alternative Hypothesis (H1): There is a difference in the proportion of squirrels eating between those that approach humans and those that do not.
2. **Test Used**: Two-proportion z-test.
3. **Significance Level**: Commonly set at 0.05.

4. **Results**:
Z-Score: The z-score measures the number of standard deviations the observed difference is from the null hypothesis (no difference).
P-Value: The probability that the observed difference occurred by chance. A p-value less than 0.05 typically indicates statistical significance. If the p-value is less than 0.05, we reject the null hypothesis, indicating a statistically significant difference in the eating habits of the two groups of squirrels. If the p-value is greater than 0.05, we fail to reject the null hypothesis, indicating no significant difference.

Based on the analysis, the p-value was found to be less than 0.05, leading to the rejection of the null hypothesis. This means that the difference in eating habits between the two groups is statistically significant and not due to random chance.

----

### Conclusion
The data analysis shows that:
- Squirrels that approach humans are significantly more likely to eat compared to those that do not approach humans.


