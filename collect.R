library(tidyverse)

import_data = function(output_dir) {
  cat(sprintf("Importing data from '%s' ...\n", output_dir))

  study_name = basename(output_dir)

  # read all files from directory
  fs = list.files(output_dir, pattern = ".csv$", full.names = TRUE)

  # these files do not have headers
  evals = lapply(fs, scan, sep = " ", n = 2L, quiet = TRUE)
  evals = evals[sapply(evals, length) == 2L]
  evals = do.call(rbind, evals)

  # give them headers
  evals = as.data.frame(evals)
  colnames(evals) = c("jobid", "evals")

  # now merge with experimental design
  setup = read.table(sprintf("data/%s.csv", study_name), header = TRUE, sep = " ")
  tbl = dplyr::left_join(setup, evals, by = "jobid", keep = FALSE)

  # eventually store
  write.table(tbl, file = sprintf("data/%s_results.csv", study_name), row.names = FALSE, quote = TRUE)
}

studies = list.dirs("data/raw", recursive = FALSE)
#studies = "data/raw/study6"
lapply(studies, import_data)
