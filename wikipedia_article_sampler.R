# TODO: would be nice to show the graph leading to the sampled article
library(magrittr)
library(data.table)

WEIGHT <- 10  # lower number increases probability of sampling closer articles

# Downloaded CSVs from Quarry (online db w/ the latest wikipedia dump)
d1 <- read.csv("~/Documents/open_data/Wikipedia-QuarryQuery/Educational_technology_distance1.csv") %>%
  data.table
d2 <- read.csv("~/Documents/open_data/Wikipedia-QuarryQuery/Educational_technology_distance2.csv") %>%
  data.table
d3 <- read.csv("~/Documents/open_data/Wikipedia-QuarryQuery/Educational_technology_distance3.csv") %>%
  data.table

articles <- rbind(d1, d2, d3)
# Duplicates should be removed, leaving only the first instance
articles <- articles[, list(link_distance = min(link_distance)),
                     by = c("page_id", "page_namespace", "page_title")]
# Sample article, weight the probability by the link distance
out <- sample(x = articles[, page_title],
       size = 5,
       prob = 1 / WEIGHT ^ articles[, link_distance])
articles[page_title %in% out]
