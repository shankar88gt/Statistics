# Corelation Analysis
# Covers Corelation Basics
"""
    Correlation  Analysis is a statistical method used to measure the relation between 2 variables
    e.g. is there a relationship between salary & age

    We usually want t know 2 things
        1) How strong the corelation is
        2) Direction

    corelation coeff =  -1 to +1

    Strength of correlation
    r           Strength
    0.0 < 0.1   No correlation 
    0.1 < 0.3   low 
    0.3 < 0.5   medium
    0.5 < 0.7   high    
    0.7 < 1     very high

    A positive correlation exists when high values of one variable go along with high values of another variable
        e.g. body size & shoe size
    A positive correlation exists when high values of one variable go along with low values of another variable

    Most Popular 
        Pearson Correlation - r
        Spearman correlation - rs
        Kendall's tau
        Point biserial correlation coeff - rpb

    Pearson Corelation - Statistical measure that quantifies the relationship between 2 variables
        the linear relationship of metric variables are measured
    
        Calculated?
            r = sum((xi - xmean)(yi - ymean)) / sqrt( sum(xi - xmean)**2 * sum(yi - ymean)**2 )
            ** the expression in the denominator ensures that the corelation coeff is scaled between -1 & +1

        The Correlation coeff is usually calculated from the data taken from sample
        However, we often want to test a hypothesis about a population; we want to know if there is a corelation in the population.

        H0: the correlation coefficient does not significantly diff from 0; there is no linear relationship
        H1: the correlation coefficient does significantly diff from 0; there is a linear relationship

        e.g is there a corelation between age & salary in the british population
        to find a sample is drawn and a test of hypothesis is done ; Use a T test

        Assumptions:
            metric variables
            non linear relationship - does not work
            metric Normally distributed 

        Spearman Rank Correlation
            Non Parametric counterpart of pearson correlation
            Does not use the raw data but ranks

            e..g age & reaction time
            Steps
                1) assign rank to each metric variable ( distributes data more evenly) - handle rank ties
                2) diff in ranks - d & di**2
                3) rs = 1 - 6 * sum( di**2 / n * (n2 - 1 )) - no rank ties
        
        Kendall's tau
            Measure of the relationship between 2 variables

            whats the diff between pearson & Kendalls rank correlation?
                Kendall's Tau - Non parametric test & hence the two variables only have ordinal scale levels
                very similar to Spearmans rank coefficient but Kendall's Tau is preferred over spearnman's if very few data with many rank ties are available
            
            Calculation
                t = C - D / C + D
                C - concordant pairs
                D - discordant pairs

                e.g. Two doctors are asked to rank 6 patients according to physical health
                one of the two doctors is defined as a reference  patients are sorted based on the ranks. the corresponding ranks of the second doctors are listed respectively
                    e.g. the patient who is 3rd place with reference doctor get a rank of 4th by the second doctor
                
                now using Kendall's tau; we want to know if there is a correlation between the 2 ratings
                we look at the each individual rank of the second doctors and note whether the values below are smaller or greater than itself

                doctor1     doctor2
                    1           3       
                    2           1       -   
                    3           4       +   +   
                    4           2       -   +   -
                    5           6       +   +   +   +   
                    6           5       +   +   +   +   -

                C = all +'s  = 11
                D = All -'s = 4

                T = 0.47  

                also varies between -1 & +1

                H0: the corelation coeff Tau = 0 - there is no relationship
                H1: the corelation coeff Tau != 0 - there is a relationship

                For calculation by hand ; use the z distribution as an approx - for this we shd have atleast 40 cases.

        Point biserial correlation
            special case of Pearson and examines the relationship between a dichotomous variable & a metric variable
            dichotomous variable -  variable with 2 values; e.g Gender, Smoke status 

            Calculated?
                e.g we are interested in the relationship between num of hours studied for the test & the test result?
                
                assign the test result values with numbers ( passsed - 1 and failed - 0)
                rpb = ( x2mean - x1mean / Sx ) * sqrt( n1 * n2 / n**2 ) -  you can either use this equation or calculate pearson
                x1 - passed, n1 - passed

                rpb varies between -1 & +1 
                0 - no correlation
                0 - -1 - negative coreelation

                H0: the corelation coeff = 0 - there is no relationship
                H1: the corelation coeff != 0 - there is a relationship

                when we compute a point biserial correlation, we get the same P value as when we compute a t test for independent samples for the same data

                Assumptions
                    to calculate the corelation coefficient, one metric & one dichotomous variable must be present
                    for hypothesis; the one metric variable shd be normally distributed



Correlation & Causality:
    Causality is the relationship between cause & an effect; i.e we have a cause and the resultant effect
    e.g drinking coffee -> caffenine ( stimulating substance) -> alertness ( effect )
    Clear requirements must be met in order to speak of causal relationship

    Correlation tells us whether there is a relationship between 2 variables
        e.g icecream sales, # of sunburn 
        correlation cannot tell us which variable influence which or whether a third variable is resonsible for the correlation
        in the above example both variables are influenced by the third variable ( summer )

    Causality means that there is a clear cause-effect relationship 
    causality exists when you can say with certainity which variable influences which

    What are the conditions for causality
        1) significant correlation between the variables 
        2) 2.a - chronological sequence
           2.b - a controlled experiment in which the variables can be influenced specifically
           2.c - well founded & plausible theory in which direction the causal relationship goes

        




























"""
