# Regression
"""

Whats Covered
    Regression Analysis
        What is regression Analysis
        Simple & Multiple Linear Regression
            Interpret results
            Assumptions
            Dummy Variables
    Logistic Analysis


Regression Analysis makes it possible to infer or predict a variable on the basis of one or more other variables
    Independent Variables
    Dependent variables

    1) Measurement of the influence of one or more variables on another variable
    2) Prediction of a variable by one or more other variables

    Simple Linear   
    Multiple Linear regression      
    Logistic Regression

    In all the above cases the independent variable can be metric, nominal or ordinal 

        y = mx + C
            m - slope
            c - receptor point / intercept

        m = r * sy/sx
        C = ymean - b*xmean

    Regression error 
        y = mx+c + epsilon
            optimize to minimize residual & epsilon

    Multiple linear Regression
            y = b1x1 + b2x2 + .....   bk*xk + C
                    if an indeedent variable changes by one unit , the associated coefficient b indicates by how much the dependent variable changes

                    
    Regression Results
        R - Multiple corelation coefficient
                Measures the relationship/ correlation betwee depepdent & independent variables
        R2 - Coefficient of determination
                Indicates how much of the variance of the dependent variable can be explained by the independent variables
        Adjusted R2 
            R2 overestimates the coefficient of determination just when many independet variables are used
        Standard estimator Error
            indicates by ow much the model overestimates the dependent variable on average

    Statistical Validation
        F test to test the null hypothesis, whether the variance explanation R2 in the population is zero
            The test is equivalent to asserting that all true slope coefficient in the population are zero : H0

            y = b1x1 + b2x2 + b3x3
                e.g p value for x1 > 0. it means that the null hyp cannot be rejected. then the coefficient b1 ( all coeff's ) is zero. i.e variable x1 doesnt help
                    p value < 0.05 then that particular variable is significant
            
    Assumptions
        Linear relationship between dependent & indepedent variables
        Normally distributed error compenent
            Analytical
                Kolmogorov Smirnov
                Shapiro Wilk                    
            Graphical
                QQ plot
        No Multicollinearity or no instability of the regression coefficient
            Two or more of the predictors corelate strongly with each other
            The effect of individual variables can then not be clearly seperated
                This is ok for prediction because only Y matter and coefficients doesnt 
                This is not of for measurement of influence since the coefficients are not accurate  
            Diagnosis
                y = b1x1 + b2x2 + b3x3 + a - original equaltion

                x1 = b2x2 + b3x3 + ....+ A  - if we are able to predict X1 accuratly then we dont need X1 in the oiginal equation
                do this similarly for other independent variables   

                T = 1 - R2
                    Attention T< 0.1  ( multicolineiarity )
                VIF ( variance inflation Factor )
                    VIF = 1 / ( 1 - R2)
                    Attention T > 10 ( multicolineiarity )
              
        No heteroskedasticity, the variance of the residuals must be constant across the predicted values
                plot between Y & error - this shd be distributed evently ( homoscedacity )

    Dummy Variables
        Categorical variables with two characteristics can be used as independent variables
            e.g Gender  - Female as 0 and male as 1
        y = b1x1 ( gender ) + b2x2 + .......

        y = b1.0 + ............... ( female as reference )
        y = b1.1 + ................ ( male )
            e.g if b1 is 400 for y as income then male earns 400 more than female 

        lets say we have vehical type with 3 possible values ( sedan, sports & SUV )
                Create dummy variables ( issedan, issports, isSUV ) - similar to one hot encoding for linear regression
                N-1 dummy variable is created so 2 variables is sufficient ( issedan & issports is enough and the 3rd is redundant )
        
    Logistic Regression
            Depedent variable is a dichotomous Variable - 0 or 1
                y axis ( target ) is transformed from the probability to the log( odds of obesity ). so the y axis can go from -infinity to + infinity
                log( odds of obesity ) = log(p/1-p)
                
            Scatter plot of 1 & 0 -  a straight line doesnt work 
                The goal of logistic regression is to estimate the probability of occurance , not the value of the variable itself
                The logistic function is used - only 0 / 1 are possible
                    1 / 1 + e ^ -z
                    z = (b1x1 + b2x2 + b3x3 + ........ + a)

            Now we to solve for coefficient inorder to best represent the data
                Maximum likehood Function 
                 



        


        



    
        

        



        

    
        



"""