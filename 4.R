generated_line <- rnorm(10000, 0, 1)
x1 <- seq(1, 10000, by = 1)
x2 <- seq(1, 10000, by = 1)
my_consistency_in_mean <- vector(length = 10000)
my_consistency_in_med <- vector(length = 10000)
count_mean <- 0
count_med <- 0
for (i in 1:10000)
{
  my_consistency_in_mean[i] <- mean(generated_line[1:i])
}
for (j in 1:10000)
{
  my_consistency_in_med[j] <- median(generated_line[1:j])
}
for (k in 1:10000)
{
  if (Mod(my_consistency_in_mean[k]) <= 0.1)
    count_mean <- count_mean+1
  print(c(k, "  ", count_mean))
}
for (k in 1:10000)
{
  if (Mod(my_consistency_in_med[k]) <= 0.1)
    count_med <- count_med+1
  print(c(k, "  ", count_med))
}
generated_line_c <- rcauchy(10000, 0, 1)
x3 <- seq(1, 10000, by = 1)
x4 <- seq(1, 10000, by = 1)
my_consistency_in_mean_c <- vector(length = 10000)
my_consistency_in_med_c <- vector(length = 10000)
count_mean_c <- 0
count_med_c <- 0
for (i in 1:10000)
{
  my_consistency_in_mean_c[i] <- mean(generated_line_c[1:i])
}
for (j in 1:10000)
{
  my_consistency_in_med_c[j] <- median(generated_line_c[1:j])
}
par(mfrow = c(1,4))
plot(x1, my_consistency_in_mean[x1], xlim = c(1,10000), type = "l")
plot(x2, my_consistency_in_med[x2], xlim = c(1, 10000), type = "l")
plot(x3, my_consistency_in_mean_c[x3], xlim = c(1,10000), type = "l")
plot(x4, my_consistency_in_med_c[x4], xlim = c(1, 10000), type = "l")
for (k in 1:10000)
{
  if (Mod(my_consistency_in_mean_c[k]) <= 0.1)
    count_mean_c <- count_mean_c+1
  print(c(k, "  ", count_mean_c))
}
for (k in 1:10000)
{
  if (Mod(my_consistency_in_med_c[k]) <= 0.1)
    count_med_c <- count_med_c+1
  print(c(k, "  ", count_med_c))
}