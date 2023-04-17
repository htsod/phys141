# multi_lens.py
# Max Liang
# created 04/14/23
# Description:
#


s1 = 20
s2 = 30
s3 = 20
s_list = [s1, s2, s3]

f1 = -10
f2 = 15
f3 = -20
f_list = [f1, f2, f3]


def s_modify(s, s_prime):
    return s - s_prime


def s_prime(si, s, f, n, m_tot):
    s_p = 1/(1/f[n] - 1/si)
    m = - s_p / si
    print(f"The magnification for {n+1}th lense is {m}"
          f"\nRelative distance from the lens = {s_p}\n\n")
    n += 1
    m_tot = m * m_tot
    if n == 3:
        print(f"The total magnification is {m_tot}")
    else:
        s_p = s_modify(s[n], s_p)
        return s_prime(s_p, s_list, f_list, n, m_tot)

s_prime(s1, s_list, f_list, n=0, m_tot=1)



