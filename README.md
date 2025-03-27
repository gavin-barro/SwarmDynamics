# Swarm Dynamics

# Authors
Gavin Barro and Austin Earl

# About
For our ISAT 441 project, we developed a simulation to explore the impact of invasive hives on local ecosystems, analyzing 
their effects on native species and environmental balance.

# Problem Statement
This project involved simulating a dynamic hive, flower, and bee ecosystem to explore how nectar availability influences 
the production and survival of both bees and flowers, while ensuring a sustainable balance between resource consumption 
and regeneration. To deepen our analysis, we developed two versions of this ecosystem: one featuring only native flower 
species and another incorporating an invasive flower species. By comparing the two models, we aimed to uncover the effects
of invasive species on resource competition among flowers, the sustainability of bee hives, and the overall health and 
resilience of the ecosystem. This approach allowed us to examine how changes in species composition can disrupt ecological
equilibrium and impact long-term sustainability.

# Problem Significance
The ease and frequency of global transportation have significantly increased the movement of species across geographic boundaries,
often leading to the unintended introduction of invasive species into new ecosystems. Additionally, human development of previously
untouched areas disrupts the balance of existing ecosystems, creating opportunities for non-native species to establish themselves. 
Invasive species such as Japanese Switchgrass, Burmese pythons, and Spotted Lanternflies exemplify this growing ecological challenge. 
These species outcompete native flora and fauna for resources, disrupt food webs, and compromise biodiversity, ultimately threatening 
the sustainability of the ecosystems they invade[1]. Understanding and mitigating the impacts of invasive species are critical to 
preserving ecological health and ensuring the resilience of both natural and human-altered environments.

# Conceptual Model
Our conceptual model draws inspiration from the Beecology Project[2], which addresses the alarming decline in wild pollinators, 
focusing on their abundance, diversity, and geographic distribution. This decline poses a critical threat to ecosystem health and 
biodiversity, with insufficient ecological data hampering effective conservation efforts. The Beecology Project engages citizen 
scientists to collect and submit data on native pollinators through innovative smartphone and web apps, complemented by online 
visualization tools designed for diverse users, including researchers, educators, and conservation groups. By analyzing bumblebee-plant
interactions and later expanding to nesting and overwintering behaviors, the project seeks to enhance pollinator habitats and identify 
the causes of their decline. Using this as a foundation, our model adapts key aspects of their approach, emphasizing ecosystem dynamics 
and species interactions, while tailoring the focus to study the impacts of invasive species on resource competition and ecological 
sustainability. This alignment allowed us to leverage proven methodologies while addressing a unique aspect of ecosystem health.

They chose to simulate a pollination ecosystem involving different types of bees, flowers, and an invasive flower species. Their model
included four different breeds: seeds, flowers, hives, and bees, each with specific properties to represent their behavior like nectar 
collection, pollination, and reproduction. Bees forage for nectar and pollen and flowers bloom and reproduce via seeds, and hives serve
as storage for collected nectar. The environment is also modeled with areas that contain seeds that directly influence where flowers grow.
Their simulation also includes adjustable parameters such as bee preferences, nectar regeneration rates, and flower lifespans to study how
these factors share the ecosystem.

Three scenarios are predefined in their model to explore different ecological outcomes. In the baseline scenario, invasive flowers fail to
dominate the ecosystem. In the second scenario, invasive flowers outcompete the native species due to high bee preferences and overlapping
bloom times. In the third scenario, bees of one species favor invasive flowers, leading to competitive displacement of the other bee species.
This model allows users to study pollination dynamics, the impact of invasive species, and how species-specific preferences influence 
biodiversity and ecosystem stability.

![Figure 1: An example of their simulation](images/figure1.png)

*Figure 1: An example of their simulation*

![Figure 2. Various bee species and flower they chose to model](images/figure2.png)

*Figure 2. Various bee species and flower they chose to model*

# Computational Model
Our computational model simulates an ecosystem comprising bees, hives, and multiple flower species, including both native and invasive varieties.
The model focuses on key interactions such as nectar collection, hive resource dynamics, and the life cycles of flowers and bees. Bees forage for 
nectar, contributing to hive resources, while flowers regenerate and reproduce, creating a dynamic interplay between species. These interactions 
form the foundation for exploring ecological relationships and the impact of invasive species within a simplified yet robust framework.

To streamline the simulation, we introduced several simplifying assumptions. Nectar regeneration occurs at a fixed rate, and external factors such
as weather, seasons, and climate changes are excluded from the model. Hive dynamics are influenced solely by nectar collection, omitting other 
potential factors like pollen. These simplifications allowed us to concentrate on the core processes shaping the ecosystem while ensuring the model 
remains computationally efficient and focused on the primary ecological dynamics.[3]

The primary differences between the two simulations lie in their complexity and focus. The first simulation emphasizes generalized interactions 
between agents, such as movement patterns and satisfaction based on neighborhood characteristics. This model explores social dynamics and emergent 
patterns by simulating the movement of agents with varying preferences. In contrast, the second simulation incorporates a more specific ecological 
system involving bees, hives, and flowers. It emphasizes biological and ecological processes like nectar collection, resource dynamics, and species 
interactions, providing a focused exploration of ecological relationships and the potential impact of invasive species.

The changes between the two simulations were made to tailor the model to different research goals. The first model makes it well-suited for studying 
broad social behaviors or spatial segregation patterns. The second model aims to capture biological realism, allowing for more nuanced exploration of 
ecological systems. These changes were driven by a need to align the model's scope with specific research questions, such as understanding invasive 
species' ecological impacts or the interplay between resource dynamics and species survival. The transition from a general agent-based framework to a 
detailed ecological model reflects a shift in focus from abstract interactions to domain-specific processes.

The code defines a simulation ecosystem consisting of flowers, bees, and hives. The Flower class models various types of flowers, tracking their age, 
species, nectar levels, and seed production, with methods to update nectar, produce seeds, and age the flower. The Hive class represents a hive, managing 
bees, nectar storage, and the seasonal cycle, with methods for storing nectar. The Bee class models individual bees, keeping track of their age, species, 
nectar collection, and movement between flowers and hives. Bees visit flowers to collect nectar, which is then stored in the hive. They can also age and 
eventually die. The WeightedEcosystem class ties everything together, running a simulation where bees visit flowers, collect nectar, and store it in hives 
while tracking the population of different flower species and the amount of nectar in the hives over multiple iterations. The ecosystem includes multiple 
flower species, such as invasive flowers and various colored flowers, and simulates the interactions between bees, flowers, and hives to observe changes 
over time. The simulation runs for a set number of iterations, collecting data to plot the results of the ecosystem's dynamics.

We will discuss the results of our simulations below.

# Results
Our results section is broken up into two categories, based on our two simulations: Random Flower Selection, where there is no invasive species and 
Weighted Flower Selection, where there is an invasive species.

# Random Flower Selection
The simulation has four types of flowers and one species of bees. There are 3 native flowers and one invasive flower. The native flowers have around the same nectar regeneration, lifespan, and reproduction rate. The invasive flowers have a higher nectar regeneration, lifespan, and the same reproduction. The way reproduction is decided is by the number of times they are visited by a bee. In the random selection, the reproduction for the invasive and native are the same to keep their counts the same. Each flower has an equal chance of being chosen, if the flower is already occupied another flower is chosen at random from the array of existing flowers. When a bee visits an unoccupied flower, it collects nectar and moves to another flower until it reaches its max carry weight. Once that happens, the bee will go back to its hive and deposit the nectar then go back to visiting flowers. Once the hive reaches a certain amount of nectar, it will produce a beer. The number of native flowers starts at 25 for each species and the number of invasive flowers starts at 10.

![Results 1](images/results1.png)

Although the number of invasive flowers starts at a lower amount, they all end up at around the same amount. 

# Weighted Flower Selection
The weighted selection is very similar to the random, the only differences are the selection and conditions from reproduction. The number of visits for the native flowers increases and the number of visits for the invasive flowers decreases. The chance for a bee to visit an invasive flower is also increased. This is done since the invasive flowers provide more nectar. 

![Results 2](images/results2.png)

The amount of invasive flowers significantly increases when the reproduction rate and selection is weighted in their favor. This causes the amount of  native flowers to decrease significantly, even leading some to die out.

# Sensitivity Analysis
Reproduction rate per turns
Ph = 6
Pl = 2
Number Of Flowers
Ch = 175
Cl = 50
Standard Sensitivity Equation: [100 * (Ch - CL) / Ch] / [100 * (Ph - Pl) / Ph]
= (100 (175 - 50) / 175) / (100 * (6 - 2) / 6) = 1.0714

![Sensitivity 1](images/sensitivity1.png)

![Sensitivity 2](images/sensitivity2.png)

These graphs came from the random selection simulation. We did the sensitivity analysis on reproduction, to see what caused the most change. The top graph we increased the reproduction for the invasive very slightly, and the next one we increased it more. This shows how as the reproduction rate increases, the amount of invasive flowers increases and stays at a steady  number.

# Model Validation
To validate our model, we conducted thorough parameter tuning, focusing particularly on the nectar decrease rate to achieve a balanced ecosystem where hive sustainability, bee population growth, and flower regeneration were all maintained. We simulated two versions of the ecosystem, one with only native flowers and one including an invasive species, to ensure our findings aligned with our initial hypotheses. Additionally, we validated hive nectar consumption by comparing it against nectar regeneration rates, ensuring realistic resource depletion dynamics. Monitoring the bee population over time allowed us to detect anomalies, such as premature extinction or unchecked exponential growth, which could indicate issues in the model. Finally, we employed debugging techniques and manual inspection of interactions to confirm that the system behaved as expected under various conditions. This rigorous validation process ensured the accuracy and reliability of our simulations.

# Model Evaluation
Our evaluation revealed distinct outcomes depending on the presence of invasive flowers. When invasive flowers were included, their higher nectar regeneration rates caused a rapid increase in hive storage, allowing them to overtake native flowers and leading to unsustainable bee population growth. This competitive exclusion of native flowers disrupted the balance of the ecosystem, resulting in long-term instability. In contrast, simulations without invasive flowers showed nectar levels stabilizing, enabling a sustainable equilibrium between hives and native flowers. The bee population exhibited steady growth and decline patterns in alignment with nectar availability, reflecting a balanced ecosystem dynamic. Emergent results from these simulations underscored the destabilizing potential of invasive species, as they monopolized resources and outcompeted native flora. Parameter tuning also highlighted the importance of nectar decrease rates, where excessively high rates caused premature hive and bee population collapse, and low rates resulted in unchecked growth, further emphasizing the need for careful calibration.

# Conclusion and Future Works
Our model successfully captured key dynamics of resource competition and population sustainability, demonstrating realistic interactions between ecosystem components under controlled conditions. However, certain limitations affect the model's realism. The lack of environmental factors, such as weather, seasons, and predation, simplified the ecosystem and may not fully represent actual ecological processes. Additionally, fixed lifespans and nectar regeneration rates for flowers might not accurately reflect the variability found in natural ecosystems. These insights highlight both the strengths of the model and opportunities for future refinement to enhance its ecological fidelity.

# Sources and Relevant Links
https://www.usgs.gov/faqs/how-have-invasive-pythons-impacted-florida-ecosystems  
https://beecology.wpi.edu/website/home 


# Acknowledgements


