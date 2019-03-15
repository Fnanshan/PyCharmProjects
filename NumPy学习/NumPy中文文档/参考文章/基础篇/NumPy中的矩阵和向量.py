import numpy as np

# A = np.array([[1, -1, 2], [3, 2, 0]])
# print(A)
# v = np.array([[2], [1], [3]])
# print(v)
# v = np.transpose(np.array([[2, 1, 3]]))
# print(v)
# print(A[1, 2])
# col = A[:, 1:2]
# print(col)
# w = np.dot(A, v)
# print(w)

print('# 用numpy求解方程组')
# A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
# b = np.transpose(np.array([[-3, 5, -2]]))
# x = np.linalg.solve(A, b)
# print(A)
# print(b)
# print(x)
# # Check that the solution is correct:
# print(np.allclose(np.dot(A, x), b))

print('# 应用：多元线性回归')

# import csv
# import numpy as np
#
#
# def readData():
#     X = []
#     y = []
#     with open('Housing.csv') as f:
#         rdr = csv.reader(f)
#         # Skip the header row
#         next(rdr)
#         # Read X and y
#         for line in rdr:
#             print('line :', line)
#             xline = [1.0]
#             # xline = []
#             for s in line[:-1]:
#                 print('s :', s)
#                 if s == "yes":
#                     s = 1
#                     xline.append(float(s))
#                 elif s == "no":
#                     s = 0
#                     xline.append(float(s))
#                 else:
#                     xline.append(float(s))
#             print('xline :', xline)
#             X.append(xline)
#             print('line[-1] :', line[-1])
#             if line[-1] == "yes":
#                 line[-1] = 1
#                 y.append(float(line[-1]))
#             else:
#                 line[-1] = 0
#                 y.append(float(line[-1]))
#     return X, y
#
#
# X0, y0 = readData()
# print('X0 :', X0)
# print('y0 :', y0)
# # # Convert all but the last 10 rows of the raw data to numpy arrays
# d = len(X0) - 10
# print('d :', d)
# X = np.array(X0[:d])
# y = np.transpose(np.array(y0[:d]))
# print(X)
# print(y)
#
# # # Compute beta
# Xt = np.transpose(X)
# XtX = np.dot(Xt, X)
# Xty = np.dot(Xt, y)
# beta = np.linalg.solve(XtX, Xty)
# print('beta :', beta)
#
# print('X0[536:] :', X0[d:])
# # # Make predictions for the last 10 rows in the data set
# for data, actual in zip(X0[d:], y0[d:2]):
#     x = np.array([data])
#     prediction = np.dot(x, beta)
#     print('prediction :', float(prediction[0]) * 100000, 'actual :', actual)
#     # print('prediction = ', str(prediction[0, 0]), 'actual = ', str(actual))
