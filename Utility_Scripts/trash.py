import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def bar_char_fingerK():
    objects = ('1', '2', '3', '4', '5', '6')
    y_pos = np.arange(len(objects))
    performance = [2.92,3.13,2.44,2.19,2.48,2.53]
    
    plt.rcParams.update({'font.size': 18})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy (meters)')
    plt.xlabel('Number of anchor Node')
    plt.tight_layout()
    plt.savefig("bar_chart_fingerK")
    plt.show()


def bar_char_comb():
    objects = ('1', '2', '3', '4', '5', '6', '7', '8')
    y_pos = np.arange(len(objects))
    performance = [2.603600738157596,2.95306838894505,2.384735463183565,3.4129687059785043,3.520879826207382,2.194711653835054,2.715602328695764,3.403287750137954]
    
    plt.rcParams.update({'font.size': 18})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy (meters)')
    plt.xlabel('Combination of anchor nodes')
    plt.tight_layout()
    plt.savefig("bar_chart_comb")
    plt.show()


def bar_char_poly():
    objects = ('3', '6', '2', '4', '7', '8')
    y_pos = np.arange(len(objects))
    performance = [2.3028055928982054,
    		       2.480382781135348,
                   1.3823725864160774,
                   1.7487151085054828,
                   1.792063522316156,
                   1.5560908124570116]
    
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('MSE')
    plt.xlabel('Anchor Node')
    plt.title('Mean Squared Error (meters)')
    plt.savefig("bar_chart_lognormal")
    plt.show()

def bar_char_log():
    objects = ('3', '6', '2', '4', '7', '8')
    y_pos = np.arange(len(objects))
    performance = [2.3028055928982054,
    		       2.480382781135348,
                   1.3823725864160774,
                   1.7487151085054828,
                   1.792063522316156,
                   1.5560908124570116]
    
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('MSE')
    plt.xlabel('Anchor Node')
    plt.title('Mean Squared Error (meters)')
    plt.savefig("bar_chart_polynomial")
    plt.show()


def autolabel(plt,rects):
    for rect in rects:
        h = rect.get_height()
        print(h)
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*h, '%0.2f'%h,
                ha='center', va='bottom')

def group_bar_chart_log():
        
    # set width of bar
    barWidth = 0.25
     
    # set height of bar
    bars1 = [3.28402604888889, 3.262832114, 3.33322453111111]
    accuracyStd = [1.74472852821789,1.73808722510631,1.73100417117658]
    bars2 = [ 0.17741, 7.571565555556 , 6.506018888889]
    timeStd = [9.30921681169038E-06, 0.004427410692723, 0.003959537870905]
    bars3 = [1.5, 1.5, 1.5]
    energyStd = [0.5, 0.5, 0.5]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Accuracy (meter)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Response Time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Energy (Joules)', yerr = energyStd)
     
    # Add xticks on the middle of the group bars
    plt.title('Results by metric')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Multilateration\nwith LLS', 'Multilateration\nwith NLS', 'Weighted\n Multilateration'])
     
    # Create legend & Show graphic
    autolabel(plt, rects1)
    autolabel(plt, rects2)
    autolabel(plt, rects3)
    plt.legend()
    plt.savefig("barCode_log")
    plt.show()

def group_bar_chart_poly():
        
    # set width of bar
    barWidth = 0.25
     
    # set height of bar
    bars1 = [2.91, 2.65, 3.78]
    accuracyStd = [1.64,2.16,2.57]
    bars2 = [ 2.16, 4.67 , 5.67]
    timeStd = [0.00509565943355, 0.02, 0.002]
    bars3 = [1.5, 1.5, 1.5]
    energyStd = [0.5, 0.5, 0.5]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Accuracy (meter)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Response Time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Energy (Joules)', yerr = energyStd)
     
    # Add xticks on the middle of the group bars
    plt.title('Results by metric')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Multilateration\nwith LLS', 'Multilateration\nwith NLS', 'Weighted\n Multilateration'])
     
    # Create legend & Show graphic
    autolabel(plt, rects1)
    autolabel(plt, rects2)
    autolabel(plt, rects3)
    plt.legend()
    plt.savefig("barCode_poly")
    plt.show()


def group_bar_chart_fing():
        
    # set width of bar
    barWidth = 0.25
     
    # set height of bar
    bars1 = [2.19, 2.74, 2.44]
    accuracyStd = [1.36,1.65,1.45]
    bars2 = [ 0.47, 9.36 , 0.65]
    timeStd = [0, 0, 0]
    bars3 = [1.5, 1.5, 1.5]
    energyStd = [0.5, 0.5, 0.5]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Accuracy (meter)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Response Time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Energy (Joules)', yerr = energyStd)
     
    # Add xticks on the middle of the group bars
    plt.title('Results by metric')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Fingerpriting\nwith KNN', 'Fingerpriting\nwith NN', 'Weighted\n Fingerpriting'])
     
    # Create legend & Show graphic
    autolabel(plt, rects1)
    autolabel(plt, rects2)
    autolabel(plt, rects3)
    plt.legend()
    plt.savefig("barCode_finger")
    plt.show()

def points_x_y_poly():
    
    # set width of bar
    barWidth = 0.25
    
    multPoly    = [3.45704806, 0.54697668, 3.44189218, 3.12709579, 5.7583891, 4.61373848, 4.09217047, 1.44386766, 3.29444614, 0.26902035, 1.2446576, 2.63650396, 1.13703992, 1.12628727, 5.47752303, 2.97256593, 1.62108528, 1.58710744]
    hyperPoly   = [5.3469478,1.2076835,3.2543549,5.49155069,6.58455764,6.1227509,6.38648434,1.72067371,2.19154019,0.23554218,1.11359291,1.4963839,1.01039786,0.26527713,3.00750348,3.54583935,1.82051234,1.57964032]
    w_multPoly  = [6.18783147,10.94338423,3.72362278,3.21650848,5.09190426,5.63592536,6.61481283,1.71423233,2.42209443,2.7896039,1.59932465,4.44864114,1.25643014,0.38741479,5.62157596,2.39220527,2.09871313,1.89634214] 
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    # Set position of bar on X axis    
    x = np.arange(len(labels))
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 3))
    
    # Make the plot
    rects1 = plt.bar(r1, multPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial NLS')
    rects2 = plt.bar(r2, hyperPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial LLS')
    rects3 = plt.bar(r3, w_multPoly, width=barWidth, align='center', edgecolor='white', label='Polynomial Weighted Mult.')
    
    plt.ylabel('Error')
    plt.xlabel('Test Points')
    plt.title('Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_poly_all")

def points_x_y_log():
    
    # set width of bar
    barWidth = 0.25
    
    multPoly    = [3.45704806, 0.54697668, 3.44189218, 3.12709579, 5.7583891, 4.61373848, 4.09217047, 1.44386766, 3.29444614, 0.26902035, 1.2446576, 2.63650396, 1.13703992, 1.12628727, 5.47752303, 2.97256593, 1.62108528, 1.58710744]
    hyperPoly   = [5.3469478,1.2076835,3.2543549,5.49155069,6.58455764,6.1227509,6.38648434,1.72067371,2.19154019,0.23554218,1.11359291,1.4963839,1.01039786,0.26527713,3.00750348,3.54583935,1.82051234,1.57964032]
    w_multPoly  = [6.18783147,10.94338423,3.72362278,3.21650848,5.09190426,5.63592536,6.61481283,1.71423233,2.42209443,2.7896039,1.59932465,4.44864114,1.25643014,0.38741479,5.62157596,2.39220527,2.09871313,1.89634214] 
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    # Set position of bar on X axis    
    x = np.arange(len(labels))
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 3))
    
    # Make the plot
    rects1 = plt.bar(r1, multPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial NLS')
    rects2 = plt.bar(r2, hyperPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial LLS')
    rects3 = plt.bar(r3, w_multPoly, width=barWidth, align='center', edgecolor='white', label='Polynomial Weighted Mult.')
    
    plt.ylabel('Error')
    plt.xlabel('Test Points')
    plt.title('Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_poly_all")

def points_x_y_Fing():
    
    # set width of bar
    barWidth = 0.25
    
    kkn     = [1.70293863659264,0.641404708432983,1.27769323391806,5.4665711373767,2.65363901086791,1.67863039410112,12162673437153,0.707742891168819,4.2573465914816,0.880227243386615,1.82915280936285,2.81440935188895,1.12378823627942,1.77341478509682,4.35142505393348,2.2959311836377,3.0356712601993,0.893196506934504]
    w_knn   = [5.3469478,1.2076835,3.2543549,5.49155069,6.58455764,6.1227509,6.38648434,1.72067371,2.19154019,0.23554218,1.11359291,1.4963839,1.01039786,0.26527713,3.00750348,3.54583935,1.82051234,1.57964032]
    nn      = [6.18783147,10.94338423,3.72362278,3.21650848,5.09190426,5.63592536,6.61481283,1.71423233,2.42209443,2.7896039,1.59932465,4.44864114,1.25643014,0.38741479,5.62157596,2.39220527,2.09871313,1.89634214] 
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    # Set position of bar on X axis    
    x = np.arange(len(labels))
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 3))
    
    # Make the plot
    rects1 = plt.bar(r1, multPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial NLS')
    rects2 = plt.bar(r2, hyperPoly, width=barWidth, align='center',  edgecolor='white', label='Polynomial LLS')
    rects3 = plt.bar(r3, w_multPoly, width=barWidth, align='center', edgecolor='white', label='Polynomial Weighted Mult.')
    
    plt.ylabel('Error')
    plt.xlabel('Test Points')
    plt.title('Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_poly_all")

def main():
    
    #bar_char_poly()
    #bar_char_log()
    #group_bar_chart_poly()
    #group_bar_chart_log()
    bar_char_fingerK()
    bar_char_comb()
if __name__== "__main__":
    main()