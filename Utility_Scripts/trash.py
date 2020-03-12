import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def bar_char():
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

def group_bar_chart():
        
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
    plt.savefig("barCode")
    plt.show()

def main():
    
    group_bar_chart()
        
if __name__== "__main__":
    main()