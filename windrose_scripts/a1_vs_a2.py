from matplotlib import pyplot as plt
from dirToList import dir_to_list
import numpy as np
import sys
import os


def timeStrToMin(x):
    time = x.split(':')
    time = [float(x) for x in time]
    tMins = time[0]*60 + time[1]
    return tMins


def calc_t_WS_WD(array):
    to_ret_arr =np.array([[]]).reshape(0,3)
    t= array[:,1] 
    u= array[:,45].astype(np.float)
    v= array[:,47].astype(np.float)
    wd= array[:,44]
    ws = np.sqrt(np.add(np.power(u,2),np.power(v,2)))
    temp = np.column_stack((t,ws,wd))
    to_ret_arr = np.vstack((to_ret_arr,temp))
    return to_ret_arr

def get_WS(fileList1, fileList2):
        array1 = np.array([[]]).reshape(0,3)
        array2 = np.array([[]]).reshape(0,3)
        for (Name1, Name2) in zip(fileList1, fileList2):
                fd1 = open(Name1)
                lines1 =[]
                for line in fd1:
                        lines1.append(line.split())
                ## Account for duplicate headers ##
                start_val = 57
                if lines1[57][0] == "HeaderLength=55":
                    print "Found duplicate header"
                    start_val+=57
                lines1 = lines1[start_val:]
                data1 = np.array(lines1)
                fd2 = open(Name2)
                lines2 =[]
                for line in fd2:
                        lines2.append(line.split())
                ## Account for duplicate headers ##
                start_val = 57
                if lines2[57][0] == "HeaderLength=55":
                    print "Found duplicate header"
                    start_val+=57
                lines2 = lines2[start_val:]
                
                data2 = np.array(lines2)
                if data1.shape[0] != data2.shape[0]:
                    (x,y) = equalize_arrays_on_time_and_wd(data1,data2,44)
                    x = calc_t_WS_WD(x)
                    y = calc_t_WS_WD(y)
                    array1 = np.concatenate((array1,x),axis=0)
                    array2 = np.concatenate((array2,x),axis=0)

                else:
                    x = calc_t_WS_WD(data1)
                    y = calc_t_WS_WD(data2)
                    array1 = np.concatenate((array1,x),axis=0)
                    array2 = np.concatenate((array2,x),axis=0)

        print array1.shape, array2.shape
        print type(array1), type(array2)
        diff_array = dif_ws_arr1_arr2(array1,array2)
        diff_array = np.array(diff_array)
        return (diff_array, array1[:,2].astype(np.float))


def dif_ws_arr1_arr2(array1,array2):
    data1= array1[:,1].astype(np.float)
    data2= array2[:,1].astype(np.float)
    to_ret = np.array(np.subtract(data1, data2))
    return to_ret


#def equalize_on_wd(array1,array2,wd_pos):
#    to_ret_arr_1 =[[]]
#    to_ret_arr_2 =[[]]
#    for x in array1:
#        for y in array2:
#            if (x[wd_pos].astype(np.float) !=np.NAN and y[wd_pos].astype(np.float) !=np.NAN):
#                to_ret_arr_1.append(list(x))
#                to_ret_arr_2.append(list(y))
#        to_ret_arr_1 = np.array(to_ret_arr_1)
#    to_ret_arr_2 = np.array(to_ret_arr_2)
#    return (to_ret_arr1,to_ret_arr2)
            

def equalize_arrays_on_time_and_wd(array1, array2, wd_pos):
    num_cols = array2.shape[1]
    time_arr_1 = list(array1[:,1])
    time_arr_2 = list(array2[:,1])
    to_ret_arr1 = [[]]
    to_ret_arr2 = [[]]
    for i in time_arr_1:
        for j in time_arr_2:
            if i == j:
                x = time_arr_1.index(j)
                y = time_arr_2.index(i)
                if (array1[x,wd_pos].astype(np.float) != np.NAN and array2[y,wd_pos].astype(np.float) != np.NAN):
                    to_ret_arr1.append(list(array1[x,:]))
                    to_ret_arr2.append(list(array2[y,:]))
    to_ret_arr1 = np.array(to_ret_arr1[1:])
    to_ret_arr2 = np.array(to_ret_arr2[1:])
    #print to_ret_arr1.shape, to_ret_arr2.shape
    return (to_ret_arr1, to_ret_arr2)

               
if __name__ == '__main__':
        dir1 = sys.argv[1]
        site_1 = sorted(dir_to_list(dir1))
        
        dir2 = sys.argv[2]
        site_2 = sorted(dir_to_list(dir2))

        (x,y) = get_WS(site_1,site_2)
        print x, x.shape
        print y, y.shape



        

