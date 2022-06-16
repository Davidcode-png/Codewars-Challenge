# return masked string
def maskify(cc):
#     if len(cc) < 4:
#         return cc
#     x = ['#' for c in cc[:-4]]
#     x =''.join(x)
#     x += cc[-4:]
#     return x
     return "#"*(len(cc)-4) + cc[-4:]
