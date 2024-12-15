eng_size = [
2.0,
2.4,
1.5,
3.5,
3.5,
3.5,
3.5,
3.7,
3.7
]

co2_em = [
196,
221,
136,
255,
244,
230,
232,
255,
267
]

eng_size_sum = 0

for size in eng_size:
	eng_size_sum += size

eng_size_mean = eng_size_sum / len(eng_size)

co2_em_sum = 0

for em in co2_em:
	co2_em_sum += em

co2_em_mean = co2_em_sum / len(co2_em)

print("engine size mean: {}, co2 emission mean: {}".format(eng_size_mean, co2_em_mean))

xy_sum = 0

for i in range(len(eng_size)):
	xy_sum += (eng_size[i] - eng_size_mean) * (co2_em[i] - co2_em_mean)

x_sqr_sum = 0

for i in range(len(eng_size)):
	diff = (eng_size[i] - eng_size_mean)
	x_sqr_sum += diff * diff

print("x y sum: {}, x squared sum: {}".format(xy_sum, x_sqr_sum))

theta_1 = xy_sum / x_sqr_sum
theta_0 = co2_em_mean - theta_1 * eng_size_mean

print("theta 1: {}, theta 0: {}".format(theta_1, theta_0))

x_pred = 2.4
y_pred = theta_0 + theta_1 * x_pred
print("x predict: {}, y predict: {}".format(x_pred, y_pred))