from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

B = linspace(.5, 4, 8) * .058
d = 3.085e-3

# Red light
D2_red = 0.336616963
D1_red = 0.237934008
Da_red = array([.238619894, .238206401, .240987808, .241783842, .242187500, .240422130, .242627278, .244072035])
Db_red = array([.233089283, .230675861, .231483057, .230427712, .230469659, .228324503, .225944102, .225905627])

# Green light
D2_green = 0.328358382
D1_green = 0.251014650
Da_green = array([.254842818, .253809363, .254972368, .255058229, .258539647, .257277817, .259721309, .262887329])
Db_green = array([.243869275, .244883806, .242938399, .241775140, .239805982, .240557075, .240097672, .238395870])

# Turquoise light
D2_tur = 0.334546387
D1_tur = 0.253769875
Da_tur = array([.255723953, .252971739, .253993034, .251933247, .254093826, .256392539, .256693542, .259651303])
Db_tur = array([.248297140, .246291056, .243135393, .244265348, .242720440, .242428064, .239779174, .237607285])

# Blue light
D2_blue = 0.311050773
D1_blue = 0.235733546
Da_blue = array([.239785805, .239263222, .240372479, .241835296, .243560284, .241949081, .246485502, .247333884])
Db_blue = array([.230842069, .231317401, .231240273, .229689389, .226355612, .226512775, .225306109, .222671136])


def delta_sigma(da, db, d1, d2):
    return (1 / (2 * d)) * ((da ** 2 - db ** 2) / (d2 ** 2 - d1 ** 2))


def theoretical_sigma(B, energy_diff):
    return (9.27e-24 * B * energy_diff) / (6.626e-34 * 299792458)


blue = [delta_sigma(Da_blue[i], Db_blue[i], D1_blue, D2_blue) for i in range(Da_blue.size)]
red = [delta_sigma(Da_red[i], Db_red[i], D1_red, D2_red) for i in range(Da_red.size)]
green = [delta_sigma(Da_green[i], Db_green[i], D1_green, D2_green) for i in range(Da_green.size)]
turquoise = [delta_sigma(Da_tur[i], Db_tur[i], D1_tur, D2_tur) for i in range(Da_tur.size)]
# print(red)
# print(green)
# print(turquoise)
# print(blue)


theo_blue = [theoretical_sigma(i, 4) for i in B]
theo_red = [theoretical_sigma(i, 2) for i in B]
theo_green = [theoretical_sigma(i, 3) for i in B]
theo_tur = [theoretical_sigma(i, 3) for i in B]
# print(theo_blue)
# print(theo_red)


m_blue, y_blue, *b = linregress(B, blue)
m_blue_theo, y_blue_theo, *b_theo = linregress(B, theo_blue)
# plot(B, blue, 'bo')
# plot(B, m_blue * B + y_blue, 'b-', label='Blue light')

m_red, y_red, *r = linregress(B, red)
m_red_theo, y_red_theo, *r_theo = linregress(B, theo_red)
# plot(B, red, 'ro')
# plot(B, m_red * B + y_red, 'r-', label='Red light')

m_green, y_green, *g = linregress(B, green)
m_green_theo, y_green_theo, *g_theo = linregress(B, theo_green)
# plot(B, green, 'go')
# plot(B, m_green * B + y_green, 'g-', label='Green light')

m_tur, y_tur, *t = linregress(B, turquoise)
m_tur_theo, y_tur_theo, *t_theo = linregress(B, theo_tur)
# plot(B, turquoise, 'co')
# plot(B, m_tur * B + y_tur, 'c-', label='Turquoise light')
#
# xlabel('B [T]')
# ylabel('$\Delta\sigma$  $[m^{-1}]$')
# legend()
# savefig('./graphs/zeeman_1.pdf')

# subplot(221)
# title('Green light')
# xlabel('B [T]')
# ylabel('$\Delta\sigma$  $[m^{-1}]$')
# plot(B, m_green * B + y_green, 'b-', label="Experimental results")
# plot(B, green, 'b.')
# plot(B, m_green_theo * B + y_green_theo, 'r-', label="Theoretical results")
# plot(B, theo_green, 'r.')
# legend()
#
# subplot(222)
# title('Blue light')
# xlabel('B [T]')
# ylabel('$\Delta\sigma$  $[m^{-1}]$')
# plot(B, m_blue * B + y_blue, 'b-', label='Experimental results')
# plot(B, blue, 'b.')
# plot(B, m_blue_theo * B + y_blue_theo, 'r-', label='Theoretical results')
# plot(B, theo_blue, 'r.')
# legend()
#
# subplot(223)
# title('Red light')
# xlabel('B [T]')
# ylabel('$\Delta\sigma$  $[m^{-1}]$')
# plot(B, m_red * B + y_red, 'b-', label="Experimental results")
# plot(B, red, 'b.')
# plot(B, m_red_theo * B + y_red_theo, 'r-', label="Theoretical results")
# plot(B, theo_red, 'r.')
# legend()
#
# subplot(224)
# title('Turquoise light')
# xlabel('B [T]')
# ylabel('$\Delta\sigma$  $[m^{-1}]$')
# plot(B, m_tur * B + y_tur, 'b-', label='Experimental results')
# plot(B, turquoise, 'b.')
# plot(B, m_tur_theo * B + y_tur_theo, 'r-', label='Theoretical results')
# plot(B, theo_tur, 'r.')
# legend()
#
# tight_layout(1)
# savefig('./graphs/splittings.pdf')

# print(m_red, m_green, m_tur, m_blue)
# print(*t)
# print("red", m_red_theo, m_red, abs(m_red_theo - m_red) / m_red_theo)
# print("tur", m_tur_theo, m_tur, abs(m_tur_theo - m_tur) / m_tur_theo)
# print("green", m_green_theo, m_green, abs(m_green_theo - m_green) / m_green_theo)
# print("blue", m_blue_theo, m_blue, abs(m_blue_theo - m_blue) / m_blue_theo)
