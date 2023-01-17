library(tidyverse)
library(ggplot2)
library(purrr)
library(tibble)
library(scales)
library(latex2exp)

# STUDY 1 - (1+1) EA in HAMMING BALL setting on OneMax and LeadingOnes
# ===
tbl = readr::read_delim("data/study1_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"


g = ggplot(filter(tbl, n == 500), aes(x = as.factor(radius), y = evals))
#g = g + geom_boxplot(aes(color = f))
g = g + geom_boxplot()
g = g + theme_bw()
g = g + labs(x = "Hamming-ball radius", y = "Nr. of function evaluations")
g = g + scale_x_discrete(breaks = seq(10, 500, by = 20))
g = g + facet_wrap(. ~ f, nrow = 2L, scales = "free_y")
g
ggsave("images/hamming_ball_onemax_lo_n500.pdf", plot = g, width = 8, height = 6)



# STUDY 2 - (1+1) EA in HAMMING BALL setting on JUMP_k
# ===
tbl = readr::read_delim("data/study2_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"

g = ggplot(tbl, aes(x = as.factor(radius), y = evals))
#g = g + geom_boxplot(aes(color = f))
g = g + geom_boxplot()
g = g + theme_bw()
g = g + scale_y_log10()
g = g + labs(x = "Hamming-ball radius", y = "Function evaluations (log-scaled)")
#g = g + theme(legend.position = "top")
#g = g + scale_color_brewer(palette = "Dark2")
g = g + facet_wrap(.~k, scales = "free", labeller = label_both)
g
ggsave("images/hamming_ball_jump_n30.pdf", plot = g, width = 8, height = 3.5)



# STUDY 3 - (1,lambda) EA in HAMMING BALL setting on ONEMAX and LeadingOnes
# ===
tbl = readr::read_delim("data/study3_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"

tblaggr = tbl %>%
  dplyr::mutate(evals = evals / maxevals) %>%
  dplyr::group_by(f, n, lambda, radius) %>%
  dplyr::summarise(evals = mean(evals), .groups = 'keep') %>%
  ungroup()
tblaggr$r = tblaggr$radius

g = ggplot(filter(tblaggr, f == "ONEMAX", radius %in% c(0, 10, 20, 30)), aes(x = lambda, y = evals))
g = g + geom_line(aes(linetype = as.factor(n), color = as.factor(n)))
g = g + geom_point(aes(shape = as.factor(n), color = as.factor(n)))
g = g + facet_wrap(. ~ r, nrow = 1L, labeller = label_both)
ns = unique(tblaggr$n)
g = g + geom_vline(data = data.frame(n = ns, f = "ONEMAX", radius = c(10, 20, 30), threshold = ceiling(log(ns, base = exp(1)/(exp(1)-1)))), mapping = aes(xintercept = threshold, linetype = as.factor(n)), color = "blue", color = "gray")
g = g + theme_bw()
g = g + theme(legend.position = "top")
g = g + scale_shape_manual(values = c(1, 2, 13))
g = g + scale_x_log10()
g = g + labs(
  x = latex2exp::TeX("$\\lambda$ (log-scaled)"),
  y = "Function evaluations\n(in percent of 100n)",
  linetype = latex2exp::TeX("#Bits $n$"),
  shape = latex2exp::TeX("#Bits $n$"),
  color = latex2exp::TeX("#Bits $n$"))
g = g + scale_color_grey(start = 0.2, end = 0.5)
g
ggsave("images/hamming_ball_1commaLambda_onemax_r10_20_30_nAll.pdf", plot = g, width = 11, height = 3.5)


# STUDY 4 - (1+1) EA in FITNESS-LEVEL setting on OneMax and LeadingOnes
# ===
tbl = readr::read_delim("data/study4_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"

g = ggplot(tbl, aes(x = as.factor(level), y = evals))
#g = g + geom_boxplot(aes(color = f))
g = g + geom_boxplot()
g = g + theme_bw()
g = g + labs(x = "Fitness level", y = "Function evaluations")
#g = g + theme(legend.position = "top")
#g = g + scale_color_brewer(palette = "Dark2")
g = g + facet_wrap(f~n, scales = "free")
g


# STUDY 5 - (1+1) EA with RANDOM PLACEMENT of target points on OneMax
# ===
tbl = readr::read_delim("data/study5_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"


g = ggplot(filter(tbl, n == 250), aes(x = as.factor(ntargets), y = evals))
#g = g + geom_boxplot(aes(color = f))
g = g + geom_boxplot()
#n = c(100, 250, 500)
#g = g + geom_hline(data = data.frame(n = n, y = 2.5 * n * log(n)), aes(yintercept = y))
g = g + theme_bw()
g = g + labs(x = "Size of target set", y = "Nr. of function evaluations")
br = seq(0, 245, by = 10)
g = g + scale_x_discrete(breaks = br, labels = parse(text = latex2exp::TeX(sprintf("$2^{%i}$", br))))
#g = g + theme(legend.position = "top")
#g = g + scale_color_brewer(palette = "Dark2")
#g = g + facet_wrap(n ~ ., nrow = 1L, scales = "free")
g
ggsave("images/random_placement_onemax_n250.pdf", plot = g, width = 8, height = 3.5)


# STUDY 6 - (1+1) EA on PLATEAU with angelic placement
# ===
tbl = readr::read_delim("data/study6_results.csv", delim = " ")
# why the hell is there a trailing dot in the name?!
colnames(tbl)[colnames(tbl) == "function."] = "f"

tblaggr = tbl %>%
  group_by(f, n, ntargets) %>%
  dplyr::summarise(evals.mean = mean(evals), evals.sd = sd(evals)) %>%
  ungroup()
tblaggr$ntargets = factor(tblaggr$ntargets, levels = sort(unique(tblaggr$ntargets)))


tbl.ridge = filter(tblaggr, f == "RIDGE")
g = ggplot(tbl.ridge, aes(x = as.factor(n), y = evals.mean, group = ntargets, shape = ntargets, color = ntargets))
g = g + geom_line()
g = g + geom_point()
g = g + geom_errorbar(aes(ymin = evals.mean - evals.sd, ymax = evals.mean + evals.sd), width = 0.1)#, position = position_dodge(1))
g = g + theme_bw()
g = g + labs(x = expression(n), y = "Nr. of function evaluations", shape = "", color = "")
g = g + theme(legend.position = "top")
#lbs = unname(TeX(c("$S = \\{\\}", "$S = \\{s_1\\}")))
lbs = unname(c("0 additional targets", "1 additional target"))
g = g + scale_shape_discrete(labels = lbs)
g = g + scale_color_brewer(palette = "Dark2", labels = lbs)
br = seq(10, 100, by = 10)
g = g + scale_x_discrete(breaks = br, labels = br)
g
ggsave("images/angelic_placement_ridge.pdf", plot = g, width = 8, height = 3.5)


tbl.plateau = filter(tblaggr, f == "PLATEAU")
g = ggplot(tbl.plateau, aes(x = as.factor(n), y = evals.mean, group = ntargets, shape = ntargets, color = ntargets))
g = g + geom_line()
g = g + geom_point()
g = g + geom_errorbar(aes(ymin = evals.mean - evals.sd, ymax = evals.mean + evals.sd), width = 0.1)#, position = position_dodge(1))
g = g + theme_bw()
g = g + labs(x = expression(n), y = "Nr. of function evaluations", shape = "Additional targets", color = "Additional targets")
g = g + theme(legend.position = "top")
lbs = unname(TeX(c("$S = \\{\\}", "$S = \\{s_1\\}", "$S = \\{s_1, s_2\\}")))
colpalette = c("#1B9E77", "#D95F02", "#7570B3")
g = g + scale_shape_discrete(labels = lbs)
g = g + scale_color_manual(values = colpalette)
br = seq(10, 100, by = 10)
g = g + scale_x_discrete(breaks = br, labels = br)
g = g + guides(color = FALSE, shape = guide_legend(override.aes = list(color = colpalette)))
g
ggsave("images/angelic_placement_plateau.pdf", plot = g, width = 5, height = 4)



