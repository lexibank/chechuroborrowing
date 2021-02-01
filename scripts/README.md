This is the online supplement to "Small-scale multilingualism through the prism of lexical borrowing".

### Files: Data and Scripts

This part of the project consists of the following files:

- *tests_and_visualizations_IJB.Rmd* — the R code for visualizations and statistical tests.
- *tests_and_visualizations_IJB.html* — an HTML page rendered on the basis of the .Rmd file.
- *words_IJB_submission.tsv* — the wordlists.
- *meta_anon.tsv* — metadata for the wordlists.
- *Villages.tsv* - the list of Villages of data collection.
- *Multilingualism.tsv* - multilingualism data.
- *bibliography.bib* - bibliography for the Rnotebook, contains the references for R packages.

The file **tests_and_visualizations.Rmd** creates the HTML version of the R-Notebook. The files **words_IJB_submission.tsv** and **meta_anon.tsv** have to be in the same directory as the **.Rmd** file. The program requires the following software and packages:

The HTML file contains versions of the plots that are slightly different from the ones presented in the paper due to the limitations of the R software. In the published verions of the plots, more convenient legends have been manually created using the **Inkscape** software, the content of the plots remained the same. Also note that the lines responsible for exporting the plots have been commented out from the **.Rmd** file. The plots used in the paper are provided here in the **Figures** folder as separate **.svg** files with the following names:

- *Fig2.svg*
- *Fig3.svg*
- *Fig4.svg*

### Software:

- R (version 3.6.3) and R Studio

*Note that the code will not run in R 4.0 due to the changed behaviour of some important functions as well as compatibility issues.*

R packages:

 - gdtools 0.2.2     
 - ggpattern 0.1.3   
 - rcompanion 2.3.26
 - rstatix 0.6.0     
 - arm 1.11-2       
 - MASS 7.3-51.5    
 - sjPlot 2.8.6      
 - ggpubr 0.4.0      
 - ggrepel 0.8.2     
 - forcats 0.5.0    
 - stringr 1.4.0     
 - dplyr 1.0.2       
 - purrr 0.3.4       
 - readr 1.4.0       
 - tidyr 1.1.2      
 - tibble 3.0.4     
 - ggplot2 3.3.2     
 - tidyverse 1.3.0   
 - lme 1.0-4        
 - lme4 1.1-26      
 - Matrix 1.2-18

The R Software and R Studio can be downloaded here: https://rstudio.com/products/rstudio/download/

Please use the **install.packages("<package_name>"** function to install the packages before running the code. To create the HTML output, use the **Knit** button.
