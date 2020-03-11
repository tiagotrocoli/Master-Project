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


def group_bar_chart():
    
    

def main():
    
    
        
if __name__== "__main__":
    main()