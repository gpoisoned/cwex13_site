from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sys
import os

def new_axes():
    fig = plt.figure(figsize=(7,7), dpi=80, facecolor='w', edgecolor='w')
    rect = [0.1, 0.1, 0.8, 0.8]
    ax = WindroseAxes(fig,rect,axisbg='w')
    fig.add_axes(ax)
    return ax

def set_legend(ax):
    l = ax.legend(borderaxespad=0.10)
    plt.setp(l.get_texts(), fontsize=8)

def dir_to_list(dir_name, *args):
    fileList = []
    for file in os.listdir(dir_name):
            dirfile = os.path.join(dir_name, file)
            if os.path.isfile(dirfile):
                if len(args) == 0:
                    fileList.append(dirfile)
                else:
                    if os.path.splitext(dirfile)[1][1:] in args:
                        fileList.append(dirfile)
    return fileList



if __name__ == '__main__':
	filesDirectory = sys.argv[1]
	allfiles = dir_to_list(filesDirectory)

	WS40 = np.array([])
	WD40 = np.array([])
	WS60 = np.array([])
	WD60 = np.array([])
	WS80 = np.array([])
	WD80 = np.array([])
	WS100 = np.array([])
	WD100 = np.array([])
	WS120 = np.array([])
	WD120 = np.array([])
	WS140 = np.array([])
	WD140 = np.array([])
	WS160 = np.array([])
	WD160 = np.array([])
	WS180 = np.array([])
	WD180 = np.array([])
	WS200 = np.array([])
	WD200 = np.array([])
	WS220 = np.array([])
	WD220 = np.array([])

	for fileName in allfiles:
		print fileName
		file = open(fileName)
		lines=[]
		# Read from File
		for line in file:
		        lines.append(line.split())
		lines = lines[57:]

		# Convert to numpy format array
		data = np.array(lines)

		# Calculate WS Wind Speed for each height and stack them into matrix
		u_40m = data[:,9].astype(np.float)
		v_40m = data[:,11].astype(np.float)
		WS_40m = np.sqrt(np.add(np.power(u_40m,2),np.power(v_40m,2)))
		u_60m = data[:,27].astype(np.float)
		v_60m = data[:,29].astype(np.float)
		WS_60m = np.sqrt(np.add(np.power(u_60m,2),np.power(v_60m,2)))
		u_80m = data[:,45].astype(np.float)
		v_80m = data[:,47].astype(np.float)
		WS_80m = np.sqrt(np.add(np.power(u_80m,2),np.power(v_80m,2)))
		u_100m = data[:,63].astype(np.float)
		v_100m = data[:,65].astype(np.float)
		WS_100m = np.sqrt(np.add(np.power(u_100m,2),np.power(v_100m,2)))
		u_120m = data[:,81].astype(np.float)
		v_120m = data[:,83].astype(np.float)
		WS_120m = np.sqrt(np.add(np.power(u_120m,2),np.power(v_120m,2)))
		u_140m = data[:,99].astype(np.float)
		v_140m = data[:,101].astype(np.float)
		WS_140m = np.sqrt(np.add(np.power(u_140m,2),np.power(v_140m,2)))
		u_160m = data[:,117].astype(np.float)
		v_160m = data[:,119].astype(np.float)
		WS_160m = np.sqrt(np.add(np.power(u_160m,2),np.power(v_160m,2)))
		u_180m = data[:,135].astype(np.float)
		v_180m = data[:,137].astype(np.float)
		WS_180m = np.sqrt(np.add(np.power(u_180m,2),np.power(v_180m,2)))
		u_200m = data[:,153].astype(np.float)
		v_200m = data[:,155].astype(np.float)
		WS_200m = np.sqrt(np.add(np.power(u_200m,2),np.power(v_200m,2)))
		u_220m = data[:,171].astype(np.float)
		v_220m = data[:,173].astype(np.float)
		WS_220m = np.sqrt(np.add(np.power(u_220m,2),np.power(v_220m,2)))

		# Calculate WD wind direction for each height and stack them into matrix
		wd_40m_deg = data[:,8].astype(np.float)
		wd_60m_deg = data[:,26].astype(np.float)
		wd_80m_deg = data[:,44].astype(np.float)
		wd_100m_deg = data[:,62].astype(np.float)
		wd_120m_deg = data[:,80].astype(np.float)
		wd_140m_deg = data[:,98].astype(np.float)
		wd_160m_deg = data[:,116].astype(np.float)
		wd_180m_deg = data[:,134].astype(np.float)
		wd_200m_deg = data[:,152].astype(np.float)
		wd_220m_deg = data[:,170].astype(np.float)

		WS40 = np.append(WS40,WS_40m)
		WD40 = np.append(WD40,wd_40m_deg)
		WS60 = np.append(WS60,WS_60m)
		WD60 = np.append(WD60,wd_60m_deg)
		WS80 = np.append(WS80,WS_80m)
		WD80 = np.append(WD80,wd_80m_deg)
		WS100 = np.append(WS100,WS_100m)
		WD100 = np.append(WD100,wd_100m_deg)
		WS120 = np.append(WS120,WS_120m)
		WD120 = np.append(WD120,wd_120m_deg)
		WS140 = np.append(WS140,WS_140m)
		WD140 = np.append(WD140,wd_140m_deg)
		WS160 = np.append(WS160,WS_160m)
		WD160 = np.append(WD160,wd_160m_deg)
		WS180 = np.append(WS180,WS_180m)
		WD180 = np.append(WD180,wd_180m_deg)
		WS200 = np.append(WS200,WS_200m)
		WD200 = np.append(WD200,wd_200m_deg)
		WS220 = np.append(WS220,WS_220m)
		WD220 = np.append(WD220,wd_220m_deg)

	# # # Fix for error with NAN values:
	# # #    Convert nan -> 0
	# WS40[np.isnan(WS40)] = -0.0
	# WD40[np.isnan(WD40)] = -0.0
	# WS60[np.isnan(WS60)] = -0.0
	# WD60[np.isnan(WD60)] = -0.0
	# WS80[np.isnan(WS80)] = -0.0
	# WD80[np.isnan(WD80)] = -0.0
	# WS100[np.isnan(WS100)] = -0.0
	# WD100[np.isnan(WD100)] = -0.0
	# WS120[np.isnan(WS120)] = -0.0
	# WD120[np.isnan(WD120)] = -0.0
	# WS140[np.isnan(WS140)] = -0.0
	# WD140[np.isnan(WD140)] = -0.0
	# WS160[np.isnan(WS160)] = -0.0
	# WD160[np.isnan(WD160)] = -0.0
	# WS180[np.isnan(WS180)] = -0.0
	# WD180[np.isnan(WD180)] = -0.0
	# WS200[np.isnan(WS200)] = -0.0
	# WD200[np.isnan(WD200)] = -0.0
	# WS220[np.isnan(WS220)] = -0.0
	# WD220[np.isnan(WD220)] = -0.0

	# WS40=WS40[np.isfinite(WS40)]
	# WD40=WD40[np.isfinite(WD40)]	
	# WS60=WS60[np.isfinite(WS60)]
	# WD60=WD60[np.isfinite(WD60)]
	# WS80=WS80[np.isfinite(WS80)]
	# WD80=WD80[np.isfinite(WD80)]
	# WS100=WS100[np.isfinite(WS100)]
	# WD100=WD100[np.isfinite(WD100)]
	# WS120=WS120[np.isfinite(WS120)]
	# WD120=WD120[np.isfinite(WD120)]
	# WS140=WS140[np.isfinite(WS140)]
	# WD140=WD140[np.isfinite(WD140)]
	# WS160=WS160[np.isfinite(WS160)]
	# WD160=WD160[np.isfinite(WD160)]
	# WS180=WS180[np.isfinite(WS180)]
	# WD180=WD180[np.isfinite(WD180)]
	# WS200=WS200[np.isfinite(WS200)]
	# WD200=WD200[np.isfinite(WD200)]
	# WS220=WS220[np.isfinite(WS220)]
	# WD220=WD220[np.isfinite(WD220)]

	# Mask invalid values:
	WS40=np.ma.masked_invalid(WS40)
	WD40=np.ma.masked_invalid(WD40)	
	WS60=np.ma.masked_invalid(WS60)
	WD60=np.ma.masked_invalid(WD60)
	WS80=np.ma.masked_invalid(WS80)
	WD80=np.ma.masked_invalid(WD80)
	WS100=np.ma.masked_invalid(WS100)
	WD100=np.ma.masked_invalid(WD100)
	WS120=np.ma.masked_invalid(WS120)
	WD120=np.ma.masked_invalid(WD120)
	WS140=np.ma.masked_invalid(WS140)
	WD140=np.ma.masked_invalid(WD140)
	WS160=np.ma.masked_invalid(WS160)
	WD160=np.ma.masked_invalid(WD160)
	WS180=np.ma.masked_invalid(WS180)
	WD180=np.ma.masked_invalid(WD180)
	WS200=np.ma.masked_invalid(WS200)
	WD200=np.ma.masked_invalid(WD200)
	WS220=np.ma.masked_invalid(WS220)
	WD220=np.ma.masked_invalid(WD220)

	#windrose like a stacked histogram with normed (displayed in percent) results
	plt.figure()
	ax = new_axes()
	ax.bar(WD40, WS40, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 40m",fontsize=16)
	plt.savefig("WS40.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD60, WS60, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 60m",fontsize=16)
	plt.savefig("WS60.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD80, WS80, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 80m",fontsize=16)
	plt.savefig("WS80.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD100, WS100, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 100m",fontsize=16)
	plt.savefig("WS100.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD120, WS120, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 120m",fontsize=16)
	plt.savefig("WS120.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD140, WS140, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 140m",fontsize=16)
	plt.savefig("WS140.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD160, WS160, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 160m",fontsize=16)
	plt.savefig("WS160.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD180, WS180, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 180m",fontsize=16)
	plt.savefig("WS180.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD200, WS200, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 200m",fontsize=16)
	plt.savefig("WS200.jpeg")

	plt.figure()
	ax = new_axes()
	ax.bar(WD220, WS220, normed=True, opening=0.8, edgecolor='white')
	set_legend(ax)
	plt.title("WS at 220m",fontsize=16)
	plt.savefig("WS220.jpeg")

