import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def bar_char_anchor_exp2_2():
    anchors = ['1', '2', '3', '4']
    y_pos = np.arange(len(anchors))
    performance = [1.38, 1.57, 2.06, 1.90]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, anchors)
    plt.ylabel('Average localization error (m)')
    plt.xlabel('Multilateration')
    #plt.title('RMSE (m)')
    plt.savefig("bar_chart_lognormal_exp22")
    plt.show()

def bar_char_anchor_exp2():
    anchors = ['1', '2', '3', '4', '5', '6']
    y_pos = np.arange(len(anchors))
    performance = [1.6801697306266985,
    		       1.5583027605847282,
                   1.4214742615412228,
                   1.1755392390729282,
                   1.3880282610664476,
                   1.2113879672043495]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('RMSE (m)')
    plt.xlabel('Anchor Node')
    #plt.title('RMSE (m)')
    plt.savefig("bar_chart_lognormal_exp2")
    plt.show()

def bar_char_mult_exp2():
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
    y_pos = np.arange(len(labels))
    error = [1.28791592,1.09327139,1.14194521,1.7186473,0.0084993,0.65162382,2.19822207,0.72593991,0.87119246,0.83637628,0.6497893,2.49048065,2.17903371,1.37229802,1.15868098,2.5094098,2.65714715]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, error, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('Localization error (m)')
    plt.xlabel('Test point')
    #plt.title('Mean Squared Error (m)')
    plt.savefig("acc_mult_exp2")
    plt.show()

def bar_char_exp2():
    objects = ['1', '2', '3', '4', '5', '6']
    y_pos = np.arange(len(objects))
    performance = [1.71,1.36, 1.09, 0.97, 1.00, 1.05]
    
    bars = plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.rcParams.update({'font.size': 14})
    autolabel(plt, bars)
    plt.rcParams.update({'font.size': 14})
    plt.xticks(y_pos, objects)
    plt.ylabel('Average locaizatoin error (m)', fontsize=14)
    plt.xlabel('Fingerpriting', fontsize=14)
    #plt.title('RMSE (m)')
    plt.savefig("exp2_Finger")
    plt.show()

def bar_char_exp2_1():
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
    y_pos = np.arange(len(labels))
    error = [1.19,0.57,0.42,1.08,0.59,0.13,0.4,0.75,0.59,1.44,1.75,0.77,1,1.1,1.77,0.55,3.79]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, error, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('Localization error (m)')
    plt.xlabel('Test point')
    #plt.title('Mean Squared Error (m)')
    plt.savefig("acc_exp2_1")
    plt.show()

def bar_char_sig_var1():
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    y_pos = np.arange(len(labels))
    varr = [0.54,1.34,3.73,3.88,5.16,5.38,1.73,4.01,1.6,0.67,4.01,1.29,2.77,1.38,0.94,1.43,0.77,5.82]
    
    plt.rcParams.update({'font.size': 16})
    plt.bar(y_pos, varr, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('RSS variance (dbm)')
    plt.xlabel('Test point')
    #plt.title('Mean Squared Error (m)')
    plt.savefig("bar_signal_var_1")
    plt.show()

def bar_char_comparisionMult():
    objects = ('A', 'B', 'C', 'D')
    y_pos = np.arange(len(objects))
    performance = [2.65,4.05,4.10,3.39]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('Average localization error (m)')
    plt.xlabel('Multilaterations with NLS.')
    plt.tight_layout()
    plt.savefig("bar_chart_comparision")
    plt.show()


def bar_char_fingerK():
    objects = ('1', '2', '3', '4', '5', '6')
    y_pos = np.arange(len(objects))
    performance = [2.92,3.13,2.44,2.19,2.48,2.53]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('Average localization error (m)')
    plt.xlabel('Fingerpriting')
    plt.tight_layout()
    plt.savefig("bar_chart_fingerK")
    plt.show()


def bar_char_comb():
    objects = ('1', '2', '3', '4', '5', '6', '7', '8')
    y_pos = np.arange(len(objects))
    performance = [2.603600738157596,2.95306838894505,2.384735463183565,3.4129687059785043,3.520879826207382,2.194711653835054,2.715602328695764,3.403287750137954]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, objects)
    plt.ylabel('Average localization error (m)')
    plt.xlabel('Fingerpriting')
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
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('RMSE (m)')
    plt.xlabel('Anchor Node')
    #plt.title('RMSE (m)')
    plt.savefig("bar_chart_polynomial")
    plt.show()

def bar_char_log():
    objects = ('3', '6', '2', '4', '7', '8')
    y_pos = np.arange(len(objects))
    performance = [2.4372677497922317,
    		       2.575777316754345,
                   1.4715544835910181,
                   1.9484094037047144,
                   2.163883356205811,
                   1.582213195046457]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(y_pos, performance, align='center', alpha=0.5, color='k')
    plt.xticks(y_pos, [])
    plt.ylabel('RMSE (m)')
    plt.xlabel('Anchor Node')
    #plt.title('Mean Squared Error (m)')
    plt.savefig("bar_chart_lognormal")
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
    bars1 = [3.10, 3.262832114, 3.33322453111111]
    accuracyStd = [1.74472852821789,1.73808722510631,1.73100417117658]
    bars2 = [ 0.17741, 7.571565555556 , 6.506018888889]
    timeStd = [9.30921681169038E-03, 4.427410692723, 3.959537870905]
    bars3 = [0.04, 1.48, 1.9]
    energyStd = [0.0, 0.0, 0.0]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Avg. localization error (m)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Avg. response Time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Avg. energy (dJ)', yerr = energyStd)
    
    # Add xticks on the middle of the group bars
    #plt.title('Results by metric')
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
    bars2 = [ 0.09, 4.67 , 5.67]
    timeStd = [0.0, 2.1, 2.81]
    bars3 = [0.04, 1.95, 2.05]
    energyStd = [0,0,0]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Avg. localization error (m)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Avg. response time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Avg. energy (dJ)', yerr = energyStd)
     
    # Add xticks on the middle of the group bars
    #plt.title('Results by metric')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Multilateration\nwith LLS', 'Multilateration\nwith NLS', 'Weighted\n Multilateration'])
     
    # Create legend & Show graphic
    autolabel(plt, rects1)
    autolabel(plt, rects2)
    autolabel(plt, rects3)
    plt.ylim(0,8.8)
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
    timeStd = [0.01, 2.2, 0.03]
    bars3 = [0.09, 0.14, 0.08]
    energyStd = [0.0, 0.0, 0.0]
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    rects1 = plt.bar(r1, bars1, width=barWidth, edgecolor='white', label='Avg. localization error (m)', yerr = accuracyStd)
    rects2 = plt.bar(r2, bars2, width=barWidth, edgecolor='white', label='Avg. response Time (ms)', yerr = timeStd)
    rects3 = plt.bar(r3, bars3, width=barWidth, edgecolor='white', label='Avg. energy (dJ)', yerr = energyStd)
     
    # Add xticks on the middle of the group bars
    #plt.title('Results by metric')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['Fingerpriting\nwith KNN', 'Fingerpriting\nwith NN', 'Weighted\n Fingerpriting'])
     
    # Create legend & Show graphic
    autolabel(plt, rects1)
    autolabel(plt, rects2)
    autolabel(plt, rects3)
    plt.legend()
    plt.savefig("barCode_finger")
    plt.show()


def points_x_y_finger():
    
    # set width of bar
    barWidth = 0.25
    
    KNN     =   [1.70293863659264,0.641404708432983,1.27769323391806,5.4665711373767,2.65363901086791,1.6786303941011,2.12162673437153,0.707742891168819,4.2573465914816,0.880227243386615,1.82915280936285,2.81440935188895,1.12378823627942,1.77341478509682,4.35142505393348,2.2959311836377,3.0356712601993,0.893196506934504]
    w_KNN   =   [2.22611769679862,0.563205113613149,1.93961336353408,6.03530446622207,3.1104019032916,2.08086520466848,1.06962610289764,1.75559106855782,4.05690768936144,0.653681879816168,2.85119273287514,2.49377224300857,0.939148550549911,1.84024454896625,4.75143136328412,2.97060599878207,3.29387310016643,1.31209755734854]
    NN      =   [4.50422654693714,3.23054249462045,2.87245294105496,2.92368848531063,5.82760782309516,3.43342976012678,4.81924947986295,0.576463161572026,4.23514014549845,0.895075183429919,1.64313692350257,1.76065645299256,2.54272278402335,0.686498208017827,4.84754539236819,2.94194603460984,0.53752314801518,1.13945253614775] 
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    # Set position of bar on X axis    
    x = np.arange(len(labels))
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 3))
    
    # Make the plot
    rects1 = plt.bar(r1, KNN, width=barWidth, align='center',  edgecolor='white', label='KNN')
    rects2 = plt.bar(r2, w_KNN, width=barWidth, align='center',  edgecolor='white', label='Weighted KNN')
    rects3 = plt.bar(r3, NN, width=barWidth, align='center', edgecolor='white', label='NN')
    
    plt.yticks(np.arange(0, 8, 2), fontsize=14)
    plt.xticks(fontsize=14)
    plt.rcParams.update({'font.size': 14})
    plt.ylabel('Localization error (m)', fontsize=18)
    plt.xlabel('Test Points', fontsize=18)
    #plt.title('Localization Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_finger_all")

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
    
    plt.yticks(np.arange(0, 12, 2), fontsize=14)
    plt.xticks(fontsize=14)
    plt.rcParams.update({'font.size': 14})
    plt.ylabel('Localization error (m)', fontsize=18)
    plt.xlabel('Test Points', fontsize=18)
    #plt.title('Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_poly_all")

def points_x_y_log():
    
    # set width of bar
    barWidth = 0.25
    
    circ    = [4.69013274,0.94101552,2.99434241,4.70080099,6.42092654,5.3303506,5.98242071,1.16162591,3.63208749,1.68893629,0.77593208,3.12458326,1.60634256,1.59341805,4.24517221,3.793392,2.92280973,3.12668897]
    hyper   = [5.12928046,1.16623597,3.36634555,5.82710829,6.77220944,6.42790205,6.58506332,1.49724119,2.23462752,0.67980278,1.31104425,1.56251032,0.97198658,0.63774399,2.47792489,3.6151227,2.89693267,2.67101891]
    w_mult  = [4.79929695,1.09267319,2.97071479,5.65100772,5.87916436,5.569888,6.25379014,2.03224376,3.0480434,1.9948004,0.94965826,3.08353913,1.80832186,1.29818804,4.72611796,2.90092798,3.17526469,2.76440093] 
    labels  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    # Set position of bar on X axis    
    x = np.arange(len(labels))
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.figure(figsize=(10, 3))
    
    # Make the plot
    rects1 = plt.bar(r1, circ, width=barWidth, align='center',  edgecolor='white', label='Lognormal NLS')
    rects2 = plt.bar(r2, hyper, width=barWidth, align='center',  edgecolor='white', label='Lognormal LLS')
    rects3 = plt.bar(r3, w_mult, width=barWidth, align='center', edgecolor='white', label='Lognormal Weighted Mult.')
    
    plt.yticks(np.arange(0, 10, 2), fontsize=14)
    plt.xticks(fontsize=14)
    plt.rcParams.update({'font.size': 14})
    plt.ylabel('Localization error (m)', fontsize=18)
    plt.xlabel('Test Points', fontsize=18)
    #plt.title('Errors for each test point')
    plt.xticks(x)
    plt.legend()
    plt.tight_layout()
    plt.savefig("barCode_log_all")

def results_exp2():
    
    objects = ('Fing. KNN', 'Weighted Fing.', 'Log.\n Mult. LLS', 'Log.\n Mult. NLS', 'Poly.\n Mult. LLS', 'Poly.\n Mult. NLS')
    x = np.arange(len(objects))
    new_x = [3*i for i in x]
    acc = [0.97,0.99,3.63, 1.38,6.21, 2.22]
    std = [0.0,0.0,0.0,0.0,0.0,0.0,]
    
    plt.rcParams.update({'font.size': 14})
    plt.bar(new_x, acc, align='center', alpha=0.5, color='k')
    plt.xticks(new_x, objects)
    plt.ylabel('Average localization error (m)')
    plt.xlabel('Fingerpriting')
    plt.tight_layout()
    plt.savefig("results_exp2")
    plt.show()  

def line_graphics_poly():
    
    multPoly    = [3.45704806, 0.54697668, 3.44189218, 3.12709579, 5.7583891, 4.61373848, 4.09217047, 1.44386766, 3.29444614, 0.26902035, 1.2446576, 2.63650396, 1.13703992, 1.12628727, 5.47752303, 2.97256593, 1.62108528, 1.58710744]
    hyperPoly   = [5.3469478,1.2076835,3.2543549,5.49155069,6.58455764,6.1227509,6.38648434,1.72067371,2.19154019,0.23554218,1.11359291,1.4963839,1.01039786,0.26527713,3.00750348,3.54583935,1.82051234,1.57964032]
    w_multPoly  = [6.18783147,10.94338423,3.72362278,3.21650848,5.09190426,5.63592536,6.61481283,1.71423233,2.42209443,2.7896039,1.59932465,4.44864114,1.25643014,0.38741479,5.62157596,2.39220527,2.09871313,1.89634214]
    labels      =   ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    plt.plot(labels, multPoly, label = "Polynomial NLS")
    plt.plot(labels, hyperPoly, label = "Polynomial LLS")
    plt.plot(labels, w_multPoly, label = "Polynomial Weighted Mult.")
    
    plt.ylabel('Localization error (m)', fontsize=14)
    plt.xlabel('Test Points', fontsize=14)
    plt.legend()
    plt.savefig("lineCode_poly_all")
    plt.show()
    
def line_graphics_log():
    
    circ    = [4.69013274,0.94101552,2.99434241,4.70080099,6.42092654,5.3303506,5.98242071,1.16162591,3.63208749,1.68893629,0.77593208,3.12458326,1.60634256,1.59341805,4.24517221,3.793392,2.92280973,3.12668897]
    hyper   = [5.12928046,1.16623597,3.36634555,5.82710829,6.77220944,6.42790205,6.58506332,1.49724119,2.23462752,0.67980278,1.31104425,1.56251032,0.97198658,0.63774399,2.47792489,3.6151227,2.89693267,2.67101891]
    w_mult  = [4.79929695,1.09267319,2.97071479,5.65100772,5.87916436,5.569888,6.25379014,2.03224376,3.0480434,1.9948004,0.94965826,3.08353913,1.80832186,1.29818804,4.72611796,2.90092798,3.17526469,2.76440093] 
    labels      =   ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    plt.plot(labels, circ, label = "Lognormal NLS")
    plt.plot(labels, hyper, label = "Lognormal LLS")
    plt.plot(labels, w_mult, label = "Lognormal Weighted Mult.")
    
    plt.ylabel('Localization error (m)', fontsize=14)
    plt.xlabel('Test Points', fontsize=14)
    plt.legend()
    plt.savefig("lineCode_log_all")
    plt.show()
    
def line_graphics_fig():
    
    KNN     =   [1.70293863659264,0.641404708432983,1.27769323391806,5.4665711373767,2.65363901086791,1.6786303941011,2.12162673437153,0.707742891168819,4.2573465914816,0.880227243386615,1.82915280936285,2.81440935188895,1.12378823627942,1.77341478509682,4.35142505393348,2.2959311836377,3.0356712601993,0.893196506934504]
    w_KNN   =   [2.22611769679862,0.563205113613149,1.93961336353408,6.03530446622207,3.1104019032916,2.08086520466848,1.06962610289764,1.75559106855782,4.05690768936144,0.653681879816168,2.85119273287514,2.49377224300857,0.939148550549911,1.84024454896625,4.75143136328412,2.97060599878207,3.29387310016643,1.31209755734854]
    NN      =   [4.50422654693714,3.23054249462045,2.87245294105496,2.92368848531063,5.82760782309516,3.43342976012678,4.81924947986295,0.576463161572026,4.23514014549845,0.895075183429919,1.64313692350257,1.76065645299256,2.54272278402335,0.686498208017827,4.84754539236819,2.94194603460984,0.53752314801518,1.13945253614775] 
    labels      =   ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    
    plt.plot(labels, KNN, label = "KNN")
    plt.plot(labels, w_KNN, label = "Weighted KNN")
    plt.plot(labels, NN, label = "NN")
    
    plt.ylabel('Localization error (m)', fontsize=14)
    plt.xlabel('Test Points', fontsize=14)
    plt.legend()
    plt.savefig("lineCode_finger_all")
    plt.show()    

    
def main():
    
    results_exp2()
    
    
if __name__== "__main__":
    main()
