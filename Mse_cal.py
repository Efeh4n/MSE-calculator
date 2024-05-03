#                       MSE(Mean Square Error)
y_true = []
y_predict = []
def mse_calculator(y_true, y_predict):
    errors = []
    for i in range(len(y_true)):
        errors.append(y_true[i]-y_predict[i])
    errors_square = []
    for i in errors:
        errors_square.append(i**2)
    mse = sum(errors_square)/len(errors_square)

    return mse    
print("Mse =",mse_calculator(y_true,y_predict))
